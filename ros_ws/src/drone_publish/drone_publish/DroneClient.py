#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial


class DroneClientNode(Node):
    def __init__(self):
        super().__init__('drone_client')
        self.client = self.create_client(AddTwoInts, 'drone_client')
        self.call_add_two_ints(6, 7)

    def call_add_two_ints(self, a, b):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn('Waiting for service to run operation')
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client.call_async(request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, a, b))

    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info('Result: %s' % response.sum)
        except Exception as e:
            self.get_logger().error('Exception: %s' % str(e))


def main(args=None):
    rclpy.init(args=args)
    node = DroneClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
