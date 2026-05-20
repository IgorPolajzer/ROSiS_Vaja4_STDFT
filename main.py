from matplotlib import pyplot as plt

from stdft import stdft

if __name__ == '__main__':
    windows, Fs, nfft = stdft("recordings/a_high_pitch.mp3", 1, 0.2, 44105)

    plt.pcolormesh(ti, fr, np.abs(sp), shading='auto') # gouraud
    plt.title('Spektrogram')
    plt.xlabel('Čas [s]')
    plt.ylabel('Frekvenca [Hz]')
    plt.colorbar(label='Amplituda')
    plt.show()