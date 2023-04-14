# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# All pins are based on the default pinout used for the NavQPlus.  
# Ports may be enabled or disabled depending on the I/O Mux configured
# For the pin mapping, check out the CPU datasheet 
# (Preview here -https://www.nxp.com/docs/en/preview/PREVIEW_IMX8MPIEC.pdf ,
# full version requires NXP account creation)
"""NXP IMX8MP SOM pin names"""
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

# TODO - implement UART/SPI ports
# UART and SPI coming still to be implemented

GPIO5_IO0 = Pin((4, 0))  # GPIO5.IO[0]
GPIO5_IO1 = Pin((4, 1))  # GPIO5.IO[1]

# I2C0 - Do not use, connected to the internal PMIC

# I2C1 - Do not use, connected to the internal PMIC

# I2C 2 - CSI 1
I2C2_SCL = Pin((4, 16))  # GPIO5_IO16
I2C2_SDA = Pin((4, 17))  # GPIO5_IO17

# I2C 3 - CSI 2
I2C3_SCL = Pin((4, 18))  # GPIO5_IO18
I2C3_SDA = Pin((4, 19))  # GPIO5_IO19

# I2C 4 - RTC
I2C4_SCL = Pin((4, 20))  # GPIO5_IO20
I2C4_SDA = Pin((4, 21))  # GPIO5_IO21


# I2C 6 - Aux (MUXd with UART4)
I2C6_SCL = Pin((3, 28))  # GPIO5_IO28
I2C6_SDA = Pin((3, 29))  # GPIO5_IO29
#

i2cPorts = (
    (2, I2C2_SCL, I2C2_SDA),
    (3, I2C3_SCL, I2C3_SDA),
    (4, I2C4_SCL, I2C4_SDA),
    (6, I2C6_SCL, I2C6_SDA),
)
