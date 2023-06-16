import re
import gitlab
import os
from no_ssl import no_ssl_verification

mb_sz = 1024 * 1024

with no_ssl_verification():
    gl = gitlab.Gitlab(url='https://{}'.format(os.environ['CI_SERVER_HOST']), private_token=os.environ['TOKEN'])
    gl.auth()
    project = gl.projects.get(432) #432
    print('Project - {}. {}'.format(project.id, project.path_with_namespace))
    delete_size = 0
    package_name = ""
    checked_package = []
    for package in project.packages.list(iterator=True):
        package_id = []
        if package.name not in checked_package:
            checked_package.append(package.name)
            for pack in project.packages.list(package_name=package.name, iterator=True):
                if "SNAPSHOT" in pack.version and pack.name == package.name:
                    print('{}. {}-{}'.format(pack.id, pack.name, pack.version))
                    package_id.append(pack.id)
            try:
                package_id.sort(reverse=True)
                package_id = [package_id[0], package_id[1]]
                print(package_id)
            except IndexError:
                print('Похоже что для пакета {} меньше 2-х snapshots'.format(pack.name))

            for pack in project.packages.list(package_name=package.name, iterator=True):
                if "SNAPSHOT" in pack.version and pack.name == package.name and pack.id not in package_id:
                    print('Package to delete - {}. {}-{}'.format(pack.id, pack.name, pack.version))
                    package_files = pack.package_files.list(get_all=True)
                    for package_file in package_files:
                        delete_size += package_file.size
                    ##########################
                    pack.delete()
                    #########################
            print('----------------------------------------------------')

    print(round(delete_size / mb_sz))
