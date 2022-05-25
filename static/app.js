window.onload = function () {
  const ctx = document.getElementById('myChart')

  const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: label,
      datasets: [
        {
          label: '# last_sold',
          data: last_bento_sold,
          backgroundColor: [
            'rgba(25, 99, 132, 0.2)',
            'rgba(4, 162, 235, 0.2)',
            'rgba(55, 206, 86, 0.2)',
            'rgba(5, 192, 192, 0.2)',
            'rgba(53, 102, 255, 0.2)',
            'rgba(25, 159, 64, 0.2)',
          ],
          borderColor: [
            'rgba(25, 99, 132, 1)',
            'rgba(4, 162, 235, 1)',
            'rgba(55, 206, 86, 1)',
            'rgba(5, 192, 192, 1)',
            'rgba(53, 102, 255, 1)',
            'rgba(25, 159, 64, 1)',
          ],
          borderWidth: 1,
        },
        {
          label: '# this week sold',
          data: bento_sold,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  })
  const ctx1 = document.getElementById('myChart1')

  const myChart1 = new Chart(ctx1, {
    type: 'doughnut',
    data: {
      labels: label,
      datasets: [
        {
          label: '# sold',
          data: listOfsale,
          backgroundColor: [
            'rgba(25, 99, 132, 0.2)',
            'rgba(4, 162, 235, 0.2)',
            'rgba(55, 206, 86, 0.2)',
            'rgba(5, 192, 192, 0.2)',
            'rgba(53, 102, 255, 0.2)',
            'rgba(25, 159, 64, 0.2)',
          ],
          borderColor: [
            'rgba(25, 99, 132, 1)',
            'rgba(4, 162, 235, 1)',
            'rgba(55, 206, 86, 1)',
            'rgba(5, 192, 192, 1)',
            'rgba(53, 102, 255, 1)',
            'rgba(25, 159, 64, 1)',
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
    // from here bottom down text of center in doughnut chart
    plugins: [
      {
        id: 'text',
        beforeDraw: function (myChart1, a, b) {
          var width = myChart1.width,
            height = myChart1.height,
            ctx = myChart1.ctx

          // ctx.restore()
          var fontSize = (height / 155).toFixed(2)
          ctx.font = fontSize + 'em sans-serif'
          // ctx.textBaseline = 'middle'

          var text = total_sale + '円',
            textX = Math.round((width - ctx.measureText(text).width) / 1.8),
            textY = height / 1.8

          ctx.fillText(text, textX, textY)
          ctx.save()
        },
      },
    ],
  })
}
