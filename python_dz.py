def func_name(a, *args):
    full_name = a.__name__.title().replace('_', ' ')
    print(full_name, *args)


def open_browser(browser_name):
    func_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    func_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func_name(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://dzen.ru/?yredirect=true")
find_registration_button_on_login_page(page_url="https://dzen.ru/?yredirect=true", button_text="click")
