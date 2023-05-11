from demoqa_tests import resources

from selene import have
from selene.support.shared import browser


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def gender(self, text):
        browser.all('[name=gender]').element_by(have.value(text)).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'[aria-label="Choose Wednesday, {month} {day}th, {year}"]').click()

    def subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def picture(self, picture):
        browser.element('#uploadPicture').send_keys(resources.path(picture))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()


    def submit(self):
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, full_name, email, gender, mobile, date_of_birth, subject, hobby, picture, address, city):
        browser.element('.table').all('td').even.should(have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subject,
                hobby,
                picture,
                address,
                city
            ))



