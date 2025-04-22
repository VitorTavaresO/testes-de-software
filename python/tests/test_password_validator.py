import pytest
from src.password_validator import PasswordValidator
from src.messages import PasswordValidatorMessages

def test_password_with_less_than_8_characters():
    validator = PasswordValidator()
    password = "1234567"
    
    result = validator.validate(password)
    
    assert result is False
    assert PasswordValidatorMessages.ERROR_TOO_SHORT in validator.get_errors()

def test_password_without_uppercase():
    validator = PasswordValidator()
    password = "12345678"
    
    result = validator.validate(password)
    
    assert result is False
    assert PasswordValidatorMessages.ERROR_NO_UPPERCASE in validator.get_errors()

def test_password_without_lowercase():
    validator = PasswordValidator()
    password = "12345678A"
    
    result = validator.validate(password)
    
    assert result is False
    assert PasswordValidatorMessages.ERROR_NO_LOWERCASE in validator.get_errors()

def test_password_without_number():
    validator = PasswordValidator()
    password = "abCdEfgH"
    
    result = validator.validate(password)
    
    assert result is False
    assert PasswordValidatorMessages.ERROR_NO_NUMBER in validator.get_errors()

def test_password_without_special_character():
    validator = PasswordValidator()
    password = "Abcdefgh1"
    
    result = validator.validate(password)
    
    assert result is False
    assert PasswordValidatorMessages.ERROR_NO_SPECIAL_CHAR in validator.get_errors()

def test_password_with_blank_space():
    validator = PasswordValidator()
    password = "Abcdefgh1! "
    
    result = validator.validate(password)
    
    assert result is False
    assert PasswordValidatorMessages.ERROR_HAS_SPACES in validator.get_errors()

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
    assert PasswordValidatorMessages.ERROR_TOO_SHORT in validator.get_errors()
    assert PasswordValidatorMessages.ERROR_NO_UPPERCASE in validator.get_errors()
    assert PasswordValidatorMessages.ERROR_NO_NUMBER in validator.get_errors()
    assert PasswordValidatorMessages.ERROR_NO_SPECIAL_CHAR in validator.get_errors()
    
def test_empty_password():
    validator = PasswordValidator()
    password = ""
    
    result = validator.validate(password)
    
    assert result is False
    assert PasswordValidatorMessages.ERROR_TOO_SHORT in validator.get_errors()