#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class SampleServiceNode(Node):
    def __init__(self):
        super().__init__('sample_service_node')
        self.srv = self.create_service(AddTwoInts, 'sample_service', self.callback_sample_service)
        self.get_logger().info("SampleServiceNode started.")

    def callback_sample_service(self, request, response):
        response.success = True
        response.message = 'Hello World!'
        self.get_logger().info("Request message: " + request.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = SampleServiceNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
