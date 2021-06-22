class UserValidationException(Exception):
    def __init__(self, message="give valid input"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
