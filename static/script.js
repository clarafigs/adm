// Função para validação de formulário de cadastro de usuário
function validateUserForm() {
    const loginUser = document.getElementById('loginUser').value;
    const senha = document.getElementById('senha').value;
    const tipoUser = document.getElementById('tipoUser').value;

    // Validação simples: checar se os campos estão preenchidos
    if (loginUser === '' || senha === '' || tipoUser === '') {
        alert('Por favor, preencha todos os campos.');
        return false;  // Impede o envio do formulário
    }

    // Regras adicionais (como a força da senha) podem ser incluídas aqui
    if (senha.length < 6) {
        alert('A senha deve ter pelo menos 6 caracteres.');
        return false;
    }

    return true;  // Permite o envio do formulário
}

// Função para validação de formulário de cadastro de produto
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

// Exibir uma mensagem de confirmação ao deletar um produto
function confirmDelete() {
    return confirm('Tem certeza de que deseja excluir este produto?');
}

// Mostrar ou esconder senha no campo de login/cadastro
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

// Função para controlar o número de produtos que um usuário pode cadastrar
function checkUserProductLimit(tipoUser) {
    const productCount = document.querySelectorAll('.product-item').length;
    const userType = tipoUser || document.getElementById('tipoUser').value;

    if (userType === 'normal' && productCount >= 3) {
        alert('Usuários normais só podem cadastrar até 3 produtos.');
        return false;
    }

    return true;
}

// Exemplo de função para interagir com uma API (caso precise de chamadas AJAX)
// function fetchProducts() {
//     fetch('/api/products')
//         .then(response => response.json())
//         .then(data => {
//             console.log('Lista de produtos:', data);
//         })
//         .catch(error => console.error('Erro ao buscar produtos:', error));
// }
