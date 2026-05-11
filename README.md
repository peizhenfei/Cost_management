# 🏗️ 房地产项目成本对比分析系统

一个基于 Python + Streamlit 的房地产项目建安成本对比分析工具，支持自动化生成专业的成本对比分析报告。

## ✨ 功能特性

- 📊 **智能成本对比**：自动对比两个项目的建安成本
- 📈 **多维度分析**：固定成本、弹性成本、业态分析
- 📋 **专业报告**：自动生成 Excel 格式的对比分析报告
- 🎯 **业态匹配**：智能匹配不同项目的业态类型
- 🌐 **Web 界面**：友好的 Streamlit Web 界面
- 💻 **命令行支持**：支持命令行批量处理

## 🚀 在线使用

访问在线应用：**[成本对比分析系统](https://share.streamlit.io/peizhenfei/cost-comparison-analysis)**

## 📦 本地安装

### 环境要求

- Python 3.9 或更高版本
- pip 包管理器

### 安装步骤

```bash
# 1. 克隆仓库
git clone https://github.com/peizhenfei/cost-comparison-analysis.git
cd cost-comparison-analysis

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行 Web 应用
streamlit run web_app.py
```

### 命令行使用

```bash
# 列出当前目录的 Excel 文件
python main.py --list

# 执行成本对比分析
python main.py "项目A.xlsx" "项目B.xlsx" -o "对比报告.xlsx"
```

## 📋 输入文件要求

输入的 Excel 文件应包含以下工作表：

- **04 目标成本控制表**：项目成本控制数据
- **05 成本测算明细**：详细的成本测算数据
- **02 项目基础信息（输入）**（可选）：项目基础信息

## 📊 输出报告

系统会生成包含三个工作表的 Excel 报告：

1. **成本对比总表**：项目整体成本对比
2. **固定单方差异明细分析**：固定成本科目差异分解
3. **弹性单方差异明细分析**：弹性成本科目差异分解

## 🛠️ 项目结构

```
cost-comparison-analysis/
├── web_app.py              # Streamlit Web 界面
├── main.py                 # 命令行入口
├── data_parser.py          # 数据解析器
├── cost_comparator.py      # 成本对比计算
├── type_matcher.py         # 业态匹配逻辑
├── output_generator.py     # Excel 报告生成
├── config.py               # 配置文件
├── requirements.txt        # 依赖列表
├── .streamlit/             # Streamlit 配置
│   └── config.toml
└── .github/                # GitHub Actions
    └── workflows/
        └── deploy.yml
```

## 🔧 核心功能

### 1. 业态智能匹配

系统支持不同命名规则的业态自动匹配：

- 叠拼 ↔ 叠墅
- 洋房 ↔ 小高层
- 地下室其他 ↔ 地下室其他

### 2. 灵活的数据获取

当输入文件缺少"02 项目基础信息表"时，系统会自动从其他工作表获取必要信息。

### 3. Excel 公式集成

生成的报告包含完整的 Excel 公式，方便后续检查和修改。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👤 作者

**peizhenfei**
- GitHub: [@peizhenfei](https://github.com/peizhenfei)

## 🙏 致谢

感谢所有开源项目的贡献者，特别是：
- [Streamlit](https://streamlit.io/)
- [openpyxl](https://openpyxl.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
