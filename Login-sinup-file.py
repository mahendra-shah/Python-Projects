######## Login-sinup using text file ###################

usr_opt = int(input("Sinup or Login 1/2 : "))
data = []
f = open("logSign.txt", "a+")
f.seek(0)
if usr_opt == 1:
    emails = input("Enter your email: ")
    passes = input("Enter your password: ")
    data.append(emails+"\n")
    data.append(passes+"\n")
    print("Congrats Sinup Completed Successfully")
    f.writelines(data)
    # print(data)


if usr_opt ==2:
    f = open("logSign.txt", 'r')
    content = f.readlines()
    # print(content)
    emails= []
    passes = []
    for i in range(len(content)):
        if i%2==0:
            emails.append(content[i][:len(content[i])-1])
        else:
            passes.append(content[i][:len(content[i])-1])

    userEmail = input("Email: ")
    userPass = input("Password: ")

    for i in range(len(emails)):
        if userEmail == emails[i] and userPass == passes[i]:
            print("Logged in succesfully")
            break
    else:
        print("Check your details and try again")

if usr_opt > 2 or usr_opt < 1:
    print("Wrong Option :(")

f.close()



