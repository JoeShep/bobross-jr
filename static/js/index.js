console.log("This was loaded from my Django app!")


const displayMovies = (movies) => {
  const list_container = document.getElementById('movie_list')
  const fragment = document.createDocumentFragment()
  const list = document.createElement('ul')
  movies.forEach(movie => {
    const list_item = document.createElement('li')
    list_item.innerHTML = `Title: ${movie.title}, released in ${movie.year_released}`
    list.appendChild(list_item)
  });
  fragment.appendChild(list)
  list_container.appendChild(fragment)
}


document.getElementById('do-nuttin').addEventListener('click', () => {
  console.log("The button was clicked!")
})

document.getElementById('go-django').addEventListener('click', () => {
  console.log("The django button was clicked!")
  fetch('/movie_data')
    .then((mov_data) => mov_data.json())
    .then((mov_json) => {
      console.table(mov_json)
      displayMovies(mov_json)
    })
    .catch((error) => {console.log("error!", error)})
})
