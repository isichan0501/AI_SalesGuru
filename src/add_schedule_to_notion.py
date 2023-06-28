"""Notionの予約データベースに予約を追加。

"""
from typing import Any, Optional, Dict, List
import datetime
from pprint import pprint
import os
from notion_client import Client
from dotenv import load_dotenv
load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])
database_id = os.environ["NOTION_DB_SCHEDULE"]


def get_week_schedule():
    my_page = notion.databases.query(
        **{
            "database_id": database_id,
            "filter": {
                "property": "予約日時",
                "date": {
                    "this_week": {},
                },
            },
        }
    )
    return my_page


def add_schedule(user: str, agent: str, site: str, date_time: datetime.datetime, memo: str = "") -> Dict:
    """DBスキーマ
    名前: title
    担当者: rich_text
    サイト: multi_select(twitter, happy, pcmax, ikukuru, email)
    予約日時: date_time(2023-06-10T12:00:00.000+09:00)
    メモ: rich_text
    """
    new_page = {
        "名前": {"title": [{"text": {"content": user}}]},
        "担当者": {"rich_text": [{"text": {"content": agent}}]},
        "サイト": {"multi_select": [{"name":site}]},
        "予約日時": {"date":{"start": date_time, "end": None}},
        "メモ": {"rich_text": [{"text": {"content": memo}}]}
    }
    res = notion.pages.create(parent={"database_id": database_id}, properties=new_page)
    return res


def get_dete_time(year: int, month: int, day: int, hour: int, minute: int) -> datetime.datetime:
    """add_scheduleの引数のdate_time用のオブジェクト生成"""
    date_time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=0, microsecond=0, tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
    return date_time.isoformat()


if __name__ == "__main__":
    my_page = get_week_schedule();print(my_page)
    res = add_schedule(user="mitu30583", agent="yuria333", site="twitter", date_time=get_dete_time(year=2023, month=6, day=12, hour=15, minute=30))
    import pdb;pdb.set_trace()
    print(res)
    