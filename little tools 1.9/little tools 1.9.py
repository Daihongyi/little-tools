from tkinter import  messagebox, filedialog
import random
import time
import tkinter as tk
import pygame
import base64

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def tools_time():
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return time_now


def tools_randint(least, max, many, remake):
    number_return = []
    if remake == True:
        for i in range(many):
            a = random.randint(least, max)
            number_return.append(a)
        return number_return
    elif remake == False:
        while len(number_return) < many:
            a = random.randint(least, max)
            if a not in number_return:
                number_return.append(a)
        return number_return


def tools_prime_number(number):
    factor_number = 0
    factor = []
    for i in range(1, number + 1):
        if number % i == 0:
            factor_number += 1
            factor.append(i)
    if factor_number == 2:
        return "质数", factor_number, factor
    elif factor_number >= 3:
        return "合数", factor_number, factor
    else:
        return "错误", factor_number, factor


def aes_encrypt(plain_text, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    padded_data = pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    encrypted_text = base64.b64encode(encrypted)  # 直接编码为base64字符串
    with open('encrypted.txt', 'wb') as f:
        f.write(encrypted_text)
    return encrypted_text  # 返回加密后的文本


def aes_decrypt(encrypted_text, key):
    encrypted_bytes = base64.b64decode(encrypted_text)  # 先将base64字符串解码为字节
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_padded = cipher.decrypt(encrypted_bytes)
    decrypt_text = unpad(decrypted_padded, AES.block_size).decode('utf-8')
    with open('decrypted.txt', 'wb') as f:
        f.write(decrypt_text.encode('utf-8'))
    return decrypt_text


def tools_mp3_player():
    pygame.mixer.init()
    player_main_window = tk.Tk()
    player_main_window.geometry("400x150")
    player_main_window.title("Audio player")

    music_file = None
    is_paused = False
    mp3_file_name = None
    def choose_file():
        nonlocal music_file , mp3_file_name
        music_file = filedialog.askopenfilename(title="选择一个音频文件", filetypes=[("Audio files", ["*.mp3","*.wav", "*.ogg"])])
        if music_file:
            if mp3_file_name:
                mp3_file_name.config(text="当前文件" + music_file)
            else:
                mp3_file_name = tk.Label(player_main_window, text="当前文件" + music_file)
                mp3_file_name.place(y=25)

    def play_music():
        nonlocal is_paused
        if music_file:
            try:
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play()
                is_paused = False
            except pygame.error as e:
                messagebox.showerror("错误", f"载入音乐时出错: {e}")

    def pause_resume_music():
        nonlocal is_paused
        if not is_paused:
            pygame.mixer.music.pause()
            pause_resume_button.config(text="继续")
            is_paused = True
        else:
            pygame.mixer.music.unpause()
            pause_resume_button.config(text="暂停")
            is_paused = False

    def stop_music():
        nonlocal is_paused
        pygame.mixer.music.stop()
        is_paused = False

    def exit_player():
        stop_music()
        player_main_window.destroy()

    # 创建播放按钮
    play_button = tk.Button(player_main_window, text="播放", command=play_music,activeforeground="blue",relief ="groove")
    play_button.place(x=25, y=100)

    # 创建暂停/继续按钮
    pause_resume_button = tk.Button(player_main_window, text="暂停", command=pause_resume_music,activeforeground="blue",relief ="groove")
    pause_resume_button.place(x=75, y=100)

    # 创建停止按钮
    stop_button = tk.Button(player_main_window, text="停止", command=stop_music,activeforeground="blue",relief ="groove")
    stop_button.place(x=125, y=100)

    # 创建选择文件按钮
    choose_file_button = tk.Button(player_main_window, text="选择文件", command=choose_file,activeforeground="blue",relief ="groove")
    choose_file_button.place(x=175, y=100)

    exit_player_button = tk.Button(player_main_window, text="退出", command=exit_player,activeforeground="blue",relief ="groove")
    exit_player_button.place(x=250, y=100)

    player_main_window.mainloop()


def main():
    color_list = ["blue", "green", "purple",  "#4FCDF5"]

    def add_line_break(list, length):
        element_len = 0
        list_str = ""
        for i in list:
            list_str += str(i) + " "
            element_len += 1
            if element_len % length == 0:
                list_str += "\n"
        return list_str

    def no_space_add_line_break(list, length):
        element_len = 0
        list_str = ""
        for i in list:
            list_str += str(i)
            element_len += 1
            if element_len % length == 0:
                list_str += "\n"
        return list_str

    main_window = tk.Tk()
    main_window.geometry("600x400")
    main_window.title("little tools 1.9")






    def gui_random_numbers():
        random_numbers_window = tk.Toplevel(main_window)
        random_numbers_window.title("随机数生成")
        random_numbers_window.geometry("300x225")

        least_val_entry = tk.Entry(random_numbers_window)
        max_val_entry = tk.Entry(random_numbers_window)
        count_entry = tk.Entry(random_numbers_window)
        remake_entry = tk.Entry(random_numbers_window)
        least_val_label = tk.Label(random_numbers_window, text="最小值")
        max_val_label = tk.Label(random_numbers_window, text="最大值")
        count_label = tk.Label(random_numbers_window, text="数量")
        remake_label = tk.Label(random_numbers_window, text="允许重复(y/n)")
        random_numbers_label = tk.Label(random_numbers_window, text="生成的随机数为：", fg=random.choice(color_list))
        exit_button = tk.Button(random_numbers_window, text="退出", command=random_numbers_window.destroy,activeforeground="blue",relief ="groove")
        least_val_entry.place(x=80, y=20)
        max_val_entry.place(x=80, y=50)
        count_entry.place(x=80, y=80)
        remake_entry.place(x=90, y=110)
        least_val_label.place(x=10, y=20)
        max_val_label.place(x=10, y=50)
        count_label.place(x=10, y=80)
        remake_label.place(x=10, y=110)
        random_numbers_label.place(x=10, y=140)
        random_numbers_label['justify'] = 'left'
        exit_button.place(x=250, y=175)

        def get_random_numbers():
            try:
                least_val = int(least_val_entry.get())
                max_val = int(max_val_entry.get())
                count = int(count_entry.get())
                remake = remake_entry.get().lower()
            except:
                messagebox.showerror("错误", "请输入整数")
                return
            if remake not in ['y', 'n']:
                messagebox.showerror("错误", "请输入y或n")
                return
            if remake == 'y':
                if max_val < least_val:
                    messagebox.showerror("错误", "最大值小于最小值")
                    return
                random_numbers = tools_randint(least_val, max_val, count, True)
                random_numbers_label.config(text="生成的随机数为：\n" + add_line_break(random_numbers, 8))
            else:
                if max_val < least_val:
                    messagebox.showerror("错误", "最大值小于最小值")
                    return
                if max_val - least_val + 1 < count:
                    messagebox.showerror("错误", "最大值与最小值之差小于数量")
                    return
                random_numbers = tools_randint(least_val, max_val, count, False)
                random_numbers_label.config(text="生成的随机数为：\n" + add_line_break(random_numbers, 8))

        make_button = tk.Button(random_numbers_window, text="生成", command=get_random_numbers,activeforeground="blue",relief ="groove")
        make_button.place(x=250, y=20)
        random_numbers_window.mainloop()

    def gui_prime_number():
        prime_number_window = tk.Toplevel(main_window)
        prime_number_window.title("质数判断器")
        prime_number_window.geometry("300x225")

        number_entry = tk.Entry(prime_number_window)
        number_text = tk.Label(prime_number_window, text="请输入需要判断的数")
        result_type_label = tk.Label(prime_number_window, text="是否为质数：")
        factor_count_label = tk.Label(prime_number_window, text="因数个数：")
        factors_label = tk.Label(prime_number_window, text="因数列表：")
        factors_label['justify'] = 'left'
        exit_button = tk.Button(prime_number_window, text="退出", command = prime_number_window.destroy,activeforeground="blue",relief ="groove")
        number_entry.place(x=140, y=20)
        number_text.place(x=10, y=20)
        result_type_label.place(x=10, y=60)
        factor_count_label.place(x=10, y=90)
        factors_label.place(x=10, y=120)
        exit_button.place(x=250, y=175)

        def get_prime_number():

            try:
                number = int(number_entry.get())
            except ValueError:
                messagebox.showerror("错误", "在获取输入时发生错误，请检查输入是否为整数")
                return
            if number <= 0:
                messagebox.showerror("错误", "请输入大于0的整数")
                return
            else:
                result_type, factor_count, factors = tools_prime_number(number)
                if result_type == "质数":
                    result_type_label.config(text="是否为质数：是")
                    factor_count_label.config(text="因数个数：" + str(factor_count))
                    factors_label.config(text="因数列表：\n" + add_line_break(factors, 8))
                else:
                    result_type_label.config(text="是否为质数：否")
                    factor_count_label.config(text="因数个数：" + str(factor_count))
                    factors_label.config(text="因数列表：\n" + add_line_break(factors, 8))

        prime_number_button = tk.Button(prime_number_window, text="判断", command=get_prime_number,activeforeground="blue",relief ="groove")
        prime_number_button.place(x=250, y=50)
        prime_number_window.mainloop()

    def gui_encipher():
        encipher_window = tk.Toplevel(main_window)
        encipher_window.title("文本加密")
        encipher_window.geometry("300x225")

        text_entry = tk.Entry(encipher_window, width=50)
        text_label = tk.Label(encipher_window, text="文本")
        key_entry = tk.Entry(encipher_window, width=50, show='*')
        key_label = tk.Label(encipher_window, text="密钥")
        secret_key_warning_label = tk.Label(encipher_window, text="密钥需为16, 24, 或32个字符", fg="red")
        encipher_label = tk.Label(encipher_window, text="加密后的文本：\n(加密完成后会写入当前目录下的encrypted.txt)\n",
                                  fg=random.choice(color_list))
        encipher_label['justify'] = 'left'

        def get_encrypted_text():
            try:
                text = text_entry.get()
                key = key_entry.get()
                if len(key) not in [16, 24, 32]:
                    messagebox.showerror("错误", "密钥长度必须为16, 24, 或32个字符")
                    return
                encrypted_text = aes_encrypt(text, key)

                encrypted_text_str = encrypted_text.decode('utf-8')
                encipher_label.config(text="加密后的文本:\n" + no_space_add_line_break(encrypted_text_str, 35))
            except Exception as e:
                messagebox.showerror("错误", f"加密失败: {e}")

        encrypt_button = tk.Button(encipher_window, text="加密", command=get_encrypted_text,activeforeground="blue",relief ="groove")
        exit_button = tk.Button(encipher_window, text="退出", command=encipher_window.destroy,activeforeground="blue",relief ="groove")

        text_entry.place(x=50, y=20, width=175)
        key_entry.place(x=50, y=60, width=175)
        text_label.place(x=10, y=20)
        key_label.place(x=10, y=60)
        encipher_label.place(x=10, y=90)
        secret_key_warning_label.place(x=10, y=175)
        encrypt_button.place(x=250, y=20)
        exit_button.place(x=250, y=175)

    def gui_decrypt():
        decrypt_window = tk.Toplevel(main_window)
        decrypt_window.title("文本解密")
        decrypt_window.geometry("300x225")

        encipher_text_entry = tk.Entry(decrypt_window, width=50)
        encipher_text_label = tk.Label(decrypt_window, text="密文")
        secret_key_warning_label = tk.Label(decrypt_window, text="密钥需为16, 24, 或32个字符", fg="red")
        secret_key_entry = tk.Entry(decrypt_window, width=50, show='*')
        secret_key_label = tk.Label(decrypt_window, text="密钥：")
        decrypt_label = tk.Label(decrypt_window, text="解密后的文本:\n(解密完成后会写入当前目录下的decrypted.txt)\n",
                                 fg=random.choice(color_list))
        decrypt_label['justify'] = 'left'

        def get_decrypted_text():
            try:
                encipher_text = encipher_text_entry.get()
                secret_key = secret_key_entry.get()
                if not encipher_text or not secret_key:
                    messagebox.showerror("错误", "请输入加密文本和密钥")
                    return

                decrypted_text = aes_decrypt(encipher_text, secret_key)
                decrypt_label.config(text="解密后的文本：\n" + no_space_add_line_break(decrypted_text, 35))
            except Exception as e:
                messagebox.showerror("错误", f"解密失败: {e}")

        decrypt_button = tk.Button(decrypt_window, text="解密", command=get_decrypted_text,activeforeground="blue",relief ="groove")
        exit_button = tk.Button(decrypt_window, text="退出", command=decrypt_window.destroy,activeforeground="blue",relief ="groove")

        encipher_text_entry.place(x=50, y=20, width=175)
        secret_key_entry.place(x=50, y=60, width=175)
        encipher_text_label.place(x=0, y=20)
        secret_key_label.place(x=0, y=60)
        decrypt_label.place(x=10, y=90)
        secret_key_warning_label.place(x=10, y=175)
        decrypt_button.place(x=250, y=20)
        exit_button.place(x=250, y=175)
        decrypt_window.mainloop()

    def gui_now_time():
        time_source = tk.Label(main_window, text="时间来源：本地", font=("Arial", 10),fg="blue")
        time_source.place(x=500, y=125)

        def update_time():
            url = "http://mshopact.vivo.com.cn/tool/config/"
            try:
                response = requests.get(url)
                response.raise_for_status()  # 检查请求是否成功
                data = response.json()
                if data['success']:
                    time_source.config(text="时间来源：vivo", fg="blue")
                    now_time = data['data']['nowTime']
                    str_now_time = time.strftime("%m/%d %H:%M:%S\n%a", time.localtime(now_time / 1000))
                    time_label.config(text=str_now_time)
                    main_window.after(1000, update_time)
                else:
                    time_source.config(text="时间来源：本地", fg="black")
                    now = time.strftime("%m/%d %H:%M:%S\n%a")
                    time_label.config(text=now)
                    main_window.after(1000, update_time)
            except requests.exceptions.RequestException as e:
                # 处理请求异常
                time_source.config(text="时间来源：本地", fg="black")
                now = time.strftime("%m/%d %H:%M:%S\n%a")
                time_label.config(text=now)
                main_window.after(1000, update_time)

        time_label = tk.Label(main_window, font=("Arial", 30), fg=random.choice(color_list))
        time_label.place(x=300, y=25)

        update_time()

    def gui_new_edition():
        messagebox.showinfo("新版本介绍", "版本号:1.9 更新内容:时间功能将优先使用在线时间API\n若失败则使用本地时间\nGUI调整")

    def exit():
        main_window.destroy()

    button_randint = tk.Button(main_window, text="随机数生成", command=gui_random_numbers,activeforeground="blue",relief ="groove")
    button_randint.place(x=25, y=25)

    button_prime_number = tk.Button(main_window, text="质数判断", command=gui_prime_number,activeforeground="blue",relief ="groove")
    button_prime_number.place(x=100, y=25)

    button_encipher = tk.Button(main_window, text="加密文本", command=gui_encipher,activeforeground="blue",relief ="groove")
    button_encipher.place(x=25, y=75)

    button_decrypt = tk.Button(main_window, text="解密文本", command=gui_decrypt,activeforeground="blue",relief ="groove")
    button_decrypt.place(x=100, y=75)

    button_time = tk.Button(main_window, text="查看时间", command=gui_now_time,activeforeground="blue",relief ="groove")
    button_time.place(x=175, y=25)

    button_mp3_player = tk.Button(main_window, text="音乐播放", command=tools_mp3_player,activeforeground="blue",relief ="groove")
    button_mp3_player.place(x=175, y=75)

    button_new_edition = tk.Button(main_window, text="新版本介绍", command=gui_new_edition,activeforeground="blue",relief ="groove")
    button_new_edition.place(x=450, y=350)

    button_exit = tk.Button(main_window, text="退出", command=exit,activeforeground="blue",relief ="groove")
    button_exit.place(x=550, y=350)

    about1 = tk.Label(main_window, text="本产品由北极星工作室——DHY荣誉出品", fg="blue")
    about2 = tk.Label(main_window, text="源码请访问 https://github.com/Daihongyi/little-tools")
    about3 = tk.Label(main_window, text="邮箱：17717460527@163.com", fg="#4FCDF5")
    about4 = tk.Label(main_window, text="北极星工作室官网：https://northstar.us.kg/", fg="red")
    about1.place(y=200)
    about2.place(y=250)
    about3.place(y=300)
    about4.place(y=350)
    # 启动事件循环
    main_window.mainloop()


if __name__ == "__main__":
    main()

