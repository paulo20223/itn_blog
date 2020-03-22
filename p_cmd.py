#!/usr/bin/env python3
import os
from shutil import rmtree
from sys import argv


class Command:
    _postgres_container_name = 'itn-postgres'
    _web_container_name = 'itn-web'
    _web_service_name = 'web'
    _default_db = 'postgres'

    def __init__(self, cmd, *args):
        self._cmd = cmd
        self._args = args

    def __call__(self):
        try:
            getattr(self, self._cmd)(*self._args)
        except AttributeError:
            self.man()

    def rm_m(self):
        """./cmd rm_m - remove migrations for all apps for django project."""

        rmtree(os.path.join('core', 'migrations'), ignore_errors=True)

    def renew(self):
        """./cmd renew - start rm_m(), setup() and csu() methods."""

        self.rm_m()
        self.setup()
        self.csu()

    def rn(self, *args):
        """./cmd rn - down, build and up all docker containers, start renew"""
        os.system('docker-compose down -v')
        os.system('docker-compose build')
        os.system('docker-compose up -d')
        self.renew()
        os.system('docker-compose stop')

    def cs(self):
        """./cmd cs - execute "python manage.py collectstatic" command for django project"""

        os.system(f'docker exec -it {self._web_container_name} python manage.py collectstatic --noinput')

    def renewdb(self):
        """WARNING! It doesn\'t work correctly due to the fact that you cann\'t kill the database that\'s currently used'
        ./cmd renewdb - recreate postgres database from health_postgres container and run migrate."""

        os.system(
            f'docker exec {self._postgres_container_name} psql -U postgres -c \"drop database {self._default_db};\"')
        self.m()

    def bash(self):
        """./cmd bash - go to bash on health_web container."""

        os.system(f'docker exec -it {self._web_container_name} bash')

    def bashdb(self):
        """./cmd bashdb - go to bash on {self._postgres_container_name} container."""

        os.system(f'docker exec -it {self._postgres_container_name} bash')

    def m(self):
        """./cmd m - execute "python manage.py migrate" command for django project"""

        os.system(f'docker exec -it {self._web_container_name} python manage.py migrate')

    def django(self):
        """./cmd django - execute python console with load django project"""

        os.system(f'docker exec -it {self._web_container_name} python manage.py shell')

    def pip(self):
        """./cmd django - execute python console with load django project"""

        os.system(f'docker exec -it {self._web_container_name} python -m pip install -r requirements_dev.txt')

    def mkm(self, *args):
        """./cmd mkm - execute "python manage.py makemigrations" command for every app for django project"""

        os.system(f'docker exec -it {self._web_container_name} python manage.py makemigrations core')

    def csu(self):
        """./cmd csu - execute "python manage.py createsuperuser" command for django project"""

        print('Please, fill data for superuser account: ')
        os.system(f'docker exec -it {self._web_container_name} python manage.py createsuperuser')

    def setup(self):
        """./cmd setup - execute "python manage.py makemigrations" and "python manage.py migrate"
              for every app (start with core) for django project"""

        self.mkm()
        self.m()

    def _get_all_docstrings_from_public_methods(self):
        return tuple([getattr(self, name).__doc__ for name, _ in Command.__dict__.items()
                      if not name.startswith('_') and getattr(self, name).__doc__ and callable(getattr(self, name))])

    def man(self):
        print(*self._get_all_docstrings_from_public_methods(), sep='\n')


if __name__ == '__main__':
    Command(*argv[1:])()
