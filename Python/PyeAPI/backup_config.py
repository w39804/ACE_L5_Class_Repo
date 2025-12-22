import pyeapi
import os
import yaml

#pyeapi.load_config('eapi.conf')

file = open('inventory.yml', 'r')
#pyeapi.load_config('eapi.conf')
device_dict = yaml.safe_load(file)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

#switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3', 'spine4', 'borderleaf1', 'borderleaf2']

for switch in device_dict:
    connect = pyeapi.connect(host=switch,username='arista',password='wid4whxyy3ggdaat',return_node=True)
    running_config = connect.get_config(as_string='True')
    path = directory+'/'+switch+'.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")