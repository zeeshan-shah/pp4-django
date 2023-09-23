document.addEventListener("DOMContentLoaded", function () {
  // Function to initialize a carousel
  function initializeCarousel(carouselId) {
    var carouselElement = document.querySelector("#" + carouselId);
    if (window.matchMedia("(min-width: 768px)").matches) {
      var carousel = new bootstrap.Carousel(carouselElement, {
        interval: false,
      });
      var carouselWidth = carouselElement.querySelector(".carousel-inner")
        .scrollWidth;
      var cardWidth = carouselElement.querySelector(".carousel-item").clientWidth;
      var scrollPosition = 0;
      carouselElement
        .querySelector(".carousel-control-next")
        .addEventListener("click", function () {
          if (scrollPosition < carouselWidth - cardWidth * 4) {
            scrollPosition += cardWidth;
            carouselElement.querySelector(".carousel-inner").scrollTo({
              left: scrollPosition,
              behavior: "smooth",
            });
          }
        });
      carouselElement
        .querySelector(".carousel-control-prev")
        .addEventListener("click", function () {
          if (scrollPosition > 0) {
            scrollPosition -= cardWidth;
            carouselElement.querySelector(".carousel-inner").scrollTo({
              left: scrollPosition,
              behavior: "smooth",
            });
          }
        });
    } else {
      $(carouselElement).addClass("slide");
    }
  }

  // Initialize each carousel
  initializeCarousel("carouselExampleControls");
  initializeCarousel("carouselExampleControls1");
  initializeCarousel("carouselExampleControls2");
  initializeCarousel("carouselExampleControls3");
});
