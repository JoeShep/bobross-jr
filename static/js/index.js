console.log("This was loaded from my Django app!")

document.getElementById('do-nuttin').addEventListener('click', () => {
  console.log("The button was clicked!")
})

document.getElementById('go-django').addEventListener('click', () => {
  console.log("The django button was clicked!")
  fetch('/movies')
    .then((response) => response.json())
    .then((myJson) => {
      console.log(myJson)
    })
    .catch((error) => {CSSConditionRule.log("error!", error)})
})
