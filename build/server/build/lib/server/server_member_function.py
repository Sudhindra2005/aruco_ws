from custom_interfaces.srv import VideoFrame
import rclpy
from rclpy.node import Node
import cv2 as cv
import cv2.aruco as aruco

from cv_bridge import CvBridge
bridge = CvBridge()

import numpy as np
import sys
from sensor_msgs.msg import Image
import time
import os


class ServerNode(Node):
    def __init__(self):
        super().__init__('server_node')
        self.srv = self.create_service(VideoFrame, 'aruco_marker_data', self.extract_aruco_data_callback)
    

    def extract_aruco_data_callback(self, request, response):
        self.detector_parameters = aruco.DetectorParameters()

        self.dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

        decompressed_image = bridge.imgmsg_to_cv2(request.image)

        self.markerCorners, self.markerIDs, self.rejected = aruco.detectMarkers(
                        decompressed_image,
                        self.dictionary,
                        parameters=self.detector_parameters,
        )

        try:
            self.no_of_detected_markers = self.markerIDs.size

            self.flattened_array = []
            self.flattened_array_ids = []

            for i in range(self.no_of_detected_markers):
                for coordinate in self.markerCorners[0][0]:
                    for num in coordinate:
                        self.flattened_array.append(float(num))

            for i in range(self.no_of_detected_markers):
                self.flattened_array_ids.append(float(self.markerIDs[i][0]))

            response.corners = self.flattened_array
            response.ids = self.flattened_array_ids

        except AttributeError:
            self.get_logger().info('***No aruco marker was found in the video frame***')

        cv.imshow('Video', decompressed_image)
        self.get_logger().info('Data sent successfully')
        
        return response
    

def main(args=None):
    rclpy.init(args=args)

    server_node = ServerNode()

    rclpy.spin(server_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
