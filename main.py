from stdft import stdft
from util import plot_spectogram

if __name__ == '__main__':
    file = "recordings/erozija_slow.mp3"
    interval = 0.1
    overlap = 0.0
    hamming = True

    fr, ti, sp = stdft(file, interval, overlap, hamming_window=hamming)
    plot_spectogram(fr, ti, sp, file, interval, overlap, hamming)

