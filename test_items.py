from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button(browser):
    browser.get(link)
    browser.maximize_window()
    assert len(browser.find_elements(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div['
                                                   '2]/form/button')) > 0, "There is no button"
