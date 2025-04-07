import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
import pygame
import os

kivy.require('2.0.0')

class FlacPlayer(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Select a FLAC file to play', font_size='20sp')
        self.layout.add_widget(self.label)

        self.filechooser = FileChooserListView(filters=['*.flac'])
        self.filechooser.bind(on_selection=self.play_flac)
        self.layout.add_widget(self.filechooser)

        self.stop_button = Button(text='Stop', size_hint=(1, 0.2))
        self.stop_button.bind(on_press=self.stop_flac)
        self.layout.add_widget(self.stop_button)

        pygame.mixer.init()

        return self.layout

    def play_flac(self, filechooser, selection):
        if selection:
            file_path = selection[0]
            self.label.text = f'Playing: {os.path.basename(file_path)}'
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

    def stop_flac(self, instance):
        pygame.mixer.music.stop()
        self.label.text = 'Select a FLAC file to play'

if __name__ == '__main__':
    FlacPlayer().run()