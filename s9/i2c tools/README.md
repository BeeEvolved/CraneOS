# I2C Communication Scripts

This repository contains various Python scripts to demonstrate and facilitate I2C communication with FT4232H Bitcrane Control Board.

## Scripts Overview

### Hashboard_I2C_Communication.py

**Key Features:**
- **Retry Mechanism:** Includes a retry mechanism (`configure_i2c()` function) for configuring the I2C connection with retries and delays.
- **Work Generation:** Generates work data (`generate_work()` function) to be sent to the hashboard.
- **Result Checking:** Checks received results (`check_results()` function) for a specific target hash pattern (`b'\x00\x00\x00'`).
- **Main Loop:** Continuously sends work data, receives results, and checks them until a valid hash is found or a maximum number of attempts is reached.

### I2C_Communicatn_Config.py

**Key Features:**
- **Configuration:** Configures the I2C connection directly in `configure_i2c()` function without retry logic.
- **Communication Functions:** Provides separate functions (`communicate_with_hashboard()`) for writing initialization data and reading data from the hashboard.
- **Direct Interaction:** Writes specific initialization data (`[0x00, 0x01, 0x02]`) and reads a fixed number of bytes (3) from the hashboard.

### FT4232H_I2C_Communication.py

**Key Features:**
- **Demonstrates configuration and communication over I2C** using an FT4232H device.
- **Uses the pyftdi library's I2cController** for I2C communication setup.
- **Configures the I2C controller** to connect to port A of the FT4232H device (`'ftdi://ftdi:ft4232h/1'`).
- **Illustrates writing data** to an I2C slave device.

### I2C_Device_Scanner.py

**Key Features:**
- **Configures an I2C controller (I2cController)** for communication with an FT4232H device on port A (`'ftdi://ftdi:ft4232h/1'`).
- **Implements a function (`scan_i2c_devices(i2c)`) to scan** for active I2C devices within the address range `0x03` to `0x77`.
- **Uses try-except blocks** to handle `I2cNackError`, indicating devices that do not respond.
- **Returns a list of hexadecimal addresses (found_devices)** where responsive I2C devices are detected.
- **In `main()`**, prints the addresses of detected I2C devices or indicates if no devices were found.

### Hashboard_Communication_Tester.py

**Key Features:**
- **Sets up an I2C controller (I2cController)** to communicate with an FT4232H device on port A (`'ftdi://ftdi:ft4232h/1'`).
- **Defines a function (`test_hashboard(i2c, address)`) to test communication** with a hashboard device at a specified address.
- **Writes initialization data (`[0x00, 0x01, 0x02]`)** to the hashboard and reads 3 bytes of data from it.
- **Handles `I2cNackError` exceptions** when communication with the hashboard fails.
- **In `main()`**, tests communication with hashboards at addresses `0x4d` and `0x51` (as found_addresses).
- **Prints initialization and read data** from each hashboard if communication is successful, interpreting the data based on the hashboard's protocol if necessary.

### Serial_Port_List.py

**Key Features:**
- **Utilizes `serial.tools.list_ports`** from the PySerial library to enumerate available serial ports.
- **Defines `list_serial_ports()`** to retrieve a list of tuples containing the device name (`port.device`) and description (`port.description`) for each serial port.
- **In `main()`**, calls `list_serial_ports()` to fetch and display available serial ports.
- **Outputs a list of detected serial ports** with their corresponding descriptions if ports are found; otherwise, it indicates if no serial ports are detected.

### I2C_Hashboard_Interaction.py

**Key Features:**
- **Sets up an I2C controller (I2cController)** to connect with an FT4232H device on port A (`'ftdi://ftdi:ft4232h/1'`).
- **Implements `communicate_with_hashboard(i2c, address)`** to manage interactions with a hashboard device at a specified I2C address.
- **Sends initialization data (`[0x00, 0x01, 0x02]`)** to the hashboard and manages `I2cNackError` exceptions if communication fails during the write operation.
- **Receives 3 bytes of data from the hashboard** and manages `I2cNackError` exceptions if communication fails during the read operation.
- **In `main()`**, attempts communication with hashboards at addresses `[0x0c, 0x4d, 0x51]`.
- **Prints initialization and read data** from each hashboard if communication is successful or logs errors if communication fails during either operation.
