const sendAsync = (method, url, callback, data) => {
  const xhr = new XMLHttpRequest()
  xhr.onload = () => {
    if (xhr.status >= 200 && xhr.status < 300) {
      const response = JSON.parse(xhr.response)
      callback(response)
    } else {
      console.log('The request failed!')
    }
  }
  xhr.open(method, url)
  if (data) {
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
    xhr.send(JSON.stringify(data))
  } else xhr.send()
}

const deleteEventListener = (elem, articleName, url) => {
  const listenElem = elem.querySelector('.delete-article')
  listenElem.addEventListener('click', event => {
    const t = 'Are you sure you want to delete "' + articleName.innerHTML + '"?'
    if (confirm(t) == true) {
      sendAsync('DELETE', url, () => deleteItem(elem))
    }
  })
}

const editEventListener = (elem, articleName, url) => {
  const listenElem = elem.querySelector('.edit-article')
  listenElem.addEventListener('click', event => {
    const t = articleName.innerHTML
    const p = prompt('Edit article' , t)
    if (p != null && p !== t) {
      const payload = {'article_name': p}
      sendAsync('PUT', url, () => editItem(articleName, p), payload)
    }
  })
}

const deleteItem = (elem) => elem.style.display = 'none'
const editItem = (elem, text) => elem.innerHTML = text
const addItem = (response) => {
  const article = response['article']
  const articleParent = document.querySelector('.article-list')
  const articleChild = document.createElement('li')
  articleChild.classList.add('article-item')
  articleChild.setAttribute('data-url', `${response['url']}?article_id=${article['id']}`)
  articleChild.innerHTML = `
    <span class="article-name">${article['name']}</span>
    <button class="edit-article" type="button">Edit</button>
    <button class="delete-article" type="button">Delete</button>
  `
  articleParent.prepend(articleChild)
  articleName = articleChild.querySelector('.article-name')
  url = articleChild.getAttribute('data-url')
  deleteEventListener(articleChild, articleName, url)
  editEventListener(articleChild, articleName, url)
}

for (const elem of document.querySelectorAll('.article-item')) {
  const url = elem.getAttribute('data-url')
  const articleName = elem.querySelector('.article-name')
  deleteEventListener(elem, articleName, url)
  editEventListener(elem, articleName, url)
}

addArticle = document.querySelector('.add-article')
addArticle.addEventListener('click', event => {
  const url = addArticle.getAttribute('data-url')
  const p = prompt('Add article')
  if (p != null) {
    const payload = {'article_name': p}
    sendAsync('POST', url, addItem, payload)
  }
})
