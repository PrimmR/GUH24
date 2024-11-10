console.log(test(10, 60, 450))


function test(c02_growth_rate, timescale, deforestation_rate) {
    C02_ppm = (( 37.4*c02_growth_rate*timescale - (7.6 - (7.6/4000)*deforestation_rate*timescale))*0.7)/2.13; radiating_force = 5.35*Math.log((C02_ppm+419.3)/280); temperature_change = radiating_force*3;
    glacier_volume_change = temperature_change*.055*30000000; thermal_expansion= 1335000000*0.000214*temperature_change;
    height_gained = (glacier_volume_change/1335000000 + thermal_expansion/139000000)
    return height_gained
}