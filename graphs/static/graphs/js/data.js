var $th = $('.tableFixHead').find('thead th')
$('.tableFixHead').on('scroll', function() {
  $th.css('transform', 'translateY('+ this.scrollTop +'px)');
});

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
      $("#inputYear").show();
    },
    error: function(data) {
      $("#inputYear").hide();
    }
  })
});
