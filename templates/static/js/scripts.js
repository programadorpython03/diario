document.addEventListener('DOMContentLoaded', function () {
    // Gráfico 1: Quantidade de diários por pessoa
    const ctx1 = document.getElementById('myChart');
    if (ctx1) {
        // Recupera os dados do Django usando JSON
        const nomes = JSON.parse(document.getElementById('nomes').textContent);
        const qtds = JSON.parse(document.getElementById('qtds').textContent);

        new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: nomes,
                datasets: [{
                    data: qtds,
                    label: 'Quantidade por pessoa',
                    borderWidth: 1,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    hoverBackgroundColor: 'rgba(54, 162, 235, 0.4)',
                    hoverBorderColor: 'rgba(54, 162, 235, 1)',
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Gráfico 2: Quantidade de diários por mês
    const ctx2 = document.getElementById('myChart2');
    if (ctx2) {
        // Recupera os dados do Django usando JSON
        const meses = JSON.parse(document.getElementById('meses').textContent);
        const qtd_diarios_por_mes = JSON.parse(document.getElementById('qtd_diarios_por_mes').textContent);

        new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: meses,
                datasets: [{
                    label: 'Quantidade de Diários',
                    data: qtd_diarios_por_mes,
                    borderWidth: 1,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    hoverBackgroundColor: 'rgba(255, 99, 132, 0.4)',
                    hoverBorderColor: 'rgba(255, 99, 132, 1)',
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    // Recupera os elementos de entrada e do link
    const input = document.getElementById('data');
    const link = document.getElementById('link');

    // Adiciona um listener de evento para quando a data é alterada
    input.addEventListener('input', () => {
        const data = input.value;
        if (data) {
            link.href = `/diario/dia?data=${data}`;
        } else {
            link.href = "#";
        }
    });

    // Adiciona um listener para o clique no link
    link.addEventListener('click', (e) => {
        if (!input.value) {
            e.preventDefault();
            alert('Por favor, selecione uma data antes de continuar.');
        }
    });
});
