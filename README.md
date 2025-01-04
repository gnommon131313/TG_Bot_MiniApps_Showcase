# TG_Bot_MiniApps_Showcase

Сайт работает только внутри telegram mini apps (ограничения в LocalSite_Monolith/static/js/checkApp.js)

Функционал:
Пользователь может просматривать каталог и делать заказы, которые сохраняться под его id
Вся логика реализовано очень упрощённо

Присутствует два отдельных приложения:
1)Bot - простой телеграм бот, который просто запускает телеграм приложение и также может обратиться напрямую к api сайта
2)LocalSite_Monolith - локальный сайт который будет открыт ботом в mini apps, представляет из себя простой сайт с монолит архитектурой

Для запуска:
1)Создать в Bot файл .env и указать два поля `BOT_TOKEN` и `APP_URL`
2)Запустить два приложения
3)LocalSite_Monolith будет запущен локально, но чтобы открыть его в mini apps нужен глобальный адрес, нужно использовать `cloudflared tunnel --url http://localhost:8000` чтобы не делать полный деплой, а просто предоставить временный глобальный url для локально запущенного сайта
4)Полученный url от cloudflared вставить в свое телеграм приложение `Edit Web App Url`
5)В боте команда /start
