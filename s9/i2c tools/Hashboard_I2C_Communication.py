from pyftdi.i2c import I2cController, I2cNackError
from pyftdi.ftdi import FtdiError
import time

def configure_i2c(max_retries=5, retry_delay=1):
    i2c = I2cController()
    for attempt in range(max_retries):
        try:
            print(f"Configuring I2C (attempt {attempt + 1})...")
            i2c.configure('ftdi://ftdi:ft4232h/1')
            print("I2C configured successfully")
            return i2c
        except FtdiError as e:
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    print(f"Failed to configure I2C after {max_retries} attempts.")
    raise FtdiError(f"Failed to configure I2C: {e}")

def send_work_to_hashboard(i2c, address, work_data):
    hashboard = i2c.get_port(address)
    try:
        hashboard.write(work_data)
        print(f"Work data sent to hashboard at address {hex(address)}")
    except I2cNackError as e:
        print(f"Failed to send work data to the hashboard at address {hex(address)}: {e}")

def receive_results_from_hashboard(i2c, address, num_bytes):
    hashboard = i2c.get_port(address)
    try:
        results = hashboard.read(num_bytes)
        print(f"Results received from hashboard at address {hex(address)}: {results}")
        return results
    except I2cNackError as e:
        print(f"Failed to receive results from hashboard at address {hex(address)}: {e}")
        return None

def generate_work():
    return [0x00, 0x01, 0x02, 0x03]

def check_results(results):
    target = b'\x00\x00\x00'
    if results[:3] == target:
        print("Valid hash found:", results)
        return True
    return False

def main():
    i2c = None
    try:
        i2c = configure_i2c()
    except FtdiError as e:
        print(f"Error configuring I2C: {e}")
        return

    hashboard_address = 0x51
    while True:
        work_data = generate_work()
        send_work_to_hashboard(i2c, hashboard_address, work_data)
        results = receive_results_from_hashboard(i2c, hashboard_address, 32)
        if results:
            if check_results(results):
                break
        time.sleep(1)

if __name__ == '__main__':
    main()

