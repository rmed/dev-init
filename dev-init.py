#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# dev-init
# https://github.com/rmed/dev-init
#
# Copyright (C) 2014  Rafael Medina García <rafamedgar@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
import argparse
import sys

try:
    from configparser import ConfigParser
except ImportError:
    import ConfigParser


def _init_parser():
    """ Initialize the arguments parser. """
    parser = argparse.ArgumentParser(
        description="Automatic initialization of development environment")

    # List group
    group_list = parser.add_argument_group()
    group_list.add_argument("-l", "--list", action="store_true",
        help="list all the available environment types")

    # Actions group
    group_actions = parser.add_mutually_exclusive_group()

    group_actions.add_argument("-n", "--new", metavar="env",
        help="define a new environment type")

    group_actions.add_argument("-r", "--remove", metavar="env",
        help="remove an environment type from the configuration file")

    group_actions.add_argument("-s", "--show", metavar="env",
        help="show the commands performed for a specific environemnt")

    # Default init group
    group_init = parser.add_argument_group()
    group_init.add_argument("init_env", metavar="env_type", nargs="?",
        help="initialize a new environment in current directory")


    return parser

def parse_action(parsed):
    """ Parse the action to execute. """
    if parsed.init_env:
        return init_env()

    elif parsed.list:
        return list_env(parsed.list)

    elif parsed.new:
        return new_env(parsed.new)

    elif parsed.remove:
        return remove_env(parsed.remove)

    elif parsed.show:
        return show_env(parsed.show)

if __name__ == "__main__":

    parser = _init_parser()
    args = parser.parse_args()

    if len(sys.argv) == 1:
        # No argument provided
        parser.print_help()

    parse_action(args)
