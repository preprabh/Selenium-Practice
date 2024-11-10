from selenium import webdriver
from selenium.webdriver.common.by import By
from operator import itemgetter

driver = webdriver.Chrome()
driver.get("https://edwheel.com/index.php/selenium-practice/")

table_rows = driver.find_elements(By.XPATH, "//table//tr")

table_list = []
for row in table_rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_list = tuple([cell.text for cell in cells])
    if row_list:
        table_list.append(row_list)

print(f"Table Data: {table_list}")

sorted_table = sorted(table_list, key=itemgetter(4), reverse=True)
print(f"Sorted Table: {sorted_table}")
