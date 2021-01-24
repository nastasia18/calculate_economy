from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Калькулятор ОПФ")
root.geometry("300x400")

main = Frame(root)
main.pack()


def clear():
    global main, root
    main.destroy()
    main = Frame(root)
    main.pack()


def cost_opf_end_of_year(position):
    clear()

    def calc():
        try:
            f1 = float(edit_start_sum_opf.get())
            f2 = float(edit_sum_enter.get())
            f3 = float(edit_sum_output.get())
            formula = str(f1 + f2 - f3)
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label1 = Label(main, text="Первоначальная стоимость ОПФ, млн.руб")
    edit_start_sum_opf = Entry(main, width=8)

    label1.pack()
    edit_start_sum_opf.pack()

    label2 = Label(main, text="Стоимость введенных в эксплуатацию ОПФ")
    edit_sum_enter = Entry(main, width=8)

    label2.pack()
    edit_sum_enter.pack()

    label4 = Label(main, text="Стоимость выведенных в эксплуатацию ОПФ")
    edit_sum_output = Entry(main, width=8)
    label4.pack()
    edit_sum_output.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def cost_average(position):
    clear()

    def calc():
        try:
            f1 = float(edit_start_sum_opf.get())
            f2 = float(edit_sum_enter.get())
            f_m2 = float(edit_month_enter.get())
            f3 = float(edit_sum_output.get())
            f_m3 = float(edit_month_output.get())
            formula = str(f1 + (f2 * (f_m2 / 12)) - (f3 * ((12 - f_m3) / 12)))
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label1 = Label(main, text="Первоначальная стоимость ОПФ, млн.руб")
    edit_start_sum_opf = Entry(main, width=8)
    label1.pack()
    edit_start_sum_opf.pack()

    label2 = Label(main, text="Стоимость введенных в эксплуатацию ОПФ")
    edit_sum_enter = Entry(main, width=8)
    label2.pack()
    edit_sum_enter.pack()

    label3 = Label(main, text="Введите сколько месяцев прошло от начала года\nдо введения в эксплуатацию")
    edit_month_enter = Entry(main, width=8)
    label3.pack()
    edit_month_enter.pack()

    label4 = Label(main, text="Стоимость выведенных в эксплуатацию ОПФ")
    edit_sum_output = Entry(main, width=8)
    label4.pack()
    edit_sum_output.pack()

    label5 = Label(main, text="Введите сколько месяцев прошло от \nвывода из эксплуатации до конца года")
    edit_month_output = Entry(main, width=8)
    label5.pack()
    edit_month_output.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def fondootdacha_and_fondoemkost(position):
    clear()

    def calc():
        try:
            b = float(edit_sum_product.get())
            f = float(edit_sum_average_opf.get())
            formula = " "
            if position == "Фондоотдача":
                formula = str(b / f)
            elif position == "Фондоемкость":
                formula = str(f / b)
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label7 = Label(main, text="Годовая выручка на конец года от проданной продукции")
    edit_sum_product = Entry(main, width=8)
    label7.pack()
    edit_sum_product.pack()

    label8 = Label(main, text="Среднегодовая стоимость ОПФ")
    edit_sum_average_opf = Entry(main, width=8)
    label8.pack()
    edit_sum_average_opf.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def fondovooryzhennost(position):
    clear()

    def calc():
        try:
            h = float(edit_count_people.get())
            f = float(edit_sum_average_opf.get())
            formula = str(f / h)
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label8 = Label(main, text="Среднегодовая стоимость ОПФ")
    edit_sum_average_opf = Entry(main, width=8)
    label8.pack()
    edit_sum_average_opf.pack()

    label21 = Label(main, text="Численность служащих")
    edit_count_people = Entry(main, width=8)
    label21.pack()
    edit_count_people.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def coefficient_update(position):
    clear()

    def calc():
        try:
            f_ved = float(edit_sum_enter.get())
            f_kg = float(edit_sum_opf_end_of_year.get())
            formula = str(f_ved / f_kg)
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label2 = Label(main, text="Стоимость введенных в эксплуатацию ОПФ")
    edit_sum_enter = Entry(main, width=8)
    label2.pack()
    edit_sum_enter.pack()

    label6 = Label(main, text="Стоимость ОПФ на конец года")
    edit_sum_opf_end_of_year = Entry(main, width=8)
    label6.pack()
    edit_sum_opf_end_of_year.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def coefficient_output(position):
    clear()

    def calc():
        try:
            f_v = float(edit_sum_output.get())
            f = float(edit_sum_average_opf.get())
            formula = str(f_v / f)
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")
    label4 = Label(main, text="Стоимость выведенных в эксплуатацию ОПФ")
    edit_sum_output = Entry(main, width=8)
    label4.pack()
    edit_sum_output.pack()

    label8 = Label(main, text="Среднегодовая стоимость ОПФ")
    edit_sum_average_opf = Entry(main, width=8)
    label8.pack()
    edit_sum_average_opf.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def coefficient_growth(position):
    clear()

    def calc():
        try:
            f_vv = float(edit_sum_enter.get())
            f = float(edit_sum_average_opf.get())
            formula = str(f_vv / f)
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label2 = Label(main, text="Стоимость введенных в эксплуатацию ОПФ")
    edit_sum_enter = Entry(main, width=8)
    label2.pack()
    edit_sum_enter.pack()

    label8 = Label(main, text="Среднегодовая стоимость ОПФ")
    edit_sum_average_opf = Entry(main, width=8)
    label8.pack()
    edit_sum_average_opf.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def service_life(position):
    clear()

    def calc():
        try:
            na = float(edit_norm_amort.get())
            formula = str(100 / (na * 12))
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")
    label16 = Label(main, text="Норма амортизации")
    edit_norm_amort = Entry(main, width=8)
    label16.pack()
    edit_norm_amort.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def norm_amortization(position):
    clear()

    def calc():
        try:
            life = float(edit_service_life.get())
            formula = str(100 / (life * 12))
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")
    label15 = Label(main, text="Срок службы")
    edit_service_life = Entry(main, width=8)
    label15.pack()
    edit_service_life.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def sum_amortization(position):
    clear()

    def calc():
        try:
            life = float(edit_service_life.get())
            f = float(edit_start_sum_opf.get())
            formula = " "
            if position == "Годовая сумма амортизации":
                formula = str(f / life)
            elif position == "Месячная сумма амортизации":
                formula = str(f / (life * 12))
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label15 = Label(main, text="Срок службы")
    edit_service_life = Entry(main, width=8)
    label15.pack()
    edit_service_life.pack()

    label1 = Label(main, text="Первоначальная стоимость ОПФ, млн.руб")
    edit_start_sum_opf = Entry(main, width=8)
    label1.pack()
    edit_start_sum_opf.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def sum_wear(position):
    clear()

    def calc():
        try:
            f = float(edit_start_sum_opf.get())
            ku = float(edit_coef_wear.get())
            formula = str(ku * f)
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label1 = Label(main, text="Первоначальная стоимость ОПФ, млн.руб")
    edit_start_sum_opf = Entry(main, width=8)
    label1.pack()
    edit_start_sum_opf.pack()

    label20 = Label(main, text="Коэффициент износа")
    edit_coef_wear = Entry(main, width=8)
    label20.pack()
    edit_coef_wear.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def coefficient_wear(position):
    clear()

    def calc():
        try:
            fn = float(edit_start_sum_opf.get())
            zu = float(edit_sum_wear.get())
            formula = str(zu / fn)
            label["text"] = f'{position} = {formula}'
        except ValueError:
            messagebox.showwarning("Warning", "Проверьте правильность значений")

    label1 = Label(main, text="Первоначальная стоимость ОПФ, млн.руб")
    edit_start_sum_opf = Entry(main, width=8)
    label1.pack()
    edit_start_sum_opf.pack()

    label19 = Label(main, text="Сумма износа")
    edit_sum_wear = Entry(main, width=8)
    label19.pack()
    edit_sum_wear.pack()

    btn = Button(main, text="Расчитать", command=calc)
    btn.pack()


def call(position):
    if position == "Стоимость ОПФ на конец года":
        cost_opf_end_of_year(position)
    elif position == "Среднегодовая стоимость ОПФ":
        cost_average(position)
    elif position == "Фондоотдача":
        fondootdacha_and_fondoemkost(position)
    elif position == "Фондоемкость":
        fondootdacha_and_fondoemkost(position)
    elif position == "Фондовооруженность":
        fondovooryzhennost(position)
    elif position == "Коэффициент обновления":
        coefficient_update(position)
    elif position == "Коэффициент выбытия":
        coefficient_output(position)
    elif position == "Коэффициент прироста":
        coefficient_growth(position)
    elif position == "Срок службы":
        service_life(position)
    elif position == "Норма амортизации":
        norm_amortization(position)
    elif position == "Годовая сумма амортизации" or position == "Месячная сумма амортизации":
        sum_amortization(position)
    elif position == "Сумма износа":
        sum_wear(position)
    elif position == "Коэффициент износа":
        coefficient_wear(position)


var = StringVar()
var.set("Выберете что надо рассчитать")
list_choice = OptionMenu(root, var, *["Стоимость ОПФ на конец года", "Среднегодовая стоимость ОПФ",
                                      "Фондоотдача", "Фондоемкость", "Фондовооруженность",
                                      "Коэффициент обновления", "Коэффициент выбытия", "Коэффициент прироста",
                                      "Срок службы", "Норма амортизации", "Годовая сумма амортизации",
                                      "Месячная сумма амортизации", "Сумма износа", "Коэффициент износа"], command=call)
list_choice.pack()
label = Label(root, text=" ")
label.pack()
root.mainloop()
