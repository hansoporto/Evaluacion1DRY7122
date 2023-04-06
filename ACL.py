numero_acl = input("Ingrese Numero de ACL: ")
if numero_acl.isdigit():
    numero_acl = int(numero_acl)
    if numero_acl >= 1 and numero_acl <= 99:
        print("El número de ACL " + str(numero_acl) + " es una ACL Estándar.")
    elif numero_acl >= 100 and numero_acl <= 199:
        print("El número de ACL " + str(numero_acl) + " es una ACL Extendida.")
    else:
        print("El número de ACL " + str(numero_acl) + " no corresponde a una lista de acceso.")
else:
    print("El valor ingresado no es un número de ACL válido.")