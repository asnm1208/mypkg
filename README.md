# mypkg
本リポジトリは千葉工業大学 未来ロボティクス学科 2025年度 ロボットシステム学内で行った内容に基づいて作成された練習用リポジトリです。  

# CPUチェッカー

## 概要
ROS 2を用いて、PCのCPU使用率をパブリッシュし、別ノードで購読・表示するパッケージです。  
![test](https://github.com/asnm1208/mypkg/actions/workflows/test.yml/badge.svg)  
- **talkerノード**: `psutil`ライブラリを使用してCPU使用率を取得し、`/cpu_usage`トピックへパブリッシュします。  
- **listenerノード**: `/cpu_usage`トピックをサブスクライブし、標準出力に表示します。  

## 推奨環境
- OS: Ubuntu 24.04 LTS
- ROS 2 バージョン: Jazzy Jalisco

## 使い方
1. TalkerとListenerを同時に起動（Launchファイル）  
```bash
$ ros2 launch mypkg talk_listen.launch.py
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
### 1. ローカル環境
- **OS**: Ubuntu 24.04.3 LTS
- **ROS 2**: Jazzy Jalisco
- **Python**: 3.12.x
- **依存確認済みライブラリ**: `python3-psutil`

### 2. CI環境 (GitHub Actions)
GitHub Actionsを利用し、プッシュごとに以下の環境で自動テスト（Lintおよび起動テスト）を実施しています。
- **ベース環境**: Ubuntu 24.04 (runs-on: ubuntu-24.04)
- **ROS 2 コンテナ**: `ros:jazzy-ros-base`
- **確認項目**:
  - `ament_copyright`: 著作権およびライセンス情報の有無
  - `ament_flake8`: PEP 8に基づいたコードスタイルの遵守
  - `ament_pep257`: Python docstringの記述形式
  - `launch_testing`: ノードの正常起動およびトピックの生存確認

## 著作権・ライセンス
- このソフトウェアパッケージは、GNU General Public License v3.0 (GPL-3.0-only) の下、再頒布および使用が許可されています。
- ©2025 asnm1208
