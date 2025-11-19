def power_boost(multiplier):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * multiplier
        return wrapper
    return deco
