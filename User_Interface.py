import datetime

from DB import search, add, save
from API import fetch_specific_data

ID_len = 11
min_age = 10
max_age = 100
limit = 1000


def id_checker(personal_id: str):
    return len(personal_id) == ID_len and personal_id.isdigit()


def register():
    name = input("Enter Your Name: ").capitalize()
    lname = input("Enter Your Lastname: ").capitalize()

    while True:
        try:
            age = int(input("Enter Your Age: "))
            if min_age < age < max_age:
                break
            else:
                print("Enter a Valid Age: ")
        except ValueError:
            print("Age Must Be a Number ")

    while True:
        p_id = input("Enter Your Personal_ID: ").strip()
        if not id_checker(p_id):
            print("ID Isn't Valid !")
        else:
            query = f"SELECT * FROM [dbo].[Users] WHERE Personal_ID = ?"
            params = p_id
            if not search(query, params):
                break
            else:
                print('User With This ID Already Exists\n')

    if age < 18:
        query = f"INSERT INTO [dbo].[Users] VALUES(?, ?, ?, ?, ?)"
        params = (name, lname, age, p_id, limit)
    else:
        query = f"INSERT INTO [dbo].[Users](Name, Lname, Age, Personal_ID) VALUES (?, ?, ?, ?)"
        params = (name, lname, age, p_id)

    if add(query, params):
        print("Registration Successful !")
    else:
        print("Registration Failed !")


def login(personal_id: str):

    if not id_checker(personal_id):
        return False
    else:
        query = f"SELECT Name, Lname FROM [dbo].[Users] Where Personal_ID = ?"
        params = personal_id
        return bool(search(query, params))


def exchange(amount, cur: str, p_id):
    rate = fetch_specific_data(cur)[0]['currencies'][0]['rate']
    final_amount = amount * rate
    query = "INSERT INTO Transactions VALUES(?,?,?,?,?,?,?)"
    params = (p_id, 'GEL', cur.upper(), amount, final_amount, rate, str(datetime.date.today()))
    print(save(query, params))
    return final_amount
