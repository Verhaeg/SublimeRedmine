import sublime
import sys


def console_write(string, prefix=False):
    """
    Writes a value to the Sublime Text console, encoding unicode to utf-8 first

    :param string:
        The value to write

    :param prefix:
        If the string "Redmine: " should be prefixed to the string
    """

    if int(sublime.version()) < 3000:
        if isinstance(string, unicode):
            string = string.encode('UTF-8')
    if prefix:
        sys.stdout.write('Redmine: ')
    print(string)
