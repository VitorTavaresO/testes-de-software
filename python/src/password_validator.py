class PasswordValidator:
    def __init__(self):
        self.erros = []

    def get_errors(self):
        return self.erros

    def validate(self, password):
        if len(password) < 8:
            self.erros.append("The password must be at least 8 characters long")
            return False
       
        elif not any(char.isupper() for char in password):
            self.erros.append("The password must contain at least one uppercase letter")
            return False
       
        elif not any(char.islower() for char in password):
            self.erros.append("The password must contain at least one lowercase letter")
            return False
        
        elif not any(char.isdigit() for char in password):
            self.erros.append("The password must contain at least one number")
            return False
        
        elif not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password):
            self.erros.append("The password must contain at least one special character")
            return False
        
        elif " " in password:
            self.erros.append("The password must not contain blank spaces")
            return False
        
        return True
    