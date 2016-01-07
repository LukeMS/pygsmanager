# ---------------------------------------------------------
# pygsmanager - A Scene Manager for pyglet.
# Copyright (c) 2016 Lucas de Morais Siqueira
# Distributed under the GNU Lesser General Public License version 3.
#
#       \ vvvvvvvvvvvvvvvvv /
#     >>> MAIN MENU EXAMPLE <<<
#       / ^^^^^^^^^^^^^^^^^ \
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
import shadowed_label

import resources


class MainMenu(scene_manager.BaseScene):
    """This class presents the title scene and options"""
    def __init__(self, manager):
        super(MainMenu, self).__init__(manager=manager)
        self.manager = manager
        self.window = manager.window

        self.batch = manager.batch

        self.create_bg('Karl_Brullov_-_The_Last_Day_of_Pompeii.jpg')

        self.create_title()

        self.create_menu()
        self.selection = 0
        self._menu[self.selection]['label'].highlight()

    def create_bg(self, img):
        self.bg = pyglet.sprite.Sprite(
            pyglet.resource.image(img),
            batch=self.batch,
            group=pyglet.graphics.OrderedGroup(0))

    def create_title(self):
        self.title = shadowed_label.ShadowedLabel(
            text='Pyglet Scene Manager v1.0',
            font_name='Arial',
            font_size=int(self.window.height // 17),
            color=(223, 0, 0, 223),
            x=self.window.width // 2,
            y=int(self.window.height // 5 * 4),
            anchor_x='center', anchor_y='center',
            batch=self.batch,
            layer=2)

    def create_menu(self):
        import scene_a
        self._menu = menu = [
            {
                "text": "The Last Day of Pompeii (Karl Brullov)",
                "kwargs": {
                    "scene": scene_a.Scene,
                    "manager": self.manager,
                    "img":
                        'Karl_Brullov_-_The_Last_Day_of_Pompeii.jpg',
                    "target": {
                        "scene": MainMenu,
                        "manager": self.manager
                    }
                }
            },
            {
                "text": "Sacrifice of Isaac (Caravaggio)",
                "kwargs": {
                    "scene": scene_a.Scene,
                    "manager": self.manager,
                    "img":
                        'Sacrifice_of_Isaac-Caravaggio.jpg',
                    "target": {
                        "scene": MainMenu,
                        "manager": self.manager
                    }
                }
            },
            {
                "text": (
                    "Evening shadows backwater of the Murray "
                    "(H. J. Johnstone)"
                ),
                "kwargs": {
                    "scene": scene_a.Scene,
                    "manager": self.manager,
                    "img": (
                        'HJ_Johnstone-'
                        'Evening_shadows_backwater_of_the_Murray.jpg'),
                    "target": {
                        "scene": MainMenu,
                        "manager": self.manager
                    }
                }
            },
            {
                "text": "Quit",
                "kwargs": {
                    "scene": None
                }
            }
        ]

        for i in range(len(menu)):
            item = menu[i]
            item["label"] = shadowed_label.ShadowedLabel(
                text=item["text"],
                font_name='Arial',
                font_size=24,
                color=(255, 255, 255, 223),
                x=self.window.width // 2,
                y=(
                    self.title.y - self.title.content_height * 2 -
                    self.window.height // 10 * i
                ),
                anchor_x='center', anchor_y='center',
                batch=self.batch,
                layer=2)

    def change_selection(self, symbol):
        self._menu[self.selection]['label'].unlit()
        if symbol == key.UP:
            self.selection -= 1
        else:
            self.selection += 1
        self.selection = self.selection % len(self._menu)
        self._menu[self.selection]['label'].highlight()

    def clear(self):
        self.title.delete()
        for menu in self._menu:
            menu['label'].delete()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.window.on_close()
        elif symbol in [key.UP, key.DOWN]:
            self.change_selection(symbol)
        elif symbol == key.RETURN:
            getattr(
                self.manager,
                "set_scene"
            )(**self._menu[self.selection]['kwargs'])


if __name__ == '__main__':
    manager = scene_manager.Manager(
        scene=MainMenu)
    manager.execute()
