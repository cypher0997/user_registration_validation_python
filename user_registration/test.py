from user_validation import UserValidation
from user_validation_exception import UserValidationException
import unittest


class TestUserValidation(unittest.TestCase):

    def testing_first_name(self):
        """
        this test the first name validation
        :return: shows if test was passed or failed
        """
        try:
            user_validation = UserValidation()
            result = user_validation.validate("Anurag", "^[A-Z]{1}[a-z]{2,10}$")
            self.assertEqual(True, result)
        except ValueError:
            raise

    def testing_last_name(self):
        """
        this test the last name validation
        :return: shows if test was passed or failed
        """
        try:
            user_validation = UserValidation()
            result = user_validation.validate("Bhardwaj", "^[A-Z]{1}[a-z]{2,10}$")
            self.assertEqual(True, result)
        except ValueError:
            raise UserValidationException

    def testing_email(self):
        """
        this test the last email validation
        :return: shows if test was passed or failed
        """
        try:
            user_validation = UserValidation()
            result = user_validation.validate("abc.@bl.com", "^[a-z0-9]{3,}(.[0-9a-z]+)*@[a-z]{2,}.(com|edu)(co.in)*$")
            self.assertEqual(True, result)
        except ValueError:
            raise UserValidationException

    def testing_password(self):
        """
        this test the password validation
        :return: shows if test was passed or failed
        """
        try:
            user_validation = UserValidation()
            result = user_validation.validate("ANU1@-_rag",
                                              "^(?=.*[0-9])" + "(?=.*[@#$%^&+=])" + "(?=.*[a-z])(?=.*[A-Z])" +
                                              "(?=\\S+$).{8,20}$")
            self.assertEqual(True, result)
        except ValueError:
            raise UserValidationException

    def testing_mobile_number(self):
        """
        this test the mobile number validation
        :return: shows if test was passed or failed
        """
        try:
            user_validation = UserValidation()
            result = user_validation.validate("+91 6350391128", "^\\+[0-9]+\\s[0-9]{10,15}$")
            self.assertEqual(True, result)
        except ValueError:
            raise UserValidationException

    def testing_bad_input(self):
        try:
            neo_input = None
            with self.assertRaises(Exception):
                user_validation = UserValidation()
                user_validation.validate(neo_input, "^\\+[0-9]+\\s[0-9]{10,15}$")
        except ValueError:
            raise UserValidationException
