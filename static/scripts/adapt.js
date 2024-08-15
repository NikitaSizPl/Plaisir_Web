const burger = document.getElementById('burger');
const navLinks = document.getElementById('nav-links');

burger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

const dokglobal = document.getElementById('doker-global');
const dokspan = document.getElementById('doker-span');

dokglobal.addEventListener('click', () => {
    dokspan.classList.toggle('active');
});
