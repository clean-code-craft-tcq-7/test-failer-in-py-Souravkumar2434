from alerter_send import network_alert_stub
from farenheit_to_celcius import getCelciusFromFarenheit

alert_failure_count = 0
NETWORK_ALERT_THRESHOLD = 100

def alert_in_celcius(farenheit):
    celcius = getCelciusFromFarenheit(farenheit)
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        assert returnCode == 500 # test case for not-ok response
        global alert_failure_count
        alert_failure_count += 1
