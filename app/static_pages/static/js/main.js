import { arrowLeft, arrowRight, addPagination, nextSlide, previousSlide } from './head_slider.js';

import { headerCatalog, headerCategory, addBlock, removeBlock } from './header_catalog.js';




addPagination()
arrowRight.addEventListener('click', previousSlide)
arrowLeft.addEventListener('click', nextSlide)

headerCatalog.addEventListener('mouseenter', addBlock)
headerCatalog.addEventListener('mouseleave', removeBlock)
headerCategory.addEventListener('mouseleave', removeBlock)
