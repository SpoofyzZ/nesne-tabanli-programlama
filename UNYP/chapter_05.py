# Person sınıfı (Temel Sınıf)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Ad: {self.name}, Yaş: {self.age}"


# Student sınıfı (Person sınıfından türetilmiş)
class Student(Person):
    def __init__(self, name, age, student_number):
        super().__init__(name, age)
        self.student_number = student_number

    def display_info(self):
        return f"{super().display_info()}, Öğrenci Numarası: {self.student_number}"


# Teacher sınıfı (Person sınıfından türetilmiş)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        return f"{super().display_info()}, Ders: {self.subject}"


# Kullanım Örneği
if __name__ == "__main__":
    # Person nesnesi oluşturma
    person = Person("Ahmet", 30)
    print(person.display_info())

    # Student nesnesi oluşturma
    student = Student("Ayşe", 20, "20234567")
    print(student.display_info())

    # Teacher nesnesi oluşturma
    teacher = Teacher("Mehmet", 40, "Matematik")
    print(teacher.display_info())
