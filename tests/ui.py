from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(filename='automation_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting the automation script")

try:
    # Launch the browser
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # Open Google
    driver.get("http://www.google.com")

    # Enter the keyword "amazon" in the search bar
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("amazon")
    search_box.send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 10)
    search_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.g')))

    # Click on the link which takes you to the Amazon home page
    amazon_link = driver.find_element(By.PARTIAL_LINK_TEXT, "https://www.amazon.in")
    amazon_link.click()

    # Click on the button to search & select Electronics
    all_button = driver.find_element(By.ID, 'searchDropdownBox')
    dropdown = Select(all_button)
    dropdown.select_by_visible_text('Electronics')

    # Search for Dell computers
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys("dell computers")
    search_bar.send_keys(Keys.RETURN)

    # Apply the filter of range Rs 30000 to 50000
    low_price_filter = driver.find_element(By.ID, "low-price")
    low_price_filter.send_keys("30000")

    high_price_filter = driver.find_element(By.ID, "high-price")
    high_price_filter.send_keys("50000")

    go_button = driver.find_element(By.ID, "a-autoid-1")
    go_button.click()

    # Validate products in the specified price range
    wait = WebDriverWait(driver, 10)
    products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.s-result-item')))
    for product in products:
        price_element = product.find_element(By.CLASS_NAME, '.a-price')
        price = int(price_element.text.replace('₹', '').replace(',', ''))
        if 30000 <= price <= 50000:
            print(f"Product: {product.text}")

    five_star_xpath = "//*[@id='p_72/1318476031']"
    five_star_element = wait.until(EC.presence_of_element_located((By.XPATH, five_star_xpath)))

    # Validate products with a rating of 5 out of 5 on the first 2 pages
    for page_num in range(2):
        products = driver.find_elements(By.CSS_SELECTOR, ".s-result-item")
        for product in products:
            try:
                rating_element = product.find_element(By.CSS_SELECTOR, ".a-icon-star-small span")
                rating = float(rating_element.text)
                if rating == 5.0:
                    print(f"Product with rating 5: {product.text}")
            except:
                pass
        next_button = driver.find_element(By.CSS_SELECTOR, ".a-pagination .a-last")
        next_button.click()

    # Add the first 5-star product to the wish list
    first_5_star_product = driver.find_element(By.CSS_SELECTOR,
                                               ".a-icon-star-small span[aria-label='5.0 out of 5 stars']")
    product = first_5_star_product.find_element(By.XPATH, "./ancestor::div[@data-asin]")
    wishlist_button = product.find_element(By.CSS_SELECTOR, ".a-button.a-spacing-top-mini")
    wishlist_button.click()

    # Validate the product is added to the wish list
    wishlist = driver.find_element(By.ID, "nav-link-wishlist")
    wishlist.click()

    print("Product added to wishlist successfully!")

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

logging.info("Script execution completed")
