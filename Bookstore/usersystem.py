import logging
from user import *
from exception import *
# from router import *

class UserSystem:
    def __init__(self, file):
        self.registered_user = []
        self.file = file
        self.load_user()

# guest use unregister user to log in
    def guest_login(self):
        choice = input('Are you confirm to continue shopping as guest without using user account? Type Y / N: \n')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            login_user = UnregisterUser()
            return login_user
        else:
            print('Please try again another option. \n')

# registered user login
    def reg_user_login(self):
        while True:
            choice = input('Do you have existing user account at our book store? Type Y / N: \n')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                email_id = self.check_email(input('Please input your <email ID> to log in: '))
                email_id_generator = self.generate_email(email_id)
                for each_email in email_id_generator:
                    password = input('Please input your password: ')
                    if each_email.password == password:
                        return each_email
                    else:
                        print('Your input password is not correct. ')
            elif choice.lower() == 'n' or choice.lower() == 'no':
                print('Please proceed to create new user account in the following: \n')
                reg_user = self.registration_user()
                return reg_user
            else:
                print('Please try again another option or log in as a guest.')
                break

# new user create account and generate registered user
    def registration_user(self):
        print('Welcome to registering user account with us. ')
        choice = input('Are you confirm to provide personal information to open new user account? Type Y / N:  \n')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            while True:
                firstname = str(input('Please input your first name: \n'))
                lastname = str(input('Please input your last name: \n'))
                print('In the following, you will need to create <email id> for your log in.')
                try:
                    email_id = self.check_email(str(input('Please input your email id: \n')))
                except NameIsNotMatch as err:
                    print(err)
                    continue
                print('In the following, you will need to create <password> for your log in.')
                try:
                    password = self.check_password(input('Please input at least 8 numbers / characters for creating password: \n'))
                except NameIsNotMatch as err:
                    print(err)
                    continue
                reg_user = RegisteredUser(firstname, lastname, email_id, password)
                self.registered_user.append(reg_user)
                print(f'You have successfully created user account with <{email_id}>. ')
                self.save_user()
                return reg_user
        else:
            print('Please try again another option.')


    def check_email(self, input_email):
        if "@" in input_email:
            return input_email
        else:
            raise NameIsNotMatch('You have input an incorrect email! Try again. ')

    def check_password(self, input_password):
        if len(input_password) >= 8:
            return input_password
        else:
            raise NameIsNotMatch('Please input at least 8 numbers / characters! Try again. ')

# generator for registered user's email ID
    def generate_email(self, email_id):
        try:
            if self.registered_user:
                for each_user in self.registered_user:
                    if each_user.email_id.lower() == email_id.lower():
                        yield each_user
                raise NameIsNotMatch('There is no such email ID on our system! Try again. ')
            else:
                raise NameIsNotMatch('We dont have any user record at our system now.  ')
        except NameIsNotMatch as err:
            print(err)

# save the registered user into JSON
    def save_user(self):
        try:
            if not os.path.exists(self.file):
                raise FileNotFound('The file is not exist!')
            user_dicts = [user.to_dict() for user in self.registered_user]
            with open(self.file, 'w') as file:
                json.dump(user_dicts, file, sort_keys=True, indent=4)
        except FileNotFound as err:
            print(err)
            logging.error(f'Failed to find {self.file}.')
        # else:
        #     print('The user data has been saved on JSON file successfully. \n')

# load the registered user into CSV
    def load_user(self):
        if not os.path.exists(self.file):
            logging.error(f'Failed to open {self.file}.')
            raise FileNotFound('The file is not exist! Make sure the JSON file name is correct!')
        with open(self.file, 'r') as file:
            user_dicts = json.load(file)
            self.registered_user = [RegisteredUser.from_dict(user_dict) for user_dict in user_dicts]





