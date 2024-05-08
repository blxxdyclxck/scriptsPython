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

#Al ponerlo todo en lista y si en el shell = true estamos programando de forma segura

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
subprocess.call(["ifconfig", interface, "up"])

