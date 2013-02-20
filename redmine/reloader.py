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

mod_prefix = 'Redmine.redmine'

mods_load_order = [
    '',

    '.console_write',
    '.show_error',
    '.thread_progress',

    # '.commands',
    # '.commands.add_repository_channel_command',
    # '.commands.add_repository_command',
    # '.commands.create_binary_package_command',
    # '.commands.create_package_command',
    # '.commands.disable_package_command',
    # '.commands.discover_packages_command',
    # '.commands.enable_package_command',
    # '.commands.existing_packages_command',
    # '.commands.install_package_command',
    # '.commands.list_packages_command',
    # '.commands.remove_package_command',
    # '.commands.upgrade_all_packages_command',
    # '.commands.upgrade_package_command',
]

for suffix in mods_load_order:
    mod = mod_prefix + suffix
    if mod in reload_mods:
        reload(sys.modules[mod])
