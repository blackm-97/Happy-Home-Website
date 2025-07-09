function startLoading(form){
    const button = form.querySelector('button');
    const img = button.querySelector('img');
    button.disabled = true;
    
    img.src = "/static/images/loadingGif.gif";
    img.alt = "Loading...";
    
}

  var audio = document.getElementById("browse_music");
  audio.volume = 0.25;

  ScrollReveal().reveal('.card', {
    interval: 10
});