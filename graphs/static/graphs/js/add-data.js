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
  var radioValue = $("input[name='sourceRadios']:checked").val();
  var climates = [];

  if(radioValue){
    alert("Your are - " + radioValue);
  };

  $('#years').find('.temp').each(function() {
    alert($(this).val());
    // $(this).css({
    //   "color": "green",
    //   "border": "2px solid green"
    // });
  })
})
