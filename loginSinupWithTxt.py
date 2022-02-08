###   Login and sinup
''' Srats Here '''

print('Do you have a account if not then create one')
op = int(input('Type 1 to create account or 2 for Login:   '))
aop = op
data = {'m@gmail.com':{'name':'Mahendra','contact':'9876543210','email':'m@gmail.com','userid':'ms','password':'12345678'}}
# data = {}
counter=1
while True:
    if op == 1:
        locd = {}
        sin = input('Enter your name: ')
        locd['name']=sin 

        sin2 = input('Enter your Contact: ')
        locd['contact']=sin2 
        
        sin3 = input('Enter your Email: ')
        locd['email']=sin3
        
        pas = input('Create a password: ')
        locd['password']=pas
        
        sin4 = input('Create a user ID: ')
        locd['userid']=sin4
        if "@gmail.com" in sin3 or "@navgurukul.org" in sin3:
            if len(sin2) == 10 and len(pas) >= 8:
                if sin3 in data:
                    print('Looks like you already have a account with this email')
                    lo_ = input('Enter your password: ')
                    if lo_ in data[sin3]['password']==lo_:
                        print('You are succesfully loged in :)')
                        top = input('Type 1 for Sinup or 2 for Login: ')
                        if top == 2:
                            op==2
                            continue
                        elif top == 1:
                            op==1
                            continue
                        else:
                            print('Invalid Option /n You breaked the programme!!')
                            break
                    else:
                        print('Incorrect password Try Again :(')
                else:
                    print('Hurrey, you made it! :)')                   
            else:
                print('Please enter your details properly')
                locd = {}
            data[sin3]=locd
        else:
            print('Invalid email address!!')    
    
    if op == 2:
        locd2 = {}
        log = input('Enter your Email: ')
        locd2['email'] = log

        pas = input('Enter your password: ')
        locd2['password'] = pas
        print(locd2['email'])

        if locd2['email']  in data and locd2['password'] == data[log]['password']:
            print('Hurrey, you made it! :)')
            # print(locd2)
            top = input('Type 1 for Sinup or 2 for Login: ')
            if top == 2:
                op==2
                continue
            elif top == 1:
                op==1
                continue
            else:
                print('Invalid Option /n You breaked the programme')
    else:
        print('Invalid Option /n You breaked the programme!')
        
# print(data)
''' End Here '''
