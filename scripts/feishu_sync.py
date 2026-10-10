#!/usr/bin/env python3
"""把本包产出的归档/清单同步到飞书群（自定义机器人卡片消息）。

用法:
    python feishu_sync.py <文件路径> [--mode task|archive|awaken|career]

前置:
    1) pip install requests
    2) 把 config.example.json 复制为 config.json，填入飞书自定义机器人 webhook

说明:
    - 本脚本只是"把已经产出的文件推到飞书"，不生成内容、不做任何决策。
    - 卡片正文最多展示 2000 字，超出部分截断（飞书单卡片限制）。
    - 推送前会脱敏检查：发现疑似 webhook/token 字样会中止。
"""

import argparse
import json
import os
import sys

try:
    import requests
except ImportError:
    sys.exit("缺少依赖：请先执行 pip install requests")

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
MAX_CONTENT = 2000

COLOR_MAP = {
    "task": "blue",
    "archive": "orange",
    "awaken": "red",
    "career": "violet",
}
MODE_LABEL = {
    "task": "执行清单",
    "archive": "归档",
    "awaken": "觉醒",
    "career": "求职",
}
SENSITIVE_HINTS = ("webhook", "token", "secret", "access_key")


def load_config():
    if not os.path.exists(CONFIG_PATH):
        sys.exit(
            "未找到 config.json。请复制 config.example.json 为 config.json 并填入 webhook_url。"
        )
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    if not cfg.get("webhook_url") or "xxxxxxxx" in cfg["webhook_url"]:
        sys.exit("config.json 里的 webhook_url 未填写。")
    return cfg


def redact(text: str) -> str:
    """粗粒度脱敏：把可能含凭据的行整行替换。"""
    lines = []
    for line in text.splitlines():
        low = line.lower()
        if any(h in low for h in SENSITIVE_HINTS):
            lines.append("[已脱敏]")
        else:
            lines.append(line)
    return "\n".join(lines)


def build_payload(file_path: str, content: str, mode: str) -> dict:
    name = os.path.basename(file_path)
    shown = redact(content[:MAX_CONTENT])
    if len(content) > MAX_CONTENT:
        shown += "\n\n…（内容超长已截断，请查看本地文件）"
    return {
        "msg_type": "interactive",
        "card": {
            "config": {"wide_screen_mode": True},
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": "鲁大魔方法论 | {} · {}".format(MODE_LABEL.get(mode, mode), name),
                },
                "template": COLOR_MAP.get(mode, "blue"),
            },
            "elements": [
                {"tag": "div", "text": {"tag": "lark_md", "content": shown}},
                {"tag": "hr"},
                {
                    "tag": "note",
                    "elements": [
                        {
                            "tag": "plain_text",
                            "content": "本卡片由本地技能包生成，内容未经事实核验，仅供参考。",
                        }
                    ],
                },
            ],
        },
    }


def main():
    parser = argparse.ArgumentParser(description="同步归档文件到飞书")
    parser.add_argument("file_path", help="要同步的文件路径")
    parser.add_argument("--mode", default="task", choices=list(COLOR_MAP.keys()))
    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        sys.exit("文件不存在: {}".format(args.file_path))

    with open(args.file_path, "r", encoding="utf-8") as f:
        content = f.read()

    cfg = load_config()
    payload = build_payload(args.file_path, content, args.mode)

    try:
        resp = requests.post(
            cfg["webhook_url"],
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            timeout=10,
        )
    except requests.RequestException as e:
        sys.exit("请求失败: {}".format(e))

    ok = False
    try:
        ok = resp.json().get("code") == 0
    except ValueError:
        pass

    if ok:
        print("已同步: {}".format(os.path.basename(args.file_path)))
    else:
        print("飞书返回异常，状态码 {}：{}".format(resp.status_code, resp.text[:300]))
        sys.exit(1)


if __name__ == "__main__":
    main()
