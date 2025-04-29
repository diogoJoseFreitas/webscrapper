from time import sleep

from webscrapper import Webscrapper

driver = Webscrapper()

driver.get("https://iptu.campogrande.ms.gov.br/")

# sleep(4)
if driver.input_text('[id="inputInscricao"]', 6830270050):

    print("chegou")
else:
    print("não chegou")

driver.wait_for_object('/html/body/section[1]/div/div/div[2]/div[2]', by='xpath', loop_times=10)

driver.click_button('//*[@id="list-table-1"]/tbody/tr[2]/th/div/input', by='xpath')
driver.click_button('[id="spanCopiarCodigoBarras"]')
