#fonte=http://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line
import rospy
import math 
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('geppetto_node', anonymous=False)
    velocity_publisher = rospy.Publisher('/catvehicle/cmd_vel', Twist, queue_size=1)
    vel_msg = Twist()

   

  
    #Since we are moving just in x-axis
    vel_msg.linear.x = 1.0
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0
    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        vel_msg.angular.z = float(math.cos(rospy.Time.now().to_sec()/8))
        
        #Loop to move the turtle in an specified distance
    
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        #t1=rospy.Time.now().to_sec()
            

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
