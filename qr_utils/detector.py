
import cv2 as cv

qrcode_detector = cv.QRCodeDetector()

def detect_qr(frame):
    return qrcode_detector.detectAndDecode(frame)
