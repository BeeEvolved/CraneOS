import serial.tools.list_ports

def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = []

    for port in ports:
        available_ports.append((port.device, port.description))

    return available_ports

def main():
    ports = list_serial_ports()
    if ports:
        print("Available serial ports:")
        for port, description in ports:
            print(f"{port}: {description}")
    else:
        print("No serial ports found.")

if __name__ == "__main__":
    main()

