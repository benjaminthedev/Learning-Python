import platform


def main():
    message()


def message():
    print('this is python version {}'.format(platform.python_version()))
    print('Hello World')


print('See I come first but if I was indented I would come after the Hello World Print')
# if I do a print outside of the loop it will come first
