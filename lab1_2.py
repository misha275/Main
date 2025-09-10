# Y(t)=A*sin(2*π*f*t+φ),
import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
import pandas as pd


frequency =  35# Частота сигнала (Гц)
Fs = 200 # Частота дискретизации (Гц)
duration =  1# Длительность сигнала (с)
samples = Fs * duration  # Количество отсчётов

delta_T = 1 / Fs  # Шаг дискретизации (с)
t = np.arange(0, duration, delta_T)  # Список из дискетных значений

sin_signal = 1 * np.sin(2 * np.pi * frequency * t)

#преобразование Фурье
fft_result = np.abs(np.fft.rfft(sin_signal)) / (samples / 2)
frequencies = np.fft.rfftfreq(samples, delta_T)

# Создаем новые области для построения графиков
fig1, ax1 = plt.subplots(2, 1)

# Первый график
ax1[0].plot(t, sin_signal)
ax1[0].set_title('Первый график')
ax1[0].set_xlabel('Ось Х')
ax1[0].set_ylabel('Ось Y')
ax1[0].grid(True)
# Второй график
ax1[1].plot(frequencies, fft_result)
ax1[1].set_title('Второй график')
ax1[1].set_xlabel('Ось Х')
ax1[1].set_ylabel('Ось Y')
ax1[1].grid(True)

# Общие настройки
fig1.suptitle('Графики генерируемого сигнала')
# Создание словарей
dictionary_time = {
    'sin_signal': sin_signal,
    't': t
}

dictionary_freq = {
    'fft_result': fft_result,
    'frequencies': frequencies
}

# Создание df
df_time = pd.DataFrame(dictionary_time)
df_freq = pd.DataFrame(dictionary_freq)

# Объединение df
df_1 = pd.concat([df_time, df_freq], axis=1)

df_1.to_csv('sin.csv')

df_2 = pd.read_csv('sin.csv', index_col=0)

# Создаем новые области для построения грфиков
fig2, ax2 = plt.subplots(2, 1)

# Первый график
ax2[0].plot(df_2['t'], df_2['sin_signal'])
ax2[0].set_title('Первый график')
ax2[0].set_xlabel('Ось Х')
ax2[0].set_ylabel('Ось Y')
ax2[0].grid(True)
#
# # Второй график
ax2[1].plot(df_2['frequencies'], df_2['fft_result'])
ax2[1].set_title('Второй график')
ax2[1].set_xlabel('Ось Х')
ax2[1].set_ylabel('Ось Y')
ax2[1].grid(True)

# Общие настройки
fig2.suptitle('Графики csv')


# Определение подключенных RTL-SDR
serial_numbers = RtlSdr.get_device_serial_addresses()

# Инициализируем подключенное RTL-SDR для дальнейшей работы
sdr = RtlSdr(RtlSdr.get_device_index_by_serial(serial_numbers[0]))

# Настройка устройства
sdr.sample_rate = 2.4e6
sdr.center_freq = 95e6
sdr.gain = 4

samples = sdr.read_samples(256*1024) # Счетчик отчетов
sdr.close()


# Построение графиков

fig, ax = plt.subplots(2, 1)

ax[0].plot(samples.real[:1024])
ax[0].plot(samples.imag[:1024])
ax[0].legend(["Действительное", "Мнимое"])
ax[0].set_title('Частотное представление')
ax[0].set_xlabel('Время')
ax[0].set_ylabel('Амплитуда')

ax[1].psd(samples, NFFT=1024, Fs=sdr.sample_rate / 1e6, Fc=sdr.center_freq / 1e6)
ax[1].set_title('Частотное представление')
ax[1].set_xlabel('Частоты (МГц)')
ax[1].set_ylabel('Мощность сигнала (дБ)')

# Создание словарей
dictionary_time1 = {
    'real_sample': samples.real[:1024],
    'imag_sample': samples.imag[:1024]
}


# Создание df
df_time = pd.DataFrame(dictionary_time1)

df_time.to_csv('sampleData.csv')

df_2 = pd.read_csv('sampleData.csv', index_col=0)

# Создаем новые области для построения грфиков
fig2, ax2 = plt.subplots(2, 1)

complex_spis = []

for i in range(1024):
    n_complex = complex(dictionary_time1['real_sample'][i], dictionary_time1['imag_sample'][i])
    complex_spis.append(n_complex)

# Первый график
ax2[0].plot(df_2['real_sample'])
ax2[0].plot(df_2['imag_sample'])
ax2[0].set_title('Первый график')
ax2[0].set_xlabel('Ось Х')
ax2[0].set_ylabel('Ось Y')
ax2[0].grid(True)


ax[1].psd(complex_spis, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
ax[1].set_title('Частотное представление')
ax[1].set_xlabel('Частоты (МГц)')
ax[1].set_ylabel('Мощность сигнала (дБ)')

plt.show()




