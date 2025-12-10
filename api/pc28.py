# api/pc28.py
import requests
import json

def pc28(request):
    # 抓取 52pc28.com 的加拿大 PC28 最新一期数据
    SOURCE_URL = "https://www.52pc28.com/lottery/getLatest?game=jnd28"
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.52pc28.com/",
            "Accept": "application/json"
        }
        r = requests.get(SOURCE_URL, timeout=10, headers=headers)
        r.raise_for_status()
        data = r.json()
        
        if data.get("code") == 200 and "data" in data:
            raw = data["data"]
            numbers = [int(x) for x in raw["opencode"].split(",")]
            issue = raw["expect"]
            total = sum(numbers)
            
            result = {
                "issue": issue,
                "numbers": numbers,
                "sum": total
            }
            return (
                json.dumps(result, ensure_ascii=False),
                200,
                {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            )
        else:
            raise Exception("Invalid response from source")
            
    except Exception as e:
        return (
            json.dumps({"error": str(e)}),
            500,
            {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        )
