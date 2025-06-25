function startLoading(form){
    const button = form.querySelector('button');
    const img = button.querySelector('img');
    button.disabled = true;
    
    img.src = "/static/images/loadingGif.gif";
    img.alt = "Loading...";
    
}