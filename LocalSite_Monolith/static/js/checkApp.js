export function isTgWebApp() {
    // Проверка на запуск сайта внутри телеграма (через Mini Apps)
    if (window.Telegram && window.Telegram.WebApp) {
        let tg = window.Telegram.WebApp;
        const user = tg.initDataUnsafe.user;

        if (user) {
            alert(user.id);
            return true;
        } else {
            alert('user data is empty');
            return false;
        }
    } else {
        alert('WebApp not found');
        return false;
    }
}
