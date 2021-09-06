from RPA.Browser.Selenium import Selenium


def new_repo():
    browser = Selenium()
    browser.open_available_browser("https://github.com/")
    browser.click_link('/html/body/div[1]/header/div/div[1]/div[2]/a')
    browser.wait_until_page_contains_element('/html/body/div[3]/main/div/div[4]/form/div/input[1]')
    browser.input_text('/html/body/div[3]/main/div/div[4]/form/input[2]', "daniyaltestdjango@gmail.com")
    browser.input_text('/html/body/div[3]/main/div/div[4]/form/div/input[1]', "testaccount1212")
    browser.open_available_browser("https://github.com/")
    browser.wait_until_page_contains_element('/html/body/div[4]/div/aside/div[2]/div[1]/div/h2/a')
    browser.click_link('/html/body/div[4]/div/aside/div[2]/div[1]/div/h2/a')
    browser.input_text('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input', "new repository by bot")
    browser.click_button('/html/body/div[4]/main/div/form/div[4]/button')
    return None
