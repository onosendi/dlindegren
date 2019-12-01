const sendAsync = (method, url, callback, data) => {
  const xhr = new XMLHttpRequest()
  xhr.onload = () => {
    if (xhr.status >= 200 && xhr.status < 300) {
      try {
        const response = JSON.parse(xhr.response)
        console.log(response)
        callback(response)
      }
      catch(error) {
        console.log('Not a json string')
      }
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

/**
* Admin Blog
*/
const adminBlog = document.getElementById('admin-blog')
if (adminBlog) {

console.log(adminBlog)

const createArticleEl = (response) => {
  console.log('testing')
}

adminBlog.querySelector('.add-article').addEventListener('click', event => {
  const payload = {'article_name': 'article testing9'}
  sendAsync('POST', '/admin/blog/article', createArticleEl, payload)
})

}
