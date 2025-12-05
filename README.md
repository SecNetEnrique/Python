# Python
Repo showcasing my Python learning journey toward becoming a Junior Penetration Tester. Contains practical scripts for automation, enumeration, parsing tool output, and CTF-style problem-solving. Built to demonstrate growing cybersecurity and coding skills.

# Hosts Manager Tool

This Python script lets you:
- Add entries to /etc/hosts
- Remove entries
- Show all entries
- Clear duplicates

## Usage (Hosts Manager Tool)
1. Run `sudo python3 hosts_manager.py`
2. Follow the menu

# Nmap Auto Scan Tool (nmap_auto)

This Python script (`nmap_auto`) automates a full Nmap scan using commonly used flags for pentesting and CTF practice.  
It runs a detailed scan, timestamps the output, and saves results into a clean text file for later analysis.

## What This Script Does (nmap_auto)
- Performs a detailed Nmap scan using:
  - `-sV` → Version detection  
  - `-sC` → Default scripts  
  - `-O` → OS detection  
  - `-Pn` → Skip host discovery  
  - `-T4` → Faster timing  
- Automatically names output files with:
  - Target IP/domain  
  - Current timestamp  
- Saves results to a `.txt` file  
- Shows the full Nmap command being executed  
- Built for pentesting labs, HTB, TryHackMe, and OSCP-style workflows

## Usage (nmap_auto)
Run with root privileges:

```bash
sudo python3 nmap_auto.py <target>
