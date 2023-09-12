def counter(func):
    # 使用闭包来保存调用次数
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"函数 {func.__name__} 已经被调用 {count} 次")
        return func(*args, **kwargs)

    return wrapper


# 使用装饰器将计数器应用于特定函数
@counter
def some_function():
    print("这是一个示例函数")


@counter
def another_function():
    print("这是另一个示例函数")


if __name__ == "__main__":
    some_function()
    some_function()
    another_function()
    another_function()
    some_function()
