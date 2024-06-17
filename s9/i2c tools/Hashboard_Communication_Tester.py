from pyftdi.i2c import I2cController, I2cNackError

def configure_i2c():
    i2c = I2cController()
    i2c.configure('ftdi://ftdi:ft4232h/1')
    return i2c

def test_hashboard(i2c, address):
    hashboard = i2c.get_port(address)
    try:
       
        hashboard.write([0x00, 0x01, 0x02])
        print(f"Initialization data written to hashboard at address {hex(address)}")

        
        read_data = hashboard.read(3)
        print(f"Read data from hashboard at address {hex(address)}: {read_data}")
        return read_data
    except I2cNackError as e:
        print(f"Failed to communicate with the hashboard at address {hex(address)}: {e}")
        return None

def main():
    i2c = configure_i2c()
    found_addresses = [0x4d, 0x51]

    for address in found_addresses:
        print(f"Testing address {hex(address)}...")
        data = test_hashboard(i2c, address)
        if data:
            
            print(f"Received data from address {hex(address)}: {data}")

if __name__ == '__main__':
    main()

