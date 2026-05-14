# 🏗️ 房地产项目成本对比分析系统

一个基于 Python + Streamlit 的房地产项目建安成本对比分析工具，支持自动化生成专业的成本对比分析报告。

## ✨ 功能特性

- 📊 **智能成本对比**：自动对比两个项目的建安成本
- 📈 **多维度分析**：固定成本、弹性成本、业态分析
- 📋 **专业报告**：自动生成 Excel 格式的对比分析报告
- 🎯 **业态匹配**：智能匹配不同项目的业态类型
- 🌐 **Web 界面**：友好的 Streamlit Web 界面
- 💻 **命令行支持**：支持命令行批量处理
- 🤖 **Trae Skill 集成**：支持作为 Trae 的全局 Skill 使用

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

## 🤖 Trae Skill 集成

本项目已集成到 Trae 的全局 Skill 系统，提供更便捷的使用体验。

### 部署 Skill

```bash
# 运行部署脚本
bash deploy_skill.sh
```

或者手动部署：

```bash
# 1. 创建 Skill 目录
mkdir -p ~/.trae-cn/builtin/work/default/skills/cost-analysis

# 2. 复制 Skill 文件
cp skill/SKILL.md ~/.trae-cn/builtin/work/default/skills/cost-analysis/SKILL.md
cp skill/execute.py ~/.trae-cn/builtin/work/default/skills/cost-analysis/execute.py
```

### 使用 Skill

#### 方式一：在 Trae 中直接调用
在 Trae 对话中直接说：
```
帮我做成本对比分析
```

或者：
```
使用成本分析技能，对比项目A和项目B
```

#### 方式二：命令行调用
```bash
# 列出可用项目文件
python3 ~/.trae-cn/builtin/work/default/skills/cost-analysis/execute.py --list

# 执行成本对比分析
python3 ~/.trae-cn/builtin/work/default/skills/cost-analysis/execute.py "项目A.xlsx" "项目B.xlsx" -o "对比报告.xlsx"
```

#### 方式三：通过 skill_entry.py
```bash
# 使用项目中的 skill_entry.py
python skill_entry.py --list
python skill_entry.py "项目A.xlsx" "项目B.xlsx" -o "对比报告.xlsx"
```

## 📋 输入文件要求

输入的 Excel 文件应包含以下工作表：

- **04 目标成本控制表**：项目成本控制数据
- **05 成本测算明细**：详细的成本测算数据
- **02 项目基础信息（输入）**（可选）：项目基础信息

## 📊 输出报告

系统会生成包含三个工作表的 Excel 报告：

1. **成本对比总表**：项目整体成本对比，包含合计-毛坯和总建安成本的 SUM 公式
2. **固定单方差异明细分析**：固定成本科目差异分解
3. **弹性单方差异明细分析**：弹性成本科目差异分解

## 🛠️ 项目结构

```
cost-comparison-analysis/
├── web_app.py              # Streamlit Web 界面
├── main.py                 # 命令行入口
├── skill_entry.py          # Skill 入口脚本
├── deploy_skill.sh         # Skill 部署脚本
├── data_parser.py          # 数据解析器
├── cost_comparator.py      # 成本对比计算
├── type_matcher.py         # 业态匹配逻辑
├── output_generator.py     # Excel 报告生成
├── config.py               # 配置文件
├── requirements.txt        # 依赖列表
├── SKILL_成本对比分析.md    # Skill 描述文件
├── skill/                  # Skill 文件目录
│   ├── SKILL.md           # Skill 元数据
│   └── execute.py         # Skill 执行脚本
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

生成的报告包含完整的 Excel 公式：
- **合计-毛坯**：自动汇总前期工程、桩基工程、岩土工程、单体工程、配套工程、室外工程
- **总建安成本**：自动汇总毛坯、户内装饰工程、基础设施工程、卖场包装费用
- 支持数据联动和自动计算

### 4. 多执行方式

- Web 界面（Streamlit）
- 命令行工具
- Trae Skill 集成
- Python API 调用

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
