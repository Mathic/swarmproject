$("#inputName").change(function () {
  var url = $("#climateForm").attr("data-years-url");  // get the url of the `load_years` view
  var nameId = $(this).val();  // get the selected student ID from the HTML input

  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-years/)
    data: {
      'student': nameId       // add the student id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_years` view function
      $("#inputYear").html(data);  // replace the contents of the year input with the data that came from the server
    }
  });

});

$("#addData").click(function() {
  var url = $("#climateForm").attr("data-save-url");
  var radioValue = $("input[name='sourceRadios']:checked").val();
  var climates = [];
  temps = []
  precips = []
  var student_id = $("#inputName").val();

  $('#inputYear').find('.data').each(function() {
    if($(this).val() == ""){
      climates.push($(this).text());
    } else {
      climates.push($(this).val());
    }
  });

  $('#inputYear').find('.temps').each(function() {
    temps.push($(this).val())
  });

  $('#inputYear').find('.precips').each(function() {
    precips.push($(this).val())
  });

  console.log("temps")
  console.log(temps)
  console.log("precips")
  console.log(precips)

  $.ajax({
    url: url,
    data: {
      'climates': climates,
      'temps': temps,
      'precips': precips,
      'source': radioValue,
      'student_id': student_id
    },
    success: function (data) {
      $("#success-alert").show();
      $("#success-alert").fadeOut(3250);
    },
    error: function() {
      $("#error-alert").show();
      $("#error-alert").fadeOut(3250);
    }
  });
})
