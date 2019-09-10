// Chart drawing

getData()

function getData() {
    $.get("/chart_info", function(err, req, resp) {
            console.log(resp.responseJSON.apply_clicks)
            // draw_chart({"date_posted": ["aa", "bb"], "apply_clicks": [1, 2, 3] })
            draw_chart(resp.responseJSON)
    });
  }

function draw_chart(info) {
    var ctx = document.getElementById('chart_container').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: info.date_posted,
            datasets: [{
                label: 'lukukerrat / päivää auki',
                data: info.apply_clicks,
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