document.addEventListener('DOMContentLoaded', function() {
    revelarLinhasProgressivamente();
});

function revelarLinhasProgressivamente() {
    const linhas = document.querySelectorAll('.linha-apartamento');
    const loadingContainer = document.getElementById('loadingContainer'); // Certifique-se de que este ID corresponde ao seu HTML

    if (linhas.length > 0) {
        linhas.forEach((linha, index) => {
            setTimeout(() => {
                linha.style.opacity = 1; // Faz a linha aparecer
                linha.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

                // Se for a última linha, ajusta o scroll para o final e esconde a animação de carregamento
                if (index === linhas.length - 1) {
                    setTimeout(() => {
                        window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
                        // Esconde a animação de carregamento e o container
                        loadingContainer.style.display = 'none';
                    }, 500); // Tempo adicional para a última linha ser revelada antes de esconder a animação
                }
            }, index * 500); // Intervalo entre a revelação de cada linha
        });
    } else {
        // Se não houver linhas, esconde a animação imediatamente
        loadingContainer.style.display = 'none';
    }
}

