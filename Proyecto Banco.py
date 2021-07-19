
"""
Created on Tue Jun 15 16:38:14 2021

@author: Agus y Sil
"""
class Menu:
    def __init__(self):
        pass
          
    def menu(self):
        print()
        print("********************************")
        print("        Sistema Bancario")
        print("********************************")
        print()
        
        op = 0
        
        while op != 4:
            print("1. Acceder como Banco")
            print("2. Acceder como Cliente")
            print("3. Acceder como Empleado")
            print("4. Salir")
            op = int(input("Seleccione una opción: "))
        
            if op == 1:
                menuBanco().opcionesBanco()
            elif op == 2:
                Clientes()
            elif op == 3:
                Empleados()
            elif op == 4:
                print("\nMuchas Gracias!!!!!!")
            else:
                print("Opción incorrecta, ingrese la opción correcta")
                op = int(input("Seleccione una opción del menú: "))   

class menuBanco:
    def __init__(self):
        pass
    
    def opcionesBanco(self):
        print("\n***********¿Qué desea hacer?***********\n")
        
        op = 0
        
        while op != 4:
            print("1. Sector Clientes")
            print("2. Sector Empleados")
            print("3. Consultar Total Depositado")
            print("4. Volver al Menú Principal")
            op = int(input("Seleccione una opción: "))
                     
            if op == 1:
                Banco().Clientes.cargarDatos()
                #Banco().Clientes().cargarDatos()
            elif op == 2:
                Banco().Empleados().cargarDatos()
            elif op == 3:
                Banco.totalDepositado()
            elif op == 4:
                Menu().menu()
            else:
               print("Opción incorrecta, ingrese la opción correcta")
               op = int(input("Seleccione una opción del menú: "))
        

#Banco tiene una relación de Agregación con Clientes y Empleados        
class Banco:
    
    #Creamos el constructor de la clase Banco
    def __init__(self):
        self.clientes = Clientes()
        self.empleados = Empleados()
        totalDepositado = 0

#clase Padre que será heredada por Clientes y Empleados
class Persona:
    
    def __init__(self):
        self.dni = 0
        self.nombre = ""
        self.telefono = 0
        self.email = ""
        self.datosClientes = {Clientes()}
        #self.datosEmpleados = {} 
    
    def cargarDatos(self):
        self.dni = int(input("Ingrese el DNI de la persona: "))
        self.nombre = input("Ingrese el nombre de la persona ")
        self.telefono = int(input("Ingrese el teléfono de la persona: "))
        self.email = input("Ingrese el email de la persona: ")
      
    """def modificarDatos(self):
        dni = input("Ingrese el DNI de la persona que quiere modificar")
        for c in :
            self.nombre
       """ 
        
        
#clase Empleados hereda de clase Persona  
class Empleados(Persona): 
    def __init__(self):
        super().__init__()
        self.datosEmpleados(self)
        pass
    
    def cargarDatos(self):
        super().cargarDatos() 
        self.datosEmpleados.append(self.dni, self.nombre, self.telfono, self.email)

    
        
#clase Clientes hereda de clase Persona
class Clientes(Persona):
    
    #Contructor de la clase Clientes
    def __init__(self):
        super().__init__()
        self.CajaAhorro = CajaAhorro(self.nombre, 0)
        self.PlazoFijo = PlazoFijo(self.nombre, 0,0,0.0)
        #se actualiza la lista
        super().datosClientes.append(self)
        
    def cargarDatos(self):
        super().cargarDatos()
        super().datosClientes.append(self.dni, self.nombre, self.telfono, self.email)

        
    #Método depositar
    def depositar(self):
        monto = int(input("Ingrese el monto a depositar $ "))
        #acumula los montos depositados por el cliente
        self.cantidad += monto
        #se actualiza el diccionario
        self.datosClientes[self.dni] = [self.nombre, self.cantidad]
    
    #Método extraer, controlamos que la extracción sea menor al saldo de la cuenta
    def extraer(self):
        importe = int(input("Ingrese el importe a extraer $"))
        #el monto a extraer debe ser menor al saldo xq no puede quedar la cuenta en $0
        while importe >= self.cantidad:
            print("Debe ingresar un monto menor a $",self.cantidad)
            importe = int(input("Ingrese el nuevo importe a extraer $"))
        #ingresado el monto correcto, se descuenta del saldo de la cuenta del cliente
        self.cantidad -= importe
        print("****Retire su dinero****")
        #se actualiza el diccionario
        self.datosClientes[self.dni] = [self.nombre, self.cantidad]
        
    #Método mostrar Total
    def imprimirTotal(self):
        total = self.cantidad
        print("Su saldo actual es de $", total)
        
#clase Padre, que será heredada de Caja de Ahorro y Plazo Fijo   
class Cuentas:
    
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    def imprimir(self):
        print("Titular de la Cuenta ", self.titular)
        print("Saldo de la Cuenta ", self.cantidad)
        
#clase hija de Cuentas
class CajaAhorro(Cuentas):
    
    #constructor de la clase, hereda el constructor de Cuentas
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    
    #Método para impirmir los datos de la Caja de Ahorro
    def imprimir(self):
        print("***Caja de Ahorro***")
        super().imprimir()

#clase hija de Cuentas        
class PlazoFijo(Cuentas):
    #constructor de la clase, hereda el constructor de Cuentas
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
        
    def importeInteres(self):
        interesTotal = self.cantidad * self.interes/100
        return interesTotal
    
    #Método para impirmir los datos del Plazo Fijo
    def imprimir(self):
        print("***Plazo Fijo***")
        super().imprimir()
        print("El plazo fijo es a ", self.plazo, "días, con tasa de interés de ", self.interes, "%")
        print("El interés total es de ", self.importeInteres())
        
m = Menu()
m.menu()

#c = Clientes()
#print(m.listaClientes)
#banco = Banco(Clientes)
"""c.depositar()
c.extraer()
c.imprimirTotal()
c.CajaAhorro
c.PlazoFijo"""