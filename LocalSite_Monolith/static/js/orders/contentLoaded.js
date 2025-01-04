export function initializeOnContentLoaded() {
    let tg = window.Telegram.WebApp;
    const user = tg.initDataUnsafe.user;

    // Тут после ? передаеться аргумент для функции которая привязана к api (не совсем передаеться а скорее становиться частью строки а далее функция на сророне api сама достанет нужные значения из строки)
    fetch(`api/order?user_id=${user.id}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось загрузить данные');
        }
        return response.json(); // Парсим JSON-ответ
    })
    .then(data => {
        // Вывод в консоль браузера (F12 что посмотреть)
        console.log(data);

        // Очищаем таблицу перед добавлением новых данных
        const newList = document.getElementById('orders-list');
        newList.innerHTML = '';

        // Заполняем таблицу полученными данными
        data.orders.forEach(function(order) {
            let row = `<tr>
                <td>${order.id}</td>
                <td>${order.date}</td>
                <td>${order.total}</td>
                <td>${order.product_id}</td>
                <td>${order.status}</td>
            </tr>`;
            newList.insertAdjacentHTML('beforeend', row);
        });
    })
    .catch(error => {
        alert(error.message);
    });
}