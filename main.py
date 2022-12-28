from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


df = pd.read_csv("D://torrent games//Burhan's Immigration Database (Top 10 Countries)  - Standard Immigration Data.csv")

url = 'https://www4.formularservice.gv.at/formularserver/user/formular.aspx?pid=fe66cedb506e495c94b3e826701443e5&pn=B461f73088ab946fe9bd1d1cce573d81a&lang=en'


driver = webdriver.Chrome('D:\pythonProject2\chromedriver')
driver.implicitly_wait(10)

driver.get(url)
empty_list = []
wait = WebDriverWait(driver, 15)

#Employer form part
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_Name_input"]').send_keys((df['Employer Name'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_EMailAdresse_input"]').send_keys((df["Employer Email Address"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_GewerbebefugnisUGegenstand_input"]').send_keys((df['Occupation'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_UID_input"]').send_keys((df['Employer VAT Identification Number'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_PLZ_input"]').send_keys((df['Employer postal code'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_Ort_input"]').send_keys((df['Employer City'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_Land_input"]').send_keys((df['Employer Country'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_Adresse_input"]').send_keys((df['Employer Name'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_Name_input"]').send_keys((df['Employer Address'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block1_Block1_b1_TelNr_input"]').send_keys((df['Employer Telephone Number'][0]))


#Applicant's form part
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_Name_input"]').send_keys((df["Applicant's surname(s)"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_Vornamen_input"]').send_keys((df["Applicant's given name(s)"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_Geburtsdatum_input"]').send_keys((df["Applicant's date of birth"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_Adresse_input"]').send_keys((df["Applicant's residential address"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_Staatsbuergerschaft_input"]').send_keys((df['First Nationality'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_PLZ_input"]').send_keys((df["Applicant's residential postal code"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_Ort_input"]').send_keys((df["Applicant's residential city"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_Land_input"]').send_keys((df["Applicant's residential country"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_TelNr_input"]').send_keys((df["Applicant's telephone number (country, region or dial code)"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block2_Block2_b2_EMailAdresse_input"]').send_keys((df['Email Address'][0]))


#contact person part
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block3_Block3_b2_Name_input"]').send_keys((df['Contact Person Last Name'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block3_Block3_b2_Vornamen_input"]').send_keys((df['Contact Person First Name'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block3_Block3_b2_Adresse_input"]').send_keys((df['Contact Person Address'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block3_Block3_b2_PLZ_input"]').send_keys((df['Contact Person Postal Code'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block3_Block3_b2_Land_input"]').send_keys((df['Contact Person Country'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block3_Block3_b2_Ort_input"]').send_keys((df['Contact Person City'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block3_Block3_b2_Ort_input"]').send_keys((df['Contact Person City'][0]))

#Company part
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block4_GruppeFlieszend3_ddlAuftragperson_input_1"]').click()
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block4_b4_Name_input"]').send_keys((df['If company, insert inviting company name'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block4_b4_Adresse_input"]').send_keys((df['If company, insert inviting company address'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block4_b4_PLZ_input"]').send_keys((df['If company, insert inviting company postal code'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block4_b4_Ort_input"]').send_keys((df['If company, insert inviting company city location'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block4_b4_Land_input"]').send_keys((df['If company, insert inviting company country location'][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block4_b4_EMailAdresse_input"]').send_keys((df["If company, insert inviting company contact's email address"][0]))

#Period of secondment 
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block5_BlockZR_b6_BeginnDat_input"]').send_keys((df["Entry Permit issued from (Valid From)"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block5_BlockZR_b6_EndeDat_input"]').send_keys((df["Entry Permit issued from (Valid Until)"][0]))

#stay details
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block6_GruppeFlieszend10_GrpOrtValidation_GrpRptOrte_list__1_ort_Ort_input"]').send_keys((df["Hotel City"][0]))
driver.find_element("xpath", '//*[@id="Xml_zko_3_Steps_Seitenfolge1_Inner_Seite1_Block6_GruppeFlieszend10_GrpOrtValidation_GrpRptOrte_list__1_ort_Anschrift_input"]').send_keys((df["Hotel Street name"][0]))
