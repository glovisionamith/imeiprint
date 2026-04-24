import subprocess

PRINTER_NAME = "TVS-E_RP_3230"

print("✅ Ready to scan IMEI...")

while True:
    try:
        imei = input().strip()

        if len(imei) == 0:
            continue

        print(f"🖨️ Printing: {imei}")

        # 👉 No spacing, single clean line
        spaced_imei = imei

        data = (
            "\x1b\x40"        # Initialize printer
            "\x1b\x61\x01"    # Center align
            "\x1b\x45\x01"    # Bold ON
            "\x1b!\x20"       # Balanced size
            + spaced_imei + "\n"
            "\x1b\x45\x00"    # Bold OFF
            "\n\n\n\n"        # Gap
            "\x1d\x56\x00"    # Cutter
        )

        subprocess.run(
            ["lp", "-d", PRINTER_NAME, "-o", "raw"],
            input=data.encode("utf-8")
        )

    except KeyboardInterrupt:
        print("⛔ Stopped")
        break

    except Exception as e:
        print("❌ Error:", e)
