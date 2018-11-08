function collatz(num) {
  if (num === 1) {
    return 1;
  } else if (num % 2 === 0) {
    num = Math.floor(num / 2);
    console.log(num);
    return collatz(num);
  } else {
    num = num * 3 + 1;
    console.log(num);
    return collatz(num);
  }
}

collatz(3)