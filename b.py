
#TODO: This code Generating and Plotting Sine Wave


import numpy as np #INFO: providing powerful numerical computation tools like arrays and linear algebra functions.
import matplotlib.pyplot as plt #INFO: for creating visualizations.


# INFO:generates and plots a sine wave with user-defined parameters.
def draw_sine_wave(peak_amplitude, frequency, phase, duration=1):
    
    t = np.linspace(0, duration, 1000)  
    #NOTE: Create a Time Vector from 0 to (duration) seconds with 1000 points
    y = peak_amplitude * np.sin(2 * np.pi * frequency * t + phase)
    # NOTE: Calculate the Sine Wave using the formula: y(t) = A * sin(2πf * t + φ)
    plt.figure(figsize=(10, 5)) #NOTE: Create a figure with size 10x5
    plt.plot(t, y, label=f'Sine Wave\nAmplitude: {peak_amplitude}, Frequency: {frequency} Hz, Phase: {phase} radians')
    #NOTE: Plot the Sine Wave
    plt.title('Sine Wave') 
    #NOTE: Set the title of the plot
    plt.xlabel('Time (seconds)')
    #NOTE: Set the x-axis label of the plot
    plt.ylabel('Amplitude')
    #NOTE: Set the y-axis label of the plot
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    #NOTE: Add a horizontal line at y=0 to the plot
    plt.grid(True)
    #NOTE: Add gridlines to the plot
    plt.legend()
    #NOTE: Show the legend of the plot
    plt.xlim(0, duration)
    #NOTE: Set the x-axis limits of the plot
    plt.ylim(-peak_amplitude * 1.5, peak_amplitude * 1.5)
    #NOTE: Set the y-axis limits of the plot
    plt.show()
    #NOTE: Display the plot


#TODO: Generate and plot a sine wave 
peak_amplitude = 1.0    #NOTE: Peak Amplitude of the Sine Wave initially set to 1
frequency = 5.0         #NOTE: Frequency of the Sine Wave initially set to 5 Hz
phase = 0               #NOTE: Phase of the Sine Wave initially set to 0 radians

draw_sine_wave(peak_amplitude, frequency, phase)
#NOTE: Call the draw_sine_wave function to generate and plot the Sine Wave