#!/usr/bin/env python3
"""
Simple Port Scanner
Educational tool for learning network concepts
"""

import socket
import sys

def scan_port(host, port):
    """Check if a port is open"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 port_scanner.py <host>")
        sys.exit(1)
    
    host = sys.argv[1]
    print(f"Scanning {host}...")
    
    # Scan common ports
    common_ports = [21, 22, 23, 25, 80, 443, 3306, 3389, 8080]
    
    for port in common_ports:
        if scan_port(host, port):
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

if __name__ == "__main__":
    main()
