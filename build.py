import subprocess
import os

def main():
    icon_path = os.path.join(os.getcwd(), "user.png")  # 获取 user.png 的完整路径
    files = [file for file in os.listdir() if file.endswith(".py")]  # 获取所有的 .py 文件
    for file in files:
        subprocess.call(["pyinstaller", "--onefile", "--noconsole", "--icon", icon_path, file])

if __name__ == "__main__":
    main()
