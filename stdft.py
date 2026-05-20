from math import ceil

from util import *


def stdft(file_name, interval_length, overlap_percentage, nfft=1024, hamming_window=False):
    samples, Fs = read_signal_from_mp3(file_name)

    # 1. Split signal into parts.
    windows = []
    t = []
    number_of_samples = int(interval_length * Fs)

    idx = 0
    while idx < len(samples) - 1:
        second_idx = idx
        if idx + number_of_samples <= len(samples):
            second_idx += number_of_samples
        else:
            second_idx= len(samples)

        window = samples[idx:second_idx]

        # 1.2 Apply hamming window.
        if hamming_window:
            window = window * np.hamming(len(window))

        # 1.3 Pad the samples.
        if len(window) < nfft:
            window = np.pad(window, (0, nfft - len(window)))

        hop = len(window) * (1 - overlap_percentage)
        t.append((idx * hop + len(window) / 2) / Fs)

        # 1.4 Apply FFT
        windows.append(np.fft.fft(window))
        idx += ceil(number_of_samples - overlap_percentage * number_of_samples)

    # Calculate aditional values.

    # Frequency bins (y axis on spectogram).
    f = np.fft.rfftfreq(nfft, d=1/Fs)



    return f, t, windows



