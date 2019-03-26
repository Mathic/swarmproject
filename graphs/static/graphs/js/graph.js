$(document).ready(function(){
  var ul = document.getElementById('chartChooser');
  var target = '';
  var climeLabels = []
  var climateData1 = climateData2 = []

  if(target == '') {
    callAjax('api/chart/year_avg_temp', yearlyAvgTemp);
    $(document.getElementById('api/chart/year_avg_temp')).addClass('active')
  }

  ul.onclick = function(event) {
    target = event.target.id;
    var a = document.getElementById(target);
    $(a).addClass('active').parent().siblings().children().removeClass('active');
    console.log(a);

    switch(target) {
      case 'api/chart/year_avg_temp':
        callAjax(target, yearlyAvgTemp);
        break;
      case 'api/chart/year_avg_prec':
        callAjax(target, yearlyAvgPrec);
        break;
      case 'api/chart/month_avg_temp':
        callAjax(target, monthlyAvgTemp);
        break;
      case 'api/chart/month_avg_prec':
        callAjax(target, monthlyAvgPrec);
        break;
    };
  };

  function callAjax(endpoint, callFunction) {
    $("#loading-alert").show();
    $.ajax({
      method: "GET",
      url: endpoint,
      success: function(data){
        climateLabels = data.climate_labels
        climateData1 = data.climate_data1
        climateData2 = data.climate_data2

        callFunction();
        $("#loading-alert").hide();
        $("#success-alert").show();
        $("#success-alert").fadeOut(3250);
      },
      error: function(error_data){
        console.log("error")
      }
    });
  };

  function yearlyAvgTemp(){
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
      y: climateData2,
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
        title: 'Year',
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Temperature difference (°C)',
        rangemode: 'nonnegative',
        range: [-2.5, 2.5],
        nticks: 5,
      }
    };

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  };

  function yearlyAvgPrec(){
    var trace2 = {
      x: climateLabels,
      y: climateData1,
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
      y: climateData2,
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
      title: "Yearly average precipitation in mm",
      legend: {
        title: 'Year',
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

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  };

  function monthlyAvgTemp(){
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
      y: climateData2,
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
        title: 'Month',
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

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  };

  function monthlyAvgPrec(){
    var trace2 = {
      x: climateLabels,
      y: climateData1,
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
      y: climateData2,
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
        title: 'Month',
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

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  };
});
