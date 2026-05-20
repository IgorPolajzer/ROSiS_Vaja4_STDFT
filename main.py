from stdft import stdft
from util import plot_spectogram

if __name__ == '__main__':
    fr, ti, sp = stdft("recordings/a_high_pitch.mp3", 1, 0, 44105)
    plot_spectogram(fr, ti, sp)

