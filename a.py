
#TODO: This code Generating and Plotting Analog and Digital Signals


import numpy as np  #INFO: providing powerful numerical computation tools like arrays and linear algebra functions.
import matplotlib.pyplot as plt #INFO: for creating visualizations.



#info: np.linspace(start, stop, num): 
# info: Generates an array of evenly spaced values between start (inclusive) and stop (exclusive) with num elements.
t = np.linspace(0, 1, 1000)  #NOTE: Create Time vector from 0 to 1 second with 1000 points



#info: Generate an analog signal (sine wave)
frequency = 5  #NOTE: Initial Frequency of sine wave in Hz (cycles per second)
analog_signal = np.sin(2 * np.pi * frequency * t)  #NOTE:Generates the analog signal, a sine wave 
#NOTE: 2 * np.pi: Represents 2π , frequency * t : Represents the angular frequency



#info: Convert the analog signal to a digital signal (binary 0 or 1) 
digital_signal = np.where(analog_signal > 0, 1, np.where(analog_signal < 0, -1, 0))
#NOTE: np.where(condition, x, y): Returns x if condition is True, else y.
#NOTE: If analog_signal > 0, set digital_signal to 1
#NOTE: If analog_signal < 0, set digital_signal to -1
#NOTE: If analog_signal = 0, set digital_signal to 0



#info: Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 6))
#NOTE: Create a figure (fig) & gride of subplots 2x1 with size 10x6 (axs)



#info: Plotting the Analog Signal
axs[0].plot(t, analog_signal, label='Analog Signal', color='g') 
#NOTE: set the frist subplot(top one)=> axs[0]
axs[0].set_title('Analog Signal') 
#NOTE: Set the title of the frist subplot
axs[0].set_xlabel('Time (s)') 
#NOTE: Set the x-axis label of the frist subplot
axs[0].set_ylabel('Amplitude')
#NOTE: Set the y-axis label of the frist subplot
axs[0].axhline(0, color='black', linewidth=0.5, linestyle='--') 
#NOTE: Add a horizontal line at y=0 to the frist subplot
axs[0].grid() 
#NOTE: Add gridlines to the plot of the frist subplot
axs[0].legend()
#NOTE: Show the legend of the frist subplot



#info: Plotting the Digital Signal
axs[1].step(t, digital_signal, label='Digital Signal', where='post', color='r')
#NOTE: set the second subplot(bottom one)=> axs[1]
axs[1].set_title('Digital Signal')
#NOTE: Set the title of the second subplot
axs[1].set_xlabel('Time (s)') 
#NOTE: Set the x-axis label of the second subplot
axs[1].set_ylabel('Amplitude')
#NOTE: Set the y-axis label of the second subplot
axs[1].axhline(0, color='black', linewidth=0.5, linestyle='--')
#NOTE: Add a horizontal line at y=0 to the second subplot
axs[1].grid()
#NOTE: Add gridlines to the plot of the second subplot
axs[1].legend() 
#NOTE: Show the legend of the second subplot



#info: Show plots
plt.tight_layout() #NOTE: Adjusts the spacing between subplots to prevent overlapping
plt.show() #NOTE: Displays the final plot, combining both the analog and digital signal plots


