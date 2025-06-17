
import qrcode

def generate_qr(data, output_path="examples/generated_qr.png"):
    img = qrcode.make(data)
    img.save(output_path)
