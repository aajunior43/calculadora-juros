// Função para calcular juros chamada quando o botão no formulário é clicado
function calcularJuros() {
    // Obtém os valores do usuário do formulário
    const principal = parseFloat(document.getElementById('principal').value);
    const taxa = parseFloat(document.getElementById('taxa').value) / 100; // Converte percentual para decimal
    const tempo = parseFloat(document.getElementById('tempo').value);

    // Calcula juros simples
    const jurosSimples = principal * taxa * tempo;

    // Calcula juros compostos
    const montanteComposto = principal * Math.pow((1 + taxa), tempo);
    const jurosComposto = montanteComposto - principal;

    // Mostra os resultados na página
    document.getElementById('resultado-juros').innerHTML = `
        <p>Juros Simples: R$ ${jurosSimples.toFixed(2)}</p>
        <p>Juros Compostos: R$ ${jurosComposto.toFixed(2)}</p>
    `;
}
