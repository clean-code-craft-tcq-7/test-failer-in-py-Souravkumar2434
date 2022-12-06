from alertincelcius import NETWORK_ALERT_THRESHOLD

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if celcius > NETWORK_ALERT_THRESHOLD:
        return 500
    else:
        return 200
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    #return celcius
