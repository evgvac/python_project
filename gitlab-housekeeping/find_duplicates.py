import re
import gitlab
import os
import sys
from no_ssl import no_ssl_verification

mb_sz = 1024 * 1024

with no_ssl_verification():
    gl = gitlab.Gitlab(url='https://{}'.format(os.environ['CI_SERVER_HOST']), private_token=os.environ['TOKEN'])
    gl.auth()
    delete_size = 0
    pattern = re.compile(r'(-\d{8}.\d{6}-\d{1,4})')
    projects_list = sys.argv[1:]
    for project_id in projects_list:
        project = gl.projects.get(432)
        print('Project - {}. {}'.format(project.id, project.path_with_namespace))
        for package in project.packages.list(iterator=True):
            filename_dict = {}
            package_files = package.package_files.list(get_all=True)
            for package_file in package_files:
                filename = re.sub(pattern, '', package_file.file_name)
                if filename in filename_dict:
                    filename_dict[filename] += 1
                else:
                    filename_dict[filename] = 1
            for filename in filename_dict.keys():
                if filename_dict[filename] != 1:
                    print(filename)
                    file_id = 0
                    for package_file in package_files:
                        if filename == re.sub(pattern, '', package_file.file_name):
                            print('{}. {} {} Size = {}'.format(package_file.id, package_file.created_at, package_file.file_name, package_file.size))
                            if package_file.id > file_id:
                                file_id = package_file.id
                    print(file_id)
                    for i in range(len(package_files)):
                        file = package_files[i]
                        if filename == re.sub(pattern, '', file.file_name) and file.id != file_id:
                            print('File to delete - {}. {} '.format(file.id, file.file_name))
                            delete_size += file.size
                            # ##################!!!!!!!!!!!!!
                            file.delete()
                            # ##############!!!!!!!!!!!!!!
    print('{}Мб удалено'.format(round(delete_size/mb_sz)))


