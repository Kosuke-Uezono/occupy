var graphData = {{ graph_data|tojson }};
var ctx = document.getElementById('chart').getContext('2d');

new Chart(ctx, {
    type: 'line',
    data: {
        labels: graphData.labels,
        datasets: graphData.datasets
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                stacked: true
            }
        }
    }
});
