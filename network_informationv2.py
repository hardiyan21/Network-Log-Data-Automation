myfile = open("/home/rama/Downloads/EBR.BRN.2", "rt")
contents = myfile.read()

def hostname():
    # Get hostname
    start_content = (contents.find('Hostname: '))
    f_host = contents[start_content:(start_content + 22)].replace("\n", "")
    print("--------------------------")
    print("Hostname has been found !!!")
    print(f_host)
    print("--------------------------")
    myfile.close()

def version():
    # Get version of Junos
    start_content = (contents.find('Junos: '))
    f_ver = contents[start_content:(start_content + 16)].replace("\n", "")
    print("--------------------------")
    print("Version has been found !!!")
    print(f_ver)
    print("--------------------------")
    myfile.close()

def chassis_part1():
    # Get model of Juniper chassis
    start_content = (contents.find('Model: '))
    f_chas = contents[start_content:(start_content + 13)].replace("\n", "")
    print("--------------------------")
    print("Chassis model has been found !!!")
    print(f_chas)
    print("--------------------------")
    f_sn = f_chas[7:13]

    # Get Serial Number of Juniper chassis
    print("--------------------------")
    print("Chassis SN has been found !!!")
    sn_format = ('{} chassis, serial number '.format(f_sn))
    sn_content = (contents.find(sn_format))
    g_sn = contents[sn_content:(sn_content + 41)]
    print(g_sn)
    print("--------------------------")
    myfile.close()

def chassis_part2():
    # Get chassis environment
    start_content = (contents.find('Routing Engine 0 CPU '))
    f_chas = contents[start_content:(start_content + 55)].replace("\n", "")
    print("--------------------------")
    print("RE status has been found !!!")
    print(f_chas)
    start2_content = (contents.find('Routing Engine 1 CPU '))
    f_chas2 = contents[start2_content:(start2_content + 55)].replace("\n", "")
    print(f_chas2)
    print("--------------------------")
    myfile.close()

def chassis_part3():
    # Get thresholds chassis temp
    start_content = (contents.find('show chassis temperature-thresholds'))
    f_thr = contents[start_content:(start_content + 430)].replace("\n", "")
    print("--------------------------")
    print("Chassis Thresholds has been found !!!")

    # Print Minimum thresholds
    min = f_thr[416:418]
    max = f_thr[422:424]
    print("Minimum thresholds: {} C".format(min))
    print("Maximum thresholds: {} C".format(max))
    print("--------------------------")
    myfile.close()

def fan():
    # Get fan detail
    start_content = (contents.find('Top Fan Tray Temp'))
    start_content2 = (contents.find('Bottom Fan Tray Temp'))
    f_fan = contents[start_content:(start_content + 54)].replace("\n", "")
    f_fan2 = contents[start_content2:(start_content2 + 54)].replace("\n", "")
    print("--------------------------")
    print("Fan detail has been found !!!")
    top = f_fan[42:44]
    bottom = f_fan2[42:44]
    print("Top Fan Tray Temp: {} C".format(top))
    print("Bottom Fan Tray Temp: {} C".format(bottom))
    print("\t")

    #Fan top spinning detail
    start_top_tray_fan1 = (contents.find('Top Tray Fan 1'))
    f_top_tray_fan1 = contents[start_top_tray_fan1:(start_top_tray_fan1 + 66)].replace("\n", "")
    Top_1 = f_top_tray_fan1[54:66]
    print("Top Tray Fan 1 at {}".format(Top_1))

    start_top_tray_fan2 = (contents.find('Top Tray Fan 2'))
    f_top_tray_fan2 = contents[start_top_tray_fan2:(start_top_tray_fan2 + 66)].replace("\n", "")
    Top_2 = f_top_tray_fan2[54:66]
    print("Top Tray Fan 2 at {}".format(Top_2))

    start_top_tray_fan3 = (contents.find('Top Tray Fan 3'))
    f_top_tray_fan3 = contents[start_top_tray_fan3:(start_top_tray_fan3 + 66)].replace("\n", "")
    Top_3 = f_top_tray_fan3[54:66]
    print("Top Tray Fan 3 at {}".format(Top_3))

    start_top_tray_fan4 = (contents.find('Top Tray Fan 4'))
    f_top_tray_fan4 = contents[start_top_tray_fan4:(start_top_tray_fan4 + 66)].replace("\n", "")
    Top_4 = f_top_tray_fan4[54:66]
    print("Top Tray Fan 4 at {}".format(Top_4))

    start_top_tray_fan5 = (contents.find('Top Tray Fan 5'))
    f_top_tray_fan5 = contents[start_top_tray_fan5:(start_top_tray_fan5 + 66)].replace("\n", "")
    Top_5 = f_top_tray_fan5[54:66]
    print("Top Tray Fan 5 at {}".format(Top_5))

    start_top_tray_fan6 = (contents.find('Top Tray Fan 6'))
    f_top_tray_fan6 = contents[start_top_tray_fan6:(start_top_tray_fan6 + 66)].replace("\n", "")
    Top_6 = f_top_tray_fan6[54:66]
    print("Top Tray Fan 6 at {}".format(Top_6))

    start_top_tray_fan7 = (contents.find('Top Tray Fan 7'))
    f_top_tray_fan7 = contents[start_top_tray_fan7:(start_top_tray_fan7 + 66)].replace("\n", "")
    Top_7 = f_top_tray_fan7[54:66]
    print("Top Tray Fan 7 at {}".format(Top_7))

    start_top_tray_fan8 = (contents.find('Top Tray Fan 8'))
    f_top_tray_fan8 = contents[start_top_tray_fan8:(start_top_tray_fan8 + 66)].replace("\n", "")
    Top_8 = f_top_tray_fan8[54:66]
    print("Top Tray Fan 8 at {}".format(Top_8))

    start_top_tray_fan9 = (contents.find('Top Tray Fan 9'))
    f_top_tray_fan9 = contents[start_top_tray_fan9:(start_top_tray_fan9 + 66)].replace("\n", "")
    Top_9 = f_top_tray_fan9[54:66]
    print("Top Tray Fan 9 at {}".format(Top_9))

    start_top_tray_fan10 = (contents.find('Top Tray Fan 10'))
    f_top_tray_fan10 = contents[start_top_tray_fan10:(start_top_tray_fan10 + 66)].replace("\n", "")
    Top_10 = f_top_tray_fan10[54:66]
    print("Top Tray Fan 10 at {}".format(Top_10))

    start_top_tray_fan11 = (contents.find('Top Tray Fan 11'))
    f_top_tray_fan11 = contents[start_top_tray_fan11:(start_top_tray_fan11 + 66)].replace("\n", "")
    Top_11 = f_top_tray_fan11[54:66]
    print("Top Tray Fan 11 at {}".format(Top_11))

    start_top_tray_fan12 = (contents.find('Top Tray Fan 12'))
    f_top_tray_fan12 = contents[start_top_tray_fan12:(start_top_tray_fan12 + 66)].replace("\n", "")
    Top_12 = f_top_tray_fan12[54:66]
    print("Top Tray Fan 12 at {}".format(Top_12))

    print("\t")
    # Fan Bottom spinning detail
    start_Bottom_tray_fan1 = (contents.find('Bottom Tray Fan 1'))
    f_Bottom_tray_fan1 = contents[start_Bottom_tray_fan1:(start_Bottom_tray_fan1 + 66)].replace("\n", "")
    Bottom_1 = f_Bottom_tray_fan1[54:66]
    print("Bottom Tray Fan 1 at {}".format(Bottom_1))

    start_Bottom_tray_fan2 = (contents.find('Bottom Tray Fan 2'))
    f_Bottom_tray_fan2 = contents[start_Bottom_tray_fan2:(start_Bottom_tray_fan2 + 66)].replace("\n", "")
    Bottom_2 = f_Bottom_tray_fan2[54:66]
    print("Bottom Tray Fan 2 at {}".format(Bottom_2))

    start_Bottom_tray_fan3 = (contents.find('Bottom Tray Fan 3'))
    f_Bottom_tray_fan3 = contents[start_Bottom_tray_fan3:(start_Bottom_tray_fan3 + 66)].replace("\n", "")
    Bottom_3 = f_Bottom_tray_fan3[54:66]
    print("Bottom Tray Fan 3 at {}".format(Bottom_3))

    start_Bottom_tray_fan4 = (contents.find('Bottom Tray Fan 4'))
    f_Bottom_tray_fan4 = contents[start_Bottom_tray_fan4:(start_Bottom_tray_fan4 + 66)].replace("\n", "")
    Bottom_4 = f_Bottom_tray_fan4[54:66]
    print("Bottom Tray Fan 4 at {}".format(Bottom_4))

    start_Bottom_tray_fan5 = (contents.find('Bottom Tray Fan 5'))
    f_Bottom_tray_fan5 = contents[start_Bottom_tray_fan5:(start_Bottom_tray_fan5 + 66)].replace("\n", "")
    Bottom_5 = f_Bottom_tray_fan5[54:66]
    print("Bottom Tray Fan 5 at {}".format(Bottom_5))

    start_Bottom_tray_fan6 = (contents.find('Bottom Tray Fan 6'))
    f_Bottom_tray_fan6 = contents[start_Bottom_tray_fan6:(start_Bottom_tray_fan6 + 66)].replace("\n", "")
    Bottom_6 = f_Bottom_tray_fan6[54:66]
    print("Bottom Tray Fan 6 at {}".format(Bottom_6))

    start_Bottom_tray_fan7 = (contents.find('Bottom Tray Fan 7'))
    f_Bottom_tray_fan7 = contents[start_Bottom_tray_fan7:(start_Bottom_tray_fan7 + 66)].replace("\n", "")
    Bottom_7 = f_Bottom_tray_fan7[54:66]
    print("Bottom Tray Fan 7 at {}".format(Bottom_7))

    start_Bottom_tray_fan8 = (contents.find('Bottom Tray Fan 8'))
    f_Bottom_tray_fan8 = contents[start_Bottom_tray_fan8:(start_Bottom_tray_fan8 + 66)].replace("\n", "")
    Bottom_8 = f_Bottom_tray_fan8[54:66]
    print("Bottom Tray Fan 8 at {}".format(Bottom_8))

    start_Bottom_tray_fan9 = (contents.find('Bottom Tray Fan 9'))
    f_Bottom_tray_fan9 = contents[start_Bottom_tray_fan9:(start_Bottom_tray_fan9 + 66)].replace("\n", "")
    Bottom_9 = f_Bottom_tray_fan9[54:66]
    print("Bottom Tray Fan 9 at {}".format(Bottom_9))

    start_Bottom_tray_fan10 = (contents.find('Bottom Tray Fan 10'))
    f_Bottom_tray_fan10 = contents[start_Bottom_tray_fan10:(start_Bottom_tray_fan10 + 66)].replace("\n", "")
    Bottom_10 = f_Bottom_tray_fan10[54:66]
    print("Bottom Tray Fan 10 at {}".format(Bottom_10))

    start_Bottom_tray_fan11 = (contents.find('Bottom Tray Fan 11'))
    f_Bottom_tray_fan11 = contents[start_Bottom_tray_fan11:(start_Bottom_tray_fan11 + 66)].replace("\n", "")
    Bottom_11 = f_Bottom_tray_fan11[54:66]
    print("Bottom Tray Fan 11 at {}".format(Bottom_11))

    start_Bottom_tray_fan12 = (contents.find('Bottom Tray Fan 12'))
    f_Bottom_tray_fan12 = contents[start_Bottom_tray_fan12:(start_Bottom_tray_fan12 + 66)].replace("\n", "")
    Bottom_12 = f_Bottom_tray_fan12[54:66]
    print("Bottom Tray Fan 12 at {}".format(Bottom_12))

    print("--------------------------")
    myfile.close()

def power():
    # Get power detail
    start_power0 = (contents.find('PEM 0            Rev'))
    f_power0 = contents[start_power0:(start_power0 + 85)].replace("\n", "")

    start_power1 = (contents.find('PEM 1            Rev'))
    f_power1 = contents[start_power1:(start_power1 + 85)].replace("\n", "")

    start_power2 = (contents.find('PEM 2            Rev'))
    f_power2 = contents[start_power2:(start_power2 + 85)].replace("\n", "")

    start_power3 = (contents.find('PEM 3            Rev'))
    f_power3 = contents[start_power3:(start_power3 + 85)].replace("\n", "")
    print("--------------------------")
    print("Power detail has been found !!")
    print(f_power0)
    print(f_power1)
    print(f_power2)
    print(f_power3)
    print("--------------------------")
    myfile.close()

def power_temp():
    # Get power detail
    start_power0 = (contents.find('show chassis environment no-forwarding'))
    f_power0 = contents[start_power0:(start_power0 + 158)].replace("\n", "")

    start_power1 = (contents.find('show chassis environment no-forwarding'))
    f_power1 = contents[start_power1:(start_power1 + 234)].replace("\n", "")

    start_power2 = (contents.find('show chassis environment no-forwarding'))
    f_power2 = contents[start_power2:(start_power2 + 310)].replace("\n", "")

    start_power3 = (contents.find('show chassis environment no-forwarding'))
    f_power3 = contents[start_power3:(start_power3 + 386)].replace("\n", "")
    print("--------------------------")
    print("Power temperature has been found !!")
    power0_temp = f_power0[145:158]
    power1_temp = f_power1[220:234]
    power2_temp = f_power2[295:310]
    power3_temp = f_power3[370:386]
    print("PEM 0 --> {}".format(power0_temp))
    print("PEM 1 --> {}".format(power1_temp))
    print("PEM 2 --> {}".format(power2_temp))
    print("PEM 3 --> {}".format(power3_temp))
    print("--------------------------")
    myfile.close()

def memory():
    # Get Memory detail
    start_content = (contents.find('Total memory: '))
    f_host = contents[start_content:(start_content + 29)].replace("\n", "")

    start_content2 = (contents.find('Active memory: '))
    f_host2 = contents[start_content2:(start_content2 + 29)].replace("\n", "")
    print("--------------------------")
    print("Memory has been found !!!")
    print(f_host)
    print(f_host2)
    print("--------------------------")
    myfile.close()


hostname()
version()
chassis_part1()
chassis_part2()
chassis_part3()
fan()
power()
power_temp()
memory()