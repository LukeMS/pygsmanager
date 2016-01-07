# ---------------------------------------------------------
# pygsmanager - A Scene Manager for pyglet.
# Copyright (c) 2016 Lucas de Morais Siqueira
# Distributed under the GNU Lesser General Public License version 3.
#
#       \ vvvvvvvvvvvvv /
#     >>> SCENE EXAMPLE <<<
#       / ^^^^^^^^^^^^^ \
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


import sys
import os

import pyglet
from pyglet.window import key

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import scene_manager

import resources


class Scene(scene_manager.BaseScene):
    def __init__(self, manager, img=None, target=None):
        super(Scene, self).__init__(manager=manager)
        self.manager = manager
        self.window = manager.window
        self.batch = manager.batch
        self.target = target

        if img:
            self.create_bg(img)

    def create_bg(self, img):
        self.bg = pyglet.sprite.Sprite(
            pyglet.resource.image(img),
            batch=self.batch,
            group=pyglet.graphics.OrderedGroup(0))

    def on_key_press(self, symbol, modifiers):
        if symbol in [key.ESCAPE, key.RETURN]:
            self.go_to(**self.target)


if __name__ == '__main__':
    manager = scene_manager.Manager(
        scene=Scene)
    manager.execute()
