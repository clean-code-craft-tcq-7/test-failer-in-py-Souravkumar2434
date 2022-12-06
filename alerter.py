from alertincelcius import alert_in_celcius, alert_failure_count

alert_in_celcius(210.2)
alert_in_celcius(212)
alert_in_celcius(213)
print(f'{alert_failure_count} alerts send failed.')
assert alert_failure_count > 0, f'alert fail count not incremented {alert_failure_count} times.'
print("All is well!!")
