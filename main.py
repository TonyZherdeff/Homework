print("Задание 1")


class Plist:
    def __init__(self):
        self.plist = []

    def input_num(self, number):
        self.plist.append(number)

    def take_list(self):
        return self.plist

    def remove_num(self, number):
        self.plist.remove(number)

    def removeall_num(self, number):
        try:
            while True:
                self.plist.remove(number)
        except ValueError:
            pass

    def change_num(self, number, new_number):
        num_index = self.plist.index(number, 0, len(self.plist))
        self.plist[num_index] = new_number

    def changeall_num(self, number, new_number):
        try:
            while True:
                num_index = self.plist.index(number, 0, len(self.plist))
                self.plist[num_index] = new_number
        except ValueError:
            pass


def check_num(num_checked):
    if '.' in num_checked:
        return float(num_checked)
    else:
        return int(num_checked)


plist1 = Plist()
print("Привет! Для начала рабоы необходимо заполнить список.\n"
      "Для заполнения можно использовать только целые и дробные числа\n")
while True:
    try:
        num = input("Введи число: (Для выхода из режима заполнения списка введи 'exit')\n")
        if num.upper() == 'EXIT':
            print("Готово!")
            break
        check_num(num)
        if num is None:
            raise ValueError
    except ValueError:
        print("Введены некорректные данные!\n"
              "Для работы с программой необходимо ввести число или десятичную дробь.\n"
              "Пустой ввод также не допускается!")
    else:
        plist1.input_num(num)

print("Для добавления нового числа в список введи 'add'\n"
      "Для удления числа из списка введи 'remove'\n"
      "Для удления числа и всех его копий из списка введи 'removeAll'\n"
      "Для просмотра содержимого списка введи 'view'\n"
      "Для проверки наличия числа в списке введи 'check'\n"
      "Для замены значения в списке введи 'change'\n"
      "Для замены значений всех копий числа в списке введи 'changeAll'\n"
      "Для вывода меню на экран введи 'menu'\n"
      "Для выхода введи 'exit'\n")
while True:
    try:
        num = None
        choose = input("Введи наименование нужной опции:\n")
        if choose.upper() == 'ADD':
            num = input("Введи число для добавления:\n")
            check_num(num)
            if num is None:
                raise ValueError
        elif choose.upper() == 'REMOVE':
            num = input("Введи число для удаления:\n")
            check_num(num)
            if num is None:
                raise ValueError
        elif choose.upper() == 'REMOVEALL':
            num = input("Введи число для удаления:\n")
            check_num(num)
            if num is None:
                raise ValueError
        elif choose.upper() == 'VIEW':
            print(plist1.take_list())
        elif choose.upper() == 'CHECK':
            num = input("Введи число для проверки:\n")
            check_num(num)
            if num is None:
                raise ValueError
        elif choose.upper() == 'CHANGE':
            num = input("Введи число для замены:\n")
            check_num(num)
            if num is None:
                raise ValueError
        elif choose.upper() == 'CHANGEALL':
            num = input("Введи число для замены:\n")
            check_num(num)
            if num is None:
                raise ValueError
        elif choose.upper() == 'MENU':
            print("Для добавления нового числа в список введи 'add'\n"
                  "Для удления числа из списка введи 'remove'\n"
                  "Для удления числа и всех его копий из списка введи 'removeAll'\n"
                  "Для просмотра содержимого списка введи 'view'\n"
                  "Для проверки наличия числа в списке введи 'check'\n"
                  "Для замены значения в списке введи 'change'\n"
                  "Для замены значений всех копий числа в списке введи 'changeAll'\n"
                  "Для вывода меню на экран введи 'menu'\n"
                  "Для выхода введи 'exit'\n")
        elif choose.upper() == 'EXIT':
            print("До свидания!")
            break
        else:
            print("Введено наименование несуществующей опции,\n"
                  "повтори попытку снова.")
    except ValueError:
        print("Введены некорректные данные!\n"
              "Для работы с программой необходимо ввести число или десятичную дробь.\n"
              "Пустой ввод также не допускается!")
    else:
        if choose.upper() == 'ADD':
            taken_list = plist1.take_list()
            if num in taken_list:
                print("Число уже есть в списке, добавление невозможно.")
            else:
                plist1.input_num(num)
                print("Готово!")
        elif choose.upper() == 'REMOVE':
            taken_list = plist1.take_list()
            if num in taken_list:
                plist1.remove_num(num)
                print("Готово!")
            else:
                print("Данного числа нет в списке, удаление невозможно.")
        elif choose.upper() == 'REMOVEALL':
            taken_list = plist1.take_list()
            if num in taken_list:
                plist1.removeall_num(num)
                print("Готово!")
            else:
                print("Данных чисел нет в списке, удаление невозможно.")
        elif choose.upper() == 'CHECK':
            taken_list = plist1.take_list()
            num_count = 0
            if num in taken_list:
                for i in taken_list:
                    if i == num:
                        num_count += 1
                print(f'Данное значение есть в списке и встречаеся {num_count} раз(а).')
            else:
                print("Данное число в списке не встречается.")
        elif choose.upper() == 'CHANGE':
            try:
                taken_list = plist1.take_list()
                if num in taken_list:
                    new_num = input("Введите новое значение:\n")
                    check_num(new_num)
                    if new_num is None:
                        raise ValueError
                    plist1.change_num(num, new_num)
                    print("Готово!")
                else:
                    print("Данного числа нет в списке, замена невозможна.")
            except ValueError:
                print("Введены некорректные данные!\n"
                      "Для работы с программой необходимо ввести число или десятичную дробь.\n"
                      "Пустой ввод также не допускается!")
        elif choose.upper() == 'CHANGEALL':
            try:
                taken_list = plist1.take_list()
                if num in taken_list:
                    new_num = input("Введите новое значение:\n")
                    check_num(new_num)
                    if new_num is None:
                        raise ValueError
                    plist1.changeall_num(num, new_num)
                    print("Готово!")
                else:
                    print("Данных чисел нет в списке, замена невозможна.")
            except ValueError:
                print("Введены некорректные данные!\n"
                      "Для работы с программой необходимо ввести число или десятичную дробь.\n"
                      "Пустой ввод также не допускается!")


print("Задание 2")


class StringStack:
    def __init__(self, max_length: int):
        self.stack = []
        self.max_length = max_length

    def add_value(self, value: str):
        if len(self.stack) == 0 or len(self.stack) < self.max_length:
            self.stack.append(value)
            print("Done")
        else:
            print("You've reached the limit of elements in stack, adding is impossible")

    def view_stack(self):
        return self.stack

    def remove_value(self, value: str):
        if value in self.stack:
            self.stack.pop(self.stack.index(value))
            print("Done")
        else:
            print(f"There is no {value} in this stack, removing is impossible")

    def number_of_strings(self):
        return f'Number of strings in this stack is "{len(self.stack)}"'

    def empty_check(self):
        if len(self.stack) == 0:
            return f'Stack is empty'
        else:
            return f'Stack is not empty, there are "{len(self.stack)}" values'

    def clean_stack(self):
        self.stack = []
        print("Stack is already cleaned up!")

    def top_value(self):
        if len(self.stack) != 0:
            return f'Top value of this stack is "{self.stack[-1]}"'
        else:
            return f'Stack is empty, there is no values inside'


def run():
    print("Hi! This is a string stack with a fixed value of strings onboard!\n"
          "At first you need to set a limit of strings in this stack.")
    while True:
        try:
            stack_len_limit = int(input("Please, write here a value:\n"))
        except ValueError:
            print("You can use only integer value to set a limit of strings in stack!")
        else:
            print(f'You have a string stack with element limit set to "{stack_len_limit}"')
            stack = StringStack(stack_len_limit)
            print("You have now a following options:\n"
                  "To add a new string in stack write 'Add'\n"
                  "To remove a string from stack write 'Remove'\n"
                  "To view stack write 'View'\n"
                  "To view number of strings in stack write 'NOS'\n"
                  "To find out if the stack is empty write 'EmptyCheck'\n"
                  "To cleanup this stack write 'CleanUP'\n"
                  "To take a top value of stack without removing write 'Top'\n"
                  "To see this menu again write 'Menu'\n"
                  "To exit write 'Exit'")
            while True:
                try:
                    option_choose = str(input("Choose an option:\n"))
                    if option_choose.upper() == "EXIT":
                        print("Good bye!")
                        break
                    elif option_choose.upper() == "MENU":
                        print("You have now a following options:\n"
                              "To add a new string in stack write 'Add'\n"
                              "To remove a string from stack write 'Remove'\n"
                              "To view stack write 'View'\n"
                              "To view number of strings in stack write 'NOS'\n"
                              "To find out if the stack is empty write 'EmptyCheck'\n"
                              "To cleanup this stack write 'CleanUP'\n"
                              "To take a top value of stack without removing write 'Top'\n"
                              "To see this menu again write 'Menu'\n"
                              "To exit write 'Exit'")
                    elif option_choose.upper() == "ADD":
                        new_string = str(input("Write here a new value of this string:\n"))
                        stack.add_value(new_string)
                    elif option_choose.upper() == "REMOVE":
                        new_string = str(input("Write here a value, that you would like to remove from this stack:\n"))
                        stack.remove_value(new_string)
                    elif option_choose.upper() == "VIEW":
                        print(stack.view_stack())
                    elif option_choose.upper() == "NOS":
                        print(stack.number_of_strings())
                    elif option_choose.upper() == "EMPTYCHECK":
                        print(stack.empty_check())
                    elif option_choose.upper() == "CLEANUP":
                        stack.clean_stack()
                    elif option_choose.upper() == "TOP":
                        print(stack.top_value())

                except ValueError:
                    print("You've got a wrong option, please try again!")
            break


run()


print("Задание 3")


class StringStack1:
    def __init__(self):
        self.stack = []

    def add_value(self, value: str):
        self.stack.append(value)
        print("Done")

    def view_stack(self):
        return self.stack

    def remove_value(self, value: str):
        if value in self.stack:
            self.stack.pop(self.stack.index(value))
            print("Done")
        else:
            print(f"There is no {value} in this stack, removing is impossible")

    def number_of_strings(self):
        return f'Number of strings in this stack is "{len(self.stack)}"'

    def empty_check(self):
        if len(self.stack) == 0:
            return f'Stack is empty'
        else:
            return f'Stack is not empty, there are "{len(self.stack)}" values'

    def clean_stack(self):
        self.stack = []
        print("Stack is already cleaned up!")

    def top_value(self):
        if len(self.stack) != 0:
            return f'Top value of this stack is "{self.stack[-1]}"'
        else:
            return f'Stack is empty, there is no values inside'


def run():
    print("Hi! This is a string stack with a non-fixed value of strings onboard!\n")
    while True:
        stack = StringStack1()
        print("You have now a following options:\n"
              "To add a new string in stack write 'Add'\n"
              "To remove a string from stack write 'Remove'\n"
              "To view stack write 'View'\n"
              "To view number of strings in stack write 'NOS'\n"
              "To find out if the stack is empty write 'EmptyCheck'\n"
              "To cleanup this stack write 'CleanUP'\n"
              "To take a top value of stack without removing write 'Top'\n"
              "To see this menu again write 'Menu'\n"
              "To exit write 'Exit'")
        while True:
            try:
                option_choose = str(input("Choose an option:\n"))
                if option_choose.upper() == "EXIT":
                    print("Good bye!")
                    break
                elif option_choose.upper() == "MENU":
                    print("You have now a following options:\n"
                          "To add a new string in stack write 'Add'\n"
                          "To remove a string from stack write 'Remove'\n"
                          "To view stack write 'View'\n"
                          "To view number of strings in stack write 'NOS'\n"
                          "To find out if the stack is empty write 'EmptyCheck'\n"
                          "To cleanup this stack write 'CleanUP'\n"
                          "To take a top value of stack without removing write 'Top'\n"
                          "To see this menu again write 'Menu'\n"
                          "To exit write 'Exit'")
                elif option_choose.upper() == "ADD":
                    new_string = str(input("Write here a new value of this string:\n"))
                    stack.add_value(new_string)
                elif option_choose.upper() == "REMOVE":
                    new_string = str(input("Write here a value, that you would like to remove from this stack:\n"))
                    stack.remove_value(new_string)
                elif option_choose.upper() == "VIEW":
                    print(stack.view_stack())
                elif option_choose.upper() == "NOS":
                    print(stack.number_of_strings())
                elif option_choose.upper() == "EMPTYCHECK":
                    print(stack.empty_check())
                elif option_choose.upper() == "CLEANUP":
                    stack.clean_stack()
                elif option_choose.upper() == "TOP":
                    print(stack.top_value())
            except ValueError:
                print("You've got a wrong option, please try again!")
        break


run()
