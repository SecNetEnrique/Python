#!/usr/bin/env python3
import os

HOSTS_FILE = "/etc/hosts"

def read_hosts():
    with open(HOSTS_FILE, "r") as f:
        return f.readlines()

def write_hosts(lines):
    with open(HOSTS_FILE, "w") as f:
        f.writelines(lines)

def entry_exists(ip, domain):
    lines = read_hosts()
    for line in lines:
        if line.strip() == f"{ip} {domain}":
            return True
    return False

def add_entry():
    ip = input("Enter IP address: ").strip()
    domain = input("Enter domain name: ").strip()

    if entry_exists(ip, domain):
        print("[!] Entry already exists.")
        return
    
    entry = f"{ip} {domain}\n"
    os.system(f'echo "{entry.strip()}" | sudo tee -a {HOSTS_FILE} > /dev/null')
    print(f"[+] Added: {entry.strip()}")

def remove_entry():
    ip = input("Enter IP address: ").strip()
    domain = input("Enter domain name: ").strip()
    
    lines = read_hosts()
    new_lines = [l for l in lines if l.strip() != f"{ip} {domain}"]

    if len(lines) == len(new_lines):
        print("[!] Entry not found.")
        return
    
    write_hosts(new_lines)
    print(f"[+] Removed: {ip} {domain}")

def show_entries():
    print("\n=== /etc/hosts CONTENT ===")
    os.system(f"cat {HOSTS_FILE}")
    print("==========================\n")

def clear_duplicates():
    lines = read_hosts()
    seen = set()
    new_lines = []

    for line in lines:
        if line.strip() not in seen:
            new_lines.append(line)
            seen.add(line.strip())
    
    write_hosts(new_lines)
    print("[+] Removed duplicate entries.")

def menu():
    while True:
        print("""
========= HOSTS MANAGER =========
1) Add entry
2) Remove entry
3) Show hosts file
4) Clear duplicates
5) Exit
=================================
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            remove_entry()
        elif choice == "3":
            show_entries()
        elif choice == "4":
            clear_duplicates()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
