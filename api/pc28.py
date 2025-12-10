# api/pc28.py
import requests
import json

def handler(request):
    try:
        # 抓取 52pc28.com 的加拿大 PC28 最新一期
        url = "https://www.52pc28.com/lottery/getLatest?game=jnd28"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Referer": "https://www.52pc28.com/"
        }
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if data.get("code") == 200 and "data" in data:
            raw = data["data"]
            nums = [int(x) for x in raw["opencode"].split(",")]
            issue = raw["expect"]
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
        else:
            raise Exception("Invalid data")

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
