import qrcode

def generate_qr_png(data, output_file):

    # Create QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=16,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR code saved as PNG in {output_file}")

if __name__ == "__main__":

    # Generate links
    base_url = "https://promisiune.aflaraspunsul.ro/"
    links = [f"{base_url}random"] + [f"{base_url}text{x}" for x in range(1, 101)]

    # Output OR Code names
    filenames = [f"qr_code_random.png"] + [f"qr_code_{x}.png" for x in range(1, 101)]


     # Generate QR codes into a zip
    for link, filename in zip(links, filenames):
        generate_qr_png(link, filename)
