// Desliza a página até o topo
function scrollTop() {
    document.documentElement.scrollTop = 0;
}

// Feedback caso ocorra erros nos inputs do cadastro
const email_error = document.querySelector('div#email-error');
const senha_error = document.querySelector('div#senha-error');
const recaptcha_error = document.querySelector('div#senha-error');
if (email_error) {
    $('#email').addClass('input-error');
}
if (senha_error) {
    $('#confirma_senha').addClass('input-error');
}
if (recaptcha_error) {
    $('.recaptcha-checkbox-border').addClass('input-error');
}