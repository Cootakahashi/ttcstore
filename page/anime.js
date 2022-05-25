const Elem = document.querySelectorAll('#anime')

const serviceElem = document.querySelectorAll('.service-anime')
const opElem = document.querySelectorAll('.opas')
const shadowElem = document.querySelectorAll('.shadows')
const japanElem = document.querySelectorAll('.japans')

// document.addで引数今回は、スクロールする度に中身が処理される
document.addEventListener('scroll', function () {
  for (let i = 0; i < Elem.length; i++) {
    const getdistance =
      Elem[i].getBoundingClientRect().top + Elem[i].clientHeight * 0.1
    //   最上部から要素上部までの距離
    if (i === 1) {
      console.log(getdistance)
    }
    // console.log(getdistance)
    console.log('画面の高さ', window.innerHeight)
    if (window.innerHeight > getdistance) {
      Elem[i].setAttribute('id', 'show')
    }
  }

  for (let i = 0; i < serviceElem.length; i++) {
    const Distance =
      serviceElem[i].getBoundingClientRect().top +
      serviceElem[i].clientHeight * 0.2

    if (window.innerHeight > Distance) {
      serviceElem[i].classList.add('.anime-show')
      serviceElem[i].setAttribute('id', 'anime-show')
    }
  }

  for (let i = 0; i < opElem.length; i++) {
    const Dist =
      opElem[i].getBoundingClientRect().top + opElem[i].clientHeight * 0.1
    if (window.innerHeight > Dist) {
      opElem[i].setAttribute('id', 'opaid')
    }
  }

  for (let i = 0; i < shadowElem.length; i++) {
    const Distan =
      shadowElem[i].getBoundingClientRect().top +
      shadowElem[i].clientHeight * 0.1
    if (window.innerHeight > Distan) {
      shadowElem[i].setAttribute('id', 'shadowid' + [i])
    }
  }

  for (let i = 0; i < japanElem.length; i++) {
    const Di =
      japanElem[i].getBoundingClientRect().top + japanElem[i].clientHeight * 0.1
    if (window.innerHeight > Di) {
      japanElem[i].setAttribute('id', 'japanid')
    }
  }
})

window.onload = function () {
  const spinner = document.getElementById('loading')
  spinner.classList.add('loaded')
}
