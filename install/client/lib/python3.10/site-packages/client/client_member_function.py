from custom_interfaces.srv import VideoFrame
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge

bridge = CvBridge()

import cv2 as cv
import cv2.aruco as aruco
import numpy as np
import sys
from sensor_msgs.msg import Image
import time
import os


class ClientNode(Node):
    
    def __init__(self):
        super().__init__('client_node')
        self.cli = self.create_client(VideoFrame, 'aruco_marker_data')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.req = VideoFrame.Request()


    def send_request(self, msg):        
        self.req.image = msg

        self.future = self.cli.call_async(self.req)
    
        return self.future.result()
    


def main(args=None):
    rclpy.init(args=args)

    filePath = input('Enter path of the video file: ')
    capture = cv.VideoCapture(filePath)

    if capture.isOpened() == False:
        print('Video could not be opened.')
    
    while(capture.isOpened()):
        isTrue, frame = capture.read()

        msg = bridge.cv2_to_imgmsg(frame)

        if isTrue == True:
            client_node = ClientNode()
            client_node.send_request(msg)

            while rclpy.ok():
                rclpy.spin_once(client_node)
                if client_node.future.done():
                    try:
                        response = client_node.future.result()
                    except Exception as e:
                        client_node.get_logger().info(
                            "Service call failed %r" % (e,)
                        )
                    else:
                        client_node.get_logger().info('Successfully received')
                    break

        array_size = int(len(response.corners)/8)

        third_dim = []
        second_dim = []
        first_dim = []

        i = 0

        for length in range(array_size):
            for width in range(4):
                for height in range(2):
                    first_dim.append(response.corners[i])
                    i += 1
                second_dim.append(first_dim)
                first_dim = []
            third_dim.append(second_dim)
            second_dim = []

        print('Total no. of detected markers: %d' % (array_size))
            
        for i in range(array_size):
            print('\nFeatures of detected marker_%d: ' % (i)) 
            print('Marker ID: %d' % (response.ids[i]))
            print('Coordinates of corner points: ')
            print('Top-left: {}\nTop-right: {}\nBottom-right: {}\nBottom-left: {}'.format(
                third_dim[i][0], third_dim[i][1], third_dim[i][2], third_dim[i][3]))
        print('---------------------------------------------------------------')


    client_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

