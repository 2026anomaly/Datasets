# -*- coding: utf-8 -*-
"""从 NASA POWER 拉取逐小时气象数据。

用法：
    python fetch_nasa_power.py --lat 29.56 --lon 106.55 --out chongqing.csv
    python fetch_nasa_power.py --lat 29.56 --lon 106.55 --start 20150101 --end 20241231

说明：
- 数据源为 NASA POWER（power.larc.nasa.gov），底层是 MERRA-2 再分析资料。
- 免费、免注册，无需 API Key。
- 服务器偶发 SSL 断连（curl exit 35），重试 2~3 次即可成功。
- 返回的 CSV 前若干行是文件头，数据从以 YEAR 开头的那一行开始。
"""
from __future__ import annotations

import argparse
import sys
import time
import urllib.error
import urllib.request

API = "https://power.larc.nasa.gov/api/temporal/hourly/point"

# 常用参数，需要别的去官网查参数表
DEFAULT_PARAMS = [
    "T2M",                # 2 米气温 (℃)
    "RH2M",               # 2 米相对湿度 (%)
    "WS2M",               # 2 米风速 (m/s)
    "PS",                 # 地面气压 (kPa)
    "PRECTOTCORR",        # 修正降水量 (mm/h)
    "ALLSKY_SFC_SW_DWN",  # 全天空短波辐照 (W/m^2)
]


def fetch(lat: float, lon: float, start: str, end: str,
          params: list[str] | None = None,
          community: str = "RE",
          retries: int = 3,
          timeout: int = 180) -> str:
    """返回原始 CSV 文本（含文件头）。"""
    params = params or DEFAULT_PARAMS
    url = (
        f"{API}?parameters={','.join(params)}"
        f"&community={community}"
        f"&longitude={lon}&latitude={lat}"
        f"&start={start}&end={end}&format=CSV"
    )

    last_err = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(url, timeout=timeout) as r:
                text = r.read().decode("utf-8", errors="replace")
            if "YEAR," in text:
                return text
            last_err = RuntimeError("返回内容不含数据表头，可能被限流")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = e
        print(f"  第 {attempt} 次失败：{last_err}，重试中…", file=sys.stderr)
        time.sleep(3)

    raise RuntimeError(f"拉取失败（{retries} 次）：{last_err}")


def main():
    ap = argparse.ArgumentParser(description="拉取 NASA POWER 逐小时气象数据")
    ap.add_argument("--lat", type=float, required=True, help="纬度，如 29.56")
    ap.add_argument("--lon", type=float, required=True, help="经度，如 106.55")
    ap.add_argument("--start", default="20150101", help="起始日期 YYYYMMDD")
    ap.add_argument("--end", default="20241231", help="结束日期 YYYYMMDD")
    ap.add_argument("--out", required=True, help="输出文件路径")
    ap.add_argument("--retries", type=int, default=3)
    args = ap.parse_args()

    print(f"拉取中：lat={args.lat}, lon={args.lon}, {args.start}~{args.end}")
    text = fetch(args.lat, args.lon, args.start, args.end, retries=args.retries)
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    n = sum(1 for line in text.splitlines() if line[:4].isdigit())
    print(f"完成：{args.out}（{n} 条记录）")


if __name__ == "__main__":
    main()
