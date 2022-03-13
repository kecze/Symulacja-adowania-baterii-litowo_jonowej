import pandas as df

# full_cap - max capacity of the car
# SOC - actual at the beginning of charging
# c h_time - time that we have [min]
# power - max power of the charger
# time - time spend at the charging point
# act_cap - actual capacity


def charging(soc, full_cap, power, ch_time):
    act_cap = soc/100 * full_cap
    time = 0
    x = []
    y = []
    while act_cap <= 0.8 * full_cap and time < ch_time:
        pow_used = power
        act_cap += pow_used * 1 / 60
        time += 1
        soc_v = (act_cap / full_cap) * 100
        x.append(time)
        y.append(pow_used)
    while 0.8 * full_cap <= act_cap <= 1 * full_cap and time < ch_time:
        soc_v = (act_cap / full_cap) * 100
        pow_used = power * (-0.01667 * soc_v ** 3 + 4.771 * soc_v ** 2 - 456.9 * soc_v + 14650)/100
        #pow_used = power * (-0.013333 * soc_v ** 3 + 3.9 * soc_v ** 2 - 381.2 * soc_v + 12460) / 100
        act_cap += pow_used * 1 / 60
        time += 1
        x.append(time)
        y.append(pow_used)
    df.plot(x,y)
    print("po",ch_time,"minutach ładowania SOC będzie wynosiło",round(soc_v),"%")


charging(0, 40, 7, 480)
