Selenium is finicky. If you just need to scrape some data from a page, you don't have time to worry about its intricacies.
RDriver ("Reliable Driver") is a simple package that abstracts out some of the complexities of Selenium, allowing you
to focus on getting the job done.

Use is simple:
```
    from RDriver import RDriver

    driver = RDriver("/Users/comish/Projects/Scripts/chromedriver")  # <-- Instantiate RDriver, pointing it to your chromedriver executable
    driver.navigate("https://en.wikipedia.org/wiki/Manx_cat")        # <-- Give it a page to navigate to
    driver.type("manx flag", "searchInput", "id")                    # <-- Type some text into a textarea
    driver.click("searchButton", "id")                               # <-- Tell it to click something on the page
    data = driver.get_data("firstHeading", "id")                     # <-- Retrieve the raw web element to extract data from
```

Most of what this package accomplishes is takes out the need for you to put custom wait times in your code. It instead
polls the element you pass in until it becomes interactable (or fails if it never does).