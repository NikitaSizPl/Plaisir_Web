const translates = {

'en': {
    'main': 'HOME',
    'category': 'CATEGORIES',
    'contact': 'CONTACT',
    },

'ru': {
    'main': 'ГЛАВНАЯ',
    'category': 'КАТАЛОГ',
    'contact': 'КОНТАКТЫ',
    },

'pl': {
    'main': 'STRONA GLÓWNA',
    'category': 'KATALOG',
    'contact': 'KONTAKT',
    }
};

function loadTranslations(lang) {
    const navLinks = document.querySelectorAll('#nav-links a');

    navLinks.forEach(link => {
        const langKey = link.getAttribute('lang');
        if (langKey && translates[lang]) {
            link.textContent = translates[lang][langKey];
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const btnPl = document.getElementById('btn-pl');
    const btnEn = document.getElementById('btn-en');
    const btnRu = document.getElementById('btn-ru');

    btnPl.addEventListener('click', () => loadTranslations('pl'));
    btnEn.addEventListener('click', () => loadTranslations('en'));
    btnRu.addEventListener('click', () => loadTranslations('ru'));
});


