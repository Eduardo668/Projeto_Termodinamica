// Faz com que o header fica semi transparente quando descer a pagina
const opacityHeader = function(){ 
    let header = document.getElementById('header_site')
    let body = document.getElementById('body')
    header.style.opacity = "90%"
    let posicaoBody = body.getBoundingClientRect();
    if (posicaoBody.y == 0){
        header.style.opacity = "100%"
    }
}
//Executa Quando é clicado o botão calcular - Tem a Função de realizar os calculos
const calculadoraRendimento = function(){
    let trabalho = document.getElementById('trabalho_input').value
    let calor = document.getElementById('energia_input').value
    let deltaUDisplay = document.getElementById('delta')
    let display = document.getElementById('displayCalculadoraRendimento')
    let simboloDeIgual = document.getElementById('simboloDeIgual').style.display = "initial"
    let simboloDeIgualdeltaU = document.getElementById('simboloDeIgualdeltaU').style.display = "initial"
    let rendimento = trabalho / calor
    let deltaU = trabalho - calor
    console.log(trabalho)
    console.log(calor)
    if (trabalho && calor == 0){
        display.innerHTML = 0 + '<p id="delta" class="deltaUResultado"> '+0+'</p>'
        
    }
    else{
        display.innerHTML = rendimento.toFixed(2) + '<p id="delta" class="deltaUResultado"> '+deltaU+'</p>'  
    }


    
}
// Executa quando é clicado o botão limpar - Tem a Função de Remover o resultado e os valores digitados
const limparResultadoRendimento = function(){
    document.getElementById('displayCalculadoraRendimento').textContent = ""
    document.getElementById('trabalho_input').value = 0
    document.getElementById('energia_input').value = 0
    document.getElementById('simboloDeIgual').style.display = "none"
    document.getElementById('simboloDeIgualdeltaU').style.display = "none"
}

const zerarInputTrabalho = function(){
    document.getElementById('trabalho_input').value = undefined
}
const zerarInputCalor = function(){
    document.getElementById('energia_input').value = undefined
}

const talvezVoltarOzeroTrabalho = function(){
    let input_trabalho = document.getElementById('trabalho_input').value
    if (input_trabalho == undefined){
        input_trabalho = 0
        console.log('oi')
    }
}

