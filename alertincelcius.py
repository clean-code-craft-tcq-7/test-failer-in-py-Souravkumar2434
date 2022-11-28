from alerter_send import network_alert_stub

alert_failure_count = 0

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        assert returnCode == 500 # test case for not-ok response
        global alert_failure_count
        alert_failure_count += 0
