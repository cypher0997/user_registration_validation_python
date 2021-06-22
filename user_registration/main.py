from user_validation_exception import UserValidationException
from user_validation import UserValidation


def main():
    """
    all the execution will start from here
    :return: it prints the result of validation
    """
    try:
        user_validate = UserValidation()
        usr_input = user_validate.returns_user_input()
        patterns = user_validate.returns_pattern()
        res = user_validate.validate(usr_input, patterns)
        print(res)
    except ValueError:
        raise UserValidationException


if __name__ == '__main__':
    main()
