from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Instantiate a WebDriver (in this case, using Chrome)
driver = webdriver.Chrome()

# Open Google's homepage
driver.get("https://www.google.com")

# Find the search bar element by its name attribute
search_bar = driver.find_element_by_name("q")

# Enter the search query
search_bar.send_keys("OpenAI")

# Submit the search query
search_bar.send_keys(Keys.RETURN)

# Wait for a few seconds to see the search results
driver.implicitly_wait(5)

# Close the browser
driver.quit()
