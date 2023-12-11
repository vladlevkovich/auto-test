import pytest
import subprocess
from framework.login_page import LoginPage
from tests.conftest import driver


# @pytest.fixture(scope='function', autouse=True)
# def clear_data():
#     subprocess.call(['adb', 'shell', 'pm', 'clear', 'com.ajaxsystems'])
#     yield


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)


