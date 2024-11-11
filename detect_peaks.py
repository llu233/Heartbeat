# detect_peaks.py
from scipy.signal import find_peaks
import numpy as np

def detect_r_peaks(waveform, min_distance=50):
    """
    Detect the R-peaks (major heartbeat spikes) in the waveform.
    :param waveform: 1D numpy array of extracted ECG waveform.
    :param min_distance: Minimum number of samples between peaks (adjust based on sampling rate).
    :return: Indices of detected R-peaks.
    """
    # Detect peaks using the find_peaks function
    r_peaks, _ = find_peaks(waveform, distance=min_distance)
    
    return r_peaks
