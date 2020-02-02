from _datetime import datetime
# print(datetime.now())

"""
    function for enter data in text file
    by mention date and time
    !Only 1 time data enter in per month!
"""
def lock_data():
    while True:
        person_name = input("Enter Person Name: ")
        if person_name.lower() == "q":
            break
        elif person_name.lower() == "farrukh" or person_name.lower() == "taha" or person_name.lower() == "usama" or person_name.lower() == "umair":
            person_name += ".txt"
            c = 0
            try:
                content = open(person_name, "a")
                val = open(person_name, "r")
            except:
                print("file not found!")
            date = datetime.now()
            month = int(date.month)
            c_month = month
            if val.read() == "":
                content.write(f"{month}")
            else:
                with open(person_name, "r") as value:
                    c_mon = value.read()
                    c_month = c_mon[len(c_mon)-1]
            if int(month) == int(c_month):
                amount = input("Enter Amount: ")
                date = datetime.now()
                month = int(date.month)
                str = f"-- Month and Date: \'{date}\'\n    Amount: \'{amount}\'\n"
                content.write(str)
                content.write("    ------------------------------------------\n")
                content.write(f"{month+1}")
                val.close()
                content.close()
            else:
                print("You already enter the amount of this month!")
        else:
            print("Enter valid name")


"""
    function for return data from text file
    only return amount and entry data and time
    Show total amount.   
"""
def retrive_data():
    while True:
        person_name = input("Enter Person Name: ")
        if person_name.lower() == "q":
            break
        elif person_name.lower() == "farrukh" or person_name.lower() == "taha" or person_name.lower() == "usama" or person_name.lower() == "umair":
            person_name += ".txt"
            amount = []
            c = 3
            try:
                with open(person_name, "r") as obj_ret:
                    data = obj_ret.read()
                    data = data.split("'")
                    print(f"{'-' * 40}")
                    print(f"Amount{' '*8}Date")
                    while c < len(data):
                        dif = 14 - len(data[c])
                        print(f"{data[c]}{' '*dif}{data[c-2]}")
                        amount.append(data[c])
                        c += 4
                total_amount = 0
                for a in range(len(amount)):
                    total_amount += int(amount[a])
                print(f"{'-'*40}")
                print(f"Total Amount of {len(amount)} months:{' '*5}Rs: {total_amount}/.")
                print(f"{'-' * 40}")
            except:
                print("No such file is present!")

"""
    Main control of function where all functions call
"""
while True:
    print("===-------*****-------===")
    print("What do you want!")
    print("1: Data lock")
    print("2: Data Retive")
    print("3: Exit")
    decision = int(input("Enter: "))
    if decision == 1:
        lock_data()
    elif decision == 2:
        retrive_data()
    elif decision == 3:
        break
