from pyftdi.i2c import I2cController, I2cNackError

def configure_i2c():
    
    i2c = I2cController()

    
    i2c.configure('ftdi://ftdi:ft4232h/1')

    
    return i2c

def communicate_with_hashboard(i2c):
    
    hashboard_address = 0x20  

    # Get I2C port for the hashboard
    hashboard = i2c.get_port(hashboard_address)
    
    
    try:
        hashboard.write([0x00, 0x01, 0x02])
        print("Initialization data written to hashboard")
    except I2cNackError as e:
        print(f"Failed to communicate with the hashboard: {e}")
        return

    
    try:
        read_data = hashboard.read(3)
        print(f"Read data from hashboard: {read_data}")
    except I2cNackError as e:
        print(f"Failed to read from hashboard: {e}")

def main():
    
    i2c = configure_i2c()

   
    communicate_with_hashboard(i2c)

if __name__ == '__main__':
    main()

