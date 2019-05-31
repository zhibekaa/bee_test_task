import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

#Объект App с элементами GUI
class App:
    
    def __init__(self, master):
        
        #Строка
        self.label = ttk.Label(master, text='Вставьте ссылку')          
        self.label.pack()

        #Поле ввода ссылки
        self.entry = ttk.Entry(master, width=50)                        
        self.entry.pack()

        #Кнопка
        self.button = ttk.Button(master, text='Получить заголовок')     
        self.button.pack()
        
        
        self.strvar = tk.StringVar(master)
        self.strvar.set('__________________________________')

        #Cтрока вывода
        self.answer = ttk.Label(master, text=self.strvar.get())         
        self.answer.pack()

        #В параметрах кнопки указываем метод getLink()
        self.button.config(command = self.getLink)

    def getLink(self):

        #ip адрес и порт взяты с сайта https://sslproxies.org
        proxies = {                                      
            "https":"47.252.4.130:3128",
            "http":"47.252.5.243:3128"
            }
        #Присвоим переменной url значение из ttk.Entry
        url = self.entry.get()

        #Запрос на ссылку, с настроенным прокси
        page = requests.get(url, proxies=proxies)
        print(page.status_code)

        #Синтаксический разбор страницы с помощью встроенного html.parser в объекте BeautifulSoup
        soup = BeautifulSoup(page.text, 'html.parser')

        #Первый элемент из списка найденных значений по шаблону
        t = soup.findAll('title')[0].get_text()

        print(t)

        #tk.StringVar - теперь t
        self.strvar.set(t)

        #Параметр text элемента ttk.Label теперь тоже t
        self.answer.config(text=self.strvar.get())

        
def launchApp():
    #root - базовое окно приложения
    root = tk.Tk()
    root.geometry("600x100")
    #Классу App задаем атрибут root
    App(root)
    tk.mainloop()


if __name__ == '__main__':launchApp()

