import requests
import os
import sys
import subprocess

classeur_logo_url = "https://app.classeur.io/0.14.0/assets/images/logo.png" 
home_path = os.environ['HOME']
classeur_url = "https://app.classeur.io/"
script_path = home_path + '/bin/'
shortcut_path = home_path + '/.local/share/applications/'

if not os.path.exists(script_path):
    os.makedirs(script_path)
if not os.path.exists(shortcut_path):
    os.makedirs(shortcut_path)
subprocess.call(['chmod', '-R', '+rwx', script_path])

icon = open(script_path + "classeur.png",'wb')
icon.write(requests.get(classeur_logo_url).content)
icon.close()

s = open(script_path + 'classeur.sh', 'w')
s.write('google-chrome --app='+ classeur_url +'\n')
print(s)
s.close()

f = open(shortcut_path + 'classeur.desktop', 'w')
f.write('[Desktop Entry]\n')
f.write('Type=Application\n')
f.write('Terminal=true\n')
f.write('Name=Classeur\n')
f.write('Icon='+script_path+'classeur.png\n')
f.write('Exec='+script_path+'classeur.sh\n')
print(f)
f.close()

subprocess.call(['chmod', '-R', '+rwx', script_path])
sys.path.append(script_path)