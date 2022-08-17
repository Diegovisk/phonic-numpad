def play_key_sound(key, duration=0.3):
    import pyaudio
    import numpy as np

    mapping = {
        "1": (697, 1209),
        "2": (697, 1336),
        "3": (697, 1477),
        "4": (770, 1209),
        "5": (770, 1336),
        "6": (770, 1477),
        "7": (852, 1209),
        "8": (852, 1336),
        "9": (852, 1477),
        "0": (941, 1336),
        "*": (941, 1209),
        "#": (941, 1477),
    }

    p = pyaudio.PyAudio()

    volume = 0.5            # range [0.0, 1.0], modifies our signal amplitude
    fs = 8000              # sampling rate, Hz, must be integer
    f1 = mapping[key][0]    # sine frequency, Hz, may be float
    f2 = mapping[key][1]    # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    wave1 = (np.sin(2*np.pi*np.arange(fs*duration)*f1/fs)).astype(np.float32)
    wave2 = (np.sin(2*np.pi*np.arange(fs*duration)*f2/fs)).astype(np.float32)

    samples = wave1 + wave2

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(samples*volume)

    stream.stop_stream()
    stream.close()

    p.terminate()
