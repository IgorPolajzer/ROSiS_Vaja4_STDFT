from matplotlib import pyplot as plt
from pydub import AudioSegment
import numpy as np


def read_signal_from_mp3(input_file):
    sound = AudioSegment.from_mp3(input_file)
    samples = np.frombuffer(sound.raw_data, dtype=np.int16).astype(np.float32) / 32767
    return samples, sound.frame_rate


def plot_spectogram(fr, ti, sp):
    plt.pcolormesh(ti, fr, np.log10(sp) , shading='auto')
    plt.title('Spektrogram')
    plt.xlabel('Čas [s]')
    plt.ylabel('Frekvenca [Hz]')
    plt.colorbar(label='Amplituda')
    plt.show()

