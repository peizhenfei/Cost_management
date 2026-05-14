#!/bin/bash
# 成本对比分析Skill部署脚本
# 将Skill文件部署到Trae的全局Skill系统

set -e

# 项目根目录
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Trae Skill目录
SKILL_DIR="$HOME/.trae-cn/builtin/work/default/skills/cost-analysis"

echo "========================================"
echo "  成本对比分析Skill部署脚本"
echo "========================================"
echo ""

# 创建Skill目录
echo "创建Skill目录..."
mkdir -p "$SKILL_DIR"

# 复制文件
echo "复制Skill文件..."
cp "$PROJECT_DIR/skill/SKILL.md" "$SKILL_DIR/SKILL.md"
cp "$PROJECT_DIR/skill/execute.py" "$SKILL_DIR/execute.py"

# 设置执行权限
chmod +x "$SKILL_DIR/execute.py"

echo ""
echo "✅ 部署成功！"
echo ""
echo "Skill位置: $SKILL_DIR"
echo ""
echo "测试Skill:"
echo "  python3 $SKILL_DIR/execute.py --list"
echo ""
