export const productMenuItems = document.querySelectorAll('.product_info__list_link').forEach(link => {
  link.addEventListener('click', function(event) {
    event.preventDefault()
    
    document.querySelectorAll('.product_info__list_link').forEach(el => el.classList.remove('active_item'))
    this.classList.add('active_item')

    document.querySelectorAll('.info_item').forEach(item => item.classList.remove('active_item'))

    const targetClass = this.getAttribute('data-target')
    const targetItem = document.querySelector(`.${targetClass}`)
    if (targetItem) {
      targetItem.classList.add('active_item')
    }
  })
})