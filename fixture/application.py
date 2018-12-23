from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, baseurl):
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome()
        elif browser == "Ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.baseurl = baseurl
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

