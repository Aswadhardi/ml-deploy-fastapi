from fastapi import FastAPI
import uvicorn

app  = FastAPI(title='Ping')


@app.get('/ping')
def ping():
    return 'Pong'



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")