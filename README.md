# Luhn Algorithm

This project implements the Luhn algorithm in Python.

## What is the Luhn Algorithm?
The Luhn algorithm is a simple checksum formula used to validate identification numbers such as credit card numbers. It is designed to catch common data entry errors.

## How It Works
1. Starting from the right, double every second digit.
2. If doubling results in a number greater than 9, subtract 9 from it.
3. Sum all the digits.
4. If the total modulo 10 is 0, the number is valid.

## Usage
Run the script using Python 3:

```bash
python3 luhnAlgo.py
```

You can modify the script to validate different numbers or integrate it into other projects.

## Files
- `luhnAlgo.py`: Main Python script implementing the algorithm.
- `README.md`: Project documentation.

## License
This project is open source and free to use.