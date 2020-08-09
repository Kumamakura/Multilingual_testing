import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    # даю возможность проверяющему посмотреть, какой язык у страницы
    time.sleep(5)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), \
        'Кнопка "Добавить в корзину" отсутствует'
