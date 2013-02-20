import sublime
import sys

from imp import reload

reloader_name = 'Redmine.redmine.reloader'
# Make sure all dependencies are reloaded on upgrade
if reloader_name in sys.modules:
    reload(sys.modules[reloader_name])

try:
    # Python 3
    from .redmine import reloader

#     from .redmine.commands.add_repository_channel_command import AddRepositoryChannelCommand
#     from .redmine.commands.add_repository_command import AddRepositoryCommand
#     from .redmine.commands.create_binary_package_command import CreateBinaryPackageCommand
#     from .redmine.commands.create_package_command import CreatePackageCommand
#     from .redmine.commands.disable_package_command import DisablePackageCommand
#     from .redmine.commands.discover_packages_command import DiscoverPackagesCommand
#     from .redmine.commands.enable_package_command import EnablePackageCommand
#     from .redmine.commands.install_package_command import InstallPackageCommand
#     from .redmine.commands.list_packages_command import ListPackagesCommand
#     from .redmine.commands.remove_package_command import RemovePackageCommand
#     from .redmine.commands.upgrade_all_packages_command import UpgradeAllPackagesCommand
#     from .redmine.commands.upgrade_package_command import UpgradePackageCommand

#     from .redmine.package_cleanup import PackageCleanup

except (ValueError):
    # Python 2
    from redmine import reloader

#     from redmine.commands.add_repository_channel_command import AddRepositoryChannelCommand
#     from redmine.commands.add_repository_command import AddRepositoryCommand
#     from redmine.commands.create_binary_package_command import CreateBinaryPackageCommand
#     from redmine.commands.create_package_command import CreatePackageCommand
#     from redmine.commands.disable_package_command import DisablePackageCommand
#     from redmine.commands.discover_packages_command import DiscoverPackagesCommand
#     from redmine.commands.enable_package_command import EnablePackageCommand
#     from redmine.commands.install_package_command import InstallPackageCommand
#     from redmine.commands.list_packages_command import ListPackagesCommand
#     from redmine.commands.remove_package_command import RemovePackageCommand
#     from redmine.commands.upgrade_all_packages_command import UpgradeAllPackagesCommand
#     from redmine.commands.upgrade_package_command import UpgradePackageCommand

#     from redmine.package_cleanup import PackageCleanup
