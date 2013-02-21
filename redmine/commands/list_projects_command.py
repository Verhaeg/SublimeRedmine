import sublime, sublime_plugin
import threading

from ..show_error import show_error

class RedmineListProjectsCommand(sublime_plugin.WindowCommand):
    """
    List Redmine projects
    """

    def run(self):
        RedmineListProjectsThread(self.window).start()

    def on_done(self, input):
        return True

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

class RedmineListProjectsThread(threading.Thread):
    """
    A thread to prevent the listing of projects from freezing the UI
    """

    def __init__(self, window):
        """
        :param window:
            An instance of :class:`sublime.Window` that represents the Sublime
            Text window to show the list of installed Projects in.
        """

        self.window = window
        print "ok"
        threading.Thread.__init__(self)

    def run(self):
        self.project_list = []

        def show_quick_panel():
            if not self.project_list:
                show_error('There are no projects to list')
                return
            self.window.show_quick_panel(self.project_list, self.on_done)
        sublime.set_timeout(show_quick_panel, 10)

    def on_done(self, picked):
        """
        Quick panel user selection handler - opens the homepage for any
        selected package in the user's browser

        :param picked:
            An integer of the 0-based package name index from the presented
            list. -1 means the user cancelled.
        """

        if picked == -1:
            return
        project_name = self.project_list[picked][0]

        def select_project():
            print project_name
        sublime.set_timeout(select_project, 10)
