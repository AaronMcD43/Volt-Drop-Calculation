# Volt-Drop-Calculation
This program calculates the sending end voltage required to maintain the load voltage after a voltage drop on a Transmission system.

![](/images/PowerSys.PNG)

Using Object Oriented Programming I created class for the Transformer, cable and the Load on the system. 

 # Inputs
 ## System Inputs
 *  Sending end Reference Voltage
 *  Recieving End Voltage Level
 *  Voltage reference for the calculations of current and impedance

  ## Input the class attributes
 * Transformer (Resistance, Reactance, High Voltage, Low Voltage)
 * Cable (Resistance, Reactance, Length, Connected Voltage)
 * Load (Power(MW), Power Factor, Connected Voltage)
 
 #  Outputs
 * Load Current measured at the recieving end voltage
 * Load Current measured at the sending end voltage
 * Total System impedence viewed from the Sending end voltage reference
 * Voltage difference from the Sending end voltage
