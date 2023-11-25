from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class DragAndDropExample:
    def __init__(self):
        self.url = "https://jqueryui.com/droppable/"
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        sleep(4)

    def perform_drag_and_drop(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(0)  # Switch to the frame where the draggable and droppable elements are present

        draggable_element = self.driver.find_element(by=By.ID, value="draggable")
        droppable_element = self.driver.find_element(by=By.ID, value="droppable")

        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable_element, droppable_element).perform()

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    try:
        drag_and_drop_example = DragAndDropExample()
        drag_and_drop_example.perform_drag_and_drop()
        sleep(6)
    finally:
        drag_and_drop_example.close_browser()