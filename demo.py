import uvicorn
from fastapi import FastAPI
from fastapi import Form
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
# 挂载模版文件夹
tmp = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def index():  # async加了就支持异步  把Request赋值给request
    with open('./templates/index-bak.html', 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


@app.post("/data")
async def get_data(
        request: Request,
        zid: str = Form(...),
        sid: str = Form(None),
        company_id: str = Form(None),
        start: str = Form(None),
        end: str = Form(None)
):
    """"
    sql 查询出来的数据 return出去
    """
    print(zid, sid, company_id, start, end)
    import time
    time.sleep(10)

    # return {
    #     "code": 1,
    #     "msg": "test 异常",
    #     "count": 10,
    #     "data": []
    # }
    return {
        "code": 1,
        "msg": "test 异常",
        "count": 10,
        "data": [
            {
                "zid": 1,
                "sid": 108,
                "date": "2022-08-23",
                "ordered": 305
            },
            {
                "zid": 1,
                "sid": 105,
                "date": "2022-08-24",
                "ordered": 316
            },
        ]
    }


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
