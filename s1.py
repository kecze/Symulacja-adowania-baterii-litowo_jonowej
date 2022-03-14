import matplotlib.pyplot as plt

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
    z = []
    while act_cap <= 0.8 * full_cap and time < ch_time:
        pow_used = power
        act_cap += pow_used * 1 / 60
        time += 1
        soc_v = (act_cap / full_cap) * 100
        x.append(time)
        y.append(pow_used)
        z.append(act_cap/full_cap * 100)
    while 0.8 * full_cap <= act_cap <= 1 * full_cap and time < ch_time:
        soc_v = (act_cap / full_cap) * 100
        #pow_used = power * (-0.01667 * soc_v ** 3 + 4.771 * soc_v ** 2 - 456.9 * soc_v + 14650)/100
        pow_used = power * (0.005333 * soc_v ** 3 - 1.306 * soc_v ** 2 + 100.4 * soc_v - 2306) / 100
        act_cap += pow_used * 1 / 60
        time += 1
        x.append(time)
        y.append(pow_used)
        z.append(act_cap / full_cap * 100)
    plt.subplot(2, 1, 1)
    plt.plot(x, y)
    plt.xlabel('time [min]')
    plt.ylabel('power [kW]')
    plt.subplot(2, 1, 2)
    plt.plot(x, z)
    plt.xlabel('time [min]')
    plt.ylabel('SOC [%]')
    print("after",ch_time,"minutes of charging SOC is",round(soc_v),"%")


charging(0, 40, 7, 960)

