# mypkg
本リポジトリは千葉工業大学 未来ロボティクス学科 2025年度 ロボットシステム学内で行った内容に基づいて作成された練習用リポジトリです。  

# CPUチェッカー

## 概要
ROS 2を用いて、PCのCPU使用率をパブリッシュし、別ノードで購読・表示するパッケージです。  
![test](https://github.com/asnm1208/mypkg/actions/workflows/test.yml/badge.svg)  
- talkerノード: `psutil`ライブラリを使用してCPU使用率を取得し、`/cpu_usage`トピックへパブリッシュします。  
- listenerノード: `/cpu_usage`トピックをサブスクライブし、標準出力に表示します。  

## 推奨環境
- OS: Ubuntu 24.04 LTS
- ROS 2 バージョン: Jazzy Jalisco
- Python 3.12
- Pythonライブラリ: python3-psutil

## 使い方
1. TalkerとListenerを同時に起動（Launchファイル）  
```bash
$ ros2 launch mypkg talk_listen.launch.py
```
実行例
```
$ ros2 launch mypkg talk_listen.launch.py
 [talker-1] [INFO] [1767580404.951161764] [cpu_talker]: Publishing CPU Usage: 5.0%
 [listener-2] [INFO] [1767580404.951177775] [cpu_listener]: Received CPU Usage: 5.0%
 [talker-1] [INFO] [1767580405.903514188] [cpu_talker]: Publishing CPU Usage: 0.5%
 [listener-2] [INFO] [1767580405.904432249] [cpu_listener]: Received CPU Usage: 0.5%
 [talker-1] [INFO] [1767580406.903105790] [cpu_talker]: Publishing CPU Usage: 0.1%
```

2. 個別に起動する場合  
Talker (送信側)
```bash
$ ros2 run mypkg talker
```
Listener (受信側)
```bash
$ ros2 run mypkg listener
```

## 通信仕様
- トピック名: /cpu_usage  
- メッセージ型: std_msgs/msg/Float32  
- 更新頻度: 1.0 Hz

## テスト環境
テストの実施環境や詳細な検証内容については、こちらのテスト報告書を参照してください。

## 著作権・ライセンス
- このソフトウェアパッケージは、GNU General Public License v3.0 (GPL-3.0-only) の下、再頒布および使用が許可されています。
- ©2025 asnm1208
