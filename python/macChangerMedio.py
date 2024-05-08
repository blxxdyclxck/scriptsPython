import subprocess
import netifaces


def get_network_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces

if __name__ == "__main__":
    print("Interfaces de red disponibles:")
    for interface in get_network_interfaces():
        print(interface)

interface = input("interface (eth0 predeterminado)> ")

print("Ejemplo de MAC: 00:11:22:33:44:77")
newMac = input("Nueva MAC > ")

print("[+] Cambiando dirección MAC para " + interface + " a " + newMac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

#Este mac changer tiene una falla de inyección de comandos:
#Interfaces de red disponibles:
#lo
#eth0
#interface (eth0 predeterminado)> eth0; ls; pwd --> al escribir esto cuando ejecutemos saldra el output de los comandos
