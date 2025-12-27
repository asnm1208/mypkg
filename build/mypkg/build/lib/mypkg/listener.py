#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 asnm1208 <otomo6475@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class CpuListener(Node):
    def __init__(self):
        super().__init__('cpu_listener')
        # 'cpu_usage' トピックを購読
        self.subscription = self.create_subscription(
            Float32,
            'cpu_usage',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        # 80%を超えたら警告を出すなどの処理も可能
        if msg.data > 80.0:
            self.get_logger().warn(f'High CPU Load: {msg.data}%')
        else:
            self.get_logger().info(f'Received CPU Usage: {msg.data}%')


def main(args=None):
    rclpy.init(args=args)
    node = CpuListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
