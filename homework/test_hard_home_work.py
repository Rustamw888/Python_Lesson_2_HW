from selene import be, by, have
from selene.support.shared import browser
from homework.config import first_fixture_part2

firstName = "Rustam"
lastName = "Tyapaev"
email = "test@gmail.com"
gender = "Other"
mobileNumber = "1234567890"
birthDay = "19"
birthMonth = "11"
birthMonthStr = "December"
birthYear = "1988"
subjects = ["Computer Science", "English"]
hobbies = "Music"
currentAddress = "ulica Pushkina dom Kolotushkina"
state = "NCR"
city = "Delhi"


def test_practice_form(first_fixture_part2):
    # form fields filling
    browser.execute_script("document.querySelector(\"footer\").hidden = 'true';" +
                           "document.querySelector(\"#fixedban\").hidden = 'true'")
    browser.element('#firstName').should(be.blank).type(firstName)
    browser.element('#lastName').should(be.blank).type(lastName)
    browser.element('#userEmail').should(be.blank).type(email)
    browser.element(by.text(gender)).click()
    browser.element('#userNumber').should(be.blank).type(mobileNumber)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="' + birthYear + '"]').click()
    browser.element('.react-datepicker__month-select [value="' + "11" + '"]').click()
    browser.element('.react-datepicker__month .react-datepicker__week .react-datepicker__day--0' + birthDay + '').click()
    for value in subjects:
        browser.element('#subjectsInput').click()
        browser.element('#subjectsInput').type(value).press_enter()
    browser.element(by.text(hobbies)).click()
    browser.element('#uploadPicture')
    browser.element('#currentAddress').should(be.blank).type(currentAddress)
    browser.element('#state input').type(state).press_tab()
    browser.element('#city input').type(city).press_tab()
    browser.element("#submit").click()

    # Assertions
    browser.elements("table tr").element(1).should(have.text(firstName))
    browser.elements("table tr").element(1).should(have.text(lastName))
    browser.elements("table tr").element(2).should(have.text(email))
    browser.elements("table tr").element(3).should(have.text(gender))
    browser.elements("table tr").element(4).should(have.text(mobileNumber))
    browser.elements("table tr").element(5).should(have.text(birthYear))
    browser.elements("table tr").element(5).should(have.text(birthMonthStr))
    browser.elements("table tr").element(5).should(have.text(birthDay))
    browser.elements("table tr").element(6).should(have.text(subjects[0]))
    browser.elements("table tr").element(6).should(have.text(subjects[1]))
    browser.elements("table tr").element(7).should(have.text(hobbies))
    browser.elements("table tr").element(8).should(have.text(""))
    browser.elements("table tr").element(9).should(have.text(currentAddress))
    browser.elements("table tr").element(10).should(have.text(state))
    browser.elements("table tr").element(10).should(have.text(city))
    browser.element("#closeLargeModal").click()
