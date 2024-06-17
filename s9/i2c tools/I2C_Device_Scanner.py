from pyftdi.i2c import I2cController, I2cNackError

def configure_i2c():
    i2c = I2cController()
    i2c.configure('ftdi://ftdi:ft4232h/1')
    return i2c

def scan_i2c_devices(i2c):
    found_devices = []
    for address in range(0x03, 0x78):
        try:
            i2c.get_port(address).read(1)
            found_devices.append(hex(address))
        except I2cNackError:
            continue
    return found_devices

def main():
    i2c = configure_i2c()
    devices = scan_i2c_devices(i2c)
    if devices:
        print("Found I2C devices at addresses:", devices)
    else:
        print("No I2C devices found.")

if __name__ == '__main__':
    main()

