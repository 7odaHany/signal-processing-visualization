
#TODO:  convert a signal from the frequency domain back to the time domain


import numpy as np #INFO: providing powerful numerical computation tools like arrays and linear algebra functions.
import matplotlib.pyplot as plt #INFO: for creating visualizations.



#INFO: To convert a signal from the frequency domain back to the time domain
def to_time_domain(frequency_domain):
    return np.fft.ifft(frequency_domain)
    #NOTE: convert a signal from the frequency domain to the time domain using the Inverse Fast Fourier Transform
    
    
#TODO: Plot the reconstructed signal
def plot_reconstructed_signal(time, reconstructed_signal):
    plt.figure(figsize=(8,4)) 
    #INFO: Create a figure with size 8x4
    plt.plot(time,np.real(reconstructed_signal))
    #INFO: Plot the reconstructed signal
    plt.title('Reconstructed Signal from Frequency Domain')
    #INFO: Set the title of the plot
    plt.xlabel('Time (s)')
    #INFO: Set the x-axis label of the plot
    plt.ylabel('Amplitude')
    #INFO: Set the y-axis label of the plot
    plt.grid(True)
    #INFO: Add gridlines to the plot
    plt.show()
    #INFO: Display the plot



#FIXME: Example of Signal Reconstruction using FFT and IFFT
sample_rate = 1000      #INFO: sample rate in Hz  initialy set 1000 Hz
duration = 1            #INFO: Signal duration in seconds initialy set 1 second
t = np.linspace(0, duration, sample_rate, endpoint=False)
                        #INFO: Create a sample signal in the time domain


#BUG: Generating sample frequency domain representation (e.g., two sine waves)
frequency1 = 5      #INFO: Frequency of the first sine wave in Hz
frequency2 = 15     #INFO: Frequency of the second sine wave in Hz
amplitude1 = 1      #INFO: Amplitude of the first sine wave 
amplitude2 = 0.5    #INFO: Amplitude of the second sine wave

#BUG: Generate the frequency domain (complex values) of the signal
freq_domain = np.zeros(sample_rate, dtype=complex)
freq_domain[int(frequency1)] = amplitude1  #Info: Add the first sine wave to the frequency domain
freq_domain[int(frequency2)] = amplitude2  #Info: Add the second sine wave to the frequency domain

#BUG: Convert back to the time domain
reconstracted_signal = to_time_domain(freq_domain)

#TODO: Plot the reconstructed signal
plot_reconstructed_signal(t, reconstracted_signal)