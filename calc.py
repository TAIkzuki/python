def summa(a,b):
    return a+b
def differense(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def devision(a,b):
    if b==0:
        print("Деление на 0 невозможно")
    return a/b
def procent(a,b):
    return a%b
import tkinter as tk

def on_click(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")

# Виджет для ввода
entry = tk.Entry(root, width=16, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Кнопки для цифр и операций
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=' , '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Кнопка для очистки
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_entry).grid(row=row_val, column=col_val)

# Кнопка для вычисления
tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 14), command=calculate).grid(row=row_val, column=col_val + 1)

# Запускаем главный цикл
root.mainloop()
