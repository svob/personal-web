$(function() {

  "use strict";

  /*===============================================
    Toggle Menu
  ===============================================*/
  var menu = $(".menu");
  var toggleBtn = $(".toggle-btn");

  toggleBtn.on("click", function(e) {
    if (menu.hasClass("show-menu")) {
      menu.removeClass("show-menu");
    }
    else {
      menu.addClass("show-menu");
    }
    e.stopPropagation();
  });

  // Close menu when click outside
  $("html").click(function() {
    if (menu.hasClass("show-menu")) {
      menu.removeClass("show-menu");
      toggleBtn.removeClass("toggle-close");
    }
  });

  // Navicon transform into X //
  toggleBtn.on("click", function() {
    if (toggleBtn.hasClass("toggle-close")) {
      toggleBtn.removeClass("toggle-close");
    }
    else {
      toggleBtn.addClass("toggle-close");
    }
  });

  /*===============================================
    Parallax
  ===============================================*/
  $(".parallax-section").parallax({ 
    speed : 0.3 
  });

  /*===============================================
    Owl Carousel
  ===============================================*/

  // Blog Slider
  $("#blogSlider").owlCarousel({
    items: 2,
    itemsDesktop: [1199,2], // Show 2 items on Desktop
    itemsDesktopSmall: [979,2], // 2 items on Small Deskktop
    itemsTablet: [768,1], // 1 item on Tablet
    itemsMobile: [479,1], // 1 item on Mobile
    slideSpeed: 500, // 0.5 seconds
    pagination: false,
    navigation: false,
    rewindSpeed: 700
  });

  // Custom Navigation
  var blogNavigation = $("#blogSlider");
 
  // Events
  $("#next").on("click", function(){
    blogNavigation.trigger('owl.next');
  })
  $("#prev").on("click", function(){
    blogNavigation.trigger('owl.prev');
  })
  // end Custom Navigation

  // Blog Page
  $("#postSlider").owlCarousel({
    slideSpeed: 500, // 0.5 seconds
    pagination: false,
    navigation: true,
    navigationText: ["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
    rewindSpeed: 700,
    singleItem: true
  });

  /*===============================================
    Counter
  ===============================================*/
  $("#skills [data-to]").each(function() {
    var $this = $(this);
    $this.appear(function() {
      $this.countTo({
        speed: 1500
      });
    }, {accX: 0, accY: -10});
  });


  /*===============================================
    Contact Form
  ===============================================*/
  $("#contactform").on('submit',function(e) {
    var name = $("#name").val();
    var email = $("#email").val();
    var phone = $("#phone").val();
    var message = $("#message").val();
    if (name == '') {
      $("#name").css('border-color','rgba(255, 0, 0, 0.5)');
    }
    if (email == '') {
      $("#email").css('border-color','rgba(255, 0, 0, 0.5)');
    }
    if (phone == '') {
      $("#phone").css('border-color','rgba(255, 0, 0, 0.5)');
    }
    if (message == '') {
      $("#message").css('border-color','rgba(255, 0, 0, 0.5)');
    }
    else {
      $.ajax({
        url:'contact_form.php',
        data:$(this).serialize(),
        type:'POST',
        success:function(data){
          $("#success").show().fadeIn(1000); //=== Show Success Message==
          $('#contactform').each(function(){
            this.reset();
          });
        },
        error:function(data){
          $("#error").show().fadeIn(1000); //===Show Error Message====
        }
      });
    }
    e.preventDefault();
  });

    /*===============================================
    Google Maps
  ===============================================*/
  var markerIcon = "static/web/images/marker.png";
  // Map Initial Location
  var initLatitude = 49.05209; // <- Latitude here
  var initLongitude = 15.80865; // <- Longitude here

  var map = new GMaps({
    el: '#map-canvas',
    lat: initLatitude,
    lng: initLongitude,
    zoom: 16,
    scrollwheel: false
  });
  map.addMarker({
    lat : initLatitude,
    lng : initLongitude,
    icon: markerIcon
  });
  /*===============================================
    end Google Maps
  ===============================================*/
});