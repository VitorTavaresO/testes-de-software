import re

class PasswordValidator:
    def __init__(self):
        self.erros = []
        self.validation_patterns = [
            (re.compile(r'.{8,}'), "The password must be at least 8 characters long"),
            (re.compile(r'[A-Z]'), "The password must contain at least one uppercase letter"),
            (re.compile(r'[a-z]'), "The password must contain at least one lowercase letter"),
            (re.compile(r'[0-9]'), "The password must contain at least one number"),
            (re.compile(r'[!@#$%^&*()\-_=+\[\]{};:,.<>?/]'), "The password must contain at least one special character"),
            (re.compile(r'^[^ ]+$'), "The password must not contain blank spaces")
        ]

    def get_errors(self):
        return self.erros

    def validate(self, password):
        self.erros = []
        for pattern, error_msg in self.validation_patterns:
            if not pattern.search(password):
                self.erros.append(error_msg)
        return len(self.erros) == 0