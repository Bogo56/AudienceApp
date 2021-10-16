import os, sys
from kivy.resources import resource_add_path
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from controller.controller import AudienceManager
from model.model import Model
from kivy.core.audio import SoundLoader
from kivy.core.audio import SoundLoader

Builder.load_file("menu.kv")
Builder.load_file("audience.kv")
Builder.load_file("token.kv")


"""
This module controls the graphical user interface and connects it with controller classes and methods.
"""

class MainMenuScreen(Screen):

    sound = SoundLoader.load('resources/music/star_wars.mp3')
    sound_saber = SoundLoader.load('resources/music/saber.mp3')

    sound_saber.play()

    # Playing a LightSaber sound on startup. The App design is Star Wars inspired (kind of :D)
    def the_force_on(self):
        if self.sound:
            self.sound.play()
            self.ids.force_quote.text = "May The Force Guide You JEDI"

    def the_force_off(self):
        if self.sound:
            self.sound.stop()
            self.ids.force_quote.text = ""


class AudienceScreen(Screen):

    def search_audience(self):
        if self.ids.toggler.state != "down":
            keyword = self.ids.keyword.text
            limit= 300
            if keyword:
                res = AudienceManager.get_interest(keyword=keyword,
                                                   limit=limit)
                if res:
                    self.ids.output.text = res
                    self.ids.audience_log.text = ""
                else:
                    self.ids.audience_log.text = "Missing Token"
            else:
                self.ids.audience_log.text = "Enter A Keyword First"
        else:
            self._suggest()

    def _suggest(self):
        keyword = self.ids.keyword.text
        limit= 450
        if keyword:
            res = AudienceManager.get_suggestion(keyword=keyword,
                                                 limit=limit)
            if res:
                self.ids.output.text = res
                self.ids.audience_log.text = ""
            else:
                self.ids.audience_log.text = "Missing Token"
        else:
            self.ids.audience_log.text = "Enter A Keyword First"


class TokenScreen(Screen):

    def enter_token(self):
        token = self.ids.token.text
        if token:
            Model.insert_token(token=token)
            self.ids.token_log.text = "Token Updated"
        else:
            self.ids.token_log.text = "Enter A Token First"


class ScreenSwitch(ScreenManager):
    pass


class AudienceTool(App):
    def build(self):
        Window.clearcolor = (0/255,0/255,0/255,1)
        return ScreenSwitch()




if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    AudienceTool().run()