document.addEventListener('DOMContentLoaded', function () {
    console.log("JavaScript para ng_final carregado.");

    function iniciarSorteio() {
        // Oculta mensagens existentes
        var mensagens = document.querySelector('.messages');
        if (mensagens) mensagens.style.display = 'none';

        // Mostra a animação de carregamento
        document.getElementById('loadingContainer').style.display = 'block';

        // Oculta o formulário de sorteio para evitar múltiplas submissões
        document.getElementById('botao-iniciar').style.display = 'none';

        // Espera 5 segundos antes de submeter o formulário
        setTimeout(function() {
            // Submete o formulário, enviando a requisição POST para o servidor
            document.getElementById('formulario-sorteio').submit();
        }, 5000); // 5000 milissegundos = 5 segundos
    }

    function mostrarResultados() {
        var resultadosContainer = document.getElementById('resultadosContainer');
        var resultadoRows = document.querySelectorAll('.resultado-row');
        var index = 0;

        function mostrarProximaLinha() {
            if (index < resultadoRows.length) {
                resultadoRows[index].style.display = 'flex';
                index++;
                setTimeout(mostrarProximaLinha, 500); // Mostra a próxima linha após 500ms
            } else {
                document.getElementById('loadingContainer').style.display = 'none';
                document.getElementById('sorteioFinalizadoContainer').style.display = 'block';
                document.getElementById('qrCodeContainer').style.display = 'block';
            }
        }

        resultadosContainer.style.display = 'block';
        mostrarProximaLinha();
    }

    // Adiciona o ouvinte de evento ao botão de sorteio
    document.getElementById('botao-iniciar').addEventListener('click', function(event) {
        event.preventDefault(); // Previne o comportamento padrão do botão
        iniciarSorteio();
    });

    // Chama mostrarResultados se o sorteio já foi iniciado
    if (document.getElementById('resultadosContainer').style.display !== 'none') {
        mostrarResultados();
    }
});
