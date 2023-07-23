import cv2
import numpy as np
import configparser


def load_config(config_file_path):
    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config


def focus_peaking(frame, threshold=100, blur_kernel_size=(5, 5)):
    # Convert the frame to grayscale
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the frame to reduce noise
    blurred_img = cv2.GaussianBlur(img, blur_kernel_size, 0)

    # Calculate the gradient magnitude using Sobel operators
    gradient_x = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

    # Convert the gradient magnitude to 8-bit image
    gradient_8bit = np.uint8(gradient_magnitude)

    # Threshold the gradient magnitude to find edges
    _, edges = cv2.threshold(gradient_8bit, threshold, 255, cv2.THRESH_BINARY)

    # Convert the original frame to color for highlighting edges in red
    img_color = frame.copy()

    # Apply the red color to in-focus pixels
    img_color[edges > 0] = [0, 0, 255]

    return img_color


def main(config_file_path):
    # Load configuration from the file
    config = load_config(config_file_path)

    # Get camera index from the configuration
    camera_index = int(config.get('Camera', 'Index'))

    # Initialize the video capture object for the webcam
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Could not access the camera. Make sure it's connected and not in use.")
        return

    # Wait for the user to accept using the camera
    print("Press 'q' to quit the application.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Apply focus peaking to the frame
        threshold = int(config.get('FocusPeaking', 'Threshold'))
        blur_kernel_size = eval(config.get('FocusPeaking', 'BlurKernelSize'))
        output_frame = focus_peaking(frame, threshold, blur_kernel_size)

        # Display the frame with focus peaking
        cv2.imshow("Focus Peaking", output_frame)

        # Exit when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    config_file_path = "config.ini"
    main(config_file_path)
