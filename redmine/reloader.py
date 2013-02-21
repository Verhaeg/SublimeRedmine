import sublime
import sys

from imp import reload

# Python allows reloading modules on the fly, which allows us to do live upgrades.
# The only caveat to this is that you have to reload in the dependency order.
#
# Thus is module A depends on B and we don't reload B before A, when A is reloaded
# it will still have a reference to the old B. Thus we hard-code the dependency
# order of the various Redmine modules so they get reloaded properly.
#
# There are solutions for doing this all programatically, but this is much easier
# to understand.

reload_mods = []
for mod in sys.modules:
    if mod[0:15].lower().replace(' ', '_') == 'redmine' and sys.modules[mod] != None:
        reload_mods.append(mod)

mod_prefix = 'redmine.redmine'

mods_load_order = [
    '',

    '.console_write',
    '.show_error',
    '.thread_progress',

    '.commands',
    '.commands.list_projects_command'
]

for suffix in mods_load_order:
    mod = mod_prefix + suffix
    if mod in reload_mods:
        reload(sys.modules[mod])
