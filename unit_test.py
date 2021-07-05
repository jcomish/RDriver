from RDriver import RDriver

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