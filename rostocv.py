import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


#function to convert images from ros format to opencv and detect edges

def image_callback(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")    

    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_image, 100, 200)  

    cv2.imshow("Edges", edges)

    cv2.waitKey(1)


def edge_detection():
    rospy.init_node('edge_detection_node', anonymous=True)     #initializes the ROS node
    rospy.Subscriber("image_topic", Image, image_callback)     #subscriber to the ROS topic, img callback is called whenever image is received
    rospy.spin()

if __name__ == '__main__':
    edge_detection()
