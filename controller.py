#!/usr/bin/env python3
import rospy
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.msg import ModelState

def move(name,x,y,z):
    state = ModelState()
    state.model_name = name
    state.pose.position.x = x
    state.pose.position.y = y
    state.pose.position.z = z
    state.pose.orientation.w = 1
    srv(state)

rospy.init_node("ctrl")
rospy.wait_for_service("/gazebo/set_model_state")
srv = rospy.ServiceProxy("/gazebo/set_model_state", SetModelState)

while not rospy.is_shutdown():
    c = input("輸入顏色：")

    print("抓球")
    move("ball_0",0,0,1)

    rospy.sleep(1)

    print("丟到固定位置")
    move("ball_0",2,0,0.2)
