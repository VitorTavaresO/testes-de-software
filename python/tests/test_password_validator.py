import pytest
from src.password_validator import PasswordValidator

def test_password_with_less_than_8_characters():
    validator = PasswordValidator()
    password = "1234567"
    
    result = validator.validate(password)
    
    assert result is False
    assert "The password must be at least 8 characters long" in validator.get_errors()

def test_password_without_uppercase():
    validator = PasswordValidator()
    password = "12345678"
    
    result = validator.validate(password)
    
    assert result is False
    assert "The password must contain at least one uppercase letter" in validator.get_errors()

def test_password_without_lowercase():
    validator = PasswordValidator()
    password = "12345678A"
    
    result = validator.validate(password)
    
    assert result is False
    assert "The password must contain at least one lowercase letter" in validator.get_errors()

def test_password_without_number():
    validator = PasswordValidator()
    password = "abCdEfgH"
    
    result = validator.validate(password)
    
    assert result is False
    assert "The password must contain at least one number" in validator.get_errors()

def test_password_without_special_character():
    validator = PasswordValidator()
    password = "Abcdefgh1"
    
    result = validator.validate(password)
    
    assert result is False
    assert "The password must contain at least one special character" in validator.get_errors()

def test_password_with_blank_space():
    validator = PasswordValidator()
    password = "Abcdefgh1! "
    
    result = validator.validate(password)
    
    assert result is False
    assert "The password must not contain blank spaces" in validator.get_errors()

def test_valid_password():
    validator = PasswordValidator()
    password = "Abcde123!"
    
    result = validator.validate(password)
    
    assert result is True
    assert len(validator.get_errors()) == 0

def test_password_with_multiple_errors():
    validator = PasswordValidator()
    password = "abc"
    
    result = validator.validate(password)
    
    assert result is False
    assert "The password must be at least 8 characters long" in validator.get_errors()
    assert "The password must contain at least one uppercase letter" in validator.get_errors()
    assert "The password must contain at least one number" in validator.get_errors()
    assert "The password must contain at least one special character" in validator.get_errors()
    
def test_empty_password():
    validator = PasswordValidator()
    password = ""
    
    result = validator.validate(password)
    
    assert result is False
    assert "The password must be at least 8 characters long" in validator.get_errors()