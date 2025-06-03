import openai
import json
from semantic_search import search 

# Описание доступных функций для GPT
functions = [
    {
        "name": "send_invoice",
        "description": "Отправка счета и реквизитов оплаты",
        "parameters": {
            "type": "object",
            "properties": {
                "product_article": {"type": "string"},
                "contact": {"type": "string", "description": "Email/телефон клиента"}
            },
            "required": ["product_article", "contact"]
        }
    },
    {
        "name": "handover_to_manager",
        "description": "Передача лида менеджеру",
        "parameters": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "enum": ["complex_question", "manager_request", "compatibility_check"]
                },
                "contact": {"type": "string"},
                "product_article": {"type": "string"}
            },
            "required": ["reason", "contact"]
        }
    }
]

# Отправка запроса в GPT с учетом истории и контекста
def get_gpt_response(query, history):
    context = "\n".join(search(query))  # semantic search
    system_prompt = open('../prompt/system_prompt.txt').read()

    messages = [
        {"role": "system", "content": f"{system_prompt}\n\nCONTEXT:\n{context}"},
        *history,
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        functions=functions,
        temperature=0.5
    )

    return response["choices"][0]["message"]

# Имитация отправки счета
def send_invoice(product_article: str, contact: str):
    print(f"Счет отправлен: {product_article} -> {contact}")
    return {"status": "invoice_sent"}

# Имитация передачи заявки менеджеру
def handover_to_manager(reason: str, contact: str, product_article=""):
    print(f"Передача менеджеру: причина={reason}, контакт={contact}, артикул={product_article}")
    return {"status": "handover_complete"}

# Пример вызова
if __name__ == "__main__":
    query = "Можете прислать счет на тормозные диски для Audi на номер +79998887766?"
    history = []

    response = get_gpt_response(query, history)

    if "function_call" in response:
        func_name = response["function_call"]["name"]
        args = json.loads(response["function_call"]["arguments"])

        if func_name == "send_invoice":
            send_invoice(**args)
        elif func_name == "handover_to_manager":
            handover_to_manager(**args)
        else:
            print(f"Неизвестная функция: {func_name}")
    else:
        print("GPT ответил текстом:", response.get("content"))
