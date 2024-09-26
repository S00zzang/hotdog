from fastapi import FastAPI
from typing import Union
from fastapi.templating import Jinja2Templates
from fastapi import Request
from PIL import Image

import random

app = FastAPI()


html = Jinja2Templates(directory="public")


@app.get("/welcome")
async def root():
    return {"🌭": "Welcome to HOTDOG WORLD"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://github.com/user-attachments/assets/101129fd-b180-4532-88fa-a716139b1638"
    dog_1 = "https://github.com/user-attachments/assets/487f4de1-e3d1-47f0-a6b6-29cdd23d0eae"
    dog_2 = "https://github.com/user-attachments/assets/a12bac57-61b3-47a8-b8fe-0751461e5839"
    dog_3 = "https://github.com/user-attachments/assets/8e6fbf0e-d7cb-4239-b926-5c8e74500ed2"

    image_url = random.choice([hotdog, dog_1, dog_2, dog_3])
    return html.TemplateResponse("index.html", {"request":request, "image_url": image_url})

@app.get("/predict")
def hotdog():

    return {"YOU ARE": random.choice(["HOTDOG!", "NOT HOTDOG"])}

@app.post("/upload your ID")
async def create_upload_file(file: UploadFile):
    # 파일 저장
    img =  await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    # 이미지 바이트를 PIL 이미지로 변환
    img = Image.open(io.BytessIO(u=img))
    p = model(img)
    # TODO
    # 의존성 모듈 설치해서 오류 없이 서버 가동
    # if predictions 값이 배열과 같이 나오면 높은 확률의 값을 추출해서 리턴하기

    return {"Hi": p}
