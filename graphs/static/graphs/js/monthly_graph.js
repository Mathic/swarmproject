$(document).ready(function(){
  var endpoint = 'api/chart/monthly-data'
  var climeLabels = []
  var climateData1 = climateData2 = climateData3 = climateData4 = []

  $.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
      month_names = data.month_names
      vmonths_temp = data.vmonths
      omonths_temp = data.omonths
      vmonths_p = data.vmonths_p
      omonths_p = data.omonths_p

      avTempChart()
      precipitationChart()
    },
    error: function(error_data){
      console.log("error")
    }
  })

  function avTempChart(){
    var trace1 = {
      x: month_names,
      y: omonths_temp,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Ottawa',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(221, 48, 17)",
        "width": 2
      },
    }

    var trace3 = {
      x: month_names,
      y: vmonths_temp,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Victoria',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(255,140,0)",
        "width": 2
      },
    }

    var data = [trace1, trace3];

    var layout = {
      title: "Monthly average temperature from 1929-2018",
      legend: {
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Temperature (°C)',
        rangemode: 'nonnegative',
        range: [-30, 30],
        nticks: 5,
      }
    };

    Plotly.newPlot('avgTemperatureChart', data, layout)
  };

  function precipitationChart(){
    var trace2 = {
      x: month_names,
      y: omonths_p,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Ottawa',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(48, 41, 173)",
        "width": 2
      },
    }

    var trace4 = {
      x: month_names,
      y: vmonths_p,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Victoria',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(100,118,248)",
        "width": 2
      },
    }

    var data = [trace2, trace4];

    var layout = {
      title: "Monthly average precipitation from 1929-2018",
      legend: {
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Precipitation (mm)',
        side: 'left',
        overlaying: 'y',
        range: [0, 140],
        nticks: 11,
      }
    };

    Plotly.newPlot('precipitationChart', data, layout)
  };
});
