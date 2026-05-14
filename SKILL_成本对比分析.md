---
name: cost-analysis
description: "房地产项目建安成本对比分析工具。用于分析两个住宅项目的成本差异，输出标准化的成本对比分析报告Excel文件。支持智能业态匹配、多维度成本对比、固定/弹性成本差异分解，生成带SUM公式的Excel报告。"
version: 1.0.0
author: AI Assistant
tags: [成本分析, 房地产, Excel处理, 数据分析]
input_format: |
  两个Excel文件（.xlsx格式），每个文件需包含：
  - 04 目标成本控制表：各成本科目的总价、建面单方、可售单方
  - 05 成本测算明细：详细的成本测算数据、含量指标、单价数据
  - 02 项目基础信息（可选）：基础指标（总建筑面积、可售面积等）
output_format: |
  Excel文件，包含三个工作表：
  1. 成本对比总表：项目整体成本对比，含合计-毛坯和总建安成本SUM公式
  2. 固定单方差异明细分析：固定成本科目差异分解
  3. 弹性单方差异明细分析：弹性成本科目差异分解
---

# 成本对比分析技能

## 功能概述

本技能提供房地产项目建安成本对比分析功能：

- **智能业态匹配**：自动匹配叠拼↔叠墅、洋房↔小高层等不同命名规则的业态
- **多维度成本对比**：总价、建面单方、可售单方对比分析
- **差异分解分析**：固定成本与弹性成本差异详细分解
- **公式联动报告**：生成带SUM公式的Excel报告，支持数据联动

## 执行命令

```bash
# 直接执行分析
python main.py <项目A文件> <项目B文件> [-o 输出文件]

# 列出可用项目文件
python main.py --list
```

## 输出报告

生成的Excel报告包含三个工作表：

1. **成本对比总表**
   - 各成本科目的总价、相对建面指标、总建面指标
   - 差异分析（相对建面单方差异、总建面单方差异、总金额差）
   - 汇总行嵌入SUM公式（合计-毛坯、总建安成本）

2. **固定单方差异明细分析**
   - 按业态细分的固定成本分析
   - 含量差异影响和价格差异影响分解

3. **弹性单方差异明细分析**
   - 按业态细分的弹性成本分析
   - 入户门、外立面门窗、安防、电梯等科目的含量指标和配置单价分析

## 技术特性

- **智能业态匹配**：自动匹配不同命名规则的业态类型
- **Excel公式集成**：汇总行自动嵌入SUM公式，支持数据联动
- **错误处理**：完善的异常处理和日志记录

## 项目结构

```
cost-comparison-analysis/
├── main.py                  # 命令行入口
├── web_app.py               # Streamlit Web界面
├── data_parser.py           # 数据解析器
├── cost_comparator.py       # 成本对比计算
├── type_matcher.py          # 业态匹配逻辑
├── output_generator.py      # Excel报告生成
├── skill_entry.py           # Skill入口脚本
├── config.py                # 配置文件
├── data/                    # 输入文件目录
└── output/                  # 输出文件目录
```

## 使用示例

```bash
# 对比两个项目
python main.py "项目A.xlsx" "项目B.xlsx"

# 指定输出文件名
python main.py "海淀树村地块.xlsx" "摩天轮地块.xlsx" -o "成本对比报告.xlsx"
```

## 全局Skill集成

本项目同时也集成到Trae的全局Skill系统中，Skill位置：

```
/Users/zhenfei/.trae-cn/builtin/work/default/skills/cost-analysis/
├── SKILL.md      # Skill元数据描述
└── execute.py    # 执行入口脚本
```
