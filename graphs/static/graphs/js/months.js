$("#inputYear").change(function () {
  var url = $("#dataMonth").attr("data-months-url");
  var yearId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'yearId': yearId
    },
    success: function (data) {
      $("#months").html(data);
      console.log("yay");
    }
  });
});
