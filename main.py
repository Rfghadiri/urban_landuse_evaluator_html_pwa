import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Api
GROQ_API_KEY = "Your groq API"
PROXY_URL = None

class ChatReq(BaseModel):
    message: str
    model: str
    language: str = "auto"
    project_context: dict = {}

@app.get("/api/models")
async def get_models():
    try:
        async with httpx.AsyncClient(proxies=PROXY_URL, timeout=15.0) as client:
            res = await client.get(
                "https://api.groq.com/openai/v1/models",
                headers={"Authorization": f"Bearer {GROQ_API_KEY}"}
            )
            data = res.json()
            models = [
                {"id": m["id"], "label": f"{m['id']} (Groq)"}
                for m in data.get("data", [])
                if "whisper" not in m["id"] and "guard" not in m["id"]
            ]
            if models:
                return {"models": models}
    except Exception:
        pass
    return {
        "models": [
            {"id": "llama-3.1-8b-instant", "label": "Llama 3.1 8B Instant (Groq)"},
            {"id": "llama-3.3-70b-versatile", "label": "Llama 3.3 70B Versatile (Groq)"},
            {"id": "openai/gpt-oss-120b", "label": "GPT-OSS 120B (Groq)"}
        ]
    }

@app.post("/api/ai/chat")
async def chat(req: ChatReq):
    system_prompt = (
        "تو دستیار تخصصی برنامه‌ریزی شهری هستی و به زبان فارسی پاسخ می‌دهی.\n"
        "خروجی تو باید حتماً یک آبجکت JSON معتبر با دو کلید زیر باشد:\n"
        '1. "answer": متن پاسخ فارسی به کاربر (توضیح نتیجه یا تغییر اعمال‌شده).\n'
        '2. "actions": آرایه‌ای از تغییرات درخواستی کاربر با ساختار {"target": "...", "value": ...}. اگر کاربر درخواست تغییر عددی یا متنی نداشت، آرایه خالی [] بگذار.\n\n'
        "قوانین مقداردهی target در actions:\n"
        '- تغییر جمعیت مبنای طرح -> {"target": "population", "value": 1961260}\n'
        '- تغییر نام پروژه -> {"target": "project", "value": "نام جدید"}\n'
        '- تغییر مساحت یک کاربری (مثلاً مسکونی، پارک، آموزشی، درمانی) -> {"target": "مساحت مسکونی", "value": 1500000}\n'
        '- تغییر حداقل یا حداکثر استاندارد یک کاربری -> {"target": "حداقل پارک", "value": 10} یا {"target": "حداکثر مسکونی", "value": 30}\n'
        '- تغییر پارامترهای پیش‌بینی CA-Markov -> target برابر با "سال پایه"، "سال دوم"، "سال هدف" یا "جمعیت آینده"\n\n'
        f"داده‌های فعلی پروژه در لحظه ارسال پیام: {json.dumps(req.project_context, ensure_ascii=False)}"
    )

    try:
        async with httpx.AsyncClient(proxies=PROXY_URL, timeout=30.0) as client:
            res = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                json={
                    "model": req.model,
                    "response_format": {"type": "json_object"},
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": req.message}
                    ]
                }
            )
            data = res.json()
            if res.status_code != 200:
                err_msg = data.get("error", {}).get("message", str(data))
                return {"answer": f"❌ خطای سرور Groq (کد {res.status_code}): {err_msg}", "actions": []}

            raw_content = data["choices"][0]["message"]["content"]
            parsed = json.loads(raw_content)

            return {
                "answer": parsed.get("answer", ""),
                "actions": parsed.get("actions", [])
            }

    except Exception as e:
        return {"answer": f"❌ خطای سرور پایتون: {str(e)}", "actions": []}

