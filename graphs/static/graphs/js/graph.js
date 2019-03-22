$(document).ready(function(){
  var endpoint = 'api/chart/data'
  var climeLabels = []
  var climateData1 = climateData2 = climateData3 = climateData4 = []
  $("#loading-alert").show();

  $.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
      climateLabels = data.climate_labels
      climateData1 = data.climate_data1
      climateData2 = data.climate_data2
      climateData3 = data.climate_data3
      climateData4 = data.climate_data4

      avTempChart()
      precipitationChart()
      $("#loading-alert").hide();
      $("#success-alert").show();
      $("#success-alert").fadeOut(3250);
    },
    error: function(error_data){
      console.log("error")
    }
  })

  function avTempChart(){
    var trace1 = {
      x: climateLabels,
      y: climateData1,
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
      x: climateLabels,
      y: climateData3,
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
      title: "Yearly average temperature compared to the 1929-2018 average (at 0°C)",
      legend: {
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Temperature difference (°C)',
        rangemode: 'nonnegative',
        range: [-2, 2],
        nticks: 5,
      }
    };

    Plotly.newPlot('avgTemperatureChart', data, layout)
  };

  function precipitationChart(){
    var trace2 = {
      x: climateLabels,
      y: climateData2,
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
      x: climateLabels,
      y: climateData4,
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
      title: "Average yearly precipitation in mm",
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
