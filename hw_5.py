from selene import browser, have
import os


def test_complete_the_form():
    browser.open('/automation-practice-form')

    # Ввод имени и фамилии
    browser.element('#firstName').type('An')
    browser.element('#lastName').type('Melekhova')

    # Ввод почты
    browser.element('#userEmail').type('test@gmail.com')

    # Выбор пола
    browser.element('#gender-radio-2').double_click()

    # Ввод номера
    browser.element('#userNumber').type('89000500500')

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').press()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="3"').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1997"]').click()
    browser.element('div [aria-label="Choose Wednesday, April 9th, 1997"]').click()

    # Ввод Subject
    browser.element('#subjectsInput').type('Hindi').press_enter()

    # Выбор хобби
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()

    # Загрузка файла
    browser.element('#uploadPicture').send_keys(os.getcwd()+'/IMAGE.jpg')

    # Заполнение адреса
    browser.element('#currentAddress').type('Moscow, b1')
    browser.element('#react-select-3-input').type('Uttar').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    # Клик Submit
    browser.element('#submit').press_enter()

    # Проверка - форма отправлена
    browser.element('[class="modal-title h4"]').should(have.exact_text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts('Student Name An Melekhova', 'Student Email test@gmail.com',
    'Gender Female', 'Mobile 8900050050', 'Date of Birth 09 April,1997', 'Subjects Hindi', 'Hobbies Sports, Music',
    'Picture IMAGE.jpg', 'Address Moscow, b1', 'State and City Uttar Pradesh Agra'))
