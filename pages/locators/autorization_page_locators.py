from selenium.webdriver.common.by import By

picture_authorization = (
    By.XPATH, '(//*[@id="header-user-actions-container"]//div[@role="presentation" and @aria-haspopup="true"])[1]')
log_in_in_window = (By.XPATH, "//span[@class='_ZDS_REF_SCOPE_ smZi2j']")
new_client_in_window = (By.XPATH, "//span[@class='_ZDS_REF_SCOPE_ smZi2j']")
text_welcome = (By.XPATH, "//div[@class='Wn-EjT']")
e_mail_address_second = (By.XPATH, "//input[@id='login.email']")
password_second = (By.XPATH, "//input[@id='login.secret']")
log_in = (By.XPATH, "//button[@data-testid='login_button']")
log_out_button = (By.XPATH, "//a[@class='_ZDS_REF_SCOPE_ dEnX-X l9TUOd CKDt_l LyRfpJ JT3_zV _5Yd-hZ']")
forgot_password = (By.XPATH, "//span[@class='KxHAYs _2kjxJ6 dgII7d sxs3x9']")
register = (By.XPATH, "//button[@data-testid='toggle_register_button']")
text_first_time_here = (By.XPATH, "(//h3[@class='KxHAYs gr9aYh FxZV-M _4F506m'])[2]")
text_privacy_policy = (By.XPATH, "//li[@data-testid='footer_privacy_policy']")
text_reglament = (By.XPATH, "//li[@data-testid='terms_of_use']")
text_company_data = (By.XPATH, "//li[@data-testid='footer_legal_notice']")
name = (By.XPATH, "//input[@name='register.first_name']")
surname = (By.XPATH, "//input[@name='register.last_name']")
e_mail_address_first = (By.XPATH, "//input[@name='register.email']")
password_first = (By.XPATH, "//input[@name='register.secret']")
cookies_accept_button = (By.XPATH, '//*[@id="uc-btn-accept-banner"]')
