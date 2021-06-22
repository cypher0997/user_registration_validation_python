import re
from user_validation_exception import UserValidationException


class UserValidation:

    def returns_user_input(self):
        """
        takes user input in string , that will be validated against the corresponding pattern
        :return: returns user input for further operation
        """
        user_input = input("enter the valid input")
        return user_input

    def returns_pattern(self):
        """
        on basis of user choice it will give correct pattern for checking or validating
        :return: returns pattern for checking or validation
        """
        patterns_for_validation = {1: "^[A-Z]{1}[a-z]{2,10}$",
                                   2: "^[A-Z]{1}[a-z]{2,10}$",
                                   3: "^[a-z0-9]{3,}(.[0-9a-z]+)*@[a-z]{2,}.(com|edu)(co.in)*$",
                                   4: "^\\+[0-9]+\\s[0-9]{10,15}$",
                                   5: "^(?=.*[0-9])" + "(?=.*[@#$%^&+=])" + "(?=.*[a-z])(?=.*[A-Z])" + "(?=\\S+$).{8,"
                                                                                                       "20}$ "
                                   }
        choice = int(input("enter the choice,for first name validation enter '1',for  last name '2'" +
                           ",for email '3',for mobile number '4',for password '5'"))
        if choice is None:
            raise UserValidationException
        for i in patterns_for_validation:
            if choice == i:
                return patterns_for_validation.get(i)

    def validate(self, usr_input, patterns):
        """
        this methods performs main operation or validation of basis of required input
        :param usr_input: user given string that is checked for validation
        :param patterns: pattern against which user input is being checked
        :return: returns true if pattern and input is matched or false if its not
        """
        u_i = usr_input
        pattern = patterns
        if re.search(pattern, u_i):
            return True
        else:
            return False
