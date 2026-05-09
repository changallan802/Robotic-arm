#!/usr/bin/env python3
import rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose
import random

def main():
    rospy.init_node("spawn")
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)

    for i in range(5):
        sdf = """
        <sdf version='1.6'>
          <model name='ball'>
            <link name='link'>
              <visual>
                <geometry><sphere><radius>0.05</radius></sphere></geometry>
              </visual>
            </link>
          </model>
        </sdf>
        """

        pose = Pose()
        pose.position.x = random.uniform(0.5,1.5)
        pose.position.z = 0.1

        spawn(f"ball_{i}", sdf, "", pose, "world")

if __name__ == "__main__":
    main()
