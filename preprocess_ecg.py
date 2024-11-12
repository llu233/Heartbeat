import cv2
import numpy as np

def preprocess_ecg_image(image_path):
    """
    Load an ECG image, convert it to binary format, and extract the waveform.
    :param image_path: Path to the ECG image.
    :return: 1D numpy array representing the ECG waveform.
    """
    # Load the ECG image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image file '{image_path}' not found.")

    # Resize the image to a standard width (optional)
    img_resized = cv2.resize(img, (500, 200))

    # Apply a Gaussian blur to reduce noise
    blurred_img = cv2.GaussianBlur(img_resized, (5, 5), 0)

    # Apply adaptive thresholding to highlight the ECG waveform in the image
    binary_img = cv2.adaptiveThreshold(
        blurred_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # Extract the waveform by summing pixel intensities along columns
    waveform = np.sum(binary_img, axis=0)
    waveform = waveform / np.max(waveform)  # Normalize to range [0, 1]

    return waveform
