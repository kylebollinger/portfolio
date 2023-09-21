const globalMenu = document.querySelector('[data-global-nav-btn]');
globalMenu.addEventListener('click', event => {
    globalMenu.classList.toggle('active');
});