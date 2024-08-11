# Manual Ethercat Configuration

In case of  miss-understanding with how to create the YAML drive configuration file using `ethercat cstruct` theres no need to panic.

This is a short and concise guide on how to find every thing that you need.

## PDOs

first we need to understand superficially what PDOs are.
PDOs are the data that cyclicly transferred and received every ethercat cycle \*

now PDOs are divided in two groups:
- RPDO: the data that the ethercat master expect to receive from a drive
- TPDO: the data that the master sends to the drive
those are configured as follows: \*\*
```
rpdo:  # RxPDO = receive PDO Mapping
  - index: 0x1600
    channels:
      - {index: 0x6040, sub_index: 0, type: uint16, command_interface: control_word, default: 0}  # Control word
      - {index: 0x607a, sub_index: 0, type: int32, command_interface: position}  # Target position
  - index: 0x1601
    channels:
      - {index: 0x6060, sub_index: 0, type: int8, command_interface: mode_of_operation, default: 9}  # Mode of operation
      - {index: 0x60ff, sub_index: 0, type: int32, command_interface: velocity, default: 0}  # Target velocity
tpdo:  # TxPDO = transmit PDO Mapping
  - index: 0x1a00
    channels:
      - {index: 0x6041, sub_index: 0, type: uint16, state_interface: status_word}  # Status word
      - {index: 0x6064, sub_index: 0, type: int32, state_interface: position}  # Position actual value
  - index: 0x1a01
    channels:
      - {index: 0x6061, sub_index: 0, type: int8, state_interface: mode_of_operation}  # Mode of operation display
      - {index: 0x606c, sub_index: 0, type: int32, state_interface: velocity}  # Velocity actual value 65536 = 1 encoder increment/sample (internal driver slow loop : 1khz )

```

## CIA402
We are working with a protocol called COE (can over ethercat), which means that we are bound by the canopen protocol.
this protocol determine the mapping of every register from the address 0x6000 and up
addresses 0x2000 to 0x5fff are manufactures specific and needed to be added per data sheet or contact with the manufacture



## Notes

* \* ethercat cycle- ethercat is a synced protocol, thus it operated precisely every \<X> determined time. we usually run at 100\[Hz]
the following part of the YAML file controls the cycle time:
```
sdo:  # sdo data to be transferred at drive startup
  - {index: 0x60C2, sub_index: 1, type: int8, value: 1} # Set interpolation time for cyclic modes to 10 ms #lets call this Alpha
  - {index: 0x60C2, sub_index: 2, type: int8, value: -2} # Set base 10-3s # lets call this Beta
```
so this is $(\alpha * 10^{\beta})$

* \*\* if you cant find the channels with the `ethercat cstruct` command and you cant find channel config in the drives datasheet you should try putting all the RPDOs in channel **0x1600** and all the TPDOs in channel **0x1a00** as this is a common practice.


## Further Reading
[icube-docs](https://icube-robotics.github.io/ethercat_driver_ros2/)
