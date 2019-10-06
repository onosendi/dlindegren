(() => {
  "use strict";

  const sendAsync = (method, url, callbackArray, data) => {
    const xhr = new XMLHttpRequest();
    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) {
        callbackArray.map(callback => callback());
        console.log(xhr);
      } else {
        console.log('The request failed!');
      }
    };
    xhr.open(method, url);
    if (data) {
      xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      xhr.send(JSON.stringify(data));
    } else xhr.send();
  };

  const deleteItem = (elem) => elem.style.display = 'none';
  const editItem = (elem, text) => elem.innerHTML = text;
  const addItem = (articleName) => {
    console.log(articleName);
  };

  const articleItems = document.querySelectorAll('.article-item');

  for (const elem of articleItems) {
    const url = elem.getAttribute('data-url');
    const articleName = elem.querySelector('.article-name');
    
    const deleteElem = elem.querySelector('.delete-article');
    deleteElem.addEventListener('click', event => {
      const t = 'Are you sure you want to delete "' + articleName.innerHTML + '"?';
      if (confirm(t) == true) {
        sendAsync('DELETE', url, [() => deleteItem(elem)]);
      }
    });

    const editElem = elem.querySelector('.edit-article');
    editElem.addEventListener('click', event => {
      const t = articleName.innerHTML;
      const p = prompt('Edit article' , t);
      if (p != null && p !== t) {
        const payload = {'article_name': p}
        sendAsync('PUT', url, [() => editItem(articleName, p)], payload);
      }
    });
  }

  const addArticle = document.querySelector('.add-article');
  if (addArticle) {
    addArticle.addEventListener('click', event => {
      const url = addArticle.getAttribute('data-url');
      const p = prompt('Add article');
      if (p != null) {
        const payload = {'article_name': p}
        sendAsync('POST', url, [() => addItem(p)], payload);
      }
    });
  }
})();
