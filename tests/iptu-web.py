from time import sleep

from webscrapper import webscrapper

driver = webscrapper()

driver.get("https://iptu.campogrande.ms.gov.br/")

# sleep(4)
if driver.input_text('[id="inputInscricao"]', 6830270050):
    
    print("chegou")
else:
    print("não chegou")

driver.click_button('[type="submit"]')

# sleep(20)
