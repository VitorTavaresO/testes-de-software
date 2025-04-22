import re
from src.messages import PasswordValidatorMessages

class PasswordValidator:
    def __init__(self):
        self.erros = []
        self.validation_patterns = [
            (re.compile(r'.{8,}'), PasswordValidatorMessages.ERROR_TOO_SHORT),
            (re.compile(r'[A-Z]'), PasswordValidatorMessages.ERROR_NO_UPPERCASE),
            (re.compile(r'[a-z]'), PasswordValidatorMessages.ERROR_NO_LOWERCASE),
            (re.compile(r'[0-9]'), PasswordValidatorMessages.ERROR_NO_NUMBER),
            (re.compile(r'[!@#$%^&*()\-_=+\[\]{};:,.<>?/]'), PasswordValidatorMessages.ERROR_NO_SPECIAL_CHAR),
            (re.compile(r'^[^ ]+$'), PasswordValidatorMessages.ERROR_HAS_SPACES),
        ]

    def get_errors(self):
        return self.erros

    def validate(self, password):
        self.erros = []
        for pattern, error_msg in self.validation_patterns:
            if not pattern.search(password):
                self.erros.append(error_msg)
        return len(self.erros) == 0