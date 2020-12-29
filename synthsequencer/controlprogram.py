from mido.messages import Message

from synthsequencer.volca.drum import VolcaDrumControls

class ControlProgram():
    def __init__(self, values, channel, control: VolcaDrumControls):
        self.values = values
        self.channel = channel
        self.control = control
        
    def message(self, value):
        return Message('control_change', channel=self.channel, control=self.control.value, value=value)
    
    def sequence(self):
        return [self.message(v) for v in self.values]
