import qrcode
import io

""" export module to create and return generated password as a qr code image
"""


def make_qr_code(psw):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
            
    )
    qr.add_data(psw) 
    img = qr.make_image()
    # converting PilImage to bytes array
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr
