/* let numDeUniProd1 = Number(prompt("Digite o número de unidades do produto 1: "));
let numDeUniProd2 = Number(prompt("Digite o número de unidades do produto 2: "));
let precoProd1 = Number(prompt("Digite o preço do produto 1: "));
let precoProd2 = Number(prompt("Digite o preço do produto 2: "));
console.log(`O preço a ser pago pelo produto 1 é: ${numDeUniProd1 * precoProd1}`)
console.log(`O preço a ser pago pelo produto 2 é: ${numDeUniProd2 * precoProd2}`)*/

/* Faça um programa que receba dia, mês e ano atual e dia, mês e ano de nascimento de 
uma pessoa e mostre se esta pessoa não é eleitor ainda (idade menor que 16 anos), 
se é eleitor facultativo (idade entre 16 e 18 anos ou maior do que 65 anos) 
ou se é eleitor obrigatório (idade entre 18 e 65 anos). */


/*let anoNasci = Number(prompt("Digite o seu ano de nascimento: "));
let anoAtual = Number(prompt("Digite o ano atual: "));
const idade = anoAtual - anoNasci;
if ( idade < 16 ) {
    alert("Esta pessoa não é eleitor ainda");
}else if ( (idade >= 16 && idade < 18) || idade > 65 ) {
    alert("Esta pessoa é eleitor facultativo");
}else {
    alert("Esta pessoa é eleitor obrigatório");
}*/


/* 
Faça um programa que receba um valor inteiro positivo N e mostre os 
N números naturais a partir do 1, mas que não mostre os números impares.
*/

/* let N = Number(prompt("Digite o valor de N: "));

for (let i = 0; i <= N; i += 2) {
    if ( i == 0 ) {
        console.log(1)
    }else {
        console.log(i)
    }
}

let i = 0;
while (i <= N) {
    if ( i == 0 ) {
        console.log(1)
    }else {
        console.log(i)
    }
    i += 2;
} */

/* 
Faça um algoritmo que:
    Receba n elementos e armazene-os em uma lista;
    Percorra essa lista, calcule a média dos seus 
    elementos e retorne a soma dos elementos pares que são acima dessa média;
 */

/* let a = 0;
let lista = [];
while (a >= 0) {
    a = Number(prompt("Digite o valor de N: "));
    if (a >= 0) {
        lista.push(a);
    }
}
let soma = 0;
for (let i = 0; i < lista.length; i++) {
    soma += lista[i];
}
let media = soma / lista.length
console.log("o valor da média é: " + media)
console.log(`o valor da média é: ${media}`)
lista.forEach((elemento) => {
    if ((elemento % 2 == 0) && elemento > media) {
        console.log(elemento)
    }
})
*/












let quantidadeProdt1 = 0;
let quantidadeProdt2 = 0;
let precoProdt1 = 0;
let precoProd2 = 0;
let botaoProdt1 = document.getElementById("botaoProd1");
let botaoProdt2 = document.getElementById("botaoProd2");
let botaoCalcular = document.getElementById("botaoCalcular");


botaoProdt1.addEventListener('click', () => {
    quantidadeProdt1 = document.getElementById("quantidadeProduto1").valueAsNumber;
    precoProdt1 = document.getElementById("precoProduto1").valueAsNumber;
    document.getElementById("qntdAtualProd1").textContent = `A quantidade é: ${quantidadeProdt1}`
    document.getElementById("valorAtualProd1").textContent = `O atual valor é:   ${precoProdt1}`
})

botaoProdt2.addEventListener('click', () => {
    quantidadeProdt2 = document.getElementById("quantidadeProduto2").valueAsNumber;
    precoProdt2 = document.getElementById("precoProduto2").valueAsNumber;
    document.getElementById("qntdAtualProd2").textContent = `A quantidade é: ${quantidadeProdt2}`
    document.getElementById("valorAtualProd2").textContent = `O atual valor é:   ${precoProdt2}`
})

botaoCalcular.addEventListener('click', () => {
    let resultadoProd1 = quantidadeProdt1 * precoProdt1;
    let resultadoProd2 = quantidadeProdt2 * precoProdt2;
    document.getElementById("resultado").textContent = `Produto1: ${resultadoProd1} Produto2: ${resultadoProd2}`;
})