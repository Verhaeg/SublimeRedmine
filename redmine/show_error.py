import sublime


def show_error(string):
    """
    Displays an error message with a standard "Redmine" header

    :param string:
        The error to display
    """

    sublime.error_message(u'Redmine\n\n%s' % string)
