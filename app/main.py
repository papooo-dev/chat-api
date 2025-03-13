from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class ChatRequest(BaseModel):
    character: str
    user_input: str


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # 1) 캐릭터별 시스템프롬프트/메모리 불러오기
    # 2) RAG(선택) or 단순 OpenAI API Call
    # 3) 결과 반환
    response = "임시 답변"
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
