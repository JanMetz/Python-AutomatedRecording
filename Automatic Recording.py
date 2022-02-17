import os
import time
import pyautogui as pg


class Recorder:
    _path = 'E:\\Jan\\Pozostałe\\Nie studia\\Automatyczne Nagrywanie\\'
    _app_name = 'obs64.exe'
    _app_dir_path = 'C:\\Program Files\\obs-studio\\bin\\64bit'

    def find_and_click(self, obj_name, con):
        width, height = pg.size()
        pg.moveTo(width / 2, height)

        time.sleep(0.7)
        x, y, item_width, item_height = pg.locateOnScreen(self._path + obj_name, confidence=con)
        pg.moveTo(x, y)
        pg.click()

    def quit_app(self, obj_name, con):
        x, y, item_width, item_height = pg.locateOnScreen(self._path + obj_name, confidence=con)
        pg.moveTo(x + item_width, y)
        pg.click()

    def launch_app(self):
        os.chdir(self._app_dir_path)
        os.startfile(self._app_dir_path + '\\' + self._app_name)
        time.sleep(3)

    def set_path(self, path):
        self._path = path

    def set_app_path(self, dir_path, name):
        self._app_dir_path = dir_path
        self._app_name = name

    def __init__(self, path=None, dir_path=None, name=None):
        if path is not None and dir_path is not None and name is not None:
            self._path = path
            self._app_dir_path = dir_path
            self._app_name = name


def main():
    obj = Recorder()
    obj.launch_app()  # Launch OBS
    obj.find_and_click('start_record_obs.PNG', 0.9)  # Start Recording

    # Switch to another tab - from just opened OBS to the tab with what you want to record
    pg.keyDown('alt')
    pg.press(['tab', 'tab', 'tab'])
    pg.keyUp('alt')

    pg.scroll(-500)  # Do a simple task that will be recorded

    obj.find_and_click('logo_obs.PNG', 0.7)  # Switch back to OBS
    obj.find_and_click('stop_record_obs.PNG', 0.9)  # End Recording
    obj.quit_app('taskbar_obs.PNG', 0.9)  # Quits OBS


if __name__ == '__main__':
    main()
