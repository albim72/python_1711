class AgeError(Exception):
    def __init__(self, n, message):
        super().__init__(message)
        self.n = n
    def __str__(self):
        return f"Age must be greater than 18. {self.n} is not valid."

def register_user(n,msg):
    if n < 18:
        raise AgeError(n,"user must have age greater than 18.")
    return "User registered successfully."

try:
    result = register_user(12,"user must have age greater than 18.")
    print(result)
except AgeError as e:
    print(f"Error: {e}")
