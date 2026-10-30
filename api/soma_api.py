import requests

class SomaApi:
    timeout = 5

    def __init__(self, soma_connect_ip, soma_connect_port):
        self.soma_connect_ip = soma_connect_ip
        self.soma_connect_port = soma_connect_port
        self.list_devices()

    def list_devices(self):
        ret = requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/list_devices", timeout = self.timeout).json()
        self.soma_connect_version = ret["version"]
        return ret

    def open_shade(self, mac):
        if(self.soma_connect_version.split('.')[0] == '3'):
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/open_shade?mac="+mac, timeout = self.timeout).json()
        else:
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/open_shade/"+mac, timeout = self.timeout).json()

    def close_shade(self, mac):
        if(self.soma_connect_version.split('.')[0] == '3'):
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/close_shade?mac="+mac, timeout = self.timeout).json()
        else:
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/close_shade/"+mac, timeout = self.timeout).json()

    def stop_shade(self, mac):
        if(self.soma_connect_version.split('.')[0] == '3'):
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/stop_shade?mac="+mac, timeout = self.timeout).json()
        else:
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/stop_shade/"+mac, timeout = self.timeout).json()

    def get_shade_state(self, mac):
        if(self.soma_connect_version.split('.')[0] == '3'):
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/get_shade_state?mac="+mac, timeout = self.timeout).json()
        else:
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/get_shade_state/"+mac, timeout = self.timeout).json()

    def set_shade_position(self, mac, position, close_upwards = False, morning_mode = False):
        # Optional flags (SOMA Connect 2.2.5+) are only sent when set, so default calls are unchanged.
        # morning_mode moves the motor slowly and quietly; close_upwards closes Tilt shades upwards.
        options = ""
        if close_upwards:
            options += "&close_upwards=1"
        if morning_mode:
            options += "&morning_mode=1"
        if(self.soma_connect_version.split('.')[0] == '3'):
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/set_shade_position?mac="+mac+"&pos="+str(position)+options, timeout = self.timeout).json()
        else:
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/set_shade_position/"+mac+"/"+str(position)+options.replace("&", "?", 1), timeout = self.timeout).json()

    def get_battery_level(self, mac):
        if(self.soma_connect_version.split('.')[0] == '3'):
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/get_battery_level?mac="+mac, timeout = self.timeout).json()
        else:
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/get_battery_level/"+mac, timeout = self.timeout).json()

    def get_light_level(self, mac):
        if(self.soma_connect_version.split('.')[0] == '3'):
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/get_light_level?mac="+mac, timeout = self.timeout).json()
        else:
            return requests.get(url = "http://"+self.soma_connect_ip+":"+str(self.soma_connect_port)+"/get_light_level/"+mac, timeout = self.timeout).json()
