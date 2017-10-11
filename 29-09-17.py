class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido =  apellido
        self.email = nombre +  "." + apellido +"@copmpany.com"
        self.salario = salario

    def nombre_completo (self):
        return '{} {}'.format(self.nombre, self.apellido)

    def obtener_salario(self):
            return self.salario


empleado_1 =Empleado("hugo", "mecalco", 90000)
empleado_2 = Empleado("roberto","diaz", 80000)

#print empleado_1.email
#print str(empleado_1.obtener_salario())

print empleado_1.nombre_completo()
print Empleado.nombre_completo(empleado_1)

print empleado_2.email
print Empleado.nombre_completo(empleado_1)


