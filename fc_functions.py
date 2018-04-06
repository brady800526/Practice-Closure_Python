# First Class Function


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('p')
print_h1('Test Headline!')
print_h1('Another Paragraph!')


# Clousre


import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(
            func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)
