def password_controller(password):
    if len(password) > 8:
        return True
    else:
        return False


password = input("Please enter your password: ")

print(password_controller(password))
