from selenium import webdriver


class Web(webdriver.Firefox):
    def click_button_link_text(self, button_name):
        while True:
            try:
                button = self.find_element_by_link_text(button_name)
            except:
                pass
            else:
                break
        button.click()

    def click_button_id(self, button_id):
        while True:
            try:
                button = self.find_element_by_id(button_id)
            except:
                pass
            else:
                break
        button.click()

    def switch_frame(self, index):
        while True:
            try:
                self.switch_to.frame(index)
            except:
                pass
            else:
                break

    def sign_in(self, user_name, user_pass):
        email_blank = self.find_element_by_name('loginfmt')
        email_blank.send_keys(user_name)
        button = self.find_element_by_id('idSIButton9')
        button.click()
        while True:
            try:
                pass_blank = self.find_element_by_id('passwordInput')
            except:
                pass
            else:
                break
        pass_blank.send_keys(user_pass)
        pass_blank.submit()
