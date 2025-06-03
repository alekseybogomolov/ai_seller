# Ai-seller of auto parts

AI-продавец автозапчастей для немецких автомобилей. Отвечает на вопросы клиентов, использует знания из каталога и книги продаж, ведёт диалог в стиле настоящего менеджера, и дожимает до сделки.

## Структура проекта

```
/auto-parts-gpt/
├── data/
│   ├── catalog.json               # Каталог автозапчастей
│   ├── sales_book.json           # Речевые шаблоны продавца
├── scripts/
│   ├── embed_chunks.py           # Разбиение и векторизация чанков
│   ├── semantic_search.py        # Поиск релевантных чанков
│   ├── inference_with_context.py # Инференс с подставленным контекстом
├── prompt/
│   └── system_prompt.txt         # Системный промпт для GPT
├── examples/
│   └── sample_dialogs.md         # Примеры диалогов
├── requirements.txt
├── README.md                     # Этот файл
```

## Используемые технологии

- Python 3.10+
- OpenAI GPT-4 API
- Sentence-transformers
- FAISS


## Запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите векторизацию документов:
```bash
python scripts/embed_chunks.py
```

3. Запуск диалогов: 
```bash
python scripts/inference_with_context.py
```

## Примеры диалогов

Смотрите в [examples/sample_dialogs.md](examples/sample_dialogs.md)

## Вызов функций

Условия вызова:


- `send_invoice(details)` — вызывается, если клиент подтверждает покупку.
- `handover_to_manager(lead_data)` — вызывается, если клиент сомневается или запрашивает помощь менеджера.

