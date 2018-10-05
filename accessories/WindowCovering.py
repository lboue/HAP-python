# An Accessory mocking a temperature sensor.
# It changes its value every few seconds.
import random

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SENSOR


class WindowCovering(Accessory):

    category = CATEGORY_SENSOR

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        serv_cover = self.add_preload_service('WindowCovering')
        self.char_cur = serv_cover.configure_char('CurrentPosition')
        self.char_cur = serv_cover.configure_char('TargetPosition')
        self.char_cur = serv_cover.configure_char('PositionState')
        
        self.char_cur = serv_cover.get_characteristic('CurrentPosition')
        self.char_target = serv_cover.get_characteristic('TargetPosition')
        # The value property of PositionState must be one of the following:
        # Characteristic.PositionState.DECREASING = 0;
        # Characteristic.PositionState.INCREASING = 1;
        # Characteristic.PositionState.STOPPED = 2;        
        self.char_state = serv_cover.get_characteristic('PositionState')
        
        #self.char_hold = serv_cover.get_characteristic('HoldPosition')
        #self.char_obs = serv_cover.get_characteristic('ObstructionDetected')


    @Accessory.run_at_interval(3)
    def run(self):
        #self.char_cur.set_value(random.randint(0, 100))
        self.char_cur.set_value(50)
        self.char_target.set_value(50)
        self.char_state.set_value(2)
