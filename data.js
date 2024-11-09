console.log(test())

# can you do a for year in range
function test(c02_growth_rate) {
    C02_ppm = (37.4 + c02_growth_rate*year)/2.13; radiating_force = 5.35*log(C02_ppm/280); temperature_change = radiating_force*3;
    glacier_volume_change = temperature_change*.055*30000000; thermal_expansion: 1335000000*1.51*temperature_change;
    height_gained = glacier_volume_change/1335000000 + thermal_expansion/139000000
    return height_gained
}