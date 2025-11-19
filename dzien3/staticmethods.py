class PasswordValidator:
    @staticmethod
    def has_upper(text):
        return any(c.isupper() for c in text)

    @staticmethod
    def has_digit(text):
        return any(c.isdigit() for c in text)

    @staticmethod
    def has_min_length(text, n = 8):
        return len(text) >= n

    @staticmethod
    def has_special(text):
        specials = "!@#$%^&*()-_=+[]{};:',.<>?/\\|~"
        return any(c in specials for c in text)

    def validate(self, text):
        return (self.has_upper(text) and self.has_digit(text) and
                self.has_min_length(text) and self.has_special(text))

validator = PasswordValidator()
paswd1 = "HelloWorld"
paswd2 = "Python25!"
paswd7 = "Pyth25!"
paswd3 = "1346655"
paswd4 = "abcDEF"
paswd5 = "abcbnmvbn"

print(f"{paswd1}: {validator.validate(paswd1)}")
print(f"{paswd2}: {validator.validate(paswd2)}")
print(f"{paswd7}: {validator.validate(paswd7)}")
print(f"{paswd3}: {validator.validate(paswd3)}")
print(f"{paswd4}: {validator.validate(paswd4)}")
print(f"{paswd5}: {validator.validate(paswd5)}")
