# New Drive integration

## Steps To Integrate New Drives To The Wombat System

1. Configure the drive with its dedicated software (Easymotion for Technosoft, Motion Lab 3 for Inginia, etc..).
2. Connect to drive to a motor and test it in the dedicated software.
3. Connect the drive to robee-jetson-2 (realtime kernel jetson)
4. Start ethercat with `start_ethercat` command
5. Check to see if the ethercat master sees the drive with `ethercat slaves` command
6. Check the pdo structure with `ethercat cstruct` \*
7. Create a new YAML file for the drive pdo configuration (see [reference config](../ec_single_axis_description/config/techno.yaml) for reference on how to properly do it)
8. Change the urdf file ([urdf](../ec_single_axis_description/ros2_control/ec_single_axis.ros2_control.xacro)) to look for the correct yaml file.
9. If needed change the command_interface and state_interface field
10. Change the mode_of_operation to  match your test case (8- position control,9- velocity control)
11. Run one of the test cases with:
position:
```
python3 src/iiwa_ros2/test_nodes/scripts/trajectory_publisher.py
```

velocity:
```
python3 src/iiwa_ros2/test_nodes/scripts/velocity_publisher.py
```

12. After both tests looks fine the drive is ready to be integrated to  RobeeContech directory with the tested yaml file

## Notes
* \* when configuring the Inginia drive the drive refused to share data when asked to with the `ethercat cstruct` command, this is normal and it operates well without it. see [manual_ethercat_config](./manual_ethercat_config.md)

* Inginia registers: [inginia registers](https://drives.novantamotion.com/eve-xcr/ethercat-canopen-registers)
* Technosoft registers [technosoft registers](https://github.com/user-attachments/files/16573778/P091.064.EtherCAT.iPOS_.UM_.1123.2.pdf)
