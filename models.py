import math
Pontoon_height = 15
Pontoon_length = 120
Pontoon_breadth = 40
pon_thickness = 0.2

column_height = 15
column_diameter = 10
column_count = 6
col_thickness = 0.3

water_density = 1025 # kg/m3
steel_density = 7750 # kg/m3

####################

#COG_calculation  
Pontoon_cog  = Pontoon_height/2
column_cog = column_height/2
pontoon_area = Pontoon_height*Pontoon_length*Pontoon_breadth
column_area = column_diameter*column_height
pontoon_weight = pontoon_area*pon_thickness*steel_density
column_weight = column_area*col_thickness*steel_density
ballast_weight = 0
total_weight = pontoon_weight +column_weight + ballast_weight
pontoon_displacement  = Pontoon_height*Pontoon_length*Pontoon_breadth*water_density
column_displacement = 0
semi_total_weight = (total_weight - (pontoon_weight + ballast_weight))
total_draft = semi_total_weight /(math.pi*((column_diameter/2)**2))*water_density
print(semi_total_weight)
print(total_draft)

