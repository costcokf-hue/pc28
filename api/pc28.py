# api/pc28.py
import requests
import json

def handler(request):
    try:
        # 直接请求 52pc28.com
        resp = requests.get(
            "https://www.52pc28.com/lottery/getLatest?game=jnd28",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=8
        )
        data = resp.json()

        if data["code"] == 200:
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
