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

// Complete the repeatedString function below.
function repeatedString(s, n) {
  let a1 = 0,
    a2 = 0
  let mod = n % s.length

  for (let i = 0; i < s.length; i++) {
    if (s[i] == "a") {
      a1++
      if (i < mod) a2++
    }
  }

  return ((n - mod) / s.length) * a1 + a2
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH)

  const s = readLine()

  const n = parseInt(readLine(), 10)

  let result = repeatedString(s, n)

  ws.write(result + "\n")

  ws.end()
}
