# api/pc28.py
import json
from urllib import request, parse
from urllib.error import URLError, HTTPError

def handler(request):
    try:
        url = "https://www.52pc28.com/lottery/getLatest?game=jnd28"
        req = request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Referer": "https://www.52pc28.com/"
            }
        )
        with request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())

        if data.get("code") == 200 and "data" in data:
            raw = data["data"]
            nums = [int(x) for x in raw["opencode"].split(",")]
            issue = raw["expect"]
            total = sum(nums)

            return {
                "statusCode": 20etesting
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
        else:
            raise Exception("Invalid response")

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
