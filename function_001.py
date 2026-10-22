# 1. 定义自定义的幂函数
def custom_power(base, exp):
    # 处理 0 次幂的情况
    if exp == 0:
        return 1
    
    # 初始化结果为 1
    result = 1
    
    # 取指数的绝对值用于循环乘法
    # 比如 2^-3，我们需要先算 2^3，再取倒数
    abs_exp = abs(exp)
    
    # 使用循环进行迭代乘法
    for _ in range(abs_exp):
        result *= base
        
    # 处理负指数的情况
    if exp < 0:
        return 1 / result
    
    # 返回最终结果
    return result

# 2. 更新 calculate 函数，调用 custom_power
def calculate(a, b):
    # 按照要求，这里直接返回计算结果即可
    return custom_power(a, b)

# 3. 测试代码（对应文档里的测试用例）
if __name__ == "__main__":
    print("--- 基础测试 ---")
    print(calculate(2, 5))   # 预期: 32
    print(calculate(5, -2))  # 预期: 0.04
    print(calculate(3, 0))   # 预期: 1.0
    
    print("\n--- 进阶双重确认测试 ---")
    print(calculate(15, -2)) # 预期: 0.0044444444444444444
    print(calculate(12.5, 2))# 预期: 156.25
    print(calculate(-12.4, 3))# 预期: -1906.6240000000003
    print(calculate(105, 3)) # 预期: 1157625.0