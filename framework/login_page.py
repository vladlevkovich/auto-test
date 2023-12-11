from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from selenium.common import NoSuchElementException

from framework.page import Page


class LoginPage(Page):

    def login_test(self, email, password):
        try:
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]').click()
            sleep(1)
            # введення пошти
            self.find_element(
                AppiumBy.XPATH, '//android.widget.EditText[@resource-id="defaultAutomationId"][1]'
            ).send_keys(email)
            sleep(1)
            # # введення паролю
            self.find_element(
                AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'
            ).send_keys(password)
            sleep(1)
            # # перевірка успішновсті входу
            self.find_element(
                AppiumBy.XPATH,
                '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])['
                '4]/android.view.View/android.view.View/android.widget.Button').click()
            sleep(5)
            # перевірка чи вірні ввів дані користувач
            try:
                # вспливаюче поле повідомлення про невірні дані
                self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                         '@resource-id="com.ajaxsystems:id/snackbar_text"]')
                return False
            except NoSuchElementException:
                return True
        except NoSuchElementException as e:
            print(f'Error: {str(e)}')
            return False

    def sidebar_test(self):
        # перевіряємо sidebar

        try:
            # пошук sidebar
            self.find_element(
                AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
            ).click()
            sleep(3)
            # пошук пункта меню налаштування застосунку
            self.find_element(
                AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App '
                                'Settings"]')
            sleep(3)
            # пошук меню допомога
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/title" and @text="Help"]')
            sleep(3)
            # пошук пункту менню повідомити про проблему
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/title" and @text="Report a '
                                                     'Problem"]')
            sleep(3)
            # пошук пункту менню додати хаб
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/text"][2]')
            sleep(3)
            # умови використання
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/documentation_text"]')
            sleep(3)
            # номер версії застосунку
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/build"]')
            sleep(3)

            # перевірка іконок sidebar

            # іконка налаштувань
            self.find_element(AppiumBy.XPATH, '(//android.view.View[@resource-id="com.ajaxsystems:id/atomImage'
                                                     '"])[1]')
            sleep(3)
            # іконка допомоги
            self.find_element(AppiumBy.XPATH, '(//android.view.View[@resource-id="com.ajaxsystems:id/atomImage'
                                                     '"])[2]')
            sleep(3)
            # іконка повідомити про проблему
            self.find_element(AppiumBy.XPATH, '(//android.view.View[@resource-id="com.ajaxsystems:id/atomImage'
                                                     '"])[3]')
            sleep(3)
            # іконка на кнопці додати хаб
            self.find_element(AppiumBy.XPATH,
                                     '//android.view.View[@resource-id="com.ajaxsystems:id/start_icon"]')
            sleep(3)
            # кнопка додати хаб
            self.find_element(AppiumBy.XPATH, '//android.widget.Button')
            sleep(3)
            return True
        except Exception as e:
            print(f'Error sidebar: {str(e)}')
            return False
