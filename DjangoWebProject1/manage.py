#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys

def method_name():
	from django.core.management import execute_from_command_line
	return execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "DjangoWebProject1.settings"
    )

    execute_from_command_line = method_name()

    execute_from_command_line(sys.argv)
