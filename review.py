# numerical_methods_review.py - 工程数值方法层级复习系统
import streamlit as st
import pandas as pd

# ========== 页面配置 ==========
st.set_page_config(
    page_title="工程数值方法 - 层级复习系统",
    page_icon="📚",
    layout="wide"
)

# ========== 自定义样式 ==========
st.markdown("""
<style>
    .review-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .review-header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .review-header p {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    .course-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        cursor: pointer;
        margin: 0.5rem 0;
        transition: transform 0.2s;
        border: none;
        font-size: 1.1rem;
        font-weight: bold;
    }
    .course-btn:hover {
        transform: scale(1.02);
        opacity: 0.9;
    }
    .part-btn {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        cursor: pointer;
        margin: 0.4rem 0;
        transition: transform 0.2s;
        font-size: 1rem;
        font-weight: bold;
    }
    .part-btn:hover {
        transform: scale(1.02);
        opacity: 0.9;
    }
    .category-btn {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 0.8rem;
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
        margin: 0.3rem 0;
        transition: transform 0.2s;
        font-size: 0.95rem;
        font-weight: 500;
    }
    .category-btn:hover {
        transform: scale(1.02);
        opacity: 0.9;
    }
    .sub-btn {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        color: #1a1a2e;
        padding: 0.7rem 1rem;
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
        margin: 0.2rem 0;
        transition: transform 0.2s;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .sub-btn:hover {
        transform: scale(1.02);
        opacity: 0.9;
    }
    .knowledge-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .knowledge-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 0.8rem;
    }
    .knowledge-section {
        margin: 0.8rem 0;
        padding: 0.5rem 1rem;
        background: white;
        border-radius: 8px;
        border-left: 3px solid #764ba2;
    }
    .knowledge-section-title {
        font-weight: bold;
        color: #764ba2;
        font-size: 1.05rem;
        margin-bottom: 0.3rem;
    }
    .knowledge-text {
        line-height: 1.8;
        color: #333;
        font-size: 0.95rem;
        padding: 0.3rem 0;
    }
    .highlight-box {
        background: #fff3cd;
        padding: 0.8rem 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 0.5rem 0;
    }
    .breadcrumb {
        background: #f0f0f0;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        font-size: 0.9rem;
    }
    .breadcrumb span {
        color: #667eea;
        font-weight: bold;
    }
    .back-btn {
        background: #6c757d;
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 6px;
        border: none;
        cursor: pointer;
        font-size: 0.85rem;
        margin: 0.2rem 0;
    }
    .back-btn:hover {
        background: #5a6268;
    }
    .stButton button {
        width: 100%;
        margin: 0.2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ========== 知识点数据（完整层级结构） ==========
KNOWLEDGE_DATA = {
    "工程数值方法": {
        "误差与传播": {
            "基本概念": {
                "绝对误差": {
                    "原理": "绝对误差是指近似值与精确值之间的差值，反映了近似值的偏离程度。",
                    "核心思想": "用 e = x - x0 表示，其中 x 为近似值，x0 为精确值。绝对误差带有正负号，表示近似值相对于精确值的偏差方向和大小。",
                    "注意事项": "绝对误差只能反映误差的大小，不能反映误差的严重程度。对于不同量级的测量值，相同绝对误差的意义不同。"
                },
                "相对误差": {
                    "原理": "相对误差是绝对误差与精确值之比，反映了误差相对于被测量值的比例。",
                    "核心思想": "相对误差 = e/x0，通常用百分比表示。相对误差更能反映测量的精度，因为相同绝对误差对大小不同的量的影响不同。",
                    "注意事项": "当精确值接近零时，相对误差可能变得很大，此时需要特别注意。工程中通常要求相对误差在允许范围内。"
                },
                "有效数字": {
                    "原理": "有效数字是指从第一个非零数字开始，到最后一个数字为止的所有数字，包括最后一位可疑数字。",
                    "核心思想": "有效数字的位数反映了测量的精度，位数越多表示测量越精确。科学记数法可以清晰表达有效数字的位数。",
                    "注意事项": "判断有效数字时要注意：所有非零数字都是有效数字；零在数字中间是有效数字；零在数字前不是有效数字；零在数字后且在小数点后是有效数字。"
                },
                "截断误差": {
                    "原理": "截断误差是指用有限项级数或有限过程近似无限项或无限过程时产生的误差。",
                    "核心思想": "在数值计算中，为了避免无限计算，通常将无穷级数、无穷积分等截断为有限项，由此产生的误差即为截断误差。",
                    "注意事项": "截断误差的大小与截断位置有关，项数越多误差越小。需要根据精度要求合理选择截断位置，平衡计算量和精度。"
                },
                "舍入误差": {
                    "原理": "舍入误差是指由于计算机有限字长，对实数进行舍入处理时产生的误差。",
                    "核心思想": "计算机只能存储有限位数的数字，对超出位数的部分进行四舍五入或截断，由此产生舍入误差。",
                    "注意事项": "舍入误差会随计算次数累积，大量计算后可能产生显著误差。应避免两个相近的大数相减，防止有效数字丢失。"
                }
            },
            "误差传播": {
                "加法误差": {
                    "原理": "两个数相加时，误差也相加。加法运算的误差等于各加数误差之和。",
                    "核心思想": "对于和式 y = x1 + x2 + ... + xn，其误差等于各加数误差的绝对值之和。误差只会累积，不会相互抵消。",
                    "注意事项": "在实际计算中，应尽量避免误差较大的数参与加法运算。如果必须相加，应优先相加误差较小的数。"
                },
                "乘法误差": {
                    "原理": "两个数相乘时，误差按比例传递。乘法运算的相对误差等于各因子相对误差之和。",
                    "核心思想": "对于积式 y = x1 * x2 * ... * xn，其相对误差约等于各因子相对误差的绝对值之和。",
                    "注意事项": "乘法的误差传递与各因子的误差和量级有关。当某个因子误差特别大时，会显著影响结果的精度。"
                },
                "泰勒展开误差": {
                    "原理": "泰勒展开误差来源于用有限项多项式近似函数，余项即为截断误差。",
                    "核心思想": "泰勒展开的余项 R_n(x) = f^(n+1)(xi)/(n+1)! * (x-x0)^(n+1)，其中 xi 在 x0 和 x 之间。",
                    "注意事项": "余项的大小取决于函数的导数性质和展开点与计算点的距离。距离越远，误差越大。"
                }
            }
        },
        "插值与拟合": {
            "拉格朗日插值": {
                "原理": "拉格朗日插值通过构造基函数，使插值多项式精确通过所有已知数据点。",
                "核心思想": "基函数 L_i(x) 在对应节点处为1，在其他节点处为0。插值多项式 P(x) = sum(y_i * L_i(x))。",
                "注意事项": "拉格朗日插值在高阶时容易产生龙格现象（振荡）。节点数较多时，插值多项式在区间端点附近可能剧烈振荡。建议使用低阶插值或样条插值。"
            },
            "牛顿插值": {
                "原理": "牛顿插值通过递推计算差商，逐步构建插值多项式，便于增加插值节点。",
                "核心思想": "利用差商 f[x0,x1,...,xk] 递推计算，增加节点时不需要重新计算所有系数，只需计算新的差商。",
                "注意事项": "牛顿插值的优点是增加节点时不需要重新计算所有系数，只需计算新的差商。计算过程中差商的稳定性需要注意。"
            },
            "样条插值": {
                "原理": "样条插值采用分段低次多项式，在各段连接处满足连续性和光滑性条件。",
                "核心思想": "三次样条插值是最常用的形式，要求每段为三次多项式，且在节点处函数值、一阶导数、二阶导数都连续。",
                "注意事项": "样条插值具有良好的光滑性，不会产生龙格现象。但边界条件的选取会影响插值结果，常用的有自然样条和固定样条两种。"
            },
            "最小二乘拟合": {
                "原理": "最小二乘拟合通过最小化误差平方和，找到最优的拟合曲线，不要求曲线通过所有数据点。",
                "核心思想": "目标函数 S = sum((y_i - f(x_i))^2) 最小化。对于线性拟合，可通过正则方程求解。",
                "注意事项": "最小二乘拟合适用于数据存在测量误差的情况，通过平滑曲线反映整体趋势。拟合阶数的选择要避免过拟合或欠拟合。"
            },
            "勒让德正交多项式拟合": {
                "原理": "利用勒让德多项式在区间[-1,1]上的正交性，将函数展开为正交多项式级数。",
                "核心思想": "勒让德多项式 P0(x), P1(x), P2(x), ... 满足在[-1,1]上的正交性。利用正交性可独立求解各系数。",
                "注意事项": "正交多项式拟合具有数值稳定性好、系数独立求解等优点。但需要将数据变换到[-1,1]区间。"
            }
        },
        "代数问题": {
            "线性方程组-LU分解": {
                "原理": "LU分解将矩阵A分解为下三角矩阵L和上三角矩阵U的乘积，通过两次三角方程求解原方程组。",
                "核心思想": "A = LU，解方程组 Ax = b 等价于先解 Ly = b 得 y，再解 Ux = y 得 x。L是单位下三角矩阵。",
                "注意事项": "LU分解要求矩阵A的各阶顺序主子式不为零。如果矩阵奇异或接近奇异，需要加选主元来提高数值稳定性。"
            },
            "线性方程组-Cholesky分解": {
                "原理": "Cholesky分解是对称正定矩阵的一种特殊三角分解，A = LL^T，其中L为下三角矩阵。",
                "核心思想": "Cholesky分解利用了矩阵的对称正定性，计算量约为LU分解的一半，且数值稳定性好。",
                "注意事项": "Cholesky分解要求矩阵必须是对称正定的。如果矩阵不正定，分解过程中会出现负数开平方。"
            },
            "线性方程组-QR分解": {
                "原理": "QR分解将矩阵A分解为正交矩阵Q和上三角矩阵R的乘积，即A = QR。",
                "核心思想": "Q满足 Q^T Q = I，R为上三角矩阵。QR分解可通过Gram-Schmidt正交化或Householder变换实现。",
                "注意事项": "QR分解适用于任意矩阵，数值稳定性好。在求解最小二乘问题时特别有效。"
            },
            "线性方程组-SVD分解": {
                "原理": "SVD（奇异值分解）将任意矩阵A分解为A = U Sigma V^T，其中U和V是正交矩阵。",
                "核心思想": "Sigma的对角线元素为奇异值。SVD可以用于矩阵的伪逆、秩估计和低秩近似。",
                "注意事项": "SVD是最稳定的矩阵分解方法，但计算量较大。奇异值的分布反映了矩阵的性态。"
            },
            "非线性方程-二分法": {
                "原理": "二分法通过不断缩小区间，利用介值定理逐步逼近方程的根。",
                "核心思想": "若 f(a)*f(b) < 0，则(a,b)内有根。取中点c，判断根在(a,c)还是(c,b)，不断缩小区间。",
                "注意事项": "二分法保证收敛，但收敛速度较慢（线性收敛）。要求f(a)和f(b)异号。"
            },
            "非线性方程-牛顿法": {
                "原理": "牛顿法利用函数的切线近似，通过迭代逐步逼近方程的根。",
                "核心思想": "在x_n处作切线，切线与x轴的交点作为下一个近似值。迭代公式：x_{n+1} = x_n - f(x_n)/f'(x_n)。",
                "注意事项": "牛顿法具有二阶收敛速度，但要求初始值在根附近。需要计算导数，如果导数近似为零则迭代困难。"
            },
            "非线性方程-割线法": {
                "原理": "割线法用割线的斜率代替切线斜率，避免计算导数。",
                "核心思想": "利用前两步的近似值构造割线，迭代公式：x_{n+1} = x_n - f(x_n)*(x_n-x_{n-1})/(f(x_n)-f(x_{n-1}))。",
                "注意事项": "割线法不需要计算导数，但收敛速度介于二分法和牛顿法之间。需要两个初始值。"
            },
            "非线性方程组-牛顿法": {
                "原理": "将标量牛顿法推广到方程组，利用雅可比矩阵进行迭代。",
                "核心思想": "对于 F(x) = 0，迭代公式：x_{k+1} = x_k - J(x_k)^(-1)F(x_k)，其中J是雅可比矩阵。",
                "注意事项": "牛顿法对初始值敏感，雅可比矩阵的计算和求逆计算量大。对于大规模问题，可采用拟牛顿法。"
            },
            "非线性方程组-拟牛顿BFGS": {
                "原理": "BFGS用Hessian矩阵的近似值代替精确Hessian，减少计算量。",
                "核心思想": "利用梯度信息更新Hessian近似，满足割线条件。BFGS更新公式保证了Hessian近似保持正定。",
                "注意事项": "BFGS不需要显式计算二阶导数，对大规模问题特别有效。但收敛速度不如精确牛顿法快。"
            },
            "特征值与特征向量-幂法": {
                "原理": "幂法通过迭代向量不断向最大特征值对应的特征向量方向旋转。",
                "核心思想": "迭代：x_{k+1} = Ax_k/||Ax_k||，特征值估计 = x_k^T A x_k/(x_k^T x_k)。",
                "注意事项": "幂法只能求最大特征值及其特征向量，要求最大特征值严格大于其他特征值。"
            },
            "特征值与特征向量-反幂法": {
                "原理": "反幂法用于求解矩阵的最小特征值及其特征向量。",
                "核心思想": "对A进行LU分解，迭代求解 y = A^(-1)x_k，然后归一化。反幂法等同于对A^(-1)应用幂法。",
                "注意事项": "反幂法可以结合移位技术，用于求解最接近某个给定值的特征值。"
            },
            "特征值与特征向量-子空间迭代法": {
                "原理": "子空间迭代法同时求解多个最大特征值和对应的特征向量。",
                "核心思想": "构造一个k维子空间，在子空间内进行投影，求解投影矩阵的特征值问题。",
                "注意事项": "子空间迭代法适用于需要计算多个特征值的场合。收敛速度与幂法类似。"
            },
            "特征值与特征向量-Krylov子空间法": {
                "原理": "Krylov子空间法利用Krylov子空间进行投影，求解大规模稀疏矩阵的特征值问题。",
                "核心思想": "Krylov子空间定义为 K_k = span{r, Ar, A^2r, ..., A^(k-1)r}。通过Lanczos或Arnoldi过程构造正交基。",
                "注意事项": "Krylov子空间法是求解大型稀疏矩阵特征值问题最有效的方法之一。"
            }
        },
        "连续问题": {
            "数值积分-复合辛普森": {
                "原理": "复合辛普森法是将积分区间等分成n个子区间，在每个子区间上用辛普森公式近似积分。",
                "核心思想": "辛普森公式在每个小区间上用二次插值多项式近似被积函数，得到 ∫ f(x)dx ≈ h/6[f(x_i) + 4f(x_{i+1}) + f(x_{i+2})]。",
                "注意事项": "复合辛普森的误差为O(h^4)，精度较高。要求子区间数n为偶数。积分区间内函数必须是光滑的。"
            },
            "数值积分-高斯积分": {
                "原理": "高斯积分通过优化积分点位置，使代数精度达到2n-1阶。",
                "核心思想": "选择n个积分点和权重，使得积分公式对2n-1阶以下多项式精确成立。积分点通常取正交多项式的零点。",
                "注意事项": "高斯积分具有最高的代数精度，但积分点和权重需要事先计算。常用的有高斯-勒让德积分等。"
            },
            "数值微分-差商": {
                "原理": "差商是用函数值的差商近似导数，是数值微分的基本方法。",
                "核心思想": "前向差商：f'(x) ≈ (f(x+h)-f(x))/h；中心差商：f'(x) ≈ (f(x+h)-f(x-h))/(2h)。",
                "注意事项": "中心差商精度最高（O(h^2)）。步长h的选取需要权衡截断误差和舍入误差。"
            },
            "常微分方程-欧拉法": {
                "原理": "欧拉法是一阶显式方法，用切线近似在下一步的值。",
                "核心思想": "对于初值问题 dy/dx = f(x,y)，欧拉法给出 y_{n+1} = y_n + h f(x_n, y_n)。",
                "注意事项": "欧拉法是条件稳定的，步长h需要满足稳定性条件。精度只有一阶（O(h)）。"
            },
            "常微分方程-四阶龙格库塔": {
                "原理": "RK4法通过计算四个不同位置的斜率，取加权平均提高精度。",
                "核心思想": "RK4在每步计算四个斜率，然后 y_{n+1} = y_n + h/6(k1+2k2+2k3+k4)。",
                "注意事项": "RK4是四阶精度（O(h^4)），是工程中最常用的ODE求解器。计算量大但稳定性好。"
            },
            "常微分方程-Newmark法": {
                "原理": "Newmark法是结构动力学中常用的隐式时间积分方法，具有无条件稳定性。",
                "核心思想": "Newmark法用Taylor展开近似位移和速度，通过参数beta和gamma控制算法的稳定性和精度。",
                "注意事项": "Newmark法适用于求解二阶ODE系统，特别是结构振动问题。参数选择影响算法的能量耗散性质。"
            },
            "常微分方程-Newmark加牛顿": {
                "原理": "对于非线性动力学问题，将Newmark法与Newton迭代结合，求解非线性方程组。",
                "核心思想": "在每个时间步，先用Newmark法对位移和速度进行预测，然后用Newton法求解非线性平衡方程。",
                "注意事项": "牛顿迭代需要计算切线刚度矩阵，每次迭代都需要更新。收敛性依赖于初始预测值。"
            },
            "常微分方程-打靶法": {
                "原理": "打靶法将边值问题转化为初值问题，通过调整初始参数使解满足边界条件。",
                "核心思想": "猜测缺失的初始条件，用初值问题求解器积分到另一端，检查是否满足边界条件，调整猜测值重复计算。",
                "注意事项": "打靶法对初值猜测敏感，可能需要多次迭代。对于刚性问题可能失效。"
            },
            "偏微分方程-有限差分法": {
                "原理": "有限差分法用离散网格上的差分近似代替连续区域中的微分，将PDE转化为代数方程组。",
                "核心思想": "将求解域划分成网格，用中心差分等近似偏导数，在每个网格点上建立代数方程。",
                "注意事项": "有限差分法的精度取决于网格大小，收敛性和稳定性与差分格式有关。处理复杂边界时较困难。"
            },
            "偏微分方程-伽辽金法": {
                "原理": "伽辽金法是加权残值法的一种，用基函数作为权函数，使残值在加权积分意义下为零。",
                "核心思想": "假设近似解 u_h = sum(c_j * phi_j)，代入微分方程得残值R。令 ∫ phi_i * R dOmega = 0。",
                "注意事项": "伽辽金法具有良好的精度和稳定性，是有限元法的理论基础。基函数的选择对结果影响很大。"
            }
        }
    }
}

# ============================================================
# 导航状态管理
# ============================================================
if 'level' not in st.session_state:
    st.session_state.level = 'course'
if 'course' not in st.session_state:
    st.session_state.course = '工程数值方法'
if 'part' not in st.session_state:
    st.session_state.part = None
if 'category' not in st.session_state:
    st.session_state.category = None
if 'sub' not in st.session_state:
    st.session_state.sub = None

# ============================================================
# 导航函数
# ============================================================
def go_to_course():
    st.session_state.level = 'course'
    st.session_state.part = None
    st.session_state.category = None
    st.session_state.sub = None

def go_to_part(part_name):
    st.session_state.level = 'part'
    st.session_state.part = part_name
    st.session_state.category = None
    st.session_state.sub = None

def go_to_category(category_name):
    st.session_state.level = 'category'
    st.session_state.category = category_name
    st.session_state.sub = None

def go_to_sub(sub_name):
    st.session_state.level = 'sub'
    st.session_state.sub = sub_name

def go_back():
    if st.session_state.level == 'sub':
        st.session_state.level = 'category'
        st.session_state.sub = None
    elif st.session_state.level == 'category':
        st.session_state.level = 'part'
        st.session_state.category = None
    elif st.session_state.level == 'part':
        st.session_state.level = 'course'
        st.session_state.part = None

# ============================================================
# 渲染函数
# ============================================================
def render_course():
    st.markdown("""
    <div class="review-header">
        <h1>📚 工程数值方法</h1>
        <p>点击下方四个部分，逐层深入复习</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📖 选择复习部分")
    
    parts = ["误差与传播", "插值与拟合", "代数问题", "连续问题"]
    
    col1, col2 = st.columns(2)
    
    for i, part in enumerate(parts):
        if i % 2 == 0:
            with col1:
                if st.button(f"📌 {part}", key=f"course_{part}", use_container_width=True):
                    go_to_part(part)
                    st.rerun()
        else:
            with col2:
                if st.button(f"📌 {part}", key=f"course_{part}", use_container_width=True):
                    go_to_part(part)
                    st.rerun()

def render_part(part_name):
    st.markdown(f"""
    <div class="review-header">
        <h1>📖 {part_name}</h1>
        <p>选择具体分类，深入了解</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 面包屑导航
    st.markdown(f"""
    <div class="breadcrumb">
        📚 <span>工程数值方法</span> → <span>{part_name}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 返回按钮
    if st.button("⬅ 返回课程", use_container_width=False):
        go_to_course()
        st.rerun()
    
    st.markdown("---")
    st.markdown(f"### 📂 {part_name} - 分类")
    
    part_data = KNOWLEDGE_DATA["工程数值方法"][part_name]
    categories = list(part_data.keys())
    
    for category in categories:
        if st.button(f"📁 {category}", key=f"part_{category}", use_container_width=True):
            go_to_category(category)
            st.rerun()

def render_category(part_name, category_name):
    st.markdown(f"""
    <div class="review-header">
        <h1>📖 {category_name}</h1>
        <p>选择具体知识点，查看详细介绍</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 面包屑导航
    st.markdown(f"""
    <div class="breadcrumb">
        📚 <span>工程数值方法</span> → <span>{part_name}</span> → <span>{category_name}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 返回按钮
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("⬅ 返回", use_container_width=False):
            go_to_part(part_name)
            st.rerun()
    
    st.markdown("---")
    st.markdown(f"### 📂 {category_name} - 知识点列表")
    
    category_data = KNOWLEDGE_DATA["工程数值方法"][part_name][category_name]
    sub_items = list(category_data.keys())
    
    for sub in sub_items:
        if st.button(f"📄 {sub}", key=f"cat_{sub}", use_container_width=True):
            go_to_sub(sub)
            st.rerun()

def render_sub(part_name, category_name, sub_name):
    # 获取知识点数据
    data = KNOWLEDGE_DATA["工程数值方法"][part_name][category_name][sub_name]
    
    st.markdown(f"""
    <div class="review-header">
        <h1>📖 {sub_name}</h1>
        <p>详细知识点介绍</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 面包屑导航
    st.markdown(f"""
    <div class="breadcrumb">
        📚 <span>工程数值方法</span> → <span>{part_name}</span> → <span>{category_name}</span> → <span>{sub_name}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 返回按钮
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("⬅ 返回", use_container_width=False):
            go_to_category(category_name)
            st.rerun()
    
    st.markdown("---")
    
    # 显示知识点
    st.markdown(f"""
    <div class="knowledge-card">
        <div class="knowledge-title">🔍 {sub_name}</div>
        
        <div class="knowledge-section">
            <div class="knowledge-section-title">📌 原理</div>
            <div class="knowledge-text">{data['原理']}</div>
        </div>
        
        <div class="knowledge-section">
            <div class="knowledge-section-title">💡 核心思想</div>
            <div class="knowledge-text">{data['核心思想']}</div>
        </div>
        
        <div class="highlight-box">
            <strong>⚠️ 注意事项</strong><br>
            {data['注意事项']}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# 主程序
# ============================================================
def main():
    # 根据当前层级渲染
    if st.session_state.level == 'course':
        render_course()
    elif st.session_state.level == 'part':
        render_part(st.session_state.part)
    elif st.session_state.level == 'category':
        render_category(st.session_state.part, st.session_state.category)
    elif st.session_state.level == 'sub':
        render_sub(st.session_state.part, st.session_state.category, st.session_state.sub)

if __name__ == "__main__":
    main()