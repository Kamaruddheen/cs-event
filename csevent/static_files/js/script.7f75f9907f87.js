$(document).ready(function () {
  var countDownDate = new Date("Mar 10, 2021 10:00:00").getTime();
  var x = setInterval(function () {
    var now = new Date().getTime();
    var distance = countDownDate - now;

    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor(
      (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
    );
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    $("#day-id").text(days);
    $("#hour-id").text(hours);
    $("#min-id").text(minutes);
    $("#sec-id").text(seconds);
  });
});
