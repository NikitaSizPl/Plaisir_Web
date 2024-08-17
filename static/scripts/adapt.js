document.addEventListener('DOMContentLoaded', () => {
    const burger = document.getElementById('burger');
    const navLinks = document.getElementById('nav-links');

// Открытие/ закрытие по нажатию на меню
    burger.addEventListener('click', (event) => {
        navLinks.classList.toggle('active');
        event.stopPropagation();
        });

// Закрытие по нажатию вне меню
    document.addEventListener('click', () => {
        navLinks.classList.remove('active');
        });
});


document.addEventListener('DOMContentLoaded', () => {
    const dokglobal = document.getElementById('doker-global');
    const dokspan = document.getElementById('doker-span');

// Открытие/ закрытие по нажатию на меню
    dokglobal.addEventListener('click', (event) => {
        dokspan.classList.toggle('active');
        event.stopPropagation();
    });

// Закрытие по нажатию вне меню
    document.addEventListener('click', () => {
        dokspan.classList.remove('active');
        });
});
