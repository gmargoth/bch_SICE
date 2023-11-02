from selenium import webdriver
from selenium.webdriver.common.by import By

def login_SICE(username, password, save_to):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("prefs", {"download.default_directory": save_to})
    driver = webdriver.Chrome(options=options)
    driver.get("https://sisee.bch.hn/SICE/Login.aspx")

    username_field = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$UserName')
    password_field = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$Password')
    submit_button  = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$LoginButton')

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    return driver

from selenium.webdriver.support.ui import Select
def downaload_SICE_query(driver, serie, year, month, country):
    driver.get('https://sisee.bch.hn/SICE/ConsultaSACAjustado.aspx')
    

    series_dict = dict(Importaciones = 0, Exportaciones = 1, BalanzaCambiaria = 2)
    select_element = driver.find_element(By.ID,'ContentPlaceHolder1_DDLComercio')
    select = Select(select_element)
    select.select_by_value(str(series_dict[serie]))

    if year:
        ChkAnual = driver.find_element(By.ID,'ContentPlaceHolder1_ChkAnual')
        ChkAnual.click()

    if month:
        ChkMes = driver.find_element(By.ID,'ContentPlaceHolder1_ChkMes')
        ChkMes.click()

    if country:
        ChkPais = driver.find_element(By.ID,'ContentPlaceHolder1_ChkPais')
        ChkPais.click()

    download_button = driver.find_element(By.ID,'ContentPlaceHolder1_BtnDescargar')
    download_button.click()
