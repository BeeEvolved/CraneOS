from pyftdi.i2c import I2cController


def configure_i2c():
    
    i2c = I2cController()

    
    i2c.configure('ftdi://ftdi:ft4232h/1')

   
    return i2c


def main():
   
    i2c = configure_i2c()

   
    slave_address = 0x20  
    slave = i2c.get_port(slave_address)

    
    slave.write([0x00, 0x01, 0x02])

    
    read_data = slave.read(3)
    print(f"Read data: {read_data}")


if __name__ == '__main__':
    main()
