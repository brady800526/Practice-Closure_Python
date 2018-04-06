# First Class Function


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('p')
print_h1('Test Headline!')
print_h1('Another Paragraph!')


# Clousre


# import logging
# logging.basicConfig(filename='example.log', level=logging.INFO)


# def logger(func):
#     def log_func(*args):
#         logging.info('Running "{}" with arguments {}'.format(
#             func.__name__, args))
#         print(func(*args))
#     return log_func


# def add(x, y):
#     return x + y


# def sub(x, y):
#     return x - y


# add_logger = logger(add)
# sub_logger = logger(sub)

# add_logger(3, 3)
# add_logger(4, 5)

# sub_logger(10, 5)
# sub_logger(20, 10)


# Decorator
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}. and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec.'.format(orig_func.__name__, t2))
        return result

    return wrapper


import time


@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
