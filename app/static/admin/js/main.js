(function() {
  "use strict";

// Show an element
var show = function (elem) {
  let send = function(url, method) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function () {
      if (xhr.status >= 200 && xhr.status < 300) {
        console.log('success!', xhr);
      } else {
        console.log('The request failed!');
      }
    };
    xhr.open(method, url);
    xhr.send();
  };
  
  let articleItems = document.querySelectorAll('.article-item');
  for (let i = 0; i < articleItems.length; i++) {
    let el = articleItems[i],
        url = el.getAttribute('data-url'),
        deleteItem = el.querySelector('[data-method="delete"]');
    deleteItem.addEventListener('click', function(event) {
      event.preventDefault();
      send(url, 'DELETE');
    });
  }
})();
