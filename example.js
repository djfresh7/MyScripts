// A Variable and a constant.
var no = 1
const Med = "ok"

// Prints both the variable and constant.
console.log(no)
console.log(Med)

// Simple JS calculator.

function calculator(num1, op, num2){
  if (op == "+"){
    return num1 + num2
  } else if (op == "-"){
    return num1 - num2
  } else if (op == "*"){
    return num1 * num2
  } else if (op == "/"){
    return num1 / num2
  } else{
    return false
  }
}

// JS variables
var a = 0
let g = 2

// Simple JS checks
if (g == a){
    console.log("Equal")
} else if (g > a){
    console.log("G is bigger")
} else if (g < a){
    console.log("A is bigger")
} else{
    console.log(false)
}
