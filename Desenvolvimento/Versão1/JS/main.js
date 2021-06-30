const opacityHeader = function(){
    let header = document.getElementById('header_site')
    let body = document.getElementById('body')
    header.style.opacity = "90%"
    let posicaoBody = body.getBoundingClientRect();
    if (posicaoBody.y == 0){
        header.style.opacity = "100%"
    }
}