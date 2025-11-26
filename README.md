# Lab_2 – ROS Publisher, Subscriber, Service, and Action

## Overview
This package demonstrates the fundamental communication mechanisms in ROS using Python. It includes nodes for publishing & subscribing to topics, implementing services, and creating action servers and clients.

The goal is to understand how ROS nodes communicate and how different ROS communication interfaces work together in a real ROS workspace.

---

## Features
###  Publisher & Subscriber
- `talker.py` publishes messages on a topic.
- `listener.py` subscribes and prints received messages.

###  Custom Message
- Defined in `msg/Num.msg`.

###  Service
- `add_two_ints_server.py` creates a ROS service.
- `add_two_ints_client.py` calls the service.

###  Action Server & Client
Includes Action communication using:
- action server
- action client
- `.action` file

###  Launch Files Included
For running multiple nodes easily.

---

## Folder Structure
```
Lab_2/
├── msg/
│   └── Num.msg
├── srv/
│   └── AddTwoInts.srv
├── action/
│   └── Example.action
├── scripts/
│   ├── talker.py
│   ├── listener.py
│   ├── add_two_ints_server.py
│   ├── add_two_ints_client.py
│   ├── action_server.py
│   └── action_client.py
├── launch/
│   └── combined.launch
├── package.xml
└── CMakeLists.txt
```

---

## How to Run

### 1. Source your workspace:
```bash
source ~/catkin_ws/devel/setup.bash
```

### 2. Run the nodes:

#### Publisher:
```bash
rosrun Lab_2 talker.py
```

#### Subscriber:
```bash
rosrun Lab_2 listener.py
```

#### Service:
```bash
rosrun Lab_2 add_two_ints_server.py
```

```bash
rosrun Lab_2 add_two_ints_client.py
```

#### Action:
```bash
rosrun Lab_2 action_server.py
```

```bash
rosrun Lab_2 action_client.py
```

---

## Purpose
This package demonstrates:
- ROS topics
- Custom messages and services
- ROS actionlib basics
- Integration of multiple communication methods in a single package

---

## Requirements
- Ubuntu
- ROS Noetic
- Python 3

---

## Author
**Muhammad Elbialy**
