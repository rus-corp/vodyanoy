const filterForm = document.querySelector('.filter_form')
const checboxes = filterForm.querySelectorAll('.price_filter__checkbox')

checboxes.forEach(function(checkbox) {
  checkbox.addEventListener('change', function() {
    filterForm.submit();
  })
})


const countryFilterForm = document.querySelector('.country_filter_form')
const countrycheckboxes = countryFilterForm.querySelectorAll('.price_filter__checkbox')

countrycheckboxes.forEach(function(checkbox) {
  checkbox.addEventListener('change', function() {
    countryFilterForm.submit();
  })
})