import numpy as np
from scipy.io import wavfile

def compare_voices(reference_file, test_file, threshold=500):
    rate1, data1 = wavfile.read(reference_file)
    rate2, data2 = wavfile.read(test_file)

    # Simple shape match
    if data1.shape != data2.shape:
        return False

    # Compute difference
    diff = np.linalg.norm(data1 - data2)

    return diff < threshold
