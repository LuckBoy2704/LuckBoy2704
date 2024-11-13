import time

def show_time(func):
    def wrapper(bot, message, text, buttons):
        start_time = time.time()
        result = func(bot, message, text, buttons)
        end_time = time.time()
        res = end_time - start_time
        print('Res: ',res)
        return result
    return wrapper
