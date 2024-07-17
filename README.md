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

#### Battery and Power Distribution
- **Battery:** Lithium polymer 11.1V 3300 mah battery.
- **Power Distribution:** Power distribution board for component connectivity.

#### Radio Control System
- **Radio Control:** FrSky Taranis X7 series RC.
- **Receiver:** X8R receiver.

#### Electronic Speed Controller (ESC)
The ESC controls the propulsion system, adjusting motor speed and direction based on flight controller input for real-time flight adjustments.

### Why Mission Planner?
Mission Planner is a ground control software for planning, configuring, and operating UAVs equipped with ArduPilot. It offers a user-friendly interface and essential tools for mission execution.

#### Radio Calibration
Radio calibration ensures proper configuration and functionality of the radio control system.

#### Full Parameter List
Setting the `arm_check` parameter to 0 disables the GPS failsafe mechanism, allowing operation without GPS interference.

### Flight Modes
1. **AltHold (Altitude Hold):** Maintains stable altitude.
2. **Acro (Acrobatics):** Allows agile maneuvers.
3. **Stabilize:** Combines AltHold and Acro for stability and agility.

### ESC Calibration
Settings for optimal ESC performance were determined through various combinations.

### Failsafe Design
A failsafe mode initiates RTL (Return to Launch) sequence if battery power drops below 7.5V, ensuring safe landing.

### Frame Type
Quadcopters are preferred for their simplicity and ease of use, making them accessible to a wider range of users.

### Basic Design
The design was modified to fit available components while maintaining original connections.

### Challenges
We faced issues connecting the Raspberry Pi to the Pixhawk due to the absence of a MAVProxy heartbeat signal.

### References
- [The Drone Dojo](https://www.youtube.com/@thedronedojo3624)
- [YouTube: How to Build a Drone](https://www.youtube.com/watch?v=qmxEx28N56s)
- [YouTube: Drone Programming](https://www.youtube.com/watch?v=2Rikb6hRl5g)
- [YouTube: ArduPilot Playlist](https://www.youtube.com/playlist?list=PLk5osPy4f_U8Muv7KwCvg5C5wtEcCIjjf)
- [ArduPilot: Mission Planner](https://ardupilot.org/planner/docs/common-connect-mission-planner-autopilot.html)

---

For further questions, please contact me at [ffathy2004@gmail.com](mailto:ffathy2004@gmail.com).
