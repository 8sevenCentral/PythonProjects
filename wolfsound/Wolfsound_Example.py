#!/usr/bin/env python3
import numpy as np
import soundfile as sf

sample_rate = 44100
time = np.arange(0, 2, 1/sample_rate) 
brass_like_sound = 0.5 * np.sin(2 * np.pi * 440 * time + 5 * np.sin(2 * np.pi * 440 * time))
sf.write('brass_like_sound.mp3', brass_like_sound, sample_rate)