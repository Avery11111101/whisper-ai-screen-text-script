import subprocess
import sys
import os

def check_whisper():
    try:
        subprocess.run(["whisper", "--help"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def install_whisper():
    print("正在安裝 Whisper...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "git+https://github.com/openai/whisper.git"], check=True)
        print("Whisper 安裝成功")
    except subprocess.CalledProcessError:
        print("Whisper 安裝失敗，請檢查您的網絡連接或 Python 環境")
        sys.exit(1)

def process_audio(file_path):
    print(f"正在處理音檔文件: {file_path}")
    try:
        subprocess.run(["whisper", file_path, "--model", "turbo", "--language", "zh"], check=True)
        print("音檔處理完成")
    except subprocess.CalledProcessError:
        print("音檔處理失敗")

def main():
    try:
        while True:
            audio_file = input("請輸入音檔文件名（例如：錄音 9.m4a），或按 Ctrl+C 退出：").strip()
            if not audio_file:
                print("文件名不能為空，請重新輸入。")
                continue
            
            if not os.path.exists(audio_file):
                print(f"錯誤：找不到音檔文件 '{audio_file}'")
                continue
            
            break

        if not check_whisper():
            install_whisper()
        
        process_audio(audio_file)

    except KeyboardInterrupt:
        print("\n程式已被用戶中斷。")
        sys.exit(0)

if __name__ == "__main__":
    main()
