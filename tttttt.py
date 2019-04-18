#!/usr/bin/python
# coding:utf-8

import boto3
import logging
import datetime
import json
import csv
import os

# バケット名
BUCKET_NAME = "skynavigator-ccsdev-data-sz"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# S3に接続する
s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

"""
システムログ管理テーブルを更新する
@param type エラーの種類
@param information エラーメッセージ
"""


def updateSystemTable(information):
    # システムログ履歴情報
    params = ('debug', information)
    payload = {
        'params': params
    }
    # システムログ履歴情報登録新Lambdaを呼び出し
    lambdaResponse = boto3.client('lambda').invoke(
        FunctionName='createSystemLog',
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)  # jsonシリアライズ
    )


"""
ファイルパスより該当CSVファイルを取得する

@param: filepath csvファイルパス
@return: tile ヘーダ; rows データ json
"""


def lambda_handler(event, context):
    filePath = event.get("filePath")
    # 取得データを格納する
    data = {
        "title": [],  # CSVファイルの一目行
        "rows": []  # CSVファイルの一目行以下のデータ
    }
    try:
        # ファイルの内容を解析する
        rows = list()
        title = list()
        s3_resource.meta.client.download_file(BUCKET_NAME, filePath, '/tmp/serviceman.csv')
        with open('/tmp/serviceman.csv', 'r', encoding='utf-8-sig') as r:
            for key, item in enumerate(csv.DictReader(r)):
                if key == 0:
                    title = list(item.keys())
                rows.append(dict(item))
        data["title"] = title
        data["rows"] = rows
        os.remove('/tmp/serviceman.csv')
    except Exception as e:
        logger.error("getCSVFileData: " + str(e))
        updateSystemTable("Lambda getCSVFileData()" + filePath + '取得に失敗しました。')
        data = None
    return data
