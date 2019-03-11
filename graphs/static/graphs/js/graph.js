$(document).ready(function(){
  var endpoint = 'api/chart/data'
  var climeLabels = []
  var climateData1 = climateData2 = climateData3 = climateData4 = []

  $.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
      climateLabels = data.climate_labels
      climateData1 = data.climate_data1
      climateData2 = data.climate_data2
      climateData3 = data.climate_data3
      climateData4 = data.climate_data4

      climateChart()
    },
    error: function(error_data){
      console.log("error")
    }
  })

  function climateChart(){
    var trace1 = {
      x: climateLabels,
      y: climateData1,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Ottawa CDA Temperature',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(248,118,109)",
        "width": 2
      },
    }

    var trace2 = {
      x: climateLabels,
      y: climateData2,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Ottawa CDA Precipitation',
      yaxis: 'y2',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(100,118,248)",
        "width": 2
      },
    }

    var trace3 = {
      x: climateLabels,
      y: climateData3,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Victoria Gonzales Temperature',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(221, 48, 17)",
        "width": 2
      },
    }

    var trace4 = {
      x: climateLabels,
      y: climateData4,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Victoria Gonzales Precipitation',
      yaxis: 'y2',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(48, 41, 173)",
        "width": 2
      },
    }

    var data = [trace1, trace2, trace3, trace4];

    var layout = {
      title: "Climate data for Ottawa",
      legend: {
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Temperature (C)',
        rangemode: 'nonnegative',
        range: [-20, 80],
        nticks: 11,
      },
      yaxis2: {
        title: 'Precipitation (mm)',
        side: 'right',
        overlaying: 'y',
        range: [-40, 160],
        nticks: 11,
      }
    };

    Plotly.newPlot('climate', data, layout)
  }
})
