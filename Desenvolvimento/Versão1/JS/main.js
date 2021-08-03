const opacityHeader = function(){
    let header = document.getElementById('header_site')
    let body = document.getElementById('body')
    header.style.opacity = "90%"
    let posicaoBody = body.getBoundingClientRect();
    if (posicaoBody.y == 0){
        header.style.opacity = "100%"
    }
}
const calculadoraRendimento = function(){
    let trabalho = document.getElementById('trabalho_input').value
    let calor = document.getElementById('energia_input').value
    let display = document.getElementById('displayCalculadoraRendimento')
    let rendimento = trabalho / calor
    display.textContent = rendimento.toFixed(4) + ""
}
const limparResultadoRendimento = function(){
    let display = document.getElementById('displayCalculadoraRendimento')
    display.textContent = ""
}

