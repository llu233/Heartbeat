from preprocess_ecg import preprocess_ecg_image
from detect_peaks import detect_r_peaks
from calculate_heart_rate import calculate_heart_rate
from heart_simulation import simulate_heartbeat_from_waveform
import numpy as np

def main():
    image_path = 'ecg_image.jpg'  # Path to your downloaded ECG image
    sampling_rate = 100  # Adjust based on your image resolution (samples per second)

    # Process the ECG image to extract the waveform
    try:
        waveform = preprocess_ecg_image(image_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    # Detect R-peaks in the waveform (heartbeat detection)
    r_peaks = detect_r_peaks(waveform, min_distance=50)  # Adjust distance based on your ECG signal

    # Calculate heart rate (beats per minute)
    heart_rate = calculate_heart_rate(r_peaks, sampling_rate)
    print(f"Estimated Heart Rate: {heart_rate:.2f} BPM")

    # Simulate the heartbeat based on R-peaks and waveform data
    simulate_heartbeat_from_waveform(waveform, r_peaks)

if __name__ == "__main__":
    main()
