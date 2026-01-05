# SPDX-FileCopyrightText: 2025 asnm1208 <otomo6475@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import time

from launch import LaunchDescription
from launch_ros.actions import Node
import launch_testing
import pytest
import rclpy
from std_msgs.msg import Float32


@pytest.mark.rostest
def generate_test_description():
    talker_node = Node(
        package='mypkg',
        executable='talker',
    )
    return LaunchDescription([
        talker_node,
        launch_testing.actions.ReadyToTest(),
    ]), {'talker': talker_node}


def test_topic_data_received():
    rclpy.init()
    node = rclpy.create_node('test_node')
    received_msgs = []

    node.create_subscription(
        Float32,
        '/cpu_usage',
        lambda msg: received_msgs.append(msg),
        10
    )

    try:
        # 最大10秒間待機
        end_time = time.time() + 10.0
        while time.time() < end_time and len(received_msgs) < 1:
            rclpy.spin_once(node, timeout_sec=0.1)

        # 証拠ログを出力
        print('\n' + '='*50)
        print(f'[TEST LOG] 受信したメッセージ数: {len(received_msgs)}')
        for i, msg in enumerate(received_msgs):
            print(f'[TEST LOG] 受信データ[{i}]: {msg.data}%')
        print('='*50 + '\n')

        # データ受信の確認
        assert len(received_msgs) > 0, 'トピック /cpu_usage からデータを受信できませんでした'

        # 値の妥当性確認
        for msg in received_msgs:
            assert 0.0 <= msg.data <= 100.0, f'異常なCPU使用率を検出しました: {msg.data}'

    finally:
        node.destroy_node()
        rclpy.shutdown()
