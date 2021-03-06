"use strict"

const fs = require("fs")

process.stdin.resume()
process.stdin.setEncoding("utf-8")

let inputString = ""
let currentLine = 0

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin
})

process.stdin.on("end", (_) => {
  inputString = inputString
    .replace(/\s*$/, "")
    .split("\n")
    .map((str) => str.replace(/\s*$/, ""))

  main()
})

function readLine() {
  return inputString[currentLine++]
}

// Complete the jumpingOnClouds function below.
function jumpingOnClouds(c, s = 0) {
  if (c.length == 1) return s
  if (c.length > 2) if (c[2] == 0) return jumpingOnClouds(c.slice(2), s + 1)
  if (c[1] == 0) return jumpingOnClouds(c.slice(1), s + 1)
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH)

  const n = parseInt(readLine(), 10)

  const c = readLine()
    .split(" ")
    .map((cTemp) => parseInt(cTemp, 10))

  let result = jumpingOnClouds(c)

  ws.write(result + "\n")

  ws.end()
}
