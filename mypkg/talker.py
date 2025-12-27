#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 asnm1208 <otomo6475@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class CpuTalker(Node):
    def __init__(self):
        super().__init__('cpu_talker')
        # 'cpu_usage' というトピック名で Float32 型のメッセージを配信
        self.publisher_ = self.create_publisher(Float32, 'cpu_usage', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        # CPU使用率をパーセントで取得
        msg.data = psutil.cpu_percent()
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing CPU Usage: {msg.data}%')


def main(args=None):
    rclpy.init(args=args)
    node = CpuTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
