from tkinter import simpledialog, messagebox , filedialog
import random
import time
import tkinter as tk
import pygame


def tools_randint(least,max, many, remake):
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

def tools_encipher(text, secret_key):
    text_return = ""
    ascii_element = ""
    no_ascii_element = ""
    ascii_text = []
    ascii_secret_key = []
    ascii_encipher_text = []
    no_ascii_encipher_text = []
    for i in text:
        ascii_element = ord(i)
        ascii_text.append(ascii_element)
    for i in secret_key:
        ascii_element = ord(i)
        ascii_secret_key.append(ascii_element)
    for i in range(len(ascii_text)):
        ascii_element = ascii_text[i] + ascii_secret_key[i % len(ascii_secret_key)]
        ascii_encipher_text.append(ascii_element)
    for i in ascii_encipher_text:
        no_ascii_element = chr(i)
        no_ascii_encipher_text.append(no_ascii_element)
    for i in no_ascii_encipher_text:
        text_return = text_return + i
    origin_time = time.localtime()
    now_time = time.strftime("%Y%m%d%H%M%S", origin_time)
    with open("little tools" + now_time + "加密结果.txt", encoding="gbk", mode="w")as f:
        f.write(text_return)
    return text_return

def tools_decrypt(encipher_text, secret_key):
    no_ascii_text = []
    ascii_text = []
    text_return = ""
    ascii_element = ""
    no_ascii_element = ""
    ascii_encipher_text = []
    ascii_secret_key = []
    ascii_encipher_text = []
    for i in encipher_text:
        ascii_element = ord(i)
        ascii_encipher_text.append(ascii_element)
    for i in secret_key:
        ascii_element = ord(i)
        ascii_secret_key.append(ascii_element)
    for i in range(len(ascii_encipher_text)):
        ascii_element = ascii_encipher_text[i] - ascii_secret_key[i % len(ascii_secret_key)]
        ascii_text.append(ascii_element)
    for i in ascii_text:
        no_ascii_element = chr(i)
        no_ascii_text.append(no_ascii_element)
    for i in no_ascii_text:
        text_return = text_return + i
    origin_time = time.localtime()
    now_time = time.strftime("%Y%m%d%H%M%S", origin_time)
    with open("little tools" + now_time + "解密结果.txt", encoding="gbk", mode="w")as f:
        f.write(text_return)
    return text_return



def tools_mp3_player():
    pygame.mixer.init()  # 初始化pygame mixer
    player_main_window = tk.Tk()
    player_main_window.geometry("400x150")
    player_main_window.title("MP3 player")
    music_file = None
    is_paused = False

    def choose_file():
        nonlocal music_file
        music_file = filedialog.askopenfilename(title="选择一个MP3文件", filetypes=[("MP3 files", "*.mp3")])
        if music_file:
            mp3_file_name = tk.Label(player_main_window,text = "当前文件" + music_file)
            mp3_file_name.place(y = 25)

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
    play_button = tk.Button(player_main_window, text="播放", command=play_music)
    play_button.place(x = 25 , y = 100)

    # 创建暂停/继续按钮
    pause_resume_button = tk.Button(player_main_window, text="暂停", command=pause_resume_music)
    pause_resume_button.place(x = 75 , y = 100)

    # 创建停止按钮
    stop_button = tk.Button(player_main_window, text="停止", command=stop_music)
    stop_button.place(x = 125 , y = 100)

    # 创建选择文件按钮
    choose_file_button = tk.Button(player_main_window, text="选择文件", command=choose_file)
    choose_file_button.place(x = 175 , y = 100)

    exit_player_button = tk.Button(player_main_window, text="退出", command=exit_player)
    exit_player_button.place(x = 250 , y = 100)

    player_main_window.mainloop()

    

    

        



def main():
    color_list = ["blue", "green","purple", "orange","#4FCDF5"]

    def add_line_break(list,length):
        list_str = ""
        for i in list:
            list_str += str(i) + " "
            if (i+1) % length == 0:
                list_str += "\n"
        return list_str


    main_window = tk.Tk()
    main_window.geometry("600x400")
    main_window.title("little tools 1.6")

    def handle_random_numbers():
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
        random_numbers_label = tk.Label(random_numbers_window, text="生成的随机数为：",fg=random.choice(color_list))
        exit_button = tk.Button(random_numbers_window, text="退出", command=random_numbers_window.destroy)
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
        exit_button.place(x=250, y=60)
        def generate_random_numbers():
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
                random_numbers_label.config(text="生成的随机数为：\n" +add_line_break(random_numbers,5))
            else:
                if max_val < least_val:
                    messagebox.showerror("错误", "最大值小于最小值")
                    return
                if max_val - least_val + 1 < count:
                    messagebox.showerror("错误", "最大值与最小值之差小于数量")
                    return
                random_numbers = tools_randint(least_val, max_val, count, False)
                random_numbers_label.config(text="生成的随机数为：\n" +add_line_break(random_numbers,5))

        make_button = tk.Button(random_numbers_window, text="生成", command=generate_random_numbers)
        make_button.place(x=250, y=20)
        random_numbers_window.mainloop()

    def handle_prime_number():
        prime_number_window = tk.Toplevel(main_window)
        prime_number_window.title("质数判断器")
        prime_number_window.geometry("300x225")
        number_entry = tk.Entry(prime_number_window)
        number_text = tk.Label(prime_number_window,text="请输入需要判断的数")
        result_type_label = tk.Label(prime_number_window, text="是否为质数：")
        factor_count_label = tk.Label(prime_number_window, text="因数个数：")
        factors_label = tk.Label(prime_number_window, text="因数列表：")
        factors_label['justify'] = 'left'
        exit_button = tk.Button(prime_number_window, text="退出", command=prime_number_window.destroy)
        number_entry.place(x=140, y=20)
        number_text.place(x=10, y=20)
        result_type_label.place(x=10, y=60)
        factor_count_label.place(x=10, y=90)
        factors_label.place(x=10, y=120)
        exit_button.place(x=250, y=90)
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
                    factors_label.config(text="因数列表：\n" + add_line_break(factors, 10))
                else:
                    result_type_label.config(text="是否为质数：否")
                    factor_count_label.config(text="因数个数：" + str(factor_count))
                    factors_label.config(text="因数列表：\n" + add_line_break(factors, 7))
        
        prime_number_button = tk.Button(prime_number_window, text="判断", command=get_prime_number)
        prime_number_button.place(x=250, y=50)
        prime_number_window.mainloop()
        

    def handle_encipher():
        messagebox.showwarning("警告","加密完成后可能会出现不显示的情况，这是由于功能本身算法的局限性造成的，请不要惊慌")
        messagebox.showwarning("警告","加密完成后可能会出现结果乱码的情况，这是由于功能本身的原理造成的，说明加密成功，请不要惊慌")
        text = simpledialog.askstring("输入", "请输入文本：", parent=main_window)
        secret_key = simpledialog.askstring("输入", "请输入密钥：密钥长度请与文本长度相同：", parent=main_window)
        encipher_text = tools_encipher(text, secret_key)
        messagebox.showinfo("加密结果", "加密后的文本: " + encipher_text)

    def handle_decrypt():
        encipher_text = simpledialog.askstring("输入", "请输入加密文本：", parent=main_window)
        secret_key = simpledialog.askstring("输入", "请输入密钥：密钥长度请与文本长度相同", parent=main_window)
        decrypted_text = tools_decrypt(encipher_text, secret_key)
        messagebox.showinfo("解密结果", "解密后的文本: " + decrypted_text)

    def handle_now_time():
        
        def update_time():
            now = time.strftime("%m/%d %H:%M:%S\n%a")
            time_label.config(text=now)
            main_window.after(1000, update_time)
        time_label = tk.Label(main_window, font=("Arial", 30), fg=random.choice(color_list))
        time_label.place(x=300, y=25)
        update_time()


    def handle_new_edition():
        messagebox.showinfo("新版本介绍","版本号:1.6 更新内容:质数判断界面全面升级")


    def handle_exit():
        main_window.destroy()

    button_randint = tk.Button(main_window, text="生成随机数", command=handle_random_numbers)
    button_randint.place(x=25,y=25)

    button_prime_number = tk.Button(main_window, text="检测质数", command=handle_prime_number)
    button_prime_number.place(x=100,y=25)

    button_encipher = tk.Button(main_window, text="加密文本", command=handle_encipher)
    button_encipher.place(x=25,y=75)

    button_decrypt = tk.Button(main_window, text="解密文本", command=handle_decrypt)
    button_decrypt.place(x=100,y=75)

    button_time = tk.Button(main_window, text="时间", command=handle_now_time)
    button_time.place(x=175, y=25)

    button_mp3_player = tk.Button(main_window, text="mp3播放", command=tools_mp3_player)
    button_mp3_player.place(x=175, y=75)


    button_new_edition = tk.Button(main_window, text="新版本介绍", command=handle_new_edition)
    button_new_edition.place(x=450, y=350)

    button_exit = tk.Button(main_window, text="退出", command=handle_exit)
    button_exit.place(x=550,y=350)

    about1 = tk.Label(main_window,text="本产品由北极星工作室——DHY荣誉出品",fg="blue")
    about2 = tk.Label(main_window,text="源码请访问 https://github.com/Daihongyi/little-tools")
    about3 = tk.Label(main_window,text="邮箱：17717460527@163.com",fg="orange")
    about4 = tk.Label(main_window,text="北极星工作室官网：https://northstar.us.kg/",fg="red")
    about1.place(y=200)
    about2.place(y=250)
    about3.place(y=300)
    about4.place(y=350)
    # 启动事件循环
    main_window.mainloop()

if __name__ == "__main__":
    main()

