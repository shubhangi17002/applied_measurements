import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'font.size': 14})
plt.rcParams['lines.linewidth'] = 3
pi=np.pi

ME 3264 - Applied Measurements Laboratory
=====================================

Lab #2 - Heat Pipe
=====================================

## Objective
The objectives of this laboratory are :

1. Understand the heat transfer characteristics of a heat pipe
2. Observe the thermal response time of a heat pipe in comparison to a copper rod
3. Measure the response time and temperature profile along the heat pipe
4. Calculate the effective thermal conductivity of the heat pipe and compare it with high thermal conductivity materials

## Background

A heat pipe is a passive heat transfer device that can transfer energy with a much smaller temperature drop as compared to high thermal conductivity materials such as copper. Heat pipe devices combine the principles of thermal conductivity and phase transition to effectively transfer bewtween two solid interfaces.


### Working principle of heat pipe

In general, heat pipes consist of a shell (wall), a wick and a small amount of working fluid, as shown in Fig. 1. Typically, three sections can be identified in a heat pipe: the evaporator, the condenser, and the adiabatic sections. 

The evaporator section absorbs heat from a high temperature source and vaporizes the working fluid inside. The vapor then flows through the adiabatic section and condenses at the condenser section, releasing its latent heat of condensation to a low temperature source. The condensed liquid returns to the evaporator through the wick driven by capillary force (Fig. 1). A wickless heat pipe that relies on gravity to return the condensate to the evaporator section is called a thermosyphon.

<center><img src="./HPAnimation.gif" alt="Drawing" style="width: 400px;"/> </center>
<center>Figure 1:  Working principle of heat pipe  </center>

### Benefits and limitations

Benefits of heat pipes:
- Heat pipes have high effective thermal conductivities which allows them to transfer heat over long distances, with minimal temperature drop.
- Passive operation. No moving parts, and require no energy input other than heat to operate.
- Isothermal operation.  Very isothermal surfaces, with temperature variations as low as ± 5 mK.
- Long life with no maintenance. No moving parts that could wear out. The vacuum seal prevents liquid losses, and protective coatings can give each device a long-lasting protection against corrosion.
- Lower costs. By lowering the operating temperature, these devices can increase the Mean Time Between Failure (MTBF) for electronic assemblies.  In turn, this lowers the maintenance required and the replacement costs.  In HVAC systems, they can reduce the energy required for heating and air conditioning, with payback times of a couple of years.

The heat transfer capability of a heat pipe is not unlimited. There are several mechanisms that cause this limitation. For a wicked heat pipe in which the return of liquid to the condenser section relies on capillary action of the wick, the most important limitation is the capillary limit. The capillary limit is encountered when the wick is not capable of producing enough pressure to pump the liquid from the condenser back to the evaporator. When this heat transfer limitation is reached, the evaporator temperature will increase sharply because there is not enough liquid in the wick structure to evaporate and absorb this heat input.


### Effective length and thermal conductivity of heat pipe

Assuming 1-D heat conduction through a rod of length $L(m) $ and conductivity $k (W/m.K)$, the heat flux $\bar{q} (W/m^2)$ can be expressed using Fourier's law of heat conduction [2]

$\small \bar{q} = -k \nabla T$  (1)

where, $\nabla T$ is the 1-D temprature gradient . The minus sign in Eqn(1) indicates that the heat is always transferred in the direction of decreasing temperature. Further assuming linear temperature profile across the rod, Eqn(1) can be written as 

$\small \bar{q} = k\frac{\Delta T}{L}$   (2)

In order to quantify the performance of a heat pipe and compare it with other heat transfer devices, the concept of effective thermal conductivity, $k_{eff}$, is introduced. Effective thermal conductivity is a conductivity that an imaginary rod with the same diameter as the HP must have to be able to transfer the same amount of heat as the heat pipe over a distance equal to the adiabatic section length of the heat pipe plus half of the evaporator and condenser section lengths, $L_{eff}$. This length is usually called the effective length of heat transfer and defined as, 

$\small L_{eff} = \frac{L_e}{2} + L_a + \frac{L_c}{2}$   (3)

where ${L_e}$, $L_a$ and ${L_c}$ are the lengths of evaporator, adiabatic and condesor section of the heat pipe, respectively. 

The thermal resistance, $R$, of such an imaginary rod is [7,8]

$R = R_{HP} = \frac{L_{eff}}{k_{eff} q_{HP}} = \frac{T_{e, ave}-T_{c, ave}}{q_{HP}} $  (4)

Applying the analogy of conductive heat transfer Eqn (2) to heat pipe, 

$\small \bar{q_{HP}} = k_{eff}  \frac{\Delta T_{HP}}{L_{eff}}$   (5)

$\small \bar{q_{HP}} = k_{eff}  \frac{(T_{e, ave}-T_{c, ave})}{L_{eff}}$   (6)

where, $\bar{q_{HP}}$ is the heat flux applied to heat pipe, $k_{eff}$ is the effective thermal conductivity , $L_{eff}$ is the effective length, $T_{e, ave}$ is the average temperature of evaporator section, $T_{c, ave}$ is the average temperature of condenser section of heat pipe at steady state.

For the heat pipe with cross section $A_c = \pi \frac{D^2}{4}$ of outer diameter $D$, and applied heat input $q_{HP} (W)$, the $k_{eff}$ can be obatined as,

$\small k_{eff} = \frac {(\frac{L_e}{2} + L_a + \frac{L_c}{2})  q_{HP}}{(T_{e, ave}-T_{c, ave}) A_c}$  (7)


#### Problem 1 

The heat input of 3W is applied to evaporator end of the heat pipe. [3watt_heat_pipe.csv](3watt_heat_pipe.csv) contains the measured temprature data from thermocouples (TC1-TC7) embedded in evaporator and condenser section of the heat pipe. 
1. Use this data to produce a graph that shows the variations of the average in evaporator and condenser temperatures with time
2. Calcualte $k_{eff}$ of the heat pipe

# Read csv file and process the data
data = pd.read_csv('3watt_heat_pipe.csv',skip_blank_lines=True)     # read csv file
data =data.dropna()   # removes blank rows from csv file
data.head(5)   # display first 5 rows in the data 

# Creating new column for elapsed time from the first date_time column
data['Time'] = pd.to_datetime(data['Time'])  # change datatype of column to datetime

# add Time_elapsed column , sec
position = data.columns.get_loc('Time')
data['Time_elapsed'] =  data.iloc[1:, position] - data.iat[0, position]  
data['Time_elapsed'] = data.Time_elapsed.dt.total_seconds() 

data.head(5)  # First row for Time_elapsed is not defined

# Plot average  evaporator and condenser temperatures
plt.figure()
Tavg_c = np.array((data['Temperature'].values + data['Temperature_0'].values +data['Temperature_1'].values+data['Temperature_2'].values)/4)
Tavg_e = np.array((data['heat A'].values + data['heat B'].values+data['heat C'].values)/3)
plt.plot(data['Time_elapsed'].values, Tavg_e ,'-r', label='Tavg_evaporator')
plt.plot(data['Time_elapsed'].values, Tavg_c ,'-b',label='Tavg_condensor')
plt.legend()

plt.xlabel('time,s')
plt.ylabel('T (deg C)')


# Calculate effective thermal conductivity

def k_eff(L_eff, q_hp, D, Tavg_e, Tavg_c):
    '''returns the effective conductivity given 
    Le,La,Lc, q_hp, D,Tavg_c, T_avge'''
    k_eff = L_eff*q_hp/(Tavg_e - Tavg_c)/(pi*D**2/4)
    return k_eff


# Average temp at steady state, avergae of last 2 minute

Te = np.mean(Tavg_e[-120:-1])   # numpy back indexing, -1 if for the last element
Tc = np.mean(Tavg_c[-120:-1])

L_eff = 0.2 #m
D = 0.008 #m
q_hp = 3 # Watt

k_eff = k_eff(L_eff, q_hp, D, Te, Tc)

print("The effective conductivity of heat pipe is %1.2f W/m.K" %k_eff)

#### Check your work

Repeat the problem for $q_{Hp} = 9W $. Use the input data from - [9watt_heat_pipe.csv](9watt_heat_pipe.csv)
What is the $k_{eff}$ for this case?

## # enter your work here
k_eff =    #  W/m.K

import check_lab02 as p
p.check_p01(k_eff)


## Procedure 

The procedure and details of the experiment are included in a lab-handout [1].

[ME3264_Lab_2_Heat_Pipe.pdf](https://drive.google.com/file/d/1ZHPFokeADq2eiYQDQHjPDy2861DgZISD/view?usp=sharing)


## Notes on error propagation

The theory of error analysis gives a general formula for the uncertainty when a result is found by a calculation from a collection of measurements [4],. The formula is based on the idea of a first-order Taylor series expansion of functions of many variables. For a well behaved function $f(x,y,z,...)$
of the completely independent physical variables $x,y,z,...$ which have uncertainties $,\sigma_x,\sigma_y,\sigma_z,...$ then the uncertainty in the value of the result $\sigma_f$ is given by the formula:

$\sigma_f^2 = (\frac{\partial{f}}{\partial x})^2\sigma_x^2 + (\frac{\partial{f}}{\partial y})^2\sigma_y^2 + (\frac{\partial{f}}{\partial z})^2\sigma_z^2$   

For more details on error propagation refer to [ME 3264- Lab 1 - Heat Engine Notebook ](https://cooperrc.github.io/applied_measurements/lab_01/ME3264_Lab-01.html#lab-1-heat-engine)


## References 

1. [ME3264 Lab2 - Heat Pipe, Prof. Bryan W. Weber (Spring 2020)](https://drive.google.com/file/d/1ZHPFokeADq2eiYQDQHjPDy2861DgZISD/view?usp=sharing)
2. F.P.Incropera and D.P. Dewitt, Fundamentals of Heat and Mass Transfer, 7th Edition, Chapter 2.
3. [Heat pipe, Wikipedia](https://en.wikipedia.org/wiki/Heat_pipe)
4. [Notes on measurement uncertainties](https://drive.google.com/file/d/1WBDkb-9fM6Y-wmQF3pl28JAt8JReiKJl/view?usp=sharing)
5. [ME 3264- Lab 1 - Heat Engine Notebook ](https://cooperrc.github.io/applied_measurements/lab_01/ME3264_Lab-01.html#lab-1-heat-engine)
5. [Heat pipe .nl](http://www.heatpipe.nl/index.php?page=animation&lang=EN)
7. M. Mahdavi, S. Tiari, S. De Schampheleire, S. Qiu, Experimental study of the thermal characteristics of a heat pipe, Exp. Therm. Fluid Sci. 93 (2018) 292–304.
8. D.S. Naruka, R. Dwivedi, P.K. Singh, Experimental inquisition of heat pipe: performance evaluation for different fluids, Exp. Heat Transf. 33 (2020) 668–682.