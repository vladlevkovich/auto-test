from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from selenium.common import NoSuchElementException

from framework.page import Page


class LoginPage(Page):

    def login_test(self, email, password):
        try:
            self.click_element(
                AppiumBy.XPATH, '(//androidx.compose.ui.platform.ComposeView['
                                '@resource-id="com.ajaxsystems:id/compose_view"])['
                                '1]/android.view.View/android.view.View/android.widget.Button'
            )
            sleep(5)
            # введення пошти
            self.find_element(
                AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'
            ).send_keys(email)
            sleep(5)
            # # введення паролю
            self.find_element(
                AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'
            ).send_keys(password)
            sleep(5)
            # # перевірка успішновсті входу
            self.click_element(
                AppiumBy.XPATH, '(//androidx.compose.ui.platform.ComposeView['
                                '@resource-id="com.ajaxsystems:id/compose_view"])['
                                '4]/android.view.View/android.view.View/android.widget.Button')   #.click()
            sleep(2)
            print('TRUE')
            try:
                print('TRY')
                error_message = self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                                          '@resource-id="com.ajaxsystems:id/snackbar_text"]').text
                if error_message:
                    print(f'Error message: {error_message}')
                    return False
            except:
                print('except')
                return True
        except NoSuchElementException as e:
            print(f'Error: {str(e)}')
            return False

    def sidebar_test(self):
        # перевіряємо sidebar

        try:
            # пошук sidebar
            self.click_element(
                AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
            )   #.click()
            sleep(2)
            # пошук пункта меню налаштування застосунку
            self.find_element(
                AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App '
                                'Settings"]')
            sleep(2)
            # пошук меню допомога
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/title" and @text="Help"]')
            sleep(2)
            # пошук пункту менню повідомити про проблему
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/title" and @text="Report a '
                                                     'Problem"]')
            sleep(2)
            # пошук пункту менню додати хаб
            self.find_element(AppiumBy.XPATH, '(//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/text"])[2]')
            sleep(2)
            # умови використання
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/documentation_text"]')
            sleep(2)
            # номер версії застосунку
            self.find_element(AppiumBy.XPATH, '//android.widget.TextView['
                                                     '@resource-id="com.ajaxsystems:id/build"]')
            sleep(2)

            # перевірка іконок sidebar

            # іконка налаштувань
            self.find_element(AppiumBy.XPATH, '(//android.view.View[@resource-id="com.ajaxsystems:id/atomImage'
                                                     '"])[1]')
            sleep(2)
            # іконка допомоги
            self.find_element(AppiumBy.XPATH, '(//android.view.View[@resource-id="com.ajaxsystems:id/atomImage'
                                                     '"])[2]')
            sleep(2)
            # іконка повідомити про проблему
            self.find_element(AppiumBy.XPATH, '(//android.view.View[@resource-id="com.ajaxsystems:id/atomImage'
                                                     '"])[3]')
            sleep(2)
            # іконка на кнопці додати хаб
            self.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="com.ajaxsystems:id/start_icon"]')
            sleep(2)
            # кнопка додати хаб
            self.find_element(AppiumBy.XPATH, '//android.widget.Button')
            sleep(2)
            return True
        except Exception:
            return False
