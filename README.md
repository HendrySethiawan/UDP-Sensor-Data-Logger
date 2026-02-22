# UDP Sensor Data Logger

This Python script receives UDP packets containing sensor data (8 channels) from a remote source, validates the data, and saves it to a CSV file.

## Features

*   **UDP Reception:** Listens for incoming data on a specified IP and port.
*   **Data Validation:** Automatically filters out invalid data points (negative numbers, NaN, and Infinity).
*   **CSV Export:** Saves the collected data to a local CSV file.
*   **Graceful Shutdown:** Allows stopping the process safely using the keyboard.

## Prerequisites

You will need Python installed along with the following libraries:

*   `pandas`
*   `pynput`

You can install them using pip:

```bash
pip install pandas pynput
```

## Configuration

Before running the script, you may need to modify the configuration variables at the top of `main.py`:

*   **IP:** The IP address of the sender (default: `'192.168.88.26'`).
*   **Port:** The port number to listen on (default: `9999`).
*   **Output Path:** The file path where the CSV will be saved (default: `C:\Users\hendr\Documents\Kuliah\PKL\Kegiatan\Data\Data 4 Reyhan Jalan Tanpa Pakai Kaos Kaki.csv`).

## Usage

1.  Run the script:
    ```bash
    python main.py
    ```
2.  The script will start listening for data. You will see the timestamp and raw data printed in the console.
3.  To stop the process and save the data to the CSV file, press the **ESC** key.

## Data Format

The script expects incoming UDP packets to be formatted as comma-separated strings containing 8 values (s1, s2, s3, s4, s5, s6, s7, s8).
```
value1,value2,value3,value4,value5,value6,value7,value8
```
