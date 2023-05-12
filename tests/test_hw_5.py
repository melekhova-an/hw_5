
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_complete_the_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('An')
    registration_page.fill_last_name('Melekhova')
    registration_page.fill_email('test@gmail.com')
    registration_page.gender('Female')
    registration_page.fill_number('8900050050')
    registration_page.fill_date_of_birth('1997', 'April', '9')
    registration_page.subject('Arts')
    registration_page.hobby('Reading')
    registration_page.picture('IMAGE.jpg')
    registration_page.fill_address('Moscow, b1')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Agra')
    registration_page.submit()

    registration_page.should_registered_user_with(
        'An Melekhova',
        'test@gmail.com',
        'Female',
        '8900050050',
        '09 April,1997',
        'Arts',
        'Reading',
        'IMAGE.jpg',
        'Moscow, b1',
        'Uttar Pradesh Agra'
        )

