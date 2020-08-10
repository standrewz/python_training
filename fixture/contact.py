from selenium.webdriver.support.select import Select
import time
import re
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_address_book_entry(self, contact):
        wd = self.app.wd
        self.open_address_creation_page()
        # fill new address book form
        self.fill_contact_form(contact)
        # enter new contact
        wd.find_element_by_xpath("//input[21]").click()
        self.contact_cache = None

    def open_address_creation_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        # Select contact by index
        wd.find_elements_by_name("selected[]")[index].click()
        # Submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # Let alert be closed correctly
        time.sleep(1)
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(self, 0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index+2) + "]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        # Submit edit
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondaryphone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday_day)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday_month)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.return_to_home_page()
            self.contact_cache = []
            contact_rows = wd.find_elements_by_css_selector("tr[name=entry]")
            contact_size = len(contact_rows)
            for i_row in range(1, contact_size+1):
                base_xpath = "//table[@id='maintable']/tbody/tr[" + str(i_row+1) + "]/"
                contact_id = wd.find_element_by_xpath(base_xpath + "td[1]/input").get_attribute("id")
                last_name = wd.find_element_by_xpath(base_xpath + "td[2]").text
                first_name = wd.find_element_by_xpath(base_xpath + "td[3]").text
                address = wd.find_element_by_xpath(base_xpath + "td[4]").text
                all_emails = wd.find_element_by_xpath(base_xpath + "td[5]").text
                all_phones = wd.find_element_by_xpath(base_xpath + "td[6]").text
                self.contact_cache.append(Contact(id=contact_id, lastname=last_name, firstname=first_name,
                                                  address=address, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self):
        wd = self.app.wd
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobile=mobile, secondaryphone=secondaryphone, address=address, email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self):
        wd = self.app.wd
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text)
        if homephone is not None:
            homephone = homephone.group(1)
        else:
            homephone = ''
        workphone = re.search("W: (.*)", text)
        if workphone is not None:
            workphone = workphone.group(1)
        else:
            workphone = ''
        mobile = re.search("M: (.*)", text)
        if mobile is not None:
            mobile = mobile.group(1)
        else:
            mobile = ''
        secondaryphone = re.search("P: (.*)", text)
        if secondaryphone is not None:
            secondaryphone = secondaryphone.group(1)
        else:
            secondaryphone = ''
        return Contact(homephone=homephone, workphone=workphone,
                       mobile=mobile, secondaryphone=secondaryphone)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.return_to_home_page()
        # Select contact by id
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # Submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # Let alert be closed correctly
        time.sleep(1)
        self.app.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        # Submit edit
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.return_to_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def open_contact_to_view_by_id(self, id):
        wd = self.app.wd
        self.app.return_to_home_page()
        wd.find_element_by_css_selector("a[href='view.php?id=%s']" % id).click()








