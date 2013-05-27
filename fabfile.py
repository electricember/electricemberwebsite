# This is only an example. It is not meant to be used without editing
#   Documentation can be found at http://docs.fabfile.org/en/1.4.3/

from fabric.api import lcd, local

def prepare_deployment(branch_name):
        local('python manage.py test django_project')
            local('git add -p && git commit') # or local('hg add && hg commit')

def deploy():
    with lcd('/path/to/my/prod/area/'):
        # If hosting on remote server, use run() function instead of local()
        #   See documentation for details
        local('git pull /my/path/to/dev/area/')
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')
