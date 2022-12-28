from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


df = pd.read_csv("D://torrent games//Burhan's Immigration Database (Top 10 Countries)  - Standard Immigration Data.csv")

url = 'https://videx.diplo.de/videx/desktop/index.html#start'


driver = webdriver.Chrome('D:\pythonProject2\chromedriver')
driver.implicitly_wait(10)

driver.get(url)
empty_list = []
wait = WebDriverWait(driver, 15)


#personnel form part
driver.find_element("xpath", '//*[@id="videx-field-applicant-lastname-inputEl"]').send_keys((df["Applicant's surname(s)"][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-firstname-inputEl"]').send_keys((df["Applicant's given name(s)"][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-date-of-birth-inputEl"]').send_keys((df["Applicant's date of birth"][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-nationality-1-inputEl"]').send_keys((df["Nationality"][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-gender-inputEl"]').send_keys((df['Gender/Sex'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-family-status-inputEl"]').send_keys((df['Civil status'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-birthplace-inputEl"]').send_keys((df['Nationality at birth'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-native-country-inputEl"]').send_keys((df['Country of birth'][0]))

#Occupation
driver.find_element("xpath", '//*[@id="app-base-fieldset-1053-legendToggle-toolEl"]').click()
driver.find_element("xpath", '//*[@id="videx-field-applicant-profession-inputEl"]').send_keys((df['Occupation'][0]))

#address
driver.find_element("xpath", '//*[@id="app-base-fieldset-1061-legendToggle-toolEl"]').click()
driver.find_element("xpath", '//*[@id="videx-field-applicant-street-inputEl"]').send_keys((df["Applicant's residential address"].str[0:2].iloc[0:1]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-house-number-inputEl"]').send_keys((df["Applicant's residential address"].str[2:].iloc[0:1]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-zip-inputEl"]').send_keys((df["Applicant's residential postal code"][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-place-inputEl"]').send_keys((df["Applicant's residential city"][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-country-inputEl"]').send_keys((df["Applicant's residential country"][0]))

#travel documents
driver.find_element("xpath", '//*[@id="app-base-fieldset-1070-legendToggle-toolEl"]').click()
driver.find_element("xpath", '//*[@id="videx-field-applicant-travel-document-inputEl"]').send_keys((df['Type of travel document'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-passport-number-inputEl"]').send_keys((df['Travel document number (passport number)'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-issue-date-inputEl"]').send_keys((df['Travel Document Valid From'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-valid-until-inputEl"]').send_keys((df['Travel Document Valid Until'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-issuing-country-inputEl"]').send_keys((df['Issued by'][0]))

#fingerprints
driver.find_element("xpath", '//*[@id="app-base-fieldset-1075-legendToggle-toolEl"]').click()
if df['Were you fingerprints previously recorded for the purpose of applying for a Schengen visa?'][0] == 'Yes':
    driver.find_element("xpath", '//*[@id="videx-field-finger-prints-inputEl"]').click()
    driver.find_element("xpath", '//*[@id="videx-field-finger-prints-date-inputEl"]').send_keys((df['If Yes, specify when'][0]))

#purpose of visit
driver.find_element("xpath", '//*[@id="app-base-fieldset-1079-legendToggle-toolEl"]').click()
driver.find_element("xpath", '//*[@id="videx-field-applicant-main-purpose-1-inputEl"]').send_keys((df['Purpose of journey'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-country-first-arrival-inputEl"]').send_keys((df['Member State of First Entry'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-determination-states-1-inputEl"]').send_keys((df['Member State of Main Destination '][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-number-requested-entries-inputEl"]').send_keys((df['Number of entries'][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-arrival-inputEl"]').send_keys((df["Applicant's intended date of arrival of the first intended stay in the Schengen area"][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-departure-inputEl"]').send_keys((df["Applicant's intended date of departure after first intended stay in the Schengen area"][0]))
driver.find_element("xpath", '//*[@id="videx-field-applicant-period-inputEl"]').send_keys((df['Duration of Stay (in days)'][0]))

#reference
driver.find_element("xpath", '//*[@id="app-base-fieldset-1103-legendToggle-toolEl"]').click()
driver.find_element("xpath", '//*[@id="videx-field-applicant-reference-type-inputEl"]').send_keys((df['How have you been invited to destination country?'][0]))
driver.find_element("xpath", '//*[@id="videx-field-reference-company-name-inputEl"]').send_keys((df['If company, insert inviting company name'][0]))
driver.find_element("xpath", '//*[@id="videx-field-reference-org-lastname-inputEl"]').send_keys((df['If company, insert inviting company contact surname'][0]))
driver.find_element("xpath", '//*[@id="videx-field-reference-org-firstname-inputEl"]').send_keys((df['If company, insert inviting company contact first name'][0]))
driver.find_element("xpath", '//*[@id="videx-field-reference-org-street-inputEl"]').send_keys((df['If company, insert inviting company street address'][0]))
driver.find_element("xpath", '//*[@id="videx-field-reference-org-house-number-inputEl"]').send_keys((df['If company, insert inviting company address'][0]))
driver.find_element("xpath", '//*[@id="videx-field-reference-org-house-number-inputEl"]').send_keys((df['If company, insert inviting company postal code'][0]))
driver.find_element("xpath", '//*[@id="videx-field-reference-org-place-inputEl"]').send_keys((df['If company, insert inviting company city'][0]))
driver.find_element("xpath", '//*[@id="videx-field-referenz-org-country-inputEl"]').send_keys((df['If company, insert inviting company country'][0]))
