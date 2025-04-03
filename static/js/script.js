// Validação do formulário
document.getElementById('task-form').addEventListener('submit', function (e) {
    const input = document.getElementById('task-name');
    if (input.value.trim() === '') {
        e.preventDefault();
        input.focus();
        input.classList.add('is-invalid');
        setTimeout(() => {
            input.classList.remove('is-invalid');
        }, 1000);
    }
});

// Efeitos de hover nos botões
document.querySelectorAll('.btn-icon').forEach(btn => {
    btn.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.1)';
    });
    btn.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
    });
});