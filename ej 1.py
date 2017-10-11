class Empleado(object):

    monto_para_aumento =1.04
    numero_de_empleados = 0

    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.email = nombre + "." + apellido + "@company.com"
        self.salario = salario

        Empleado.numero_de_empleados += 1

    def nombre_completo(self):

        return "{} {}".format(self.nombre, self.apellido)

    def obtener_salario(self):
        return self.salario

    def aplicar_aumento(self):
        self.salario = int(self.salario * self.monto_para_aumento)


developer= Empleado (" jaime ", "gonzalez", 40000)

qa= Empleado("yaris ", "tranta", 3000)

#print qa.salario
#print developer.nombre_completo()
# print Empleado.numero_de_empleados

class Developer(Empleado):
    monto_para_aumento = 1.1
    def __init__(self, nombre, apellido, salario, prog_lang):
            super(Developer, self).__init__(nombre, apellido,salario)
            self.prog_lang=prog_lang


#empleado_1= Empleado("hugo", "Mecalco", 90000)
#empleado_2= Empleado("Test", "Empleado", 80000, "  python")

empleado_1= Empleado("hugo", "Mecalco", 90000)
dev_2 = Developer("prueba ", "Empleado", 80000, "python")


#print empleado_1.salarioc
#empleado_1.aplicar_aumento()
#print empleado_1.salario
class PM(Empleado):
    def __init__(self, nombre, apellido, salario, otro):
        super(PM, self).__init__(nombre, apellido, salario)
        self.otro = otro

PM_1= PM("marina", "vazquez", 80000, "cool")
print PM_1.nombre

print PM_1.apellido

print PM_1.nombre_completo()
 