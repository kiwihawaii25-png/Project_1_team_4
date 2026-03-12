# On a Wing and a Prayer

## Project Overview
This project estimates the deflection of an aircraft wing during flight using simplified aerodynamic and structural equations. The program calculates aerodynamic lift based on flight conditions and models the wing as a cantilever beam to estimate structural deformation.

The goal of this project is to demonstrate how aerodynamic forces, flight conditions, and material properties affect wing bending.

## Features
- Select from multiple aircraft types
- Choose different wing materials
- Input flight speed and altitude
- Calculates aerodynamic lift
- Estimates wingtip deflection
- Generates a graph showing wing bending along the span

## Equations Used
The program uses several engineering equations:
- Air Density (Standard Atmosphere Approximation)  
ρ = ρ₀ (1 − (Lh / T₀))^((g / (R·L)) − 1)
- Lift Equation  
L = 0.5 ρV²SCₗ
- Average Wing Chord  
c = S / b
- Wing Thickness Approximation  
h = c · t_f
- Moment of Inertia  
I = (b h³) / 12
- Distributed Lift Load  
q = L / b
- Cantilever Beam Deflection (Wingtip)  
δ = (qL⁴) / (8EI)
- Deflection Along the Wing  
y(x) = (w x² / (24EI)) (6L² − 4Lx + x²)
- Airspeed Conversion  
V = V_knots × 0.51444
- Structural Safety Check  
Deflection > 0.2L

## Inputs
The user provides:
- Aircraft type
- Wing material
- Airspeed (knots)
- Altitude (meters)

## Outputs
The program outputs:
- Total lift generated
- Estimated wingtip deflection
- Deflection values along the wing span
- A graph visualizing the wing bending

## Technologies Used
- Python
- Matplotlib
- Basic aerodynamics equations
- Beam deflection theory

## Authors
Group 4  
Kira Schweikert  
Jay Camp  
Jacob Henderson  
Alessandra Ozuna  
Aeryn Paet
Lucas Palya
