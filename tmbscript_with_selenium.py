from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.ie.options import Options as IEOptions
import time
from selenium.webdriver.chrome.service import Service

# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.


service = Service()

service.start()

driver = webdriver.Remote(service.service_url)

  
# get the desired web, in this case tmb.cat
driver.get('https://auth.tmb.cat/auth/realms/jotmbe/protocol/openid-connect/auth?scope=openid&state=hvnr1ZUj5IoUZNpOS9jp8uvBJAfLlZKeS7TUelnV_vk.Ptd1CZhyvFc.web_tmb&response_type=code&client_id=jotmbe_idp&redirect_uri=https%3A%2F%2Fauth.tmb.cat%2Fauth%2Frealms%2Ftmb%2Fbroker%2Fjotmbe%2Fendpoint&ui_locales=ca&kc_locale=ca&nonce=-0qKbKGUI9wL0Rq_SR1WpQ')
time.sleep(25) # Let the user actually see something!

# Obtain username and pass texfield and clear them
email = driver.find_element_by_id("loginEmail")
password = driver.find_element_by_id("loginPassword")
email.clear()
password.clear()

# Insert the login credentials
email.send_keys("tatiana.meyer.u@gmail.com")
password.send_keys("3Cerditos")

# Click Iniciar Sesión button
#iniciaSesionBtn = driver.find_element_by_id("loginSubmit").submit()

