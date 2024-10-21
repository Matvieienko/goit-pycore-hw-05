def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "🛑 This contact does not exist."
        except ValueError:
            return "⚠️  Give me name and phone, please."
        except IndexError:
            return "⚠️  Enter the argument for the command."
        
    return inner
