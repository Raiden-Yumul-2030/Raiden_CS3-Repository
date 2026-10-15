#9:45 PM

class Publication:
  def __init__(self, title, author):
    self.__title = title
    self.__author = author
  def get_title(self):
    return self.__title
  def get_author(self):
    return self.__author
  def set_title(self, title):
    self.__title = title
  def set_author(self, author):
    self.__author = author
  def display_info(self):
    print("Title: ", self.__title, "\nAuthor: ", self.__author)


class Book(Publication):
  def __init__(self, title, author, number_of_pages):
    super().__init__(title, author)
    if number_of_pages > 0:
      self.__number_of_pages = number_of_pages
    else:
      print("Number of pages must be positive")
      self.__number_of_pages = 1
  def get_number_of_pages(self):
    return self.__number_of_pages
  def set_number_of_pages(self, number_of_pages):
    if number_of_pages > 0:
      self.__number_of_pages = number_of_pages
    else:
      print("Number of pages must be positive")


class Magazine(Publication):
  def __init__(self, title, author, issue_number):
    super().__init__(title, author)
    if issue_number > 0:
      self.__issue_number = issue_number
    else:
      print("Issue number must be positive")
      self.__issue_number = 1
  def get_issue_number(self):
    return self.__issue_number
  def set_issue_number(self, issue_number):
    if issue_number > 0:
      self.__issue_number = issue_number
    else:
      print("Issue number must be positive")

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print("Number of pages: ",book1.get_number_of_pages())

pub2 = Publication("Generic Publication", "Computer")
book2 = Book("Generic Book", "Computer", 100)
mag2 = Magazine("Generic Magazine", "Computer", 100)

print("\nMagazine Information:")
mag1.display_info()
mag1.set_issue_number(-202)
print("Issue number: ", mag1.get_issue_number())

print("\n\nPublication Information:")
pub2.display_info()

print("\nBook Information:")
book2.set_number_of_pages(50)
book2.display_info()
print("Number of pages: ",book2.get_number_of_pages())

print("\nMagazine Information:")
mag2.set_issue_number(101)
mag2.display_info()
print("Issue number: ", mag2.get_issue_number())
