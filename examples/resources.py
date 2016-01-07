# ---------------------------------------------------------
# pygsmanager - A Scene Manager for pyglet.
# Copyright (c) 2016 Lucas de Morais Siqueira
# Distributed under the GNU Lesser General Public License version 3.
#
#       \ vvvvvvvvvvvvvvvvvvvvvvvvvvvvv /
#     >>> regular resource import stuff <<<
#       / ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \
#
# Support by using, forking, reporting issues and giving feedback:
#     https://github.com/LukeMS/pygsmanager/
#
#     Lucas de Morais Siqueira (aka LukeMS)
#     lucas.morais.siqueira@gmail.com
#
#
#    This file is part of pygsmanager.
#
#    pygsmanager is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    pygsmanager is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pygsmanager.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------


import os
import pyglet


res_list = []

_path = os.path.join('.', 'resources')
for root, dirs, files in os.walk(_path):
    name = str(root)
    res_list.append(name.replace('\\', r'/'))

pyglet.resource.path = res_list
