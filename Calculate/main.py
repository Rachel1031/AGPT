def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("除数不能为零")
    return x / y

while True:
    try:
        # 获取用户输入
        num1 = float(input("请输入第一个数字: "))
        operator = input("请输入运算符 (+, -, *, /): ")
        num2 = float(input("请输入第二个数字: "))

        # 执行相应的操作
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("无效的运算符")
            continue

        print(f"结果: {result}")

    except ValueError as e:
        print(f"错误: {e}")
    except ZeroDivisionError:
        print("错误: 除数不能为零")
    except Exception as e:
        print(f"发生未知错误: {e}")

    choice = input("继续计算？(yes/no): ")
    if choice.lower() != "yes":
        break
