class Persona(object):
    def __init__(self, nombre,email, age):
        self.nombre = nombre
        self.__email = email
        self.__age = age

    def update_email(self, new_email):
        self.__email = new_email

    def email(self):
        return self.__email

    def __show_age(self):
        return self.__age

    def show_age(self):
        return self.__get_age

    def __get_age(self):
        return self.__age

    """sobrecarga de metodos"""

    def  update_email(self, new_email, algo_mas):
        self.__email = new_email + algo_mas

tk = Persona('TK', 'tk@mail.com ', 25)

print tk.email()

