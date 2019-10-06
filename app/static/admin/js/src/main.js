(() => {

"use strict";

const sendAsync = async (url, callback) => {
  const response = await fetch(url);
  console.log(response);
};

const deleteItem = () => {
  console.log('testing');
}

document.querySelector('.add-article').addEventListener('click', event => {
  sendAsync('/admin/blog', deleteItem);
});

})();
