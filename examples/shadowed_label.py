# ---------------------------------------------------------
# pygsmanager - A Scene Manager for pyglet.
# Copyright (c) 2016 Lucas de Morais Siqueira
# Distributed under the GNU Lesser General Public License version 3.
#
#       \ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv /
#     >>> just two labels above each other to improve visibility <<<
#       / ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \
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


import pyglet


class ShadowedLabel():
    def __init__(
            self, text="", x=64, y=64,
            color=(223, 0, 0, 223),
            shadow_opacity = 127,
            layer=1, **kwargs):
        if layer == 0:
            layer += 1

        self.unlit_color = color
        self.shadow_opacity = shadow_opacity
        self.set_shadow_color(color)
        self.set_highlighted_color()

        self.shadow = pyglet.text.Label(
            text=text, x=x + 3, y=y - 3,
            color=self.shadow_color,
            group=pyglet.graphics.OrderedGroup(layer - 1),
            **kwargs)
        self.label = pyglet.text.Label(
            text=text, x=x, y=y,
            color=color,
            group=pyglet.graphics.OrderedGroup(layer),
            **kwargs)

        self.x = self.label.x
        self.y = self.label.y
        self.content_width = self.label.content_width
        self.content_height = self.label.content_height

    def set_shadow_color(self, color=False):
        shadow_color = list(color)
        for i in range(3):
            shadow_color[i] = shadow_color[i] // 3
        shadow_color[3] = self.shadow_opacity
        self.shadow_color = tuple(shadow_color)

    def set_highlighted_color(self):
        highlighted_color = list(self.unlit_color)
        for i in [0, 1, 3]:
            highlighted_color[i] = (
                (255 - highlighted_color[i]) // 2 +
                highlighted_color[i]
            )
        highlighted_color[2] = highlighted_color[2] // 3
        self.highlighted_color = tuple(highlighted_color)

    def highlight(self):
        self.label.color = self.highlighted_color

    def unlit(self):
        self.label.color = self.unlit_color

    def delete(self):
        self.shadow.delete()
        self.label.delete()

    def draw(self):
        self.shadow.draw()
        self.label.draw()
