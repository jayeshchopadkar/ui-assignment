# Instructions for Executing the Tests:
## Prerequisites:

- Install Python on your system.
- Install the Selenium WebDriver library using pip install selenium.
- Download the appropriate WebDriver (e.g., ChromeDriver) and add it to your system's PATH.

## Execution:

- Save the provided Selenium script in a file, e.g., amazon_automation.py.
- Open a terminal/command prompt.
- Navigate to the directory containing the script and the input.txt file.
- Run the script using the command python ui.py

## Details of Tools and Frameworks Used:
- Python: The scripting language used for writing the automation script.
- Selenium WebDriver: A popular tool for automating web browser interactions, used to control and automate web pages.
- ChromeDriver: The WebDriver for Google Chrome, used to automate actions in the Chrome browser.
- WebDriverWait: Part of the Selenium library, used to wait for certain conditions to be met before proceeding with the script.

## Assumptions Made while Developing Test Cases:
- Stability of Amazon Website: The script assumes that the structure and behavior of the Amazon website remain relatively stable
- Layout and Elements: The script assumes specific HTML element IDs, classes, and structures for identifying elements such as search bars, buttons, links, and product details.
- Dropdown Selection: The script uses simple examples for selecting dropdown options.
- Rating Elements: The product rating information is available and represented consistently in the specified format (e.g., "5 out of 5 stars")