# ARKV6S Flight Controller

**USA Built • NDAA Compliant • FCC Compliant**

**Pixhawk Autopilot Bus (PAB) Form Factor**  
Low-cost single industrial-grade IMU variant of the ARKV6X based on FMUV6X and Pixhawk Autopilot Bus open source standards.

## Key Features
- STM32H743IIK6 MCU (480 MHz, 2 MB Flash, 1 MB RAM)
- FRAM for reliable parameter storage
- Single TDK InvenSense IIM-42653 Industrial 6-Axis IMU
- STMicroelectronics IIS2MDC Magnetometer
- Bosch Sensortec BMP390 Barometer
- 1 W onboard heater keeps sensors warm in extreme conditions
- MicroSD slot (card included)
- Full Pixhawk Autopilot Bus (PAB) compatibility
- RGB LED indicators
- PX4 Autopilot (ships by default) / ArduPilot can be flashed

## Sensors
| Sensor | Part Number | Interface | Notes |
|--------|-------------|-----------|-------|
| IMU | TDK InvenSense IIM-42653 | SPI | Industrial grade, high shock tolerance, Accel ±4/8/16/32 g, Gyro ±31.25 to ±4000 dps |
| Magnetometer | ST IIS2MDC | I²C (0x1E) | High accuracy, low noise |
| Barometer | Bosch BMP390 | I²C (0x76) | High precision pressure / altitude |

## Electrical / Power
- Input Voltage: 5 V (via PAB)
- Total Current: 500 mA max
  - System (MCU + sensors + peripherals): 300 mA typical
  - Heater: 200 mA (1 W @ 5 V, TIM2 PWM controllable)
- Onboard Regulation:
  - 3.3 V FMU: TPSM861253 (up to 1 A)
  - 3.3 V Sensors: NCV8177 LDO
  - 3.3 V SD Card: load-switched (SIP32402)

## Mechanical
- Dimensions: 3.6 × 2.9 × 0.5 cm (36 × 29 × 5 mm)
- Weight: 5 g
- Connectors:
  - J2: Hirose DF40C-100DP-0.4V (PAB X1)
  - J3: Hirose DF40C-50DP-0.4V (PAB X2)
  - J1: Molex 5033981892 MicroSD

## Serial Port Mapping (PX4)
| UART | Device | Port |
|------|--------|------|
| USART1 | /dev/ttyS0 | GPS |
| USART2 | /dev/ttyS1 | TELEM3 |
| USART3 | /dev/ttyS2 | Debug Console |
| UART4 | /dev/ttyS3 | UART4 & I2C |
| UART5 | /dev/ttyS4 | TELEM2 |
| USART6 | /dev/ttyS5 | PX4IO / RC |
| UART7 | /dev/ttyS6 | TELEM1 |
| UART8 | /dev/ttyS7 | GPS2 |

**Pinout:** Full PAB pinout per [Pixhawk DS-010 Autopilot Bus Standard](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-010%20Pixhawk%20Autopilot%20Bus%20Standard.pdf). No deviations from standard FMU mapping.

## Firmware
- **PX4**: `ark_fmu-v6s_default` (ships by default)
- **ArduPilot**: ARKV6S target (board ID 61)
- Bootloader active on TELEM1 (UART7) only

## Compliance & Additional Notes
- USA manufactured
- NDAA compliant
- FCC compliant
- Requires a Pixhawk Autopilot Bus compliant carrier board (e.g. ARK Pixhawk Autopilot Bus Carrier)
- 3D Model: [ARKV6S.step](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARKV6S/model)
- Source Schematic/BOM: Rev 1.0 (based on ARKV6X Rev 5.1 with IMUs 2/3 removed, BMM150 → IIS2MDC, regulator updates)
- Documentation: [docs.arkelectron.com/products/flight-controller/arkv6s](https://docs.arkelectron.com/products/flight-controller/arkv6s)

---
**ARK Electronics** | Salt Lake City, Utah | arkelectron.com  
Hardware Revision 1.0 | Datasheet generated from schematic, BOM, and public product documentation
