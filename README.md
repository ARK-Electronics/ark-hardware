# ARK Electronics Hardware

STEP and STL files for [ARK Electronics](https://arkelectron.com) products and their cases, consolidated in one place. Every file here is mirrored from the product's source repository in the [ARK-Electronics](https://github.com/ARK-Electronics) GitHub org — this repo just puts them all in one predictable layout so you don't have to hunt per-product.

## Layout

```
Antennas/
└── <brand>/        # shared reference antenna STLs (beitian, maxtena, …)

<Product>/
├── model/          # STEP model of the PCBA
├── case/           # STEP/STL files of the case (if the product has one)
├── antenna/        # symlinks into Antennas/ for antennas used by this product
└── printed_parts/  # printable parts (ARK RIG5 / RIG7 only)
```

Only the latest revision of each PCBA model is included. Earlier revisions remain available in each product's source repository (linked below), and [manifest.tsv](manifest.tsv) records the exact source repo and path for every file in this repo.

## Downloading

All CAD files are stored with [Git LFS](https://git-lfs.com):

```
git lfs install
git clone git@github.com:ARK-Electronics/ark-hardware.git
```

To grab a single file without cloning, open it on GitHub and use **Download raw file** — it serves the actual file, not the LFS pointer.

## Products

| Directory | Store | Docs | Source repo |
|---|---|---|---|
| [ARKV6X](ARKV6X) | [ARKV6X](https://arkelectron.com/product/arkv6x/), [Extended Range](https://arkelectron.com/product/arkv6x-iim-42653/) | [docs](https://docs.arkelectron.com/products/flight-controller/arkv6x) | [ARKV6X_Flight_Controller](https://github.com/ARK-Electronics/ARKV6X_Flight_Controller) |
| [ARKV6S](ARKV6S) | [ARKV6S](https://arkelectron.com/product/arkv6s-flight-controller/) | [docs](https://docs.arkelectron.com/products/flight-controller/arkv6s) | [ARKV6S](https://github.com/ARK-Electronics/ARKV6S) |
| [ARK_FPV](ARK_FPV) | [ARK FPV](https://arkelectron.com/product/ark-fpv-flight-controller/) | [docs](https://docs.arkelectron.com/products/flight-controller/ark-fpv) | [ARK_FPV](https://github.com/ARK-Electronics/ARK_FPV) |
| [ARK_Pi6X](ARK_Pi6X) | [ARK Pi6X](https://arkelectron.com/product/ark-pi6x/), [ARK Pi6X Flow](https://arkelectron.com/product/ark-pi6x-flow/) | [docs](https://docs.arkelectron.com/products/flight-controller/ark-pi6x-flow) | [ARK-Pi6X](https://github.com/ARK-Electronics/ARK-Pi6X) |
| [ARK_PAB_Carrier](ARK_PAB_Carrier) | [ARK Pixhawk Autopilot Bus Carrier](https://arkelectron.com/product/ark-pixhawk-autopilot-bus-carrier/) | [docs](https://docs.arkelectron.com/products/flight-controller/ark-pixhawk-autopilot-bus-carrier) | [ARK_PAB_Carrier](https://github.com/ARK-Electronics/ARK_PAB_Carrier) |
| [ARK_Jetson_PAB_Carrier](ARK_Jetson_PAB_Carrier) | [ARK Jetson PAB Carrier](https://arkelectron.com/product/ark-jetson-pab-carrier/) | [docs](https://docs.arkelectron.com/products/flight-controller/jetson-pabs/ark-jetson-pab-carrier) | [ark_jetson_hardware](https://github.com/ARK-Electronics/ark_jetson_hardware) |
| [ARK_Jetson_PAB_V3](ARK_Jetson_PAB_V3) | [ARK Jetson PAB V3](https://arkelectron.com/product/ark-jetson-pab-v3/) | [docs](https://docs.arkelectron.com/products/flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3) | [ARK_Jetson_PAB_V3](https://github.com/ARK-Electronics/ARK_Jetson_PAB_V3) |
| [ARK_VOXL2_RTK_PAB_Carrier](ARK_VOXL2_RTK_PAB_Carrier) | [ARK VOXL2 RTK PAB Carrier](https://arkelectron.com/product/ark-voxl2-rtk-pab-carrier/) | [docs](https://docs.arkelectron.com/products/flight-controller/ark-voxl2-rtk-pab-carrier) | [VOXL2_RTK_PAB_Carrier](https://github.com/ARK-Electronics/VOXL2_RTK_PAB_Carrier) |
| [ARK_Just_A_Jetson](ARK_Just_A_Jetson) | [ARK Just A Jetson](https://arkelectron.com/product/ark-just-a-jetson/) | [docs](https://docs.arkelectron.com/products/embedded-computers/ark-just-a-jetson) | [just_a_jetson](https://github.com/ARK-Electronics/just_a_jetson) |
| [ARK_Just_A_Pi](ARK_Just_A_Pi) | [ARK Just A Pi](https://arkelectron.com/product/ark-just-a-pi/) | [docs](https://docs.arkelectron.com/products/embedded-computers/ark-just-a-pi) | [just_a_pi](https://github.com/ARK-Electronics/just_a_pi) |
| [ARK_4IN1_ESC](ARK_4IN1_ESC) | [ARK 4IN1 ESC](https://arkelectron.com/product/ark-4in1-esc/), [CONS](https://arkelectron.com/product/ark-4in1-esc-cons/) | [docs](https://docs.arkelectron.com/products/electronic-speed-controller/ark-4in1-esc) | [ARK_4IN1_ESC](https://github.com/ARK-Electronics/ARK_4IN1_ESC) |
| [ARK_GPS](ARK_GPS) | [ARK GPS](https://arkelectron.com/product/ark-gps/) | [docs](https://docs.arkelectron.com/products/gps/ark-gps) | [ARK_GPS](https://github.com/ARK-Electronics/ARK_GPS) |
| [ARK_RTK_GPS](ARK_RTK_GPS) | [ARK RTK GPS](https://arkelectron.com/product/ark-rtk-gps/), [L1 L5](https://arkelectron.com/product/ark-rtk-gps-l1-l5/) | [docs](https://docs.arkelectron.com/products/gps/ark-rtk-gps) | [ARK_RTK_GPS](https://github.com/ARK-Electronics/ARK_RTK_GPS) |
| [ARK_RTK_Base](ARK_RTK_Base) | [ARK RTK Base](https://arkelectron.com/product/ark-rtk-base/) | [docs](https://docs.arkelectron.com/products/gps/ark-rtk-base) | [ARK_RTK_Base](https://github.com/ARK-Electronics/ARK_RTK_Base) |
| [ARK_G5_RTK_GPS](ARK_G5_RTK_GPS) | [ARK G5 RTK GPS](https://arkelectron.com/product/ark-g5-rtk-gps/), [HEADING](https://arkelectron.com/product/ark-g5-rtk-heading-gps/) | [docs](https://docs.arkelectron.com/products/gps/ark-g5-rtk-gps) | [ARK_G5_RTK_GPS](https://github.com/ARK-Electronics/ARK_G5_RTK_GPS) |
| [ARK_MOSAIC-X5_RTK_GPS](ARK_MOSAIC-X5_RTK_GPS) | [ARK MOSAIC-X5 RTK GPS](https://arkelectron.com/product/ark-mosaic-x5-gps/) | [docs](https://docs.arkelectron.com/products/gps/ark-mosaic-x5-rtk-gps) | [ARK_MOSAIC-X5_GPS](https://github.com/ARK-Electronics/ARK_MOSAIC-X5_GPS) |
| [ARK_X20_RTK_GPS](ARK_X20_RTK_GPS) | [ARK X20 RTK GPS](https://arkelectron.com/product/ark-x20-rtk-gps/) | [docs](https://docs.arkelectron.com/products/gps/ark-x20-rtk-gps) | [ARK_X20_GPS](https://github.com/ARK-Electronics/ARK_X20_GPS) |
| [ARK_SAM_GPS](ARK_SAM_GPS) | [ARK SAM GPS](https://arkelectron.com/product/ark-sam-gps/) | [docs](https://docs.arkelectron.com/products/gps/ark-sam-gps) | [ARK_SAM_GPS](https://github.com/ARK-Electronics/ARK_SAM_GPS) |
| [ARK_SAM_GPS_MINI](ARK_SAM_GPS_MINI) | [ARK SAM GPS MINI](https://arkelectron.com/product/ark-sam-gps-mini/) | [docs](https://docs.arkelectron.com/products/gps/ark-sam-gps) | [ARK_SAM_GPS_MINI](https://github.com/ARK-Electronics/ARK_SAM_GPS_MINI) |
| [ARK_DAN_GPS](ARK_DAN_GPS) | [ARK DAN GPS](https://arkelectron.com/product/ark-dan-gps/) | [docs](https://docs.arkelectron.com/products/gps/ark-dan-gps) | [ARK_DAN_GPS](https://github.com/ARK-Electronics/ARK_DAN_GPS) |
| [ARK_TESEO_GPS](ARK_TESEO_GPS) | [ARK TESEO GPS](https://arkelectron.com/product/ark-teseo-gps/) | [docs](https://docs.arkelectron.com/products/gps/ark-teseo-gps) | [ARK_TESEO_GPS](https://github.com/ARK-Electronics/ARK_TESEO_GPS) |
| [ARK_Flow](ARK_Flow) | [ARK Flow](https://arkelectron.com/product/ark-flow/) | [docs](https://docs.arkelectron.com/products/sensor/ark-flow) | [ARK_Flow](https://github.com/ARK-Electronics/ARK_Flow) |
| [ARK_Flow_MR](ARK_Flow_MR) | [ARK Flow MR](https://arkelectron.com/product/ark-flow-mr/) | [docs](https://docs.arkelectron.com/products/sensor/ark-flow-mr) | [ARK_Flow_MR](https://github.com/ARK-Electronics/ARK_Flow_MR) |
| [ARK_DIST](ARK_DIST) | [ARK DIST MR](https://arkelectron.com/product/ark-dist-mr/), [SR](https://arkelectron.com/product/ark-dist-sr/) | [docs](https://docs.arkelectron.com/products/sensor/ark-dist) | [ARK_DIST](https://github.com/ARK-Electronics/ARK_DIST) |
| [ARK_MAG](ARK_MAG) | [ARK MAG](https://arkelectron.com/product/ark-mag/) | [docs](https://docs.arkelectron.com/products/sensor/ark-mag) | [ARK_MAG](https://github.com/ARK-Electronics/ARK_MAG) |
| [ARK_CANnode](ARK_CANnode) | [ARK CANnode](https://arkelectron.com/product/ark-cannode/) | [docs](https://docs.arkelectron.com/products/sensor/ark-cannode) | [ARK_CANNODE](https://github.com/ARK-Electronics/ARK_CANNODE) |
| [ARK_SCH16T](ARK_SCH16T) | [ARK SCH16T](https://arkelectron.com/product/ark-sch16t/), [K10](https://arkelectron.com/product/ark-sch16t-k10-imu/) | [docs](https://docs.arkelectron.com/products/imu/ark-sch16t) | [ARK_SCH16T](https://github.com/ARK-Electronics/ARK_SCH16T) |
| [ARK_ADIS16507](ARK_ADIS16507) | [ARK ADIS16507](https://arkelectron.com/product/ark-adis16507/) | [docs](https://docs.arkelectron.com/products/imu/ark-adis16507) | [ARK_ADIS16507](https://github.com/ARK-Electronics/ARK_ADIS16507) |
| [ARK_PAB_Power_Module](ARK_PAB_Power_Module) | [ARK PAB Power Module](https://arkelectron.com/product/ark-pab-power-module/), [No Connector](https://arkelectron.com/product/ark-pab-power-module-no-connector/) | [docs](https://docs.arkelectron.com/products/power/ark-pab-power-module) | [ARK_PAB_Power_Module](https://github.com/ARK-Electronics/ARK_PAB_Power_Module) |
| [ARK_12S_PAB_Power_Module](ARK_12S_PAB_Power_Module) | [ARK 12S PAB Power Module](https://arkelectron.com/product/ark-12s-pab-power-module/) | [docs](https://docs.arkelectron.com/products/power/ark-12s-pab-power-module) | [ARK_12S_PAB_Power_Module](https://github.com/ARK-Electronics/ARK_12S_PAB_Power_Module) |
| [ARK_12S_Payload_Power_Module](ARK_12S_Payload_Power_Module) | [ARK 12S Payload Power Module](https://arkelectron.com/product/ark-12s-payload-power-module/) | [docs](https://docs.arkelectron.com/products/power/ark-12s-payload-power-module) | [ARK_12S_PAYLOAD_POWER_MODULE](https://github.com/ARK-Electronics/ARK_12S_PAYLOAD_POWER_MODULE) |
| [ARK_M.2_LTE](ARK_M.2_LTE) | [ARK M.2 LTE](https://arkelectron.com/product/ark-m-2-lte/) | [docs](https://docs.arkelectron.com/products/radio/ark-m.2-lte) | [ARK_M.2_LTE](https://github.com/ARK-Electronics/ARK_M.2_LTE) |
| [ARK_Microhard_DDL_Carrier](ARK_Microhard_DDL_Carrier) | [ARK Microhard DDL Carrier](https://arkelectron.com/product/1w-microhard-ddl-ip-radio/) | [docs](https://docs.arkelectron.com/products/radio/ark-microhard-ddl-carrier) | [ARK_Microhard_DDL_Carrier](https://github.com/ARK-Electronics/ARK_Microhard_DDL_Carrier) |
| [ARK_Primary_Avionics_Breakout](ARK_Primary_Avionics_Breakout) | [ARK Primary Avionics Breakout](https://arkelectron.com/product/ark-primary-avionics-breakout/) | [docs](https://docs.arkelectron.com/products/accessories/ark-primary-avionics-adapter) | [ARK-Primary-Avionics-Adapter](https://github.com/ARK-Electronics/ARK-Primary-Avionics-Adapter) |
| [ARK_Secondary_Avionics_Breakout](ARK_Secondary_Avionics_Breakout) | [ARK Secondary Avionics Breakout](https://arkelectron.com/product/ark-secondary-avionics-breakout/) | [docs](https://docs.arkelectron.com/products/accessories/ark-secondary-avionics-adapter) | [ARK-Secondary-Avionics-Adapter](https://github.com/ARK-Electronics/ARK-Secondary-Avionics-Adapter) |
| [ARK_Servo_Expander](ARK_Servo_Expander) | [ARK Servo Expander](https://arkelectron.com/product/ark-servo-expander/) | [docs](https://docs.arkelectron.com/products/accessories/ark-servo-expander) | [ARK_SERVO_EXPANDER](https://github.com/ARK-Electronics/ARK_SERVO_EXPANDER) |
| [ARK_USB_Adapter](ARK_USB_Adapter) | [ARK USB Adapter](https://arkelectron.com/product/ark-usb-adapter/) | — | [ARK_USB_Adapter](https://github.com/ARK-Electronics/ARK_USB_Adapter) |
| [ARK_Pixhawk_Debug_Adapter](ARK_Pixhawk_Debug_Adapter) | [ARK Pixhawk Debug Adapter](https://arkelectron.com/product/ark-pixhawk-debug-adapter/) | — | — |
| [Servo_Adapter](Servo_Adapter) | [Servo Adapter](https://arkelectron.com/product/servo-adapter/) | — | [Servo_Adapter](https://github.com/ARK-Electronics/Servo_Adapter) |
| [Ethernet_Adapter](Ethernet_Adapter) | [Ethernet Adapter](https://arkelectron.com/product/ethernet-adapter/) | — | [Ethernet_Adapter](https://github.com/ARK-Electronics/Ethernet_Adapter) |
| [USB3_Divorcer](USB3_Divorcer) | [USB3 Divorcer](https://arkelectron.com/product/usb3-divorcer/) | — | [USB3_Divorcer](https://github.com/ARK-Electronics/USB3_Divorcer) |
| [ARK_RIG5](ARK_RIG5) | — | — | [ARK_RIG5](https://github.com/ARK-Electronics/ARK_RIG5) |
| [ARK_RIG7](ARK_RIG7) | — | — | [ARK_RIG7](https://github.com/ARK-Electronics/ARK_RIG7) |

## Antennas

Shared reference models live under `Antennas/<brand>/`. Products that ship with or pair with a given antenna symlink to it from their own `antenna/` directory (e.g. `ARK_G5_RTK_GPS/antenna/BT-T076.stl` → `Antennas/beitian/BT-T076.stl`).

| Path | Antenna | Bands |
|---|---|---|
| [Antennas/beitian/BT-T076.stl](Antennas/beitian/BT-T076.stl) | Beitian BT-T076 helical (used by G5 / MOSAIC-X5 / X20 RTK GPS) | Full multi-band: GPS L1/L2/L5, GLONASS L1/L2, Galileo E1/E5a/E5b, BDS B1/B2/B3, QZSS L1/L2/L5/L6, IRNSS L5, SBAS L1/L5, L-band |
| [Antennas/beitian/BT-560.stl](Antennas/beitian/BT-560.stl) | Beitian BT-560 helical | GPS L1/L2, GLONASS L1/L2, BDS B1/B2/B3, Galileo E1/E5b |
| [Antennas/maxtena/M7CHT-A-SMA.stl](Antennas/maxtena/M7CHT-A-SMA.stl) | Maxtena M7HCT-A-SMA helical | L1/L2: GPS L1/L2C, GLONASS L1/L3OC, Galileo E1/E5b, BeiDou B1/B2 |

## Notes

- Product variants that share a PCB use the same model files: ARK RTK GPS L1 L5, ARK G5 RTK HEADING GPS, ARK DIST MR/SR, ARK SCH16T-K10, ARK Pi6X / Pi6X Flow, ARKV6X Extended Range, and ARK PAB Power Module No Connector are covered by their base product's directory, and the ARK 4IN1 ESC CONS model sits alongside the standard ESC model in `ARK_4IN1_ESC/model/`.
- `ARK_Pixhawk_Debug_Adapter/case/STLink_V3_Mini_Holder.stl` is a printable holder that sandwiches an STLink V3 Mini between the case and the ARK Pixhawk Debug Adapter. No PCBA model is available yet (see [MISSING.md](MISSING.md)).
- The ARK Flow case is available as Rev 2 (`ARK_Flow/case/*_Rev_2.step` + `.stl`), which opens the board slot from 1.5218 mm to 1.7000 mm so it clears real PCB thickness tolerance. Rev 1 STLs are kept until Rev 2 is validated on a test print. Both revisions are modelled in the same coordinate frame as `ARK_Flow/model/`, so the case and the PCBA open already assembled.
- Products with no published CAD (telemetry radios, etc.) are tracked in [MISSING.md](MISSING.md).
