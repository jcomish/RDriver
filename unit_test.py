from RDriver import RDriver
from pathlib import Path

DOWNLOAD_DIR = str(Path.cwd())

def test_click():
    driver = RDriver("/Users/comish/Projects/Scripts/chromedriver")
    driver.navigate("https://en.wikipedia.org/wiki/Manx_cat")
    driver.click("/html/body/div[3]/div[3]/div[5]/div[1]/div[3]/ul/li[1]/a")

def test_type():
    driver = RDriver("/Users/comish/Projects/Scripts/chromedriver")
    driver.navigate("https://en.wikipedia.org/wiki/Manx_cat")
    driver.type("manx flag", "searchInput", "id")

def test_get_data():
    driver = RDriver("/Users/comish/Projects/Scripts/chromedriver")
    driver.navigate("https://en.wikipedia.org/wiki/Manx_cat")
    driver.type("manx flag", "searchInput", "id")
    driver.click("searchButton", "id")
    data = driver.get_data("firstHeading", "id")
    assert data.text == "Flag of the Isle of Man"

def test_screenshot():
    driver = RDriver("/Users/comish/Projects/Scripts/chromedriver", download_dir=DOWNLOAD_DIR)
    driver.navigate("https://en.wikipedia.org/wiki/Manx_cat")
    driver.take_screenshot("ss.png")
    assert Path(DOWNLOAD_DIR, "screenshots", "ss.png").exists()

def test_download_link():
    driver = RDriver("/Users/comish/Projects/Scripts/chromedriver", download_dir=DOWNLOAD_DIR)
    driver.navigate("https://fastest.fish/test-files")
    driver.download_file_from_link("10MB", "text")
    assert Path(DOWNLOAD_DIR, "10MB.zip").exists()

def test_download_url():
    driver = RDriver("/Users/comish/Projects/Scripts/chromedriver", download_dir=DOWNLOAD_DIR)
    driver.download_file_from_url("https://s1.q4cdn.com/806093406/files/doc_downloads/test.pdf")
    assert Path(DOWNLOAD_DIR, "test.pdf").exists()