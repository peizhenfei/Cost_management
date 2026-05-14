#!/usr/bin/env python3
"""
成本对比分析系统 - Skill入口脚本
用于嵌入到全局Skill系统中调用成本对比分析功能
"""

import os
import sys
import subprocess
import time

def run_web_app():
    """启动Streamlit Web应用"""
    try:
        # 切换到项目目录
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # 检查依赖是否安装
        try:
            import streamlit
        except ImportError:
            print("[INFO] 正在安装依赖...")
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                         capture_output=True, text=True)
        
        # 启动Streamlit
        print("[INFO] 正在启动成本对比分析系统...")
        process = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "web_app.py"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        
        # 等待服务启动
        time.sleep(5)
        
        # 检查是否成功启动
        if process.poll() is None:
            print("[SUCCESS] 成本对比分析系统已启动")
            print("[INFO] 访问地址: http://localhost:8501")
            print("[INFO] 在浏览器中打开上述地址进行成本对比分析")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"[ERROR] 启动失败: {stderr.decode('utf-8')}")
            return None
    except Exception as e:
        print(f"[ERROR] 启动异常: {str(e)}")
        return None

def run_analysis(project_a_path, project_b_path, output_path=None):
    """
    直接执行成本对比分析
    :param project_a_path: 项目A Excel文件路径
    :param project_b_path: 项目B Excel文件路径  
    :param output_path: 输出文件路径（可选）
    :return: 输出文件路径
    """
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # 构建命令
        cmd = [sys.executable, "main.py", project_a_path, project_b_path]
        if output_path:
            cmd.extend(["-o", output_path])
        
        print(f"[INFO] 正在执行成本对比分析...")
        print(f"[INFO] 项目A: {project_a_path}")
        print(f"[INFO] 项目B: {project_b_path}")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("[SUCCESS] 成本对比分析完成")
            if output_path:
                abs_output = os.path.abspath(output_path)
            else:
                abs_output = os.path.abspath("output/成本对比分析报告.xlsx")
            print(f"[INFO] 输出文件: {abs_output}")
            return abs_output
        else:
            print(f"[ERROR] 分析失败: {result.stderr}")
            return None
    except Exception as e:
        print(f"[ERROR] 分析异常: {str(e)}")
        return None

def list_project_files():
    """列出可用的项目文件"""
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    files = []
    
    if os.path.exists(data_dir):
        for f in os.listdir(data_dir):
            if f.endswith(".xlsx") and not f.startswith("~"):
                files.append(f)
    
    return files

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="成本对比分析系统 - Skill入口")
    parser.add_argument("--web", action="store_true", help="启动Web界面")
    parser.add_argument("--list", action="store_true", help="列出可用项目文件")
    parser.add_argument("project_a", nargs="?", help="项目A文件路径")
    parser.add_argument("project_b", nargs="?", help="项目B文件路径")
    parser.add_argument("-o", "--output", help="输出文件路径")
    
    args = parser.parse_args()
    
    if args.web:
        process = run_web_app()
        if process:
            # 保持运行
            try:
                process.wait()
            except KeyboardInterrupt:
                process.terminate()
                print("[INFO] 服务已停止")
    
    elif args.list:
        files = list_project_files()
        print("可用项目文件:")
        for f in files:
            print(f"  - {f}")
    
    elif args.project_a and args.project_b:
        output = run_analysis(args.project_a, args.project_b, args.output)
        if output:
            print(f"分析完成，输出文件: {output}")
        else:
            print("分析失败")
    
    else:
        parser.print_help()
