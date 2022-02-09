async function fetch() {
  return new Promise((resolve) => {
    setTimeout(resolve, 100);
  });
}

async function foo() {
  const t = await fetch();
  console.log(t);
}

foo();
