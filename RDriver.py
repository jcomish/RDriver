from selenium import webdriver
import time
from pathlib import Path

class RDriver:
    def __init__(self, driver_path, attempts=100, cooldown=100, download_dir=None, download_start_time=1):
        """

        :param driver_path: Path of your chromedriver executable.
        :param attempts: Amount of times to retry a method.
        :param cooldown: Amount of time (in milliseconds) between method retries.
        """
        # Set download settings
        self.download_dir = str(Path.cwd())
        if download_dir:
            self.download_dir = download_dir
        self.download_start_time = download_start_time

        # Make sure that directory exists
        if not Path(self.download_dir).exists():
            Path(self.download_dir).mkdir()
        if not Path(self.download_dir, "screenshots").exists():
            Path(self.download_dir, "screenshots").mkdir()

        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": self.download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        })

        self.driver = webdriver.Chrome(driver_path, chrome_options=options)
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
        if by == "text":
            return self.driver.find_element_by_link_text(locator)
        if by == "partial_link_text":
            return self.driver.find_element_by_partial_link_text(locator)
        if by == "name":
            return self.driver.find_element_by_name(locator)
        if by == "tag_name":
            return self.driver.find_element_by_tag_name(locator)

    def _wait_for_download(self):
        time.sleep(self.download_start_time)  # Wait for download to start
        while True:
            files = [str(x) for x in Path(self.download_dir).glob('**/*') if x.is_file()]
            for file in files:
                if ".crdownload" in file:
                    break
            else:
                return True
            time.sleep(self.cooldown)

    def navigate(self, url):
        """
        Navigates to a URL.
        :param url: The URL.
        :return:
        """
        self.driver.get(url)

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


    @_retry
    def download_file_from_link(self, locator, by):
        """
        Downloads and waits for a download from a link.
        :param locator: Link of an element to download
        :return:
        """
        self._find_element(locator, by).click()
        self._wait_for_download()
        return True

    def download_file_from_url(self, url):
        """
        Downloads and waits for a download from a URL.
        :param url: URL to trigger the download.
        :return:
        """
        self.driver.get(url)
        self._wait_for_download()
        return True

    def take_screenshot(self, filename):
        """
        Takes a screenshot of the page
        :param filename: Name of the file to save locally
        :return:
        """
        self.driver.save_screenshot(self.download_dir + "/screenshots/" + filename)
