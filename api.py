# api.py
import json
from urllib.request import urlopen, Request

def handler(request):
    try:
        req = Request(
            "https://www.52pc28.com/lottery/getLatest?game=jnd28",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        
        if data["code"] == 200:
            nums = [int(x) for x in data["data"]["opencode"].split(",")]
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "issue": data["data"]["expect"],
                    "numbers": nums,
                    "sum": sum(nums)
                }, ensure_ascii=False),
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
