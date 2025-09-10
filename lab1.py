import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

frequency = 35
Fs = 200
duration = 1
samples = int(Fs * duration)

delta_T = 1 / Fs
t = np.arange(0, duration, delta_T)
sin_signal = 5 * np.sin(2 * np.pi * frequency * t)

fft_result = np.abs(np.fft.rfft(sin_signal)) / (samples / 2)
frequencies = np.fft.rfftfreq(samples, delta_T)

fig1, ax1 = plt.subplots(2, 1)
ax1[0].plot(t, sin_signal)
ax1[0].set_title("Синусоида во времени")
ax1[0].set_xlabel("Время (с)")
ax1[0].set_ylabel("Амплитуда")
ax1[0].grid(True)

ax1[1].plot(frequencies, fft_result)
ax1[1].set_title("Спектр синусоиды")
ax1[1].set_xlabel("Частота (Гц)")
ax1[1].set_ylabel("Амплитуда")
ax1[1].grid(True)

fig1.suptitle("Генерация синусоидального сигнала")

df_time = pd.DataFrame({"t": t, "sin_signal": sin_signal})
df_freq = pd.DataFrame({"frequencies": frequencies, "fft_result": fft_result})
df_1 = pd.concat([df_time, df_freq], axis=1)
df_1.to_csv("sin.csv")

df_2 = pd.read_csv("sin.csv", index_col=0)

fig2, ax2 = plt.subplots(2, 1)
ax2[0].plot(df_2["t"], df_2["sin_signal"])
ax2[0].set_title("Синусоида из CSV")
ax2[0].set_xlabel("Время (с)")
ax2[0].set_ylabel("Амплитуда")
ax2[0].grid(True)

ax2[1].plot(df_2["frequencies"], df_2["fft_result"])
ax2[1].set_title("Спектр из CSV")
ax2[1].set_xlabel("Частота (Гц)")
ax2[1].set_ylabel("Амплитуда")
ax2[1].grid(True)

fig2.suptitle("Графики по данным из CSV")

print("Поиск SDR...")
serial_numbers = RtlSdr.get_device_serial_addresses()
if not serial_numbers:
    print("RTL-SDR не найден, пропускаем часть с железом.")
else:
    print("Найдено устройство:", serial_numbers)
    sdr = RtlSdr(RtlSdr.get_device_index_by_serial(serial_numbers[0]))
    sdr.sample_rate = 2.4e6
    sdr.center_freq = 95e6
    sdr.gain = 4
    samples = sdr.read_samples(256*1024)
    sdr.close()

    df_sdr = pd.DataFrame({
        "real": samples.real[:2048],
        "imag": samples.imag[:2048]
    })
    df_sdr.to_csv("sdr_samples.csv")

    fig3, ax3 = plt.subplots(2, 1)
    ax3[0].plot(samples.real[:1024])
    ax3[0].plot(samples.imag[:1024])
    ax3[0].legend(["Действительная", "Мнимая"])
    ax3[0].set_title("RTL-SDR сигнал (временная область)")
    ax3[0].set_xlabel("Отсчеты")
    ax3[0].set_ylabel("Амплитуда")

    ax3[1].psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    ax3[1].set_title("RTL-SDR спектр (PSD)")
    ax3[1].set_xlabel("Частота (МГц)")
    ax3[1].set_ylabel("Мощность (дБ)")

    fig3.suptitle("Данные с RTL-SDR")

plt.show()