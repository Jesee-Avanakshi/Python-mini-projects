from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


masterpwd = input("What is your master key? \n ")
key = load_key() + masterpwd.encode()
fer =Fernet(key)


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username,password = data.split('|')
            print("Username - ",username," password - ",fer.decrypt(password.encode()).decode())
            print()

def add():
    name = input("Enter account name : ")
    password = input("Enter the password : ")

    with open('password.txt','a') as f:
        f.write(name+ '|'+ fer.encrypt(password.encode()).decode() + '\n')


while True:
    mode = input("Enter a mode : Type 'add/view/q' \nadd - add a password, view - view password, q - quit \n")
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid input. Try again")
    
