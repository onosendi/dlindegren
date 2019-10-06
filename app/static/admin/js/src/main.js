(() => {

"use strict";

const base = 'https://jsonplaceholder.typicode.com';
fetch(base + "/posts").then(response => {
  response.json().then(json => {
    console.log(json);
  });
});

})();
