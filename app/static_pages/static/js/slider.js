const arrowLeft = document.querySelector('.arrow-left');
const arrowRight = document.querySelector('.arrow-right');
const slides = document.querySelectorAll('.slider__image');
const bottom = document.querySelector('.slider-bottom');




let currentSlideIndex = 0;
const paginationCircles = [];


function createPaginationCircle() {
  const div = document.createElement('div');
  div.className = 'pagination-circle';
  bottom.appendChild(div);
  paginationCircles.push(div);
}


function addPagination() {
  slides.forEach(createPaginationCircle);
  paginationCircles[0].classList.add('active')
}

function addActiveClass() {
  paginationCircles[currentSlideIndex].classList.add('active')
}

function removeActiveClass() {
  paginationCircles[currentSlideIndex].classList.remove('active')
}

function showSlide() {
  slides[currentSlideIndex].classList.add('block');
}

function hideSlide() {
  slides[currentSlideIndex].classList.remove('block');
}


function nextSlide() {
  hideSlide();
  removeActiveClass()
  currentSlideIndex ++;
  if (currentSlideIndex > slides.length - 1) {
    currentSlideIndex = 0;
  }
  addActiveClass();
  showSlide();
}


function previousSlide() {
  hideSlide();
  removeActiveClass()
  currentSlideIndex --;
  if (currentSlideIndex < 0) {
    currentSlideIndex = slides.length - 1;
  }
  addActiveClass()
  showSlide();
}

addPagination()
arrowRight.addEventListener('click', previousSlide)
arrowLeft.addEventListener('click', nextSlide)