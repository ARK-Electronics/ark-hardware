# Products without CAD files

Products sold on [arkelectron.com](https://arkelectron.com/shop/) that have no STEP/STL files in this repository, and why. If CAD gets published for any of these, add it here to the standard layout and remove the row.

| Product | Store | Status |
|---|---|---|
| 1W 900MHz Serial Telemetry Radio | [store](https://arkelectron.com/product/1w-900mhz-serial-telemetry-air-radio/) | No published CAD. Based on the Microhard Pico P900; only a [PDF outline drawing](https://arkelectron.com/wp-content/uploads/2020/10/Air-Module-Drawing.pdf) exists. |
| 1W 900MHz USB Serial Telemetry Radio | [store](https://arkelectron.com/product/1w-900mhz-serial-telemetry-ground-radio/) | No published CAD. |
| 1W 2.4GHz Serial Telemetry Radio | [store](https://arkelectron.com/product/1w-2400mhz-serial-telemetry-radio/) | No published CAD. Based on the Microhard Pico P2400; same [PDF outline drawing](https://arkelectron.com/wp-content/uploads/2020/10/Air-Module-Drawing.pdf) as the 900MHz air module. |
| 1W 2.4GHz USB Serial Telemetry Radio | [store](https://arkelectron.com/product/1w-2400mhz-usb-serial-telemetry-radio/) | No published CAD. |
| L1/L5 GNSS Antenna | [store](https://arkelectron.com/product/l1-l5-gnss-antenna/) | No official CAD or documentation published for this product. Of the reference STLs under [Antennas/](Antennas/), only the Beitian BT-T076 covers L5 (full multi-band including GPS L1/L2/L5); BT-560 and Maxtena M7HCT-A-SMA are L1/L2-class. ARK's pages don't confirm which (if any) is this exact SKU. |
| LiPow The USB C Lipo Battery Charger | [store](https://arkelectron.com/product/lipow-the-usb-c-lipo-battery-charger/) | Hardware lives in a personal repo ([AlexKlimaj/LiPow-Hardware](https://github.com/AlexKlimaj/LiPow-Hardware), schematic/BOM only); the case CAD is on [Onshape](https://cad.onshape.com/documents/ed31be3eeac76455b0277835/w/c7a7c12a1270b22173eee4b2/e/8ebc8b884a3338f02ab4af95). No STEP/STL in the ARK-Electronics org. |
| BQ25703A Programmable Regulator Module | [store](https://arkelectron.com/product/bq25703a-programmable-regulator-module/) | Hardware docs live in a personal repo ([AlexKlimaj/BQ25703A_Module](https://github.com/AlexKlimaj/BQ25703A_Module)); no 3D model published. |

Bundles (ARKV6X bundles, Jetson PAB / PAB V3 Orin bundles, Just A Jetson bundles) are not listed — they are combinations of products already in this repository. A combined carrier-stack assembly (`ARK_PAB_Jetson_Carrier_Bundle.step`) exists in [ark_jetson_hardware](https://github.com/ARK-Electronics/ark_jetson_hardware) if that is ever wanted here.

## Known gaps in included products

| Product | Gap |
|---|---|
| ARK Jetson PAB V3 | PCBA model only — no case CAD is published anywhere for V3 (the case files under `ARK_Jetson_PAB_Carrier/case/` are for the previous-generation carrier). |
| ARK Pixhawk Debug Adapter | STLink V3 Mini holder case only — no PCBA STEP model is published. |
