# Wraith UAV Documentation

## Project Documentation

**Contributors:**  
Fares Fathy  
Abdulrahman Saeed

**Course:**  
Computer Organization

---

### Introduction
Unmanned aerial vehicles (UAVs), also known as drones, are aircraft controlled remotely or autonomously without a human pilot onboard. UAVs can operate in hazardous environments and collect data using various sensors and cameras. As UAV technology advances, it is increasingly used in various industries and sectors.

### Why Pixhawk?
Pixhawk is a popular flight controller for UAVs due to its reliability and strong community support. It integrates various sensors and peripherals to provide UAV flight capabilities.

#### Key Benefits:
- **Reliability:** Widely tested and robust.
- **Community Support:** Large, active community with extensive resources.

### Used Components

#### Motors and Propellers
- **Motors:** 4 Readytosky 920kv motors.
  
![image](https://github.com/user-attachments/assets/d9d2960e-f5b9-456d-bab1-3d8ecbd03d52)


#### Battery and Power Distribution
- **Battery:** Lithium polymer 11.1V 3300 mah battery.
- **Power Distribution:** Power distribution board for component connectivity.
  
![image](https://github.com/user-attachments/assets/4c8b1077-9820-40cf-96db-5330e5720c62)
![image](https://github.com/user-attachments/assets/83457566-232c-49bb-a743-4ba1c7f8745d)
![image](https://github.com/user-attachments/assets/b9bc0ca1-f359-468c-9faf-41ee410dfc1f)
![image](https://github.com/user-attachments/assets/d1e6c723-c920-4700-868c-d5370812d508)


#### Radio Control System
- **Radio Control:** FrSky Taranis X7 series RC.
- **Receiver:** X8R receiver.
  
![image](https://github.com/user-attachments/assets/429f47d9-25bb-4cad-9315-c5a62d6f2a26)
![image](https://github.com/user-attachments/assets/d32f48ca-f040-4064-af92-8e644abba326)


#### Electronic Speed Controller (ESC)
The ESC controls the propulsion system, adjusting motor speed and direction based on flight controller input for real-time flight adjustments.

![image](https://github.com/user-attachments/assets/0c912ff8-ccd8-4e6d-b7c0-2f1bdae09a56)


### Why Mission Planner?
Mission Planner is a ground control software for planning, configuring, and operating UAVs equipped with ArduPilot. It offers a user-friendly interface and essential tools for mission execution.

![image](https://github.com/user-attachments/assets/be004748-31a8-4bd9-abb5-3b4604c9bd64)


#### Radio Calibration
Radio calibration ensures proper configuration and functionality of the radio control system.

![image](https://github.com/user-attachments/assets/4dcd8995-4191-4608-9d49-da0086d4d4b4)


#### Full Parameter List
Setting the `arm_check` parameter to 0 disables the GPS failsafe mechanism, allowing operation without GPS interference.

![image](https://github.com/user-attachments/assets/4aebf39c-55d1-4948-8649-8cbc7e2cdb12)


### Flight Modes
1. **AltHold (Altitude Hold):** Maintains stable altitude.
2. **Acro (Acrobatics):** Allows agile maneuvers.
3. **Stabilize:** Combines AltHold and Acro for stability and agility.

![image](https://github.com/user-attachments/assets/9d46663e-dda6-4b27-837f-e8a01496539e)


### ESC Calibration
Settings for optimal ESC performance were determined through various combinations.

![image](https://github.com/user-attachments/assets/0902accb-438c-44a4-bffc-cd2f9fa84c7b)


### Failsafe Design
A failsafe mode initiates RTL (Return to Launch) sequence if battery power drops below 7.5V, ensuring safe landing.

![image](https://github.com/user-attachments/assets/8cc1a4e1-ef8f-4533-88fc-cddc5ff25ae9)


### Frame Type
Quadcopters are preferred for their simplicity and ease of use, making them accessible to a wider range of users.

![image](https://github.com/user-attachments/assets/cd5827e5-3315-4a3a-8885-62cb7df1cef8)
![image](https://github.com/user-attachments/assets/18d29490-f75e-4fe7-87f1-593857001c55)
![image](https://github.com/user-attachments/assets/34423f4c-f4fd-4fa8-a615-f66b252e0d0d)


### Basic Design
The design was modified to fit available components while maintaining original connections.

![image](https://github.com/user-attachments/assets/65ce3c0c-0184-458a-b3f5-0c202d9b256f)
![image](https://github.com/user-attachments/assets/c4c468af-8cf2-4cff-b258-ad598bec7906)
![image](https://github.com/user-attachments/assets/b1959fcc-9595-4937-a80d-ed41c147d10e)


### Challenges
We faced issues connecting the Raspberry Pi to the Pixhawk due to the absence of a MAVProxy heartbeat signal.

![image](https://github.com/user-attachments/assets/42fc3703-090c-4e94-ba49-43f37e53f36a)


### References
- [The Drone Dojo](https://www.youtube.com/@thedronedojo3624)
- [YouTube: How to Build a Drone](https://www.youtube.com/watch?v=qmxEx28N56s)
- [YouTube: Drone Programming](https://www.youtube.com/watch?v=2Rikb6hRl5g)
- [YouTube: ArduPilot Playlist](https://www.youtube.com/playlist?list=PLk5osPy4f_U8Muv7KwCvg5C5wtEcCIjjf)
- [ArduPilot: Mission Planner](https://ardupilot.org/planner/docs/common-connect-mission-planner-autopilot.html)

---

For further questions, please contact us at [ffathy2004@gmail.com](mailto:ffathy2004@gmail.com) or [abdosaaed749@gmail.com](mailto:ffathy2004@gmail.com). 
