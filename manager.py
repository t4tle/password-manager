
mpwd = input("what is the master password:")

def view():
    with open('passwords.txt','r' ) as f:
        for line in f:
            data = line.rstrip()
            user, passw = data.split('|')
            print("user:{} passsword:{}".format(user,passw))
def add():
    name = input("Account name")
    pwd = input("Password: ")

    with open('passwords.txt','a' ) as f:
        f.write("{} | {} \n".format(name,pwd))



while True:
    mode = input("would you like to add a new password or view existing ones (view,add,q):")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue