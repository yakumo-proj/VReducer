# VReducer
[![MIT](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/kanno2inf/VReducer/blob/master/LICENSE)
![CircleCI](https://circleci.com/gh/kanno2inf/VReducer/tree/master.svg?style=shield&circle-token=7fdbd9bb86e45fc5715e148199427b7db095e955)
![Coverage Status](https://coveralls.io/repos/github/kanno2inf/VReducer/badge.svg?branch=master)

[VRoidStudio](https://vroid.pixiv.net/)でエクスポートされたモデルを[Cluster](https://cluster.mu/)アバター用に軽量化する非公式スクリプトです。


## 動作環境
* python 3.8.x

## 対応VRoidStudoバージョン
* 0.5.3
* 0.5.4

## 注意点
* 髪の毛メッシュを結合してエクスポートしたモデルを使用してください。
* 頂点の削減は非対応なので、頂点数を減らしたい場合はVRoidStudio上で調整をお願いします。
* ノーマルマップ、スフィアマップは削除されます。
* マテリアル結合により基本色、影色が他のマテリアルに結合されるため、一部マテリアルの色が変わる可能性があります。

## ダウンロード
* 安定版 : [Releaseページ](https://github.com/kanno2inf/VReducer/releases)からダウンロード

* 開発最新版 : [こちら](https://github.com/kanno2inf/VReducer/archive/master.zip) からダウンロード

## 準備
テクスチャ結合で[Pillow(PIL)](https://github.com/python-pillow/Pillow) とtomlライブラリを使用しているため、以下のコマンドで必要なモジュールをインストールしてください。
```
$ pip install -r requirements/prod.txt
```

## 使い方
```bash
$ python vreducer.py [VRM_FILE_PATH] [-f|--force] [-s|--replace-shade-color] [-t|--texture-size WIDTH,HEIGHT] [-h|--help] [-V|--version]
```


VRM_FILE_PATH: VRMファイルパス

-f, --force: ファイル保存時、確認なしに上書きする

-s, --replace-shade-color: 陰を消す(陰の色をライトが当たる部分の色と同色にする)

-e, --emissive-color: 光源を無視する([Clusterの一部会場でモデルが暗くなる問題](https://clusterhelp.zendesk.com/hc/ja/articles/360021584012-cluster-v1-6-14-2019-1-8-)への対策)。
このオプションを指定すると髪のハイライトが消えます。

-t, --texture-size TEXTURE_SIZE: テクスチャサイズを制限する(このサイズ以下に制限される)。TEXTURE_SIZEは幅,高さで指定(例：-t 512,512)。デフォルト2048x2048

-h, --help: ヘルプ表示

-V, --version: バージョン表示

変換後のファイルは以下のフォルダ以下に出力されます。
```
result
```

### 推奨コマンド
2018/02/06時点で[Clusterの一部会場でモデルが暗くなる問題](https://clusterhelp.zendesk.com/hc/ja/articles/360021584012-cluster-v1-6-14-2019-1-8-)が出ているため、```-e```オプション付けることを推奨します。
```bash
$ python vreducer.py VRoid.vrm -e
```

### 実行例
ファイルパス、変換前のモデル情報、変換後のモデル情報が表示されます。
```bash
$ python vreducer.py VRoid.vrm
VRoid.vrm
vrm materials: 15
materials: 15
textures: 25
images: 25
meshes: 3
primitives: 54
        Face.baked : 10
        Body.baked : 7
        Hair001.baked : 37
------------------------------
combine hair primitives...
shrink materials...
sort face primitives...
combine materials...
reduced images...
------------------------------
vrm materials: 6
materials: 6
textures: 9
images: 9
meshes: 3
primitives: 18
        Face.baked : 10
        Body.baked : 7
        Hair001.baked : 1
saved.
```
上記例では以下のパスに変換後のファイルが出力されます。
```
result/Vroid.vrm
```

## 軽量化内容
### 髪プリミティブ結合
髪の毛のプリミティブをマテリアル毎に結合します。

### マテリアル結合
#### 共通
| 結合マテリアル | 結合後のマテリアルパラメータ |
| -------------- | ------------------ |
| 顔、体、口 | 顔 |
| アイライン、まつ毛 | アイライン |
| 瞳孔、ハイライト、白目 | ハイライト |
| 髪の毛、頭皮の髪 | 髪の毛 |

| テクスチャ | 元サイズ | 変換後サイズ |
| ---------- | -------- | ------------ |
| 体 | 2048x2048 | 2048x1536 |
| 顔 | 1024x1024 | 512x512 |

#### 制服
| 結合マテリアル | 結合後のマテリアルパラメータ |
| -------------- | ------------------ |
| 制服上下、リボン、靴 | 制服の上着 |

| テクスチャ | 元サイズ | 変換後サイズ |
| ---------- | -------- | ------------ |
| 制服の上着 | 2048x2048 | 2048x1536 |


#### 制服(ズボン)
| 結合マテリアル | 結合後のマテリアルパラメータ |
| -------------- | ------------------ |
| 制服上下、リボン、靴 | 制服の上着 |

| テクスチャ | 元サイズ | 変換後サイズ |
| ---------- | -------- | ------------ |
| 制服の上着 | 2048x2048 | 2048x1024 |


#### ワンピース
| 結合マテリアル | 結合後のマテリアルパラメータ |
| -------------- | ------------------ |
| ワンピース、靴 | ワンピース |

| テクスチャ | 元サイズ | 変換後サイズ |
| ---------- | -------- | ------------ |
| ワンピース | 2048x2048 | 2048x1536 |


## 制限事項
* 非公式スクリプトのため、VRoidStudioのバージョンアップなどで使用不可能になる可能性があります。
