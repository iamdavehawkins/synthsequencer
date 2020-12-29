### Example

Controlling a Korg Volca Drum
```python
import synthsequencer
from synthsequencer.program import Program
from synthsequencer.controlprogram import ControlProgram
from synthsequencer.performance import Performance
from synthsequencer.volca.drum import VolcaDrumChannels, VolcaDrumControls

bass_part =  Program('o---o---o---o--o', VolcaDrumChannels.PART1)
snare_part = Program('----o-------o-o-', VolcaDrumChannels.PART4)
hh_part =    Program('oo', VolcaDrumChannels.PART2)
bass_pan =   ControlProgram([32]*8+[127]*8, 0, VolcaDrumControls.PAN)

p = Performance([bass_part, snare_part, hh_part], tempo=120, swing=.33)

await p.perform()

await p.stop()