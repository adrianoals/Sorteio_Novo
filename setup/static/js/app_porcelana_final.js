document.addEventListener('DOMContentLoaded', function() {
    const botaoIniciar = document.getElementById('botao-iniciar');
    if (botaoIniciar) {
        botaoIniciar.addEventListener('click', function(event) {
            event.preventDefault();  // Evita o comportamento padrão do botão
            const loadingContainer = document.getElementById('loadingContainer');
            loadingContainer.style.display = 'block';
            
            // Submete o formulário depois de um breve delay para mostrar a animação
            setTimeout(function() {
                document.forms[0].submit();  // Isso deve acionar a reexibição dos resultados
            }, 2000);  // Ajuste este tempo conforme necessário para a animação
        });
    }
});

