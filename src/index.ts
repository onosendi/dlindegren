async function fetch() {
  return new Promise((resolve: any) => {
    setTimeout(resolve('blahs :)'), 100);
  });
}

async function foo() {
  const t = await fetch();
  console.log(t);
}

foo();
