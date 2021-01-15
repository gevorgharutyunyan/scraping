from bs4 import BeautifulSoup
import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


def find_nustar_obs(source):
    driver = webdriver.Chrome() # Used Google Chrome WEB browser
    driver.get("https://www.ssdc.asi.it/mmia/index.php?mission=numaster") # This page is used for scraping
    driver.maximize_window()
    element = driver.find_element_by_id('sourcein') #Firstly need to fill input tag of a web page with source name datacatalog
    element.send_keys(source)
    element.send_keys(Keys.RETURN)
    driver.switch_to.window(driver.window_handles[1])
    if driver.current_url =="https://www.ssdc.asi.it/cgi-bin/catalogs":
        try:
            driver.find_element_by_tag_name('img')
        except:
            return source
        else:
            return False
    if "https://www.ssdc.asi.it/js/index.php?missione=numaster&file=" in driver.current_url:
        return True
    driver.quit()

search_names =pd.read_csv("for_check.csv")
obs = search_names.Assoc_name.to_frame()
obs["RA,Dec"] = (search_names.RA.astype(str) + ',' + search_names.DEC.astype(str))

#print(type(obs))
source_names = ['3C6.1', '3C9', '3C15', '3C17', 'NGC315', '3C31', '0106+013', '3C33', '3C47', '4C+35.03',
                'PKS0208-512', '3C66B', '0234+285', '0313-192', '3C83.1', 'PKS0405-12', '3C109', 'PKS0413-21',
                '3C111', '3C120', '3C123', '3C129', '0454-463', 'PictorA', 'PKS0521-36', '0529+075', 'PKS0605-08',
                'PKS0637-752', '3C173.1', '3C179', 'B20738+313', 'DA240', '3C189', '0827+243', '4C+29.30', '3C207',
                'OJ287', '3C212', 'PKS0903-573', '6C0905+39', 'PKS0920-397', '3C219', '3C227', 'Q0957+561',
                '4C+13.41', 'PKS1030-357', '1045-188', 'PKS1046-409', 'PKS1055+201', '3C254', 'PKS1127-145',
                'PKS1136-135', '3C263', '3C264', '3C265', '4C+49.22', 'PKS1202-262', 'NGC4261', '1222+216', 'M84',
                '3C273', 'M87', 'PKS1229-02', '3C275.1', '3C280', '3C281', '1317+520', '4C+65.15', 'CenA',
                '1334-127', 'CenB', '4C+19.44', '3C294', '3C295', '3C296', 'PKS1421-490', '3C303', '1508+572',
                'PKS1510-08', 'AP Lib', '3C321', '3C324', '4C+00.58', '3C327', '3C330', 'NGC6251', '3C345', '3C346',
                '1642+690', '3C351', '3C353', '1745+624', '1800+440', '3C371', '3C380', '3C390.3', '1849+670',
                '1928+738', '3C403', 'CygA', 'S52007+777', '4C+74.26', 'PKS2101-49', '2123-463', 'PKS2152-69',
                '2155-152', '2201+315', 'PKS2201+044', '2209+080', '2216-038', '3C445', '3C452', '3C454.3',
                '2255-282', 'PKSJ2310-437', '3C465', '2345-167']

obs_list = list(map(find_nustar_obs,obs["RA,Dec"]))
obs["Observation"] = obs_list
obs.to_csv("nustar_obs.csv",index=False)
print(obs)
#print(obs_list)

