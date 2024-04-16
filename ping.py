from ping import ProxyPing, VerificadorPingReal, ping


if __name__ == "__main__":
    print("Ejecutando el código del cliente:")
    
    # Creando un verificador de ping real
    verificador_real = VerificadorPingReal()
    
    # Creando un proxy para la verificación de ping
    proxy = ProxyPing(verificador_real)
    
    # Intentando hacer ping a una dirección IP
    direccion_ip = input("Ingresa una dirección IP para hacer ping: ")
    
    # Verificando acceso con el proxy
    if proxy.verificar_acceso(direccion_ip):
        # Si se concede acceso, realiza la operación de ping
        ping(direccion_ip)