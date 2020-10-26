import rospy
from std_msgs.msg import String
    
rospy.init_node('N1')
adicao = String()
matAngela = String()

def ContaCallBack (msg): 
    global adicao
    adicao = msg
    print (adicao.data)
    
def timerCallBack(event): 
    msg = String()
    msg.data = '2016013120'
    pub.publish(msg) 

    
pub = rospy.Publisher ('/N1', String, queue_size =10)
sub = rospy.Subscriber('/N2', String, ContaCallBack)
timer = rospy.Timer(rospy.Duration(0.1),timerCallBack)

rospy.spin()