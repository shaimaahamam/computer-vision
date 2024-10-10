import cv2
import numpy as np
import pickle

# Rectangle dimensions
RECT_WIDTH, RECT_HEIGHT = 107, 48

# Load parking positions from a pickle file
def load_parking_positions(filename='carParkPoses'):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Save parking positions to a pickle file
def save_parking_positions(posList, filename='carParkPoses'):
    with open(filename, 'wb') as f:
        pickle.dump(posList, f)

# Mouse click event handler
def mouse_click(event, x, y, posList):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        posList[:] = [pos for pos in posList if not (pos[0] < x < pos[0] + RECT_WIDTH and pos[1] < y < pos[1] + RECT_HEIGHT)]
    save_parking_positions(posList)

# Draw rectangles for parked cars and update the display
def draw_parking_spaces(img, posList, imgPro):
    spaceCount = 0
    for pos in posList:
        x, y = pos
        crop = imgPro[y:y + RECT_HEIGHT, x:x + RECT_WIDTH]
        count = cv2.countNonZero(crop)
        color, thick = ((0, 255, 0), 5) if count < 900 else ((0, 0, 255), 2)
        cv2.rectangle(img, pos, (x + RECT_WIDTH, y + RECT_HEIGHT), color, thick)
        if count < 900:
            spaceCount += 1

    # Display the number of available spaces
    cv2.rectangle(img, (10, 10), (500, 60), (0,0,0), -1)
    cv2.putText(img, f'There are "{spaceCount}" free of "{len(posList)}"', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

# Main function to set up the GUI and video processing
def main():
    posList = load_parking_positions()
    
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", lambda event, x, y, flags, params: mouse_click(event, x, y, posList))

    # Load the image for marking parking spots
    img = cv2.imread("image.png")
    while True:
        for pos in posList:
            cv2.rectangle(img, pos, (pos[0] + RECT_WIDTH, pos[1] + RECT_HEIGHT), (0, 0, 255), 2)
            
        cv2.resize(img, (300,300))
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    # Open the video and process each frame
    cap = cv2.VideoCapture('parking.mp4')
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, img = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart the video if it ends
            continue

        # Image processing pipeline
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 1)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 25, 16)
        dilated = cv2.dilate(cv2.medianBlur(thresh, 5), np.ones((3, 3), np.uint8), iterations=1)

        # Check available parking spaces
        draw_parking_spaces(img, posList, dilated)

        # Display the processed image
        cv2.resize(img, (300,300))
        cv2.imshow("Image", img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
