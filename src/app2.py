id=list(range(1,1001))


def verificar_rpm(rpm):
    rpm_min = 480
    rpm_min_aceitavel = 1650
    rpm_max_aceitavel = 2000
    rpm_max = 2520

    if rpm >= rpm_min and rpm < rpm_min_aceitavel:
        print("baixo")
    elif rpm >= rpm_min_aceitavel and rpm <=rpm_max_aceitavel:
        print("normal")
    elif rpm > rpm_max_aceitavel and rpm <= rpm_max:
        print("alto")
    else:
        print("fora dos padrões")

    
def verificar_motor(motor_power):
    motor_power_min = 1402.42
    motor_power_min_aceitavel = 5906.66
    motor_power_max_aceitavel = 13547.9
    motor_power_max = 19454.56

    if motor_power >= motor_power_min and motor_power < motor_power_min_aceitavel:
        print("baixo")
    elif motor_power >= motor_power_min_aceitavel and motor_power <=motor_power_max_aceitavel:
        print("normal")
    elif motor_power > motor_power_max_aceitavel and motor_power <= motor_power_max:
        print("alto")
    else:
        print("fora dos padrões")
        

def verificar_outletPressureBar(outlet_pressure_bar): #ou em psi?
    outlet_pressure_bar_min = 1.0
    outlet_pressure_bar_min_aceitavel = 4.44
    outlet_pressure_bar_max_aceitavel = 7.88
    outlet_pressure_bar_max = 8.66

    if outlet_pressure_bar >= outlet_pressure_bar_min and outlet_pressure_bar < outlet_pressure_bar_min_aceitavel:
        print("baixo")
    elif outlet_pressure_bar >= outlet_pressure_bar_min_aceitavel and outlet_pressure_bar <=outlet_pressure_bar_max_aceitavel:
        print("normal")
    elif outlet_pressure_bar > outlet_pressure_bar_max_aceitavel and outlet_pressure_bar <= outlet_pressure_bar_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_airFlow(air_flow):
    air_flow_min = 95.10
    air_flow_min_aceitavel = 669.49
    air_flow_max_aceitavel = 1444.81
    air_flow_max = 1539.91

    if air_flow >= air_flow_min and air_flow < air_flow_min_aceitavel:
        print("baixo")
    elif air_flow >= air_flow_min_aceitavel and air_flow <=air_flow_max_aceitavel:
        print("normal")
    elif air_flow > air_flow_max_aceitavel and air_flow <= air_flow_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_noiseDb(noise_db):
    noise_db_min = 39.88
    noise_db_min_aceitavel = 47.44
    noise_db_max_aceitavel = 57.98
    noise_db_max = 74.40

    if noise_db >= noise_db_min and noise_db < noise_db_min_aceitavel:
        print("baixo")
    elif noise_db >= noise_db_min_aceitavel and noise_db <=noise_db_max_aceitavel:
        print("normal")
    elif noise_db > noise_db_max_aceitavel and noise_db <= noise_db_max:
        print("alto")
    else:
        print("fora dos padrões")


def verificar_outletTemp(outlet_temp):
    outlet_temp_min = 76.90
    outlet_temp_min_aceitavel = 94.62
    outlet_temp_max_aceitavel = 141.93
    outlet_temp_max = 172.71

    if outlet_temp >= outlet_temp_min and outlet_temp < outlet_temp_min_aceitavel:
        print("baixo")
    elif outlet_temp >= outlet_temp_min_aceitavel and outlet_temp <=outlet_temp_max_aceitavel:
        print("normal")
    elif outlet_temp > outlet_temp_max_aceitavel and outlet_temp <= outlet_temp_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_gaccx(gaccx):
    gaccx_min = 0.54
    gaccx_min_aceitavel = 0.58
    gaccx_max_aceitavel = 0.60
    gaccx_max = 0.73

    if gaccx >= gaccx_min and gaccx < gaccx_min_aceitavel:
        print("baixo")
    elif gaccx >= gaccx_min_aceitavel and gaccx <=gaccx_max_aceitavel:
        print("normal")
    elif gaccx > gaccx_max_aceitavel and gaccx <= gaccx_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_gaccy(gaccy):
    gaccy_min = 0.27
    gaccy_min_aceitavel = 0.35  #????
    gaccy_max_aceitavel = 0.35
    gaccy_max = 0.46

    if gaccy >= gaccy_min and gaccy < gaccy_min_aceitavel:
        print("baixo")
    elif gaccy >= gaccy_min_aceitavel and gaccy <=gaccy_max_aceitavel:
        print("normal")
    elif gaccy > gaccy_max_aceitavel and gaccy <= gaccy_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_gaccz(gaccz):
    gaccz_min = 1.73
    gaccz_min_aceitavel = 3.61  #????
    gaccz_max_aceitavel = 3.92
    gaccz_max = 9.21

    if gaccz >= gaccz_min and gaccz < gaccz_min_aceitavel:
        print("baixo")
    elif gaccz >= gaccz_min_aceitavel and gaccz <=gaccz_max_aceitavel:
        print("normal")
    elif gaccz > gaccz_max_aceitavel and gaccz <= gaccz_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_haccx(haccx):
    haccx_min = 1.04
    haccx_min_aceitavel = 1.08  #????
    haccx_max_aceitavel = 1.10
    haccx_max = 1.23

    if haccx >= haccx_min and haccx < haccx_min_aceitavel:
        print("baixo")
    elif haccx >= haccx_min_aceitavel and haccx <=haccx_max_aceitavel:
        print("normal")
    elif haccx > haccx_max_aceitavel and haccx <= haccx_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_haccy(haccy):
    haccy_min = 1.27
    haccy_min_aceitavel = 1.35 #????
    haccy_max_aceitavel = 1.35
    haccy_max = 1.46

    if haccy >= haccy_min and haccy < haccy_min_aceitavel:
        print("baixo")
    elif haccy >= haccy_min_aceitavel and haccy <=haccy_max_aceitavel:
        print("normal")
    elif haccy > haccy_max_aceitavel and haccy <= haccy_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_haccz(haccz):
    haccz_min = 2.33
    haccz_min_aceitavel = 3.34  #????
    haccz_max_aceitavel = 3.50
    haccz_max = 6.11

    if haccz >= haccz_min and haccz < haccz_min_aceitavel:
        print("baixo")
    elif haccz >= haccz_min_aceitavel and haccz <=haccz_max_aceitavel:
        print("normal")
    elif haccz > haccz_max_aceitavel and haccz <= haccz_max:
        print("alto")
    else:
        print("fora dos padrões")

def verificar_exvalve(exvalve):
    exvalve_limpa = "clean"
    exvalve_suja = "dirty"
    if exvalve == exvalve_limpa:
        print("limpa")
    elif exvalve == exvalve_suja:
        print("suja")
    else:
        print("fora dos padrões")

def verificar_acmotor(acmotor):
    acmotor_estavel = "stable"
    acmotor_instavel = "unstable"
    if acmotor == acmotor_estavel:
        print("estável")
    elif acmotor == acmotor_instavel:
        print("instável")
    else:
        print("fora dos padrões")


