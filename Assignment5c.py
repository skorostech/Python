class Student:
      def __init__(self, name, age , marks , email , yob):
          self.name = name
          self.age = age
          self.marks = marks
          self.email = email
          self.yob = yob

student1 = Student('Joe' , 20 , 350 , 'joe@gmail.com' , 2007)
student2 = Student('penny' , 21 , 200 , 'penny@gmail.com' , 2007)
print('The students name is' , student1.name , 'and he is' , student1.age , 'years old')


#class laptop
class Laptop:
    def __init__(self , model , color , price):
        self.model = model
        self.color = color
        self.price = price
        
laptop1 = Laptop('hp' , 'grey', 42000)
laptop2 = Laptop('Lenovo' , 'black' , 35000)
print('This laptop is' , laptop1.model , 'and is' , laptop1.color , 'in color' , 'and is' , laptop1.price)

#class book
class Book:
    def __init__(self,book_author , title , yearofpublish):
        self.book_author = book_author
        self.title = title
        self.yearofpublish = yearofpublish
book1 = Book('John Grisham' , 'The Chamber' , 1994)
print('The author is' , book1.book_author , 'The title is' , book1.title , 'It was published in' , book1.yearofpublish )
    