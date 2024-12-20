from User_Interface import login, register, id_checker, exchange
from Currency_Codes import data
from DB import search

min_amount = 10
limit = 1000


def main():
    print("Welcome To Our Bank")
    print("-------------------")
    while True:
        p_id = input("Enter Your Personal_ID: ").strip()
        if not id_checker(p_id):
            print("ID Isn't Valid !")
        else:
            break

    if not login(p_id):
        print(f"User With This ID Isn't Registered !\n")

        if yes_or_no("Would You Like To Register [Y/N]: "):
            register()
        else:
            print("Goodbye !")
    else:
        print(f"Welcome Back !")
        print("---------------\n")
        print("Available Currencies: ")

        counter = 0
        for each in data:
            if counter == 5:
                print()
                counter = 0
            print(each, end=' | ')
            counter += 1
        while True:
            try:
                cur = input("\n\nIn Which Currency Do You Want To Exchange ? ").upper()
                if not check_cur_code(cur):
                    print(f"Please Provide Currency Code Correctly: ")
                else:
                    break
            except ValueError:
                print("Provide Valid Code !")

        while True:
            try:
                amount = int(input('Enter The Amount Of Money You Want To Exchange: '))
                if not check_amount(amount, p_id):
                    print("Enter The Valid Amount !")
                else:
                    print(round(exchange(amount, cur, p_id), 2))
                    break
            except ValueError:
                print("Enter Only Numbers !")


def yes_or_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", 'n'):
            return ans == 'y'
        print("Please Answer With Only 'Y' or 'N': ")


def check_cur_code(cur):
    return len(cur) == 3 and cur in data and cur.isdigit() is False


def check_amount(amount, p_id):
    query = f"SELECT LIMIT FROM Users WHERE Personal_ID = ?"
    if search(query, p_id)[0][0] == limit:
        if min_amount < amount < limit:
            return True
        else:
            return False
    else:
        if amount > min_amount:
            return True
        return False


if __name__ == "__main__":
    main()
