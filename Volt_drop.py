# This program calculates the sending end voltage from a system.
import math
import cmath
import numpy as np

try:
    # 11000  # Sending End Voltage Level
    VS_L_L = int(
        input("Please Enter the Sending End Voltage in units of volts: "))
    # 400# Recieving End Voltage Level
    VR_L_L = int(
        input("Please Enter the Recieving End Voltage in units of volts: "))
    # 11000  # the current and impedance at this voltage level
    Vref = int(input(
        "Please Enter the Voltage at which the current and impedance will be refeered to in units of volts: "))
except ValueError as e:
    print("Error reading inputs: %s" % e)

VS_Ph = VS_L_L/math.sqrt(3)
VR_Ph = VR_L_L / math.sqrt(3)


class Transformer():

    def __init__(self, R, X, HV, LV):
        self.R = R
        self.X = X
        self.HV = HV
        self.LV = LV
        self.Z = complex(self.R, self.X)


class Cable():

    def __init__(self, R, X, Length, V):
        self.R = R
        self.X = X
        self.Length = Length
        self.V = V

    def Total_Z(self):  # If I apply this method the R and X will be converted to Total R and Total X
        self.RM = self.R * self.Length
        self.XM = self.X * self.Length
        return complex(self.RM, self.XM)


class Load():

    def __init__(self, MW, pf, V_L_L):
        self.MW = MW
        self.pf = pf
        self.V_L_L = V_L_L
        self.MVA = MW * pf
        self.loadang = math.acos(self.pf)

    def Calc_I(self):
        self.I = (self.MW*self.pf)/(3*(self.V_L_L/math.sqrt(3)))
        return self.I


# Section were you create you create your system components
Transformer_1 = Transformer(0, 2, VS_L_L, VR_L_L)
cable_1 = Cable(3, 7, 1, VS_L_L)
cable_2 = Cable(0.01, 0.005, 1, VR_L_L)
Load_1 = Load(250000, 1, 400)

# Calculated the impedance of the system for the reference voltage Vref (set as the variable above)
z1 = cable_1.Total_Z() * (Vref/cable_1.V)**2
z2 = Transformer_1.Z * (Vref/Transformer_1.HV)**2
z3 = cable_2.Total_Z() * (Vref/cable_2.V)**2
Zt = z1 + z2 + z3  # Total Z in the system at the reference voltage

# Calculate the Load currents
I_400 = Load_1.Calc_I()  # Load current at the voltage the load is connected to
# load current seen from the HV of the network
I_11000 = Load_1.Calc_I()*(Load_1.V_L_L/VS_L_L)

# Calculate the Voltage Drops
IRZT = I_11000*(Zt)
Act_VS_Ph = math.sqrt((VS_Ph + IRZT.real)**2 + IRZT.imag**2)
# actual Sending End Voltage with that load and system of impedances
Act_VS_L_L = Act_VS_Ph*math.sqrt(3)
volt_diff = Act_VS_L_L - VS_L_L

print("The Load current measured at the load is {:.2f} A".format(I_400))
print("The Load current measured on the HV side is {:.2f} A".format(I_11000))
print("The Impedance of system with reference to Vref {:.2f} Ohms".format(Zt))
print("The Voltage drop of the system {:.2f} V".format(volt_diff))

