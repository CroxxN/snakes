import wifi

nets = wifi.Cell.all('wlan0')
for net in nets:
    print(net.ssid)
