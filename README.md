# master_thesis_code
This repository contains the code for my master's thesis

**NECESSARY PACKAGES**
1) gmapping
2) ira_laser_tools
3) urg_node
4) realsense2_camera
5) apriltag_ros
6) actionlib 

## REAL-WORLD APPLICATION 
  1) Make a map 
      - roslaunch laser_thorvald robot_019.launch (For small configuration) 
      - roslaunch autonomous_docking hokuyo.launch
      - roslaunch laser_thorvald corner_hokuyos_laser_merger.launch
      - rosrun gmapping slam_gmapping 
      Use teleoperation to move around the desired area, then save: 
      - rosrun map_server map_saver -f "name_of_map" 
      - mv .yaml and .pgm file to desired directory 
      - update ~/autonomous_docking/launch/map_dock.launch 
  2) Run the function (LASER)
      set desired properties in autonomous_docking/code/ final_controller_node
      - roslaunch laser_thorvald robot_019.launch (Check configuration!) 
      - roslaunch autonomous_docking hokuyo.launch
      - roslaunch laser_thorvald corner_hokuyos_laser_merger.launch 
      - roslaunch autonomous_docking map_dock.launch (includes amcl for localization)
      
      ***Continuous detection does not work properly yet. Run detection and stop it when Thorvald has obtained the coordinates.***
      
      - rosrun autonomous_docking laser_localization_node
      - rosrun autonomous_docking final_controller_node
  3) Run the function (CAMERA)
      set desired properties in autonomous_docking/code/ final_controller_node
      - roslaunch laser_thorvald robot_019.launch (Check configuration!) 
      - roslaunch autonomous_docking hokuyo.launch
      - roslaunch laser_thorvald corner_hokuyos_laser_merger.launch 
      - roslaunch autonomous_docking map_dock.launch (includes amcl for localization) 
      - roslaunch realsense2_camera rs_camera.launch 
      - roslaunch apriltag_ros continuous_detection.launch 
      
      ***Continuous detection does not work properly yet. Run detection and stop it when Thorvald has obtained the coordinates.***
      
      - rosrun autonomous_docking apriltag_localization_node
      - rosrun autonomous_docking final_controller_node
  4) For both sensors, use 3) and run the laser_localization node too. Remember to update the controller node. 
  
## SIMULATION 

***ONLY VIRTUAL LASER*** 

  1) Manual execution
      - roslaunch autonomous_docking dock_gazebo.launch (For small configuration) 
      - roslaunch laser_thorvald corner_hokuyos_laser_merger.launch
      - rosrun autonomous_docking sim_laser_localization_node
      
      ***Continuous detection does not work properly yet. Run detection and stop it when Thorvald has obtained the coordinates.***
      
      - rosrun autonomous_docking sim_final_controller_node
   2) As ActionServer 
      - roslaunch autonomous_docking dock_gazebo.launch (For small configuration) 
      - roslaunch laser_thorvald corner_hokuyos_laser_merger.launch
      - rosrun autonomous_docking sim_laser_localization_node
      
      ***Continuous detection does not work properly yet. Run detection and stop it when Thorvald has obtained the coordinates.***
      
      - rosrun autonomous_docking sim_controller_action
      - rosrun actionlib axclient.py /docking_controller
