import datetime
import io

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BlockingScheduler
from app.database import SessionLocal
from app.core.config import settings
import requests
from bs4 import BeautifulSoup
from app.models import BulkDeals


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
sched=BlockingScheduler()

def scrap_table():
    db=SessionLocal()
    url = "https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx"
    payload = {}
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    soup_data=BeautifulSoup(response.text,"html.parser")
    table_data=soup_data.find('table',id='ContentPlaceHolder1_gvbulk_deals')
    df=pd.read_html(io.StringIO(str(table_data)))
    df=df[0]

    df.rename(columns={
        "Deal Date": 'deal_date',
        "Security Code": "security_code",
        "Security Name": "security_name",
        "Client Name": "client_name",
        "Deal Type *": "deal_type",
        "Quantity": "quantity",
        "Price **": "price"}, inplace=True)
    records=[]
    for record in df.to_dict('records'):
        deal_date=datetime.datetime.strptime(record.pop('deal_date'),"%d/%m/%Y")
        data=BulkDeals(deal_date=deal_date,**record)
        db.add(data)
    db.commit()

sched.add_job(scrap_table,'interval',seconds=10)
sched.start()
