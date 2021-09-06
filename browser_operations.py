from RPA.Browser.Selenium import Selenium


def new_repo():
    browser = Selenium()
    browser.open_available_browser("https://github.com/")
    browser.find_element('//a[@class="HeaderMenu-link flex-shrink-0 no-underline"]').click()
    browser.input_text('//*[@id="login_field"]', "daniyaltestdjango@gmail.com")
    browser.input_text('//*[@id="password"]', "Testpassword1234")
    browser.find_element('//*[@id="login"]/div[4]/form/div/input[12]').click()
    browser.wait_until_page_contains_element('//*[@id="repos-container"]/h2/a')
    browser.find_element('//*[@id="repos-container"]/h2/a').click()
    browser.input_text('//*[@id="repository_name"]', "new repository by bot")
    browser.find_element('//*[@id="new_repository"]/div[4]/button').click()
    browser.close_browser()
