from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from plyer import accelerometer, gyroscope
import os
os.environ['KIVY_WINDOW'] = 'dummy'  # Disable GUI
os.environ['KIVY_GRAPHICS'] = 'dummy'
os.environ['KIVY_AUDIO'] = 'dummy'


# Kivy UI Layout
kv = '''
<LoadingScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Checking device sensors...'
            font_size: '20sp'

<ErrorScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'This app requires a gyroscope and accelerometer.\\nYour device does not support these sensors.'
            font_size: '20sp'
            halign: 'center'
            valign: 'middle'
            text_size: self.size

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'App Loaded Successfully!'
            font_size: '30sp'
'''

Builder.load_string(kv)

class LoadingScreen(Screen):
    pass

class ErrorScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class SensorCheckApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoadingScreen(name='loading'))
        self.sm.add_widget(ErrorScreen(name='error'))
        self.sm.add_widget(MainScreen(name='main'))
        return self.sm

    def on_start(self):
        # Check sensors after app initialization
        self.check_sensors()

    def check_sensors(self):
        has_accel = accelerometer.is_available()
        has_gyro = gyroscope.is_available()
        
        if has_accel and has_gyro:
            self.sm.current = 'main'
        else:
            self.sm.current = 'error'

if __name__ == '__main__':
    SensorCheckApp().run()