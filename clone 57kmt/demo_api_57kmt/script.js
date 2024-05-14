document.addEventListener('DOMContentLoaded', function () {
    fetch('api.aspx')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log(data); // Ghi nhật ký dữ liệu trả về để kiểm tra

            if (data.ok !== 1) {
                throw new Error('API returned an error: ' + data.msg);
            }

            let labels = [];
            let tempValues = [];
            let humidityValues = [];
            let currentTemp = null;
            let currentHumidity = null;

            data.data.forEach(item => {
                if (!labels.includes(item.time)) {
                    labels.push(item.time);
                }

                if (item.sid == 1) {
                    tempValues.push(item.value);
                    currentTemp = item.value; // Cập nhật nhiệt độ hiện tại
                    humidityValues.push(null);
                } else if (item.sid == 2) {
                    tempValues.push(null);
                    humidityValues.push(item.value);
                    currentHumidity = item.value; // Cập nhật độ ẩm hiện tại
                }
            });

            // Hiển thị nhiệt độ và độ ẩm hiện tại
            document.getElementById('currentTemp').innerText = currentTemp ? currentTemp + '°C' : 'N/A';
            document.getElementById('currentHumidity').innerText = currentHumidity ? currentHumidity + '%' : 'N/A';

            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Temperature',
                            data: tempValues,
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1,
                            spanGaps: true
                        },
                        {
                            label: 'Humidity',
                            data: humidityValues,
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1,
                            spanGaps: true
                        }
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
