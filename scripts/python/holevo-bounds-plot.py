#!/usr/bin/env python
"""\
This script plots the Holevo bounds
for the usual entanglement-based and device-independent
quantum key distribution protocols, for the sake of comparison.

Usage: holevo-bounds-plot.py
"""

# Author of the Python script
__author__      = "Ruben Andre Barreiro"

# Copyright of the Python script
__copyright__   = "Copyright 2024, Tecnico Lisboa, ULisboa"


# Import logarithm base 2 from mathematics built-in library
from math import log2

# Import square root from mathematics built-in library
from math import sqrt


# Import all the required functions from
# the PyPlot module of the MatPlotLib library
from matplotlib.pyplot import suptitle, title, xlabel, ylabel,\
                              xticks, xlim, ylim, plot,\
                              legend, gca, grid, show, savefig

# Import array range function from the NumPy library
from numpy import arange as array_range

# Import numerical array function from the NumPy library
from numpy import array as num_array

# Import numerical round function from the NumPy library
from numpy import round as num_round

# Import the float64 data type from the NumPy library
from numpy import float64



# Define a function to compute the binary entropy
def compute_binary_entropy(x_b):
    
    # If the input is zero or one
    if x_b == 0 or x_b == 1:
        
        # Return a null binary entropy
        return 0
    
    # Return the binary entropy on the given input
    return ( -x_b * log2(x_b) - (1 - x_b) * log2(1 - x_b) )



# Define a function to compute the Holevo bound for
# the usual entanglement-based quantum key distribution protocol,
# on a given quantum bit error rate for the protocol
def compute_holevo_bound_usual_entanglement_based_qkd_protocol\
    (quantum_bit_error_rate):
    
    # Compute the input for the Holevo bound according to
    # the usual entanglement-based quantum key distribution protocol,
    # on the given quantum bit error rate for the protocol  
    input_holevo_bound = (1 - quantum_bit_error_rate)
    
    
    # Return the Holevo bound for the usual entanglement-based
    # quantum key distribution protocol, according to
    # the respective associated binary entropy
    return compute_binary_entropy(input_holevo_bound)


# Define a function to compute the Holevo bound for
# the device-independent quantum key distribution protocol,
# on a given quantum bit error rate for the protocol
def compute_holevo_bound_device_independent_qkd_protocol\
    (quantum_bit_error_rate): 
    
    # Compute the input for the Holevo bound according to
    # the device-independent quantum key distribution protocol,
    # on the given quantum bit error rate for the protocol  
    input_holevo_bound = \
        ( ( 1 + sqrt( ( ( 2 * sqrt(2) * \
                          ( 1 - 2 * quantum_bit_error_rate) ) \
                        / 2 )**2 - 1 ) ) / 2 )
            
    # Return the Holevo bound for the device-independent
    # quantum key distribution protocol, according to
    # the respective associated binary entropy  
    return compute_binary_entropy(input_holevo_bound)


# Create a numerical array within
# the range [0.0,0.148[ with a step of 0.002
quantum_bit_error_rates = array_range(0.0, 0.148, 0.002)


# Create an empty list for the Holevo bounds for
# the usual entanglement-based quantum key distribution protocol 
holevo_bounds_usual_entanglement_based_qkd_protocol = []

# Create an empty list for the Holevo bounds for
# the device-independent quantum key distribution protocol 
holevo_bounds_device_independent_qkd_protocol = []


# For each quantum bit error rate
# in the respective numerical array
for quantum_bit_error_rate in quantum_bit_error_rates:
    
    # Compute the Holevo bound for the usual
    # entanglement-based quantum key distribution protocol   
    holevo_bound_usual_entanglement_based_qkd_protocol = \
        compute_holevo_bound_usual_entanglement_based_qkd_protocol\
            (quantum_bit_error_rate)
            
    # Append the Holevo bound for the usual
    # entanglement-based quantum key distribution protocol    
    holevo_bounds_usual_entanglement_based_qkd_protocol\
        .append(holevo_bound_usual_entanglement_based_qkd_protocol)
    
    
    # Compute the Holevo bound for the device-independent
    # quantum key distribution protocol    
    holevo_bound_device_independent_qkd_protocol = \
        compute_holevo_bound_device_independent_qkd_protocol\
            (quantum_bit_error_rate)
    
    # Append the Holevo bound for the device-independent
    # quantum key distribution protocol
    holevo_bounds_device_independent_qkd_protocol\
        .append(holevo_bound_device_independent_qkd_protocol)


# Define the superior title for the plot of the Holevo bounds
suptitle(r"Holevo Bounds $\chi({B}_{1}:E)$",
         fontweight = "bold", fontsize = 14, y = 1.075)

# Define the main title for the plot of the Holevo bounds
title("Usual Entanglement-Based vs. Device-Independent\n" + 
      "Quantum Key Distribution Protocol")


# Define the label for the x-axis
# for the plot of the Holevo bounds
xlabel(r"Quantum Bit Error Rate ($Q$) in %",
       fontweight = "bold")

# Define the label for the y-axis
# for the plot of the Holevo bounds
ylabel(r"Holevo Bound $\chi({B}_{1}:E)$",
       fontweight = "bold")


# Plot the Holevo bounds' curve for the usual
# entanglement-based quantum key distribution protocol
plot(quantum_bit_error_rates,
     holevo_bounds_usual_entanglement_based_qkd_protocol)

# Plot the Holevo bounds' curve for the device-independent
# quantum key distribution protocol
plot(quantum_bit_error_rates,
     holevo_bounds_device_independent_qkd_protocol)


# Define the legend for the plot of the Holevo bounds
legend(["Usual Entanglement-Based",
        "Device-Independent"])


# Create the grid lines for the plot of the Holevo bounds
grid(linestyle = '--', linewidth = 0.5, alpha = 0.75)


# Re-define the ticks for the labels for the x-axis
# (in percentage) for the plot of the Holevo bounds
xticks( ticks = xticks()[0][1:],
        labels = num_round( 100 * num_array( xticks()[0][1:],
                                             dtype = float64 ),
                            2 ) )


# Retrieve the current axis of the plot of the Holevo bounds
current_axis = gca()

# Define the facecolor of the current
# axis of the plot of the Holevo bounds
current_axis.set_facecolor( (0.0, 0.0, 0.0, 0.075) )


# Define the limit range for the x-axis of
# the plot of the Holevo bounds
xlim(0.0, 0.1465)

# Define the limit range for the y-axis of
# the plot of the Holevo bounds
ylim(0.0, 1.0)


# Save the plot of the Holevo bounds
savefig("holevo-bounds-plot.png")


# Show the plot of the Holevo bounds
show()