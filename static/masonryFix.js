  document.addEventListener("DOMContentLoaded", function () {
    const grid = document.querySelector('.grid');
    const msnry = new Masonry(grid, {
      itemSelector: '.card',
      columnWidth: '.grid-sizer',
      percentPosition: true
    });

    imagesLoaded(grid, function () {
      msnry.layout();
    });
  });