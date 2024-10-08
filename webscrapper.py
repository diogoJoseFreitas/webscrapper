from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class webscrapper(webdriver.Chrome):
    def __init__(
        self, options: Options = None, service: Service = None, keep_alive: bool = True
    ) -> None:
        super().__init__(options, service, keep_alive)

    def get_element(
        self, element_data: str, wait: float = 5, by: str = By.CSS_SELECTOR
    ):
        sleep(0.3)
        try:
            obj = WebDriverWait(self, wait).until(
                EC.visibility_of_element_located((by, element_data))
            )
        except:
            return None
        return obj

    def click_button(
        self, element_bata: str, wait: float = 5, by: str = By.CSS_SELECTOR
    ):
        button = self.get_element(element_bata, wait, by)
        if not button:
            return False
        else:
            button.click()
            return True

    def input_text(self, element_data: str, value: str = "", by: str = By.CSS_SELECTOR):
        obj = self.get_element(element_data, by=by)
        if not obj:
            return False
        else:
            if type(value) is type(""):
                lines = value.split("\n")
                if len(lines) > 1:
                    for line in lines:
                        obj.send_keys(line)
                        obj.send_keys(Keys.SHIFT + Keys.ENTER)
                    return True
            else:
                obj.send_keys(value)
                return True
