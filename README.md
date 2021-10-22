# Call-me-Lora
The investigation of LoRa wireless propagation uses a LoRaWAN transceiver shield embedded on a NUCLEO-F446RE - STM32 Nucleo-64 development board. A sensor is connected to the development board and a program for collecting and transmitting data is flashed to the microcontroller unit. The LoRaWAN transceiver sends data through a gateway to an online platform called the things network. From the things network data is sent to a database that is created for storage and visualization of data. For this project, data will be transmitted to the gateway from different geographical locations. Measurements of the received signal strength indicator (RSSI) and the signal to noise ratio (SNR) will be taken and stored in influx database. The wireless performance based on the range and topography.


The LoRaWAN transceiver shield allows the user to send data to the LoRaWAN gateway at low data rates. It provides long-range spread spectrum communication and high interference immunity whilst minimizing power consumption. It mostly targets wireless sensor network applications such as smart metering, smart cities, smartphone detection, building automation etc.

The LoRa transceivers uses worldwide license-free radio spectrum such as those in the 433/470/868/780/915 MHz ISM bands. This radio spectrum is relatively cheaper to develop and
experiences less interference compared to a wireless network like Wi-Fi.

LoRaWAN gateway
Gateways form the bridge between end devices and The Things Network. Devices use low power networks like LoRaWAN to connect to the gateway while the gateway uses high bandwidth
networks like Wi-Fi, Ethernet or Cellular to connect to The Things Network. A single gateway can serve several devices. The Multiconnect Conduit is a programmable gateway that uses an open Linux development environment for industrial IoT applications. Conduit allows users to plug in two Multiconnect mCard accessory cards supporting wired or wireless interfaces. It also provides an online application store as a platform for developers to provision and manage their gateway and associated sensors and devices. MCard options include a LoRaWAN mCard capable of supporting thousands of Multiconnect mDot long range RF modules connected to remote sensors or appliances.


The Things Network (TTN)
The Things Network is an open source, decentralized infrastructure for the Internet of Things. It is a cloud server that helps in configuring the sensor credentials such as device and apps address and network security keys for the systems security. This platform registers and hosts security details of the devices and programs. Moreover, the platform visualizes the data in real time. It also maps the available gateways and sensors uptime. it shows the uptime of the devices upon deployment. This platform allows a user to temporarily visualize raw data from the gate way before it is sent to a database for processing


This is a database that stores data that comes from the node-red data pipeline. A purposeful open source database for local host but limited edition online, developed on an open source core infrastructure for analyzing and computing metrics and events (time series data) and storing the data.
The data collected from the network of sensors is sent to the MultiTech gateway. From the gateway, the data is sent to the cloud platform (TTN). The TTN sends data to the influx DB. The data is then queried from the database and visualized on the Jupyter Notebook.
