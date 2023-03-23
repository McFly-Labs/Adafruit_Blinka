# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# All pins are based on the default pinout used for the NavQPlus.  Ports may be enabled or disabled depending on the I/O Mux configured
"""Pin definitions for the Coral Dev Board."""

from adafruit_blinka.microcontroller.nxp.imx8mp import pin

# Board name = RPI name [= alias] = pin name

# For up to documentation on the NXP NavQPlus usage, please see https://nxp.gitbook.io/8mpnavq/dev-guide/hardware-interfaces/i2c

# TODO - implement UART/SPI ports

# I2C0 - Do not use, is configured for the internal PMIC

# I2C1 - Do not use, is configured for the internal PMIC

# I2C 2 - CSI 1
I2C2_SCL = pin.I2C2_SCL
I2C2_SDA = pin.I2C2_SDA

# I2C 3 - CSI 2
I2C3_SCL = pin.I2C3_SCL
I2C3_SDA = pin.I2C3_SDA

# I2C 4 - RTC, SE050 Secure element
I2C4_SCL = pin.I2C4_SCL
I2C4_SDA = pin.I2C4_SDA


# I2C 6 - Aux (MUXd with UART4) - Picked for SDA/SCL because it is accessible externally

I2C6_SCL = SCL = pin.I2C6_SCL
I2C6_SDA = SDA = pin.I2C6_SDA

# Aux connector
GPT1CAPTURE1 = D0 = SAI3_TXC = pin.GPIO5_IO0  # GPIO5.IO[0]
GPT1CAPTURE2 = D1 = SAI3_TXD = pin.GPIO5_IO1  # GPIO5.IO[1]

i2cPorts = (
    (2, I2C2_SCL, I2C2_SDA),
    (3, I2C3_SCL, I2C3_SDA),
    (4, I2C4_SCL, I2C4_SDA),
    (6, I2C6_SCL, I2C6_SDA),
)

#
# UART0 - Bluetooth
# UART1 on /dev/ttymxc0
# UART2 - Defaulted to Linux Console for debug
# UART3 Not available (pins are multiplexed with I2C6)
