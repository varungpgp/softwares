import subprocess
import webbrowser, os

subprocess.call('powercfg /batteryreport', shell =True)

try:
    from urllib import pathname2url         # Python 2.x
except:
    from urllib.request import pathname2url # Python 3.x

url = 'file:{}'.format(pathname2url(os.path.abspath('battery-report.html')))
webbrowser.open(url)
