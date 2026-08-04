# -*- coding: utf-8 -*-
"""
柱状图模板 —— 随机数据示例
============================
功能: 生成一个带随机数据的柱状图, 供后续作图时作为模板修改。
使用方法: 把下面的"数据区"替换成你自己的数据, 再调整标题/轴标签即可。
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# ============================================================
# 0. 中文字体设置 (解决中文乱码的问题)
#    自动从可用字体里选一个支持中文的, 在 Windows / Mac / Linux 上都能正常显示
# ============================================================
def _setup_chinese_font():
    from matplotlib import font_manager
    available = {f.name for f in font_manager.fontManager.ttflist}
    for font in ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Noto Sans CJK JP",
                 "Arial Unicode MS", "PingFang SC", "WenQuanYi Zen Hei"]:
        if font in available:
            plt.rcParams["font.sans-serif"] = [font]
            break
    plt.rcParams["axes.unicode_minus"] = False   # 解决负号 "-" 显示为方块的问题

_setup_chinese_font()

# ============================================================
# 1. 数据区  (以后做图时只需要修改这里)
# ============================================================
rng = np.random.default_rng(42)          # 固定随机种子, 保证每次运行数据一致; 想每次不同就删掉 42
categories = ["类别A", "类别B", "类别C", "类别D", "类别E", "类别F"]   # X轴类别名称
values = rng.integers(10, 100, len(categories))                      # 随机生成 10~99 之间的整数

# 可选: 错误棒数据 (标准差/误差范围), 不需要就注释掉
errors = rng.uniform(1, 5, len(categories))

# ============================================================
# 2. 画图参数区  (颜色、标题、标签等都可以在这里调整)
# ============================================================
FIG_SIZE      = (8, 5)        # 画布大小 (宽, 高) 单位: 英寸
COLOR         = "#4C72B0"     # 柱子的颜色 (可改成 'skyblue', '#FF8C00' 等)
ALPHA         = 0.9           # 柱子透明度 0~1
BAR_WIDTH     = 0.6           # 柱子宽度
TITLE         = "柱状图示例标题"
X_LABEL       = "类别"
Y_LABEL       = "数值"
SHOW_VALUE    = True          # 是否在柱子顶部显示数值
SHOW_GRID     = True          # 是否显示网格
SHOW_ERRORBAR = True          # 是否显示误差棒
DPI           = 150           # 保存图片的分辨率
SAVE_PATH     = "柱状图.png"  # 保存文件名, 不需要保存就设为 None

# ============================================================
# 3. 绘图
# ============================================================
fig, ax = plt.subplots(figsize=FIG_SIZE)

# 画柱子
bars = ax.bar(
    categories,
    values,
    width=BAR_WIDTH,
    color=COLOR,
    alpha=ALPHA,
    edgecolor="black",        # 柱子边框颜色
    linewidth=0.8,            # 边框粗细
    yerr=errors if SHOW_ERRORBAR else None,   # 误差棒
    capsize=4,                # 误差棒两端短线长度
    label="数据",
)

# 在柱子顶部显示数值
if SHOW_VALUE:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),                        # 文字相对柱顶向上偏移 3 个点
            textcoords="offset points",
            ha="center", va="bottom",
            fontsize=10,
        )

# 标题与坐标轴标签
ax.set_title(TITLE, fontsize=16, fontweight="bold", pad=15)
ax.set_xlabel(X_LABEL, fontsize=12)
ax.set_ylabel(Y_LABEL, fontsize=12)

# 网格
if SHOW_GRID:
    ax.grid(axis="y", linestyle="--", alpha=0.5)   # 只加水平网格线, 更干净
    ax.set_axisbelow(True)                         # 网格线放在柱子后面

# 坐标轴范围微调 (给柱顶数值留出空间)
ax.set_ylim(0, max(values) * 1.2)

# 边框处理: 去掉上、右边框, 更接近 Origin 的简洁风格
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

# 保存图片
if SAVE_PATH:
    fig.savefig(SAVE_PATH, dpi=DPI)
    print(f"图片已保存: {SAVE_PATH}")

# 显示图片
plt.show()

# ============================================================
# 4. 打印数据, 方便核对 (非必需, 不需要可删除)
# ============================================================
print("类别:", categories)
print("数值:", list(values))
if SHOW_ERRORBAR:
    print("误差:", np.round(errors, 2))
