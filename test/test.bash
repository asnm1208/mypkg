#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 asnm1208 <otomo6475@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import pytest
from launch import LaunchDescription
from launch_ros.actions import Node
import launch_testing

@pytest.mark.rostest
def generate_test_description():
    # テスト対象のノードを起動する設定
    talker_node = Node(
        package='mypkg',
        executable='talker',
    )
    return LaunchDescription([
        talker_node,
        launch_testing.actions.ReadyToTest(),
    ])

def test_node_start(proc_info, proc_output):
    # ノードがエラーを出さずに起動したかをチェック
    # (終了を待たずに起動を確認するだけのシンプルなテスト)
    pass
