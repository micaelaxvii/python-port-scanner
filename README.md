## My first TCP port scanner built with Python.

### Requirements

- Python 3.9 or newer
- No third-party packages required.

### Installation

Clone the repository:
```bash
git clone https://github.com/micaelaxvii/python-port-scanner.git
```

### Command-Line Arguments

- `-ip`, `--ip_address`: Target IP address.
- `-p`, `--port_range`: Target port range.
- `-t`, `--threads`: [Optional] Number of concurrent workers. (default: 10)
- `-v`, `--verbose`: [Optional] Enable verbose output.

### Example usage

Run the scanner with an IP address and a port range:
```bash
python port_scanner.py --ip_address 127.0.0.1 --port_range 1 1024 
 ```
The example uses 127.0.0.1, your own computer's loopback address.
