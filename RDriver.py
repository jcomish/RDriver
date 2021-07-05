from selenium import webdriver
import time


class RDriver:
    def __init__(self, driver_path, attempts=100, cooldown=100):
        """

        :param driver_path: Path of your chromedriver executable.
        :param attempts: Amount of times to retry a method.
        :param cooldown: Amount of time (in milliseconds) between method retries.
        """
        self.driver = webdriver.Chrome(driver_path)
        self.attempts = attempts
        self.cooldown = cooldown / 1000

    def _retry(f):
        """
        Decorator that streamlines method retrying.
        :return:
        """
        def magic(self, *args, **kwargs):
            for _ in range(self.attempts):
                try:
                    result = f(self, *args, **kwargs)
                    if result:
                        return result
                except Exception as e:
                    raise e
                time.sleep(self.cooldown)

        return magic

    def navigate(self, url):
        """
        Navigates to a URL.
        :param url: The URL.
        :return:
        """
        self.driver.get(url)

    def _find_element(self, locator, by):
        """
        (Private) Generalized function to find an element.
        :param locator: Some sort of locator. This is an xpath by default.
        :param by: Defines the type of locator (id, class_name, tag_name, etc)
        :return:
        """
        by = by.lower()
        if by == "xpath":
            return self.driver.find_element_by_xpath(locator)
        if by == "id":
            return self.driver.find_element_by_id(locator)
        if by == "class_name":
            return self.driver.find_element_by_class_name(locator)
        if by == "css_selector":
            return self.driver.find_element_by_css_selector(locator)
        if by == "link_text":
            return self.driver.find_element_by_link_text(locator)
        if by == "partial_link_text":
            return self.driver.find_element_by_partial_link_text(locator)
        if by == "name":
            return self.driver.find_element_by_name(locator)
        if by == "tag_name":
            return self.driver.find_element_by_tag_name(locator)

    @_retry
    def click(self, locator, by="xpath"):
        """
        Clicks an element on the page.
        :param locator: Some sort of locator. This is an xpath by default.
        :param by: Defines the type of locator (id, class_name, tag_name, etc)
        :return: None
        """
        self._find_element(locator, by).click()
        return True

    @_retry
    def type(self, text, locator, by="xpath"):
        """
        Types text into an element that accepts input.
        :param text: Text to type on the page.
        :param locator: Some sort of locator. This is an xpath by default.
        :param by: Defines the type of locator (id, class_name, tag_name, etc)
        :return: None
        """
        self._find_element(locator, by).send_keys(text)
        return True

    @_retry
    def get_data(self, locator, by):
        """
        Retrieves the web element, enabling analyis or extraction of the text.
        :param locator: Some sort of locator. This is an xpath by default.
        :param by: Defines the type of locator (id, class_name, tag_name, etc)
        :return: None
        """
        return self._find_element(locator, by)
