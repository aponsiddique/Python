print('Please register with your fullname: ')
fullname = input()
print('Enter username: ')
username = input()
print('Enter password: ')
password1 = input()
print('Re-enter password: ')
password2 = input()
if password2 == password1:
    print('Done')
    print('Welcome ' + str(fullname))
else:
    print('Incorrect, try again')
