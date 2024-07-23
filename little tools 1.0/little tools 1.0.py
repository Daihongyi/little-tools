from tkinter import simpledialog, messagebox
import random
import time
import tkinter as tk

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
        return "Prime number", factor_number, factor
    elif factor_number >= 3:
        return "Composite number", factor_number, factor
    else:
        return "Error", factor_number, factor

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
    return text_return

def tools_decrypt(encipher_text, secret_key):
    text_return = ""
    ascii_encipher_text = []
    ascii_secret_key = []
    ascii_element = ""
    no_ascii_element = ""
    ascii_text = []
    no_ascii_text = []
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
        no_ascii_element = chr(ascii_element)
        no_ascii_text.append(no_ascii_element)
    for i in no_ascii_text:
        text_return = text_return + i
    return text_return

def main():
    main_window = tk.Tk()
    main_window.geometry("500x350")
    main_window.title("little tools 1.0")

    def handle_random_numbers():
        least_val = simpledialog.askinteger("输入", "请输入最小值：", parent=main_window)
        max_val = simpledialog.askinteger("输入", "请输入最大值：", parent=main_window)
        count = simpledialog.askinteger("输入", "请输入数量：", parent=main_window)
        remake = simpledialog.askstring("输入", "是否允许重复(yes/no)：", parent=main_window)
        if remake.lower() not in ['yes', 'no', 'true', 'false']:
            messagebox.showerror("错误", "无效的输入")
            return
        result = tools_randint(least_val, max_val, count, remake.lower() == 'true')
        messagebox.showinfo("结果", "生成的随机数: " + str(result))

    def handle_prime_number():
        number = simpledialog.askinteger("输入", "请输入一个数字：", parent=main_window)
        if number is None:
            return
        result_type, factor_count, factors = tools_prime_number(number)
        messagebox.showinfo("结果", f"{result_type} - 因子数量: {factor_count}, 因子列表: {factors}")

    def handle_encipher():
        text = simpledialog.askstring("输入", "请输入文本：", parent=main_window)
        secret_key = simpledialog.askstring("输入", "请输入密钥：", parent=main_window)
        encipher_text = tools_encipher(text, secret_key)
        messagebox.showinfo("加密结果", "加密后的文本: " + encipher_text)

    def handle_decrypt():
        encipher_text = simpledialog.askstring("输入", "请输入加密文本：", parent=main_window)
        secret_key = simpledialog.askstring("输入", "请输入密钥：", parent=main_window)
        decrypted_text = tools_decrypt(encipher_text, secret_key)
        messagebox.showinfo("解密结果", "解密后的文本: " + decrypted_text)

    def handle_exit():
        main_window.destroy()

    button_randint = tk.Button(main_window, text="生成随机数", command=handle_random_numbers)
    button_randint.pack(pady=10)

    button_prime_number = tk.Button(main_window, text="检测质数", command=handle_prime_number)
    button_prime_number.pack(pady=10)

    button_encipher = tk.Button(main_window, text="加密文本", command=handle_encipher)
    button_encipher.pack(pady=10)

    button_decrypt = tk.Button(main_window, text="解密文本", command=handle_decrypt)
    button_decrypt.pack(pady=10)



    button_exit = tk.Button(main_window, text="退出", command=handle_exit)
    button_exit.pack(pady=10)

    about1 = tk.Label(main_window,text="本产品由北极星工作室荣誉出品")
    about2 = tk.Label(main_window,text="代码重构自Desktop manager 性能再升级")
    about3 = tk.Label(main_window,text="源码请访问 https://github.com/Daihongyi/little-tools")
    about1.pack()
    about2.pack()
    about3.pack()
    # 启动事件循环
    main_window.mainloop()


main()

