import bluetooth  #imorting bluetooth module
nearby_devices = bluetooth.discover_devices(lookup_names='true',lookup_class='true')# scanning for bluetooth devices in range
print('\n')

print('....scanning for nearby devices.....')
print('\n')

no_of_devices = len(nearby_devices)# finding no of devices found
print('number of devices found :',no_of_devices)
print('\n')


for addr,name,device_class in nearby_devices: #finding address,name,decicesclass for every device found
    print('address :',addr)
    print('name :',name)
    print('device_class :',device_class)
    print('\n')
