let numero = Math.random()*100;
numero = Math.round(numero);

let premios = ["common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", "common sword", 
"rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", "rare sword", 
"common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", "common character", 
"rare character", "rare character", "rare character", "rare character", "rare character", "rare character", "rare character", "rare character", "rare character", "rare character", "rare character"];

//function randomize(premio){
let premio = premios.slice(numero,numero+1);
//}
document.write("Congratulations! You won: " + premio);
