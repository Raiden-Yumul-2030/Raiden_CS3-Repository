#9:45 PM

class Publication:
  __title = ""
  __author = ""
  def __init__(self, __title, __author):
    self.__title = title
    self.__author = author
  def get_title(self):
    print("")
  def get_author(self):
    print("")
  def set_title(self, __title):
    print("")
  def set_author(self, __author):
    print("")
  def display_info(self):
    print("")


class Book(Publication):
  __number_of_pages = 0
  def __init__(self, __title, __author, __number_of_pages):
    self.__title = title
    self.__author = author
    self.__number_of_pages = number_of_pages
  def get_number_of_pages(self):
    print("")
  def set_number_of_pages(self, __number_of_pages):
    print("")


class Magazine(Publication):
  __issue_number = 0
  def __init__(self, __title, __author, __issue_number):
    self.__title = title
    self.__author = author
    self.__issue_number = issue_number
  def get_issue_number(self):
    print("")
  def set_issue_number(self, __issue_number):
    print("")

