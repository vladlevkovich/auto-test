import subprocess
import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '--base-path', '/wd/hub', '-a', 'localhost', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    capabilities_options = UiAutomator2Options().load_capabilities(android_get_desired_capabilities())
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=capabilities_options)    # wd/hub/session
    yield driver

# appium --base-path /wd/hub --port 4001 - запуск appium

