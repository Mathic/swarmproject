$("#inputYear").change(function () {
  var url = $("#dataMonth").attr("data-months-url");
  var year = $(this).val();

  console.log(year)

  $.ajax({
    url: url,
    data: {
      'year': year
    },
    success: function (data) {
      $("#months").html(data);
      console.log("yay");
    }
  });
});
