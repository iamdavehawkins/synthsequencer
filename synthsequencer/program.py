from mido.messages import Message

from synthsequencer.volca.drum import VolcaDrumChannels

class Program():
    def __init__(self, rhythm, channel: VolcaDrumChannels):
        self.channel = channel
        self.rhythm = rhythm
        
    def message(self):
        return Message('note_on', channel=self.channel.value)
    
    def sequence(self):
        return [self.message() if i == 'o' else None for i in self.rhythm]
