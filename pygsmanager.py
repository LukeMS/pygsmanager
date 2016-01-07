# ---------------------------------------------------------
# pygsmanager - A Scene Manager for pyglet.
# Copyright (c) 2016 Lucas de Morais Siqueira
# Distributed under the GNU Lesser General Public License version 3.
#
#       \ vvvvvvvvvvvvv /
#     >>> SCENE MANAGER <<<
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


import pyglet


class Window(pyglet.window.Window):
    def __init__(self, manager, width=1024, height=768, *args, **kwargs):
        super(Window, self).__init__(
            caption='Pyglet Scene Manager v1.0',
            width=width, height=height, *args, **kwargs)
        self.manager = manager
        self.batch = manager.batch

    def on_draw(self):
        """
        The drawing is performed via batch.draw() in Manager update function.
        """
        pass

    def on_key_held(self, dt):
        # a key_press function for the keys that will act while pressed
        self.manager.current_scene.on_key_held()

    def on_key_press(self, symbol, modifiers):
        self.manager.current_scene.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.manager.current_scene.on_key_release(symbol, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.manager.current_scene.on_mouse_scroll(x, y, scroll_x, scroll_y)


class BaseScene(object):
    """
    A Basic scene template to be inherited.
    """
    def __init__(self, manager):
        self.manager = manager
        self.children = []

    def start(self):
        pass

    def clear(self):
        def _delete(children):
            """
            A simple delete procedure that iterates over nested children.
            """
            for child in children:
                if type(child) in [list, tuple, dict]:
                    _delete(child)
                else:
                    child.delete()

        _delete(self.children)

    def go_to(self, *args, **kwargs):
        getattr(
            self.manager,
            "set_scene"
        )(*args, **kwargs)

    def on_key_held(self):
        """
        Actions that will be performed while the key is held down.
        Usage:
            if self.manager._keyboard[key.UP]:
                do_something()
        """
        pass

    def on_key_press(self, symbol, modifiers):
        """
        Actions that will be performed as soon as the key is pressed.
        Usage:
            if symbol  == key.UP:
                do_something()
        """
        pass

    def on_key_release(self, symbol, modifiers):
        """
        Actions that will be performed after key_press+key_release.
        Usage:
            if symbol  == key.UP:
                do_something()
        """
        pass

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass

    def on_close(self):
        self.manager.window.on_close()

    def update(self):
        """
        Should something need to be updated every frame.
        Causes performance decrease.
        """
        pass

    def on_draw(self):
        """
        The Manager.batch.draw() is called via Manager.update.
        Only use scene's on_draw if necessary, it will decrease performance.
        """
        pass


class Manager(object):
    def __init__(
            self, scene=BaseScene, framerate=60, *args, **kwargs):

        self.batch = pyglet.graphics.Batch()
        self.window = Window(manager=self, *args, **kwargs)
        self._keyboard = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(self._keyboard)

        self.set_scene(scene, manager=self)

        pyglet.clock.schedule_interval(self.update, 1 / framerate)

    def update(self, dt):
        self.current_scene.update()
        self.current_scene.on_draw()
        self.window.clear()
        self.batch.draw()

    def set_scene(self, scene=None, *args, **kwargs):
        if scene is None:
            self.window.on_close()
        else:
            if "current_scene" in self.__dict__:
                self.old_scene = self.current_scene
                self.current_scene = scene(*args, **kwargs)
                self.clear_scene()
            else:
                self.current_scene = scene(*args, **kwargs)
            self.start_scene()

    def clear_scene(self):
        self.old_scene.clear()
        del self.old_scene

    def start_scene(self):
        self.current_scene.start()

    def execute(self):
        pyglet.app.run()
