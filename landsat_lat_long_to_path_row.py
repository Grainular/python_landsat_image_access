# Selenium script to enter coordinates here: 
# https://landsat.usgs.gov/landsat_acq 
# and get the date that landsat 8 and 9 will be passing over

from selenium import webdriver
from datetime import datetime
import time

# Get soonest dates in string DD/MM/YYYY format
# Strings come in format DD/MM/YYYY
def get_soonest_date(dates):
    # # Convert date strings to datetime objects
    # date_objects = [datetime.strptime(date, "%d/%m/%Y") for date in dates]
    
    # # Find the minimum date
    # soonest_date = min(date_objects)
    
    # # Convert the soonest date back to string
    # return soonest_date.strftime("%d/%m/%Y")
    return dates[0]



def get_next_pass(lat = 45.0, long = -63.0):

    # Open the browser and go to the landsat page
    browser = webdriver.Chrome()
    browser.get('https://landsat.usgs.gov/landsat_acq#convertPathRow')

    # Select coordinates option by xpath id="llTOpr"
    coordinates = browser.find_element("xpath",'//*[@id="llTOpr"]')
    coordinates.click()

    latitude_input = browser.find_element("xpath",'//*[@id="thelat"]')
    latitude_input.send_keys(str(lat))

    longitude_input = browser.find_element("xpath",'//*[@id="thelong"]')
    longitude_input.send_keys(str(long))

    # Click on button with id "convert"
    convert_button = browser.find_element("xpath",'//*[@id="convert"]')
    convert_button.click()

    # # Get data from table with id="convertTableRows" about next pass of landsat 8 and 9
    # next_pass = browser.find_element("xpath",'//*[@id="convertTableRows"]')

    # Get rows of table by xpath "tr"
    # rows = next_pass.find_elements("xpath",'./tr')

    landsat_8_next_passes = []
    landsat_9_next_passes = []

    # # Scroll to the bottom of the page
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # time
    # # Get values from each column
    # for row in rows:
    #     columns = row.find_elements("xpath",'./td')
    #     landsat_8_next_passes.append(columns[4].text)
    #     print(columns[4].text)
    #     print(columns[5].text)
    #     landsat_9_next_passes.append(columns[5].text)

    time.sleep(10)
    landsat_path = browser.find_element("xpath",'//*[@id="convertTableRows"]/tr[1]/td[1]').text
    landsat_row = browser.find_element("xpath",'//*[@id="convertTableRows"]/tr[1]/td[2]').text
    landsat_8_next_passes.append(browser.find_element("xpath",'//*[@id="convertTableRows"]/tr[1]/td[5]').text)
    landsat_9_next_passes.append(browser.find_element("xpath",'//*[@id="convertTableRows"]/tr[1]/td[6]').text)

    # # Get the soonest dates

    soonest_landsat_8 = get_soonest_date(landsat_8_next_passes)
    soonest_landsat_9 = get_soonest_date(landsat_9_next_passes)

    return landsat_path, landsat_row, soonest_landsat_8, soonest_landsat_9

if __name__ == "__main__":
    print(get_next_pass())
    # Output: ('14/10/2021', '14/10/2021')


        