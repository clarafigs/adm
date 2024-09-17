
function validateUserForm() {
    const loginUser = document.getElementById('loginUser').value;
    const senha = document.getElementById('senha').value;
    const tipoUser = document.getElementById('tipoUser').value;


    if (loginUser === '' || senha === '' || tipoUser === '') {
        alert('Por favor, preencha todos os campos.');
        return false;  // Impede o envio do formulário
    }


    if (senha.length < 6) {
        alert('A senha deve ter pelo menos 6 caracteres.');
        return false;
    }

    return true;
}


function validateProductForm() {
    const nomeProduto = document.getElementById('nomeProduto').value;
    const quantidade = document.getElementById('quantidade').value;
    const preco = document.getElementById('preco').value;

    if (nomeProduto === '' || quantidade === '' || preco === '') {
        alert('Por favor, preencha todos os campos do produto.');
        return false;
    }

    if (quantidade <= 0) {
        alert('A quantidade deve ser maior que 0.');
        return false;
    }

    if (preco <= 0) {
        alert('O preço deve ser maior que 0.');
        return false;
    }

    return true;
}


function confirmDelete() {
    return confirm('Tem certeza de que deseja excluir este produto?');
}


function togglePasswordVisibility() {
    const senhaField = document.getElementById('senha');
    const toggleButton = document.getElementById('togglePassword');

    if (senhaField.type === 'password') {
        senhaField.type = 'text';
        toggleButton.textContent = 'Esconder Senha';
    } else {
        senhaField.type = 'password';
        toggleButton.textContent = 'Mostrar Senha';
    }
}

function checkUserProductLimit(tipoUser) {
    const productCount = document.querySelectorAll('.product-item').length;
    const userType = tipoUser || document.getElementById('tipoUser').value;

    if (userType === 'normal' && productCount >= 3) {
        alert('Usuários normais só podem cadastrar até 3 produtos.');
        return false;
    }

    return true;
}


