#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Banco:
    
    #Creamos el constructor de la clase Banco
    def __init__(self):
        self.agenda = Agenda()
        self.cliente = Clientes()
        
    def consultar_agenda_clientes(self):
        print("Agenda de clientes: ", self.agenda.datos_clientes)
    
    def consultar_agenda_empleados(self):
        print("Agenda de empleados: ", self.agenda.datos_empleados)
        
class Agenda:
    
    def __init__(self):
        #Creamos un diccionario para almacenar a los clientes y otro para los empleados
        self.datos_clientes = {}
        self.datos_empleados = {}
        
    def alta_cliente(self):
        cliente = Clientes()
        
        
    #def modificar_cliente(self):
    #def eliminar_cliente(self):
    #def alta_empleado(self):
    #def modificar_empleado(self):
    #def borrar_empleado(self):
        
#clase Clientes, hereda de agenda para editar el diccionario. Pero no deberia ser así. 
class Clientes(Agenda):
    
    #Contructor de la clase Clientes
    def __init__(self):
        #Cómo creamos el número de cuenta?
        self.numero_de_cuenta = 0
        self.nombre = input("Nombre: ")
        self.dni = int(input("DNI: "))
        self.telfono = input("Número de teléfono: ")
        self.email = input("Dirección de email: ")
        self.CajaAhorro = CajaAhorro()
        #se actualiza el diccionario
        self.datos_clientes[self.dni] = [self.nombre, self.numero_de_cuenta, self.telefono, self.email]
        
    #def iniciar_home_banking(self):
    
#Clase home banking para las operaciones del cliente
class Home_Banking:
    def __init__(self, numero_de_cuenta):
        self.numero_de_cuenta = numero_de_cuenta
        self.fondo_cuenta = 0
        
    #Método depositar
    def depositar(self):
        monto = int(input("Ingrese el monto a depositar: "))
        #acumula los montos depositados por el cliente
        self.fondo_cuenta += monto

    #Método extraer, controlamos que la extracción sea menor al saldo de la cuenta
    def extraer(self):
        importe = int(input("Ingrese el importe a extraer $"))
        #el importe a extraer debe ser menor al saldo xq no puede quedar la cuenta en $0
        while importe >= self.fondo_cuenta:
            print("Debe ingresar un monto menor a $",self.fondo_cuenta)
            importe = int(input("Ingrese el nuevo importe a extraer $"))
        #ingresado el monto correcto, se descuenta del saldo de la cuenta del cliente
        self.fondo_cuenta -= importe
        print("****Retire su dinero****")

        
    #Método mostrar Total
    def imprimirTotal(self):
        total = self.fondo_cuenta
        print("Su saldo actual es de $", total)
        
        


# In[10]:


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
        
            


# In[9]:


cliente = Clientes()
print(cliente.datos_clientes)

# In[13]:


cliente.CajaAhorro.imprimir()
print(cliente.PlazoFijo.importeInteres())

