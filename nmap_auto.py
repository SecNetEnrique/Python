
#!/usr/bin/env python3

import argparse
import subprocess
import time


def run_nmap(target):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_file = f"nmap_scan_{target}_{timestamp}.txt"


    command = [
        "nmap",
        "-sVC",
        "-O",
        "-T4",
        "-Pn",
        target
    ]

    print(f"[+] Running Nmap scan on {target} ...")
    print(f"[+] Command: {' '.join(command)}") 


    try:
        result = subprocess.run(
            command, capture_output=True, text=True, check=True
        )

        with open(output_file, "w") as f:
            f.write(result.stdout)

     
        print(f"[+] Scan complete! Saved to: {output_file}")


    except subprocess.CalledProcessError as e:
        print("[-] Error running Nmap:")
        print(e)

def main():
    parser = argparse.ArgumentParser(
        description="Simple Nmap automation script for pentesting practice."
    )
    parser.add_argument("target", help="Target IP or domain to scan")


    args = parser.parse_args()
    run_nmap(args.target)


if __name__ == "__main__":
    main()






















