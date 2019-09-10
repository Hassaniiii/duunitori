// Chart drawing

window.onload = function() {
    getData()
}

function getData() {
    $.get("/chart_info", function(err, req, resp) {
            draw_chart(resp.responseJSON)
    });
  }

function draw_chart(info) {
    var ctx = document.getElementById('chart_container').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Object.keys(Object.values(info)[0]),
            datasets: [{
                label: 'lukukerrat / päivää auki',
                data: Object.values(Object.values(info)[0]),
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}