from selenium import webdriver
from fixture.session import SessionHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper
from fixture.project import ProjectHelper

class Application:

    def __init__(self, browser, config):
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome()
        elif browser == "Ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.config = config
        self.soap = SoapHelper(self)
        self.baseurl = config['web']['baseurl']
        self.signup = SignupHelper(self)
        self.project = ProjectHelper(self)
        self.mail = MailHelper(self)
        self.james = JamesHelper(self)
        self.open_home_page()

    # def is_valid(self):
    #     try:
    #         self.wd.current_url
    #         return True
    #     except:
    #         return False

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/mantisbt-1.2.20/"):
            wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()

