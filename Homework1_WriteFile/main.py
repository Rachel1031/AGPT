# 写入文本内容到文件
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print("内容已成功写入文件。")
    except Exception as e:
        print(f"写入文件时发生错误: {e}")

# 从文件中读取文本内容
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

# 主程序
if __name__ == "__main__":
    file_name = "sample.txt"

    while True:
        print("1. 写入文本内容到文件")
        print("2. 从文件中读取文本内容")
        print("3. 退出程序")
        choice = input("请选择操作 (1/2/3): ")

        if choice == "1":
            content = input("请输入要写入文件的文本内容: ")
            write_to_file(file_name, content)
        elif choice == "2":
            file_content = read_from_file(file_name)
            if file_content is not None:
                print("从文件中读取的内容:")
                print(file_content)
        elif choice == "3":
            print("退出程序。")
            break
        else:
            print("无效的选择，请重新输入。")
