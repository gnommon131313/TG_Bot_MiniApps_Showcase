export function attachButtonEvents() {
    let tg = window.Telegram.WebApp;
    const user = tg.initDataUnsafe.user;

    // Вешаем обработчик на родительский элемент (нужно именно вешать обработчик на родительский обьект а не просто пытаться получать все кнопки с нужным id или class, тк они могут быть созданы динамически и не будут обработаны когда скрипт запуститься и не найдет их сразу)
    const container = document.getElementById('catalog-list');
    container.addEventListener('click', function(event) {
        // Проверяем, что клик произошел на кнопке с нужным классом
        if (event.target && event.target.classList.contains('create-order-btn')) {
            // Логика обработки клика
            // Получение значений из переданных атрибутов
            const productId = event.target.getAttribute('data-product-id');

            // Динамически создаем объект данных
            const data = {
                product_id: productId,
                user_id: user.id,
            };

            console.log('Клик по кнопке для товара с ID:', productId);

            // Отправка данных на сервер
            fetch('api/orders/create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(responseData => {
                alert("Ответ от сервера: " + JSON.stringify(responseData));
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
        }
    });
}