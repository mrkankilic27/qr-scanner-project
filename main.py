
import cv2 as cv
import copy
import time
import webbrowser
from qr_utils.detector import detect_qr
from qr_utils.logger import log_qr_data

def draw_overlay(image, text, points, elapsed_time):
    if points is not None:
        pts = points[0].astype(int)
        for i in range(4):
            cv.line(image, tuple(pts[i]), tuple(pts[(i+1)%4]), (0, 255, 0), 2)
        cv.putText(image, text, tuple(pts[0]), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv.putText(image, f"LATENCY: {elapsed_time * 1000:.1f} ms",
               (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    return image

def main():
    cap = cv.VideoCapture(0)
    last_qr = ""

    while True:
        start = time.time()
        ret, frame = cap.read()
        if not ret:
            break

        debug_frame = copy.deepcopy(frame)
        data, points, _ = detect_qr(frame)

        if data and data != last_qr:
            print(f"Detected: {data}")
            log_qr_data(data)
            if data.startswith("http"):
                webbrowser.open(data)
            last_qr = data

        elapsed = time.time() - start
        debug_frame = draw_overlay(debug_frame, data, points, elapsed)

        cv.imshow("QR Scanner", debug_frame)
        if cv.waitKey(1) in [27, 32]:  # ESC or SPACE
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
