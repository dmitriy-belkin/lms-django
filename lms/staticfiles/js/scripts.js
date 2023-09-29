// Открывает всплывающее окно с формой входа
function openLoginModal() {
    var modal = document.getElementById('login-modal');
    modal.style.display = 'block';
}

// Закрывает всплывающее окно с формой входа
function closeLoginModal() {
    var modal = document.getElementById('login-modal');
    modal.style.display = 'none';
}

// Функция для отправки запроса на авторизацию (переделайте под ваш API)
function login() {
    // Получите значения логина и пароля из формы
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Отправьте запрос на сервер для авторизации (используйте Ajax)

    // После успешной авторизации:
    // 1. Скройте форму входа
    closeLoginModal();
    // 2. Отобразите имя пользователя и кнопку "Выйти"
    var userInfo = document.getElementById('user-info');
    var userUsername = document.getElementById('user-username');
    userUsername.textContent = username;
    userInfo.style.display = 'block';
    // 3. Скройте кнопку "Войти"
    var loginButton = document.getElementById('login-button');
    loginButton.style.display = 'none';
}

// Функция для разлогинивания (переделайте под ваш API)
function logout() {
    // Отправьте запрос на сервер для разлогинивания (используйте Ajax)

    // После успешного разлогинивания:
    // 1. Скройте информацию о пользователе и кнопку "Вый
