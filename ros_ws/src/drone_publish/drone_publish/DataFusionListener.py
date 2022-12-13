#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class DataFusionListenerNode(Node):
    def __init__(self):
        super().__init__('DataFusionListener')
        self.subscriber = self.create_subscription(String, "DroneTalker", self.callback_drone_talker, 10)
        self.get_logger().info('data_fusion_listener started 2')

    def callback_drone_talker(self, msg: String):
        self.get_logger().info('data_fusion_listener received: {}'.format(msg.data))
        self.get_logger().info('data_fusion_listener done')


def main(args=None):
    rclpy.init(args=args)
    node = DataFusionListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
