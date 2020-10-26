import rospy
from std_msgs.msg import String

rospy.init_node('N2')


def CallBack(msg):  
    resultado = 0
    for i in range(len(msg.data)):
        resultado += int(msg.data[i])
    msg.data = str(resultado)
    pub.publish(msg)


pub = rospy.Publisher('/N2', String, queue_size=1)
sub = rospy.Subscriber('/N1', String, CallBack)

rospy.spin()