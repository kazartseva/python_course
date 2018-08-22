from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.go_to_homepage()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.go_to_homepage()

    def go_to_homepage(self):
        wd = self.app.wd
        print(wd.current_url)
        if not (wd.current_url == "http://localhost/addressbook/index.php" and len(wd.find_elements_by_xpath("//div[@id='search-az']/form/input")) > 0):
            wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        self.select_value("bday", contact.bday)
        self.select_value("bmonth", contact.bmonth)
        self.select_value("aday", contact.aday)
        self.select_value("amonth", contact.amonth)

    def select_value(self, dropdown, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(dropdown)).select_by_value(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_homepage()
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.go_to_homepage()
        self.select_first_contact()
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.go_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.go_to_homepage()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            contact_id = element.find_element_by_name("selected[]").get_attribute("value")
            contact_lastname = element.find_element_by_css_selector("td:nth-child(2)").text
            contact_name = element.find_element_by_css_selector("td:nth-child(3)").text
            contacts.append(Contact(id=contact_id, firstname=contact_name, lastname=contact_lastname))
        return contacts





