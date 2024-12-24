# MIE1075_BEDMAKINGROBOT_Project

Introduction: This project demonstrates the design and implementation of an AI-powered bed-making robot by applying advanced robotics and artificial intelligence techniques for the course MIE1075 - Artificial Intelligence for Robotics I. The key tasks include localization, path and motion planning, image process, pose and grasp estimation.

---

## Project Structure

The project consists of two main folders, each containing essential files for specific functionalities:

### Folder 1: Reinforcement_Learning_Demo_using_uf-gym
<div align="justify">
This folder contains files related to reinforcement learning for simulating picking up a pillow and displacing it to a target location. This folder contains the **uf-gym** which comes from the (https://github.com/xArm-Developer/uf-gym) which is under the MIT License as shown in the Folder with Copyright notices from Quentin Gallouédec and UFACTORY Inc. as the xarm7 comes from UFACTORY. The **uf-gym** was customized for our task with some files changed, and new ones added such as the new 3D pillow in URDF, the PillowPickNPlace, and a custom PyBullet file, which was adapted from (https://github.com/bulletphysics/bullet3).
</div>

#### Important Files:
1. **`pickNplace_task_train_pillow.py`**  
   - Implements reinforcement learning algorithms for training the model, and picking up the pillow and moving it.
   - To run training, download the proper libraries for uf-gym and simply type: ```python pickNplace_task_train_pillow.py```
2. **`pickNplace_task_test_pillow.py`**  
   - Shows the robot picking up and placing the pillow at the target location after having learned from training.
3. **`VisualTool.py`**  
   - Visualizes the base environment when modifying it or the object.

---

### Folder 2: YOLO_Demo
This folder contains files demonstrating object detection and classification using YOLO.

#### Important Files:
1. **`yolo_demo.py`**  
   - Performs object detection using the YOLO model to identify specific items like pillows, sheets, and bed covers.
2. **`yolo_state_recognize.py`**  
   - Recognizes and classifies the state of the bed (made or unmade) for action planning using the Ultralytics API.
3. **`yolo_state_recognize_output.jpg`**  
   - Shows an example of the robot detecting whether the bed is made or unmade.

---

## Demos

The project also includes demo files that showcase the robot's performance:

1. **`final_hard_coded_simulation.mp4`**  
   - Demonstrates the complete bed-making process through a simulated robotic workflow.
2. **`yolo_demo.mp4`**  
   - Displays the YOLO object detection system with an example video.
   - Its located in **YOLO_Demo/YOLOSimulationMP4**
3. **`ReinforcementLearningDemo.mp4`**
   - Displays the MP4 simulation of the pillow being moved by the robotic arm.
   - Its located in **Reinforcement_Learning_Demo_using_uf-gym/RFSimulationMP4**

---
