def imprimirContactos(contactos):
        print "Mi lista de contactos"
        print "------------"
        for i in contactos:
                print "------------"
                print ">Nombre: %s" % i[0]
                print ">Telefono: %s" % i[1]
                print ">Email: %s" % i[2]
                print "------------"
        print "------------"
                
def anhadirContacto():
        nombre = raw_input("Nombre: ")
        telefono = raw_input("Telefono: ")
        email = raw_input("Email: ")
        print ""
        return nombre, telefono, email
        

def main():
        contactos = []
        while(input("¿Insertar contacto? [1=Si | 0=No]: ") == 1):
                contactos.append(anhadirContacto())
        imprimirContactos(contactos)

if __name__ == "__main__":
        main()
