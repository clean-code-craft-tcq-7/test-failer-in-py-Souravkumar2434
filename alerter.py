from alertincelcius import alert_in_celcius, alert_failure_count

alert_in_celcius(210.2)
alert_in_celcius(212)
alert_in_celcius(213)
print(f'{alertFailureCount} alerts send failed.')
assert alertFailureCount > 0, f'alert fail count not incremented {alertFailureCount} times.'
print("All is well!!")
