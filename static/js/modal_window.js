document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("modal");
    const closeModalBtn = document.getElementById("closeModal");

    // Проверяем, является ли пользователь суперпользователем
    if (isSuperuser) {
        modal.style.display = "block"; // Показываем модальное окно
    }

    // Закрытие модального окна при клике на крестик
    closeModalBtn.addEventListener("click", function() {
        modal.style.display = "none";
    });

    // Закрытие модального окна при клике вне его
    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});