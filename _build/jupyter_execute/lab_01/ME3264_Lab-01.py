import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


ME 3264 - Applied Measurements Laboratory
=====================================

Lab #1 - Heat Engine
=====================================

## Objective
The objectives of this laboratory are :

1. Determination of thermodynamic work done during a four-stage expansion and compression cycle by lifting masses from one height to another.
1. Compare the useful mechanical work and the net thermodynamic work done during a cycle as determined via a p-V diagram.

## Basic thermodynamics concepts
#### System
The system is whatever we want to study. It may be as simple as a free body or
as complex as an entire chemical refinery. Everything external to the system is considered to be part of the system’s surroundings.The system is distinguished from its surroundings by a specified boundary, which may be at rest or in motion. 

There are two basic kinds of systems - closed systems (control amss) and open systems (control volumes). A closed system refers to a fixed quantity of matter, whereas a control volume is a region of space through which mass may flow. For exmaple, a quantity of matter contained within a closed, rigid-walled tank is a closed system, while a pipeline through which natural gas flows can be considered as control volume. Closed systems are impermeable to mass but may be permeable to energy. When closed system are impermeable to both mass and energy transfer, the system is known as isolated system.

#### System property
To describe a system and predict its behavior requires knowledge of its properties
and how those properties are related. A property is a macroscopic characteristic of a
system such as mass, volume, energy, pressure, and temperature to which a numerical
value can be assigned at a given time without knowledge of the previous behavior
(history) of the system [2].

#### State
The word "state" refers to the condition of a system as described by its properties.
Since there are normally relations among the properties of a system, the state often
can be specified by providing the values of a subset of the properties. All other properties
can be determined in terms of these few [2].
#### Process and cycle
When any of the properties of a system changes, the state changes and the system
is said to undergo a process. If a system undergo sequence of processes that begins and ends at the same state, the system is said to complete thermodynamic cycle.


### First law of thermodynamics

The first law of thermodynamics is a version of the law of conservation of energy, adapted for thermodynamic processes, distinguishing two kinds of transfer of energy, as heat and as thermodynamic work, and relating them to a amount of energy contained within a system.

The energy balance can be expressed in symbols as:

$\Delta E = Q - W$   (1)

where $\Delta E$ is the change in amount of energy contained within a system, $Q$ is the net amount of energy
transferred in across the system boundary by heat transfer, and $W$ is the  net amount of energy transferred out across the system boundary by work during the time interval.

The total energy ($E$), is comprised of internal energy ($U$), kinetic energy ($KE$) and potential energy of the system ($PE$). Hence,

$\Delta E =\Delta KE+\Delta PE+\Delta U$   (2)

if the changes in KE and PE are negligible (i.e. $\Delta KE=0, \Delta PE=0$), such as in stationary piston-cylinder engine, the Eq (1) tranforms to Eq (3)

$\Delta U = Q - W$   (3)

### Mechanical and thermodynamic work

The mechanical work $W$ done by, or on, a system evaluated in terms of macroscopically observable
forces ($\vec{F}$) and displacements ($\vec{ds}$) is

$W =  \int_{s_1}^{s_2}\vec{F}.\vec{ds}$   (4)

Consider an example of a closed system consisting of a gas (or liquid) contained in a piston–cylinder assembly as the gas expands. During the process, the gas pressure exerts a normal force on the piston. A graphical representation of a system with pressure – volume diagram ($p-V$ ) diagram) is shown in Figure 1. 

<center><img src="./figure_01.png" alt="Drawing" style="width: 300px;"/> </center>
<center>Figure 1:  Work of a quasi-equillibrium expansion or compression process </center>

The The force exerted by the gas on the piston is simply the product $pA$, where $A$ is the area of the piston face. The work done by the system as the piston is displaced a distance $dx$ is

$\delta W = pA dx$  (5)

The product $A dx$ equals the change in volume of the system, $dV$. Thus,

$\delta W = p dV$  (6)

For a change in volume from $V_1$ to $V_2$, the thermodynamic work during the process is obtained by integrating Eq(6)

$W =  \int_{V_1}^{V_2}p dV$   (7)

Note: $\delta W$ is used for work instead of $dW$ since the differential of work ($W$) is inexact. Meaning, integral of $\delta W$ cannot be evaluated without specifying the details of the process unlike integral of state properties differentials such as $\delta V$.


### Work during the cycles

Consider the cycle shown in Figure 2. The cycle shown produces a net work output because the work done by the system during the expansion process (area under path A) is greater than the work
done on the system during the compression part of the cycle (area under path B), and the difference between these two is the net work done during the cycle (the colored area, $W_{cycle}$).

$W_{cycle} = \oint p dV =  \int_{V_1}^{V_2}p dV +  \int_{V_2}^{V_1}p dV$   (8)

<center><img src="./figure_02.png" alt="Drawing" style="width: 300px;"/> </center>
<center>Figure 2:  The net work done during a cycle is the difference between the work done
by the system and the work done on the system. </center>

### Problem 1

A gas in a piston–cylinder assembly undergoes an expansion process for which the relationship between pressure and volume is given by

$pV^n = constant$

The initial pressure is 3 bar, the initial volume is 0.1 m^3, and the final volume is 0.2 m^3. Determine the work for the process, in kJ, if (a) $n$ = 1.5, (b) $n$ = 1.0, and (c) $n$ = 0.




def integrand(V, n, const):
    '''function to return the work done in polytropic process :
    pV^n = const (this could be replaced with appropriate expressions for other processes)
    This function integrates the integrand from V1 to V2 '''
    W = const/V**n
    return W

n = 1.5

V1 = 0.1 # m^3
V2 = 0.2 # m^3
p1 = 3 # bar
const = p1*10**5*V1**n
p2 = const/(V2**n)

W = quad(integrand, V1, V2, args=(n, const))
print("The work done during process, W = %1.2f kJ " %(W[0]/1000))



#### Check your work
P1. What is the work done during the process in the above exmaple if $n$ = 1.4 , initial pressure is $5 bar$, the initial volume is $0.05 m^3$ ?



# enter your work here

n = 

V1 =  # m^3
V2 =  # m^3
p1 =  # bar
const = 
p2 = 

W = # work output in J
answer = W[0]/1000  # work output in kJ
print("The work done during process, W = %1.2f kJ " %answer)


import check_lab01 as p
p.check_p01(answer)

P2. Consider a heat engine cycle in Figure 3. Heat engine is a system that converts heat or thermal energy to mechanical work.
For the cycle in Figure 3, $V_1= 0.1 m^3$, $p1 = 3 bar$ , $V_2= 0.3 m^3$ $p3 = 1 bar$

<center><img src="./figure_03.svg" alt="Drawing" style="width: 300px;"/> </center>
<center>Figure 3:  p-V diagram of a cycle </center>

What is the net work outout from the cycle ?

# enter your work here
p1 =  # bar
V1 =  #m^3
p3 =  # bar
V2 = #m^3

answer =  # area under the p-V curve
print(answer)  # total work in kJ
print("The work done during cycle, W = %1.2f kJ " %(answer))

import check_lab01 as p
p.check_p02(answer)



## Procedure 

The procedure and details of the experiment are included in a lab-handout [3].

[ME3264_Lab_1_Heat_Engine.pdf](https://drive.google.com/file/d/1Rs5Y2JRM6zzzr3pvoqTJID6fvxpyuCTx/view?usp=sharing)


## Notes on error propagation

The theory of error analysis gives a general formula for the uncertainty when a result is found by a calculation from a collection of measurements [4],. The formula is based on the idea of a first-order Taylor series expansion of functions of many variables. For a well behaved function $f(x,y,z,...)$
of the completely independent physical variables $x,y,z,...$ which have uncertainties $,\sigma_x,\sigma_y,\sigma_z,...$ then the uncertainty in the value of the result $\sigma_f$ is given by the formula:

$\sigma_f^2 = (\frac{\partial{f}}{\partial x})^2\sigma_x^2 + (\frac{\partial{f}}{\partial y})^2\sigma_y^2 + (\frac{\partial{f}}{\partial z})^2\sigma_z^2$   (9)

For example, in this experiment, we are using external weights ($mg$) to compress volume of gas in the cylinder by height $h$. Work done by the force is:

$W = mgh$  (10)

where, $g$ is the gravitational accleration. Using Eq(9), the $\sigma_W$ is obtained as:

$\sigma_W^2 = (\frac{\partial{W}}{\partial m})^2\sigma_m^2 + (\frac{\partial{W}}{\partial g})^2\sigma_g^2 + (\frac{\partial{W}}{\partial h})^2\sigma_h^2$   (11)


Note : 

- In Eq (11), for constant g , $\sigma_g = 0$
- It's a standard practice to use standard deviation as uncertainty in the measurement when multipe measurements are availabe 
- If the measurement is made only once or if you get the same measurement a few times, the minimum uncertainty can be approximated with the value of the least significant digit (least-count) of the measurement display [\[5\]](http://www.phys.lsu.edu/classes/phys2108/2108_measA.pdf). This is a more conservative way of accounting for uncertainties as you are assuming all sources of error are much smaller than the device's uncertainty. 


## References 
1. [First law of thermodynamics, Wikipedia](https://en.wikipedia.org/wiki/First_law_of_thermodynamics).
2. M.J. Moran and H.N. Shapiro, Fundamentals of Engineering Thermodynamics, Eighth Edition, Chapter 2.
3. ME3264 Lab1 - Heat Engine, Prof. Bryan W. Weber (Spring 2020)
4. [Notes on measurement uncertainties](https://drive.google.com/file/d/1WBDkb-9fM6Y-wmQF3pl28JAt8JReiKJl/view?usp=sharing)
5. [Introduction to Measurement and Data Analysis Notes](http://www.phys.lsu.edu/classes/phys2108/2108_measA.pdf)