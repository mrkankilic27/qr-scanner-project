import copy
import time
import argparse
import subprocess
import cv2 as cv


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", type=int, default=640)
    parser.add_argument("--height", type=int, default=480)
    return parser.parse_args()


def open_url(url):
    # Windows'da 'start' komutu ile varsayılan tarayıcıda aç
    subprocess.run(['cmd', '/c', 'start', '', url], shell=True)


def draw_tags(image, qrcode_result, elapsed_time):
    if len(qrcode_result[0]) > 0:
        text = qrcode_result[0]
        corner = qrcode_result[1][0]

        corner_01 = (int(corner[0][0]), int(corner[0][1]))
        corner_02 = (int(corner[1][0]), int(corner[1][1]))
        corner_03 = (int(corner[2][0]), int(corner[2][1]))
        corner_04 = (int(corner[3][0]), int(corner[3][1]))

        cv.line(image, corner_01, corner_02, (255, 0, 0), 2)
        cv.line(image, corner_02, corner_03, (255, 0, 0), 2)
        cv.line(image, corner_03, corner_04, (0, 255, 0), 2)
        cv.line(image, corner_04, corner_01, (0, 255, 0), 2)

        cv.putText(image, str(text), corner_01,
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv.LINE_AA)

        # URL ise ve henüz açılmamışsa aç
        if text.startswith("http://") or text.startswith("https://"):
            if not hasattr(draw_tags, "last_opened") or draw_tags.last_opened != text:
                open_url(text)
                draw_tags.last_opened = text

    cv.putText(image,
               f"DELAY: {elapsed_time * 1000:.1f} ms",
               (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2,
               cv.LINE_AA)

    return image


def main():
    args = get_args()

    cap = cv.VideoCapture(args.device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, args.height)

    qrcode_detector = cv.QRCodeDetector()
    elapsed_time = 0

    while True:
        start_time = time.time()
        ret, frame = cap.read()
        if not ret:
            break

        debug_frame = copy.deepcopy(frame)
        result = qrcode_detector.detectAndDecode(frame)

        debug_frame = draw_tags(debug_frame, result, elapsed_time)
        elapsed_time = time.time() - start_time

        cv.imshow("QR Scanner", debug_frame)

        key = cv.waitKey(1)
        if key == 27 or key == 32:  # ESC veya SPACE basılırsa çık
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
