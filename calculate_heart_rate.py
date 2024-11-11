import numpy as np

def calculate_heart_rate(r_peaks, sampling_rate):
    """
    Calculate the heart rate (BPM) from the R-peaks detected in the waveform.
    :param r_peaks: Indices of detected R-peaks.
    :param sampling_rate: Sampling rate of the ECG waveform (in Hz, i.e., samples per second).
    :return: Estimated heart rate (BPM).
    """
    if len(r_peaks) < 2:
        return None  # Not enough R-peaks to calculate heart rate

    # Calculate RR intervals (time between successive R-peaks) in seconds
    rr_intervals = np.diff(r_peaks) / sampling_rate

    # Calculate the average RR interval and convert to heart rate (BPM)
    avg_rr_interval = np.mean(rr_intervals)
    heart_rate = 60 / avg_rr_interval  # Convert to beats per minute (BPM)
    
    return heart_rate
