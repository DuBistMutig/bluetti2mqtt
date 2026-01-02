from typing import List
from ..commands import ReadHoldingRegisters
from .bluetti_device import BluettiDevice
from .struct import DeviceStruct

class AC180(BluettiDevice):
    def __init__(self, address: str, sn: str):
        self.struct = DeviceStruct()

        #Core
        # self.struct.add_swap_string_field('device_type', 110, 6)
        # self.struct.add_sn_field('serial_number', 116)
        self.struct.add_swap_string_field('device_type', 1101, 6)
        self.struct.add_sn_field('serial_number', 1107)

        #Battery Data
        self.struct.add_swap_string_field('battery_type', 6101, 6)
        self.struct.add_sn_field('battery_serial_number', 6107)
        self.struct.add_version_field('bcu_version', 6175)
        self.struct.add_uint_field('total_battery_percent', 102)

        #Power IO
        self.struct.add_uint_field('output_mode',123) #32 when both loads off, 40 when AC is on, 48 when DC is on, 56 when both on 
        self.struct.add_uint_field('dc_output_power', 140)
        self.struct.add_uint_field('ac_output_power', 142)
        self.struct.add_uint_field('dc_input_power', 144)
        self.struct.add_uint_field('ac_input_power', 146) #this is a guess because I didn't have a PV module handy to test

        #History
        # self.struct.add_decimal_field('power_generation', 154, 1)  # Total power generated since last reset (kwh)
        self.struct.add_decimal_field('power_generation', 1202, 1)  # Total power generated since last reset (kwh)

        # this is usefule for investigating the available data
        # registers = {0:21,100:67,700:6,720:49,1100:51,1200:90,1300:31,1400:48,1500:30,2000:67,2200:29,3000:27,6000:31,6100:100,6300:52,7000:5}
        # for k in registers:
        #     for v in range(registers[k]):
        #         self.struct.add_uint_field('testI' + str(v+k), v+k)

        super().__init__(address, 'AC180', sn)

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return [
            ReadHoldingRegisters(100, 62),
        ]

    @property
    def logging_commands(self) -> List[ReadHoldingRegisters]:
        return [
            ReadHoldingRegisters(0,21),
            ReadHoldingRegisters(100, 67),
            ReadHoldingRegisters(700,6),
            ReadHoldingRegisters(720,49),
            ReadHoldingRegisters(1100, 51),
            ReadHoldingRegisters(1200, 90),
            ReadHoldingRegisters(1300, 31),
            ReadHoldingRegisters(1400, 48),
            ReadHoldingRegisters(1500, 30),
            ReadHoldingRegisters(2000, 67),
            ReadHoldingRegisters(2200, 29),
            ReadHoldingRegisters(3000, 27),
            ReadHoldingRegisters(6000, 31),
            ReadHoldingRegisters(6100, 100),
            ReadHoldingRegisters(6300, 52),
            ReadHoldingRegisters(7000,5)
        ]
