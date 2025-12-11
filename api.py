# api.py
import json
from urllib.request import urlopen, Request

def handler(request):
    try:
        url = "https://www.52pc28.com/lottery/getLatest?game=jnd28"
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        
        if data.get("code") == 200:
            nums = [int(x) for x in data["data"]["opencode"].split(",")]
            issue = data["data"]["expect"]
            total = sum(nums)
            
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "issue": issue,
                    "numbers": nums,
                    "sum": total
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
