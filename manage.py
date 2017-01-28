#!/usr/bin/env python
import os
import sys
from getpass import getuser


def set_local_setting():
    username = getuser()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "hashboard.settings.local_{}".format(username))

if __name__ == "__main__":
    set_local_setting()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
