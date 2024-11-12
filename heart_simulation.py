import time
import os
import numpy as np  # Import numpy here

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_heart(scale):
    """
    Display an ASCII heart symbol based on the scale.
    :param scale: Amplitude of the waveform, used to adjust heart size.
    """
    heart_size = int(5 + scale * 10)  # Adjust heart size based on waveform amplitude
    print(" " * (10 - heart_size) + "❤" * heart_size)

def simulate_heartbeat_from_waveform(waveform, r_peaks):
    """
    Simulate a heartbeat animation based on the ECG waveform and R-peaks.
    :param waveform: 1D numpy array representing the ECG waveform.
    :param r_peaks: Indices of detected R-peaks.
    """
    for peak in r_peaks:
        clear_screen()
        display_heart(waveform[peak] / np.max(waveform))  # Adjust heart size based on peak amplitude
        time.sleep(0.5)  # Control display speed between heartbeats
