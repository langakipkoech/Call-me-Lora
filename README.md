# Call-me-Lora
The investigation of LoRa wireless propagation uses a LoRaWAN transceiver shield embedded on a NUCLEO-F446RE - STM32 Nucleo-64 development board. A sensor is connected to the development board and a program for collecting and transmitting data is flashed to the microcontroller unit. The LoRaWAN transceiver sends data through a gateway to an online platform called the things network. From the things network data is sent to a database that is created for storage and visualization of data. For this project, data will be transmitted to the gateway from different geographical locations. Measurements of the received signal strength indicator (RSSI) and the signal to noise ratio (SNR) will be taken and stored in influx database. The wireless performance based on the range and topography.
