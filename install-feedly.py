import requests
import os
import sys
import subprocess

app_name = "Feedly"
short_name = "feedly"
logo_url = "https://ffb2efd5105ff0aedbc9-9cdacdeebf0faa19b665bf427f0c8092.ssl.cf1.rackcdn.com/img/feedly.png" 
home_path = os.environ['HOME']
app_url = "https://feedly.com/i/my"
script_path = home_path + '/bin/'
shortcut_path = home_path + '/.local/share/applications/'

if not os.path.exists(script_path):
    os.makedirs(script_path)
if not os.path.exists(shortcut_path):
    os.makedirs(shortcut_path)
subprocess.call(['chmod', '-R', '+rwx', script_path])

icon = open(script_path + short_name +".png",'wb')
icon.write(requests.get(logo_url).content)
icon.close()

s = open(script_path + short_name +'.sh', 'w')
s.write('google-chrome --app='+ app_url +'\n')
print(s)
s.close()

f = open(shortcut_path + short_name+'.desktop', 'w')
f.write('[Desktop Entry]\n')
f.write('Type=Application\n')
f.write('Terminal=true\n')
f.write('Name='+app_name+'\n')
f.write('Icon='+script_path+short_name+'.png\n')
f.write('Exec='+script_path+short_name+'.sh\n')
print(f)
f.close()

subprocess.call(['chmod', '-R', '+rwx', script_path])
sys.path.append(script_path)
