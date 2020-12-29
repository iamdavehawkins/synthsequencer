import asyncio
from typing import List, Union, Optional

import mido

from synthsequencer.program import Program
from synthsequencer.controlprogram import ControlProgram

class Performance():

    def __init__(self, programs: List[Program], control_programs: Optional[List[ControlProgram]]=None, tempo=120, swing=0):
        self.sleep_time = 60 / tempo / 4
        self.swing = swing
        self.outport = mido.open_output()
        self.programs = programs

    async def sleep(self, is_swing_beat: int):
        sleep_time_swing_long = self.sleep_time * (1 + self.swing)
        sleep_time_swing_short = (self.sleep_time * 2) - sleep_time_swing_long
        if self.swing:
            if is_swing_beat:
                await asyncio.sleep(sleep_time_swing_short)
            else:
                await asyncio.sleep(sleep_time_swing_long)
        else:
            await asyncio.sleep(self.sleep_time)

    async def play_sequence(self, p: Union[Program, ControlProgram]):
        while True:
            for _, msg in enumerate(p.sequence()):
                # note playing a sequence of length 1, with swing, will get interesting
                if msg:
                    self.outport.send(msg)
                await self.sleep(_ % 2)

    async def perform(self):
        print('looping')
        self.loop = asyncio.get_event_loop()
        for program in self.programs:
            asyncio.ensure_future(self.play_sequence(program))

    async def stop(self):
        self.loop.stop()
