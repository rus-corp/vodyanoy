export const headerCatalog = document.querySelector('.catalog_btn')
export const headerCategory = document.querySelector('.header_catalog_view')




export function addBlock() {
  headerCategory.classList.add('category_active')
}

export function removeBlock(e) {
  if (!headerCatalog.contains(e.relatedTarget) && !headerCategory.contains(e.relatedTarget)) {
    headerCategory.classList.remove('category_active')
  }
}



