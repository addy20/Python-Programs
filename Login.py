def authenticUser(password):
    if(password=='magic'):
        message='Login Successful!!\n Welcome to System.'
    else:
        message='Password mismatch!!\n'

    return message    


print('\t LOGIN SYSTEM ')
print('===============================')
password=input('Enter Password: ')
message=authenticUser(password)
print(message)