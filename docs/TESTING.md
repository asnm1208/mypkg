# テスト報告書

本パッケージでは、以下の環境および項目でテストを行っています。

## 1. テスト環境
### ローカル環境
- **OS**: Ubuntu 24.04.3 LTS
- **ROS 2**: Jazzy Jalisco

### CI環境 (GitHub Actions)
- **環境**: Ubuntu 24.04 (runs-on: ubuntu-24.04)
- **ROS 2 コンテナ**: `ros:jazzy-ros-base`

## 2. 自動テスト項目
以下の項目について、プッシュごとに自動テストを実施しています。

- **静的解析**:
  - `ament_copyright`: 著作権およびライセンス情報の有無
  - `ament_flake8`: PEP 8に基づいたコードスタイルの遵守
  - `ament_pep257`: Python docstringの記述形式
- **動作検証 (Integration Test)**:
  - ノードの正常起動確認
  - **トピック疎通確認**: テスト用サブスクライバを用い、`/cpu_usage` からデータが送受信されているかを検証。
  - **データ妥当性チェック**: 受信したCPU使用率が 0.0% 〜 100.0% の範囲内であることを保証。
