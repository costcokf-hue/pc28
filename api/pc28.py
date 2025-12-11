# api/pc28.py
import json
import os

def handler(request):
    try:
        # 读取本地 data.json
        with open(os.path.join(os.path.dirname(__file__), '..', 'data.json'), 'r') as f:
            data = json.load(f)
        
        return {
            "statusCode": 200,
            "body": json.dumps(data, ensure_ascii=False),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
