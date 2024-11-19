import { arrowLeft, arrowRight, addPagination, nextSlide, previousSlide } from './head_slider.js';

import { headerCatalog, headerCategory, addBlock, removeBlock } from './header_catalog.js';



headerCatalog.addEventListener('mouseenter', addBlock)
headerCategory.addEventListener('mouseleave', removeBlock)
headerCatalog.addEventListener('mouseleave', removeBlock)



addPagination()
arrowRight.addEventListener('click', previousSlide)
arrowLeft.addEventListener('click', nextSlide)


