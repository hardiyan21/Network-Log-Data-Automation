myfile = open("/home/rama/Downloads/your-file", "rt")
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

hostname()
version()
chassis_part1()
chassis_part2()
chassis_part3()