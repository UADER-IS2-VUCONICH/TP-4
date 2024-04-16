#*--------------------------------------------------
#* proxy.py
#* excerpt from https://refactoring.guru/design-patterns/proxy/python/example
#*--------------------------------------------------

import subprocess
from abc import ABC, abstractmethod

class PingChecker(ABC):
    """
    The PingChecker interface declares a method for checking access to a ping operation.
    """

    @abstractmethod
    def check_access(self, ip_address: str) -> bool:
        pass


class RealPingChecker(PingChecker):
    """
    The RealPingChecker contains the actual logic for checking access to ping operation.
    """

    def check_access(self, ip_address: str) -> bool:
        """
        RealPingChecker allows ping operation only if the IP address starts with "192."
        """
        return ip_address.startswith("192.")


class PingProxy(PingChecker):
    """
    The PingProxy acts as a proxy for the PingChecker.
    """

    def __init__(self, real_checker: RealPingChecker) -> None:
        self._real_checker = real_checker

    def check_access(self, ip_address: str) -> bool:
        """
        The Proxy checks the access before allowing the ping operation.
        """
        if self._real_checker.check_access(ip_address):
            return True
        else:
            print("PingProxy: Access denied. IP address does not start with '192.'")
            return False
        
    def execute(self, ip_address: str) -> None:
        """
        Realiza un ping a la dirección IP proporcionada o a www.google.com según la lógica especificada.
        """
        if ip_address == "192.168.0.254":
            print("Ejecutando ping a www.google.com usando el método execute_free:")
            self._execute_free("www.google.com")
        else:
            print("Reenviando ping a la dirección IP proporcionada:")
            self._execute(ip_address)
    def _execute(self, ip_address: str) -> None:
        """
        Realiza la operación de ping a la dirección IP utilizando el método execute_free.
        """
        print(f"Pinging {ip_address}...")
        subprocess.run(["ping", ip_address])

    def _execute_free(self, host: str) -> None:
        """
        Realiza la operación de ping a un host utilizando el método execute_free.
        """
        subprocess.run(["ping", host])



#def ping(ip_address: str) -> None:
#    """
#    Perform ping operation to the given IP address.
#    """
#    print(f"Pinging {ip_address}...")
#    subprocess.run(["ping", ip_address])


if __name__ == "__main__":
    print("Executing the client code:")
    
    # Creating a real ping checker
    real_checker = RealPingChecker()
    
    # Creating a proxy for ping checking
    proxy = PingProxy(real_checker)
    
    # Attempting to ping an IP address
    ip_address = input("Enter an IP address to ping: ")
    
    proxy.execute(ip_address)
    # Checking access with the proxy
    #if proxy.check_access(ip_address):
        # If access is granted, perform ping operation
    #    ping(ip_address)