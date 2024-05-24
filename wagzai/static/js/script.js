$(function() {
    $('[data-toggle="tooltip"]').tooltip();
});


function register() {
    var data = {
      username: $("#username").val(),
      email: $("#email").val(),
      password: $("#password").val()
    };
  
    $.ajax({
      type: "POST",
      url: "/register",
      data: JSON.stringify(data),
      contentType: "application/json;charset=utf-8",
      dataType: "json",
      success: function (response) {
        if (response.success) {
          // Redirect to login page or display success message
        } else {
          // Display error message
        }
      },
      error: function (jqXHR, textStatus, errorThrown) {
        console.log(textStatus, errorThrown);
      }
    });
  }
