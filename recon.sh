#!/bin/bash
#
# Basic Reconnaissance Script
# Educational tool for learning enumeration
#

if [ $# -eq 0 ]; then
    echo "Usage: ./recon.sh <target-ip>"
    exit 1
fi

TARGET=$1

echo "========================================="
echo "Basic Reconnaissance on $TARGET"
echo "========================================="

echo ""
echo "[*] Running Nmap quick scan..."
nmap -F $TARGET

echo ""
echo "[*] Checking common ports..."
nmap -p 21,22,23,25,80,443,3306,3389,8080 $TARGET

echo ""
echo "[*] Scan complete!"
echo "========================================="
