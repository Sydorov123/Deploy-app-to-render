# Deploy-app-to-render

Цей проєкт представляє простий API, який розгорнуто на платформі Render. Він використовує базу даних PostgreSQL для зберігання даних про продукти. Основна мета — надати зручний інтерфейс для роботи з продуктами через HTTP-запити.

---

## Інструкції з розгортання

### Клонування репозиторію

Спершу скопіюйте репозиторій у вашу локальну директорію за допомогою команди:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

---

### Налаштування змінних середовища

Створіть файл `.env` у кореневій папці проєкту та вкажіть у ньому URL вашої бази даних у такому форматі:

```env
DATABASE_URL=postgres://username:password@hostname:port/dbname
```

Пояснення полів:
- **username** — Ім’я користувача бази даних.
- **password** — Пароль для доступу до бази даних.
- **hostname** — Адреса сервера бази даних.
- **port** — Номер порту.
- **dbname** — Назва бази даних.

Ці параметри будуть надані хостинговою платформою Render або іншим сервісом.

---

### Розгортання на Render

1. Зареєструйтесь або увійдіть до акаунта на [Render](https://render.com/).
2. Перейдіть до розділу "Web Services" та натисніть `New Web Service`.
3. Виберіть репозиторій вашого проєкту з підключеного GitHub акаунта.
4. Налаштуйте змінні середовища, наприклад, додайте `DATABASE_URL` у розділі `Environment Variables`.
5. Запустіть процес розгортання, натиснувши кнопку `Deploy`.

Після завершення Render надасть вам URL для доступу до вашого API.

---

## Як використовувати API

### Основний URL API

Ваш API буде доступний за посиланням:
```
https://your-render-app-url.com/api/v1
```

---

### Приклад запиту

Ендпоінт для отримання списку продуктів:
- **URL**: `/api/v1/productentitiestool-ui-admin/partner/getAll`
- **Метод**: `POST`

**Приклад запиту через cURL**:

```bash
curl 'https://your-render-app-url.com/api/v1/productentitiestool-ui-admin/partner/getAll' \
  -X 'POST' \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"' \
  -H 'pragma: no-cache' \
  -H 'z-currency: USD' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'content-type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'Referer: https://admin.spaceship.net/' \
  -H 'z-lang: en-US' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -d '{
    "filters": {},
    "pagination": {
      "page": 1,
      "pageSize": 10
    }
  }'
```

Не забудьте замінити `your-render-app-url.com` на реальну адресу вашого API.

---



