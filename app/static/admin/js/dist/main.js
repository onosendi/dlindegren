"use strict";

(function () {
  "use strict";

  var base = 'https://jsonplaceholder.typicode.com';
  fetch(base + "/posts").then(function (response) {
    response.json().then(function (json) {
      console.log(json);
    });
  });
})();