import PhotoSwipe from 'photoswipe';
import PhotoSwipeLightbox from 'photoswipe/lightbox';

const swipeOptions = {
  gallery: '.pswp-gallery',
  children: '.pswp-gallery__item',
  pswpModule: () => PhotoSwipe
};

const gallery = new PhotoSwipeLightbox(swipeOptions);
gallery.on('uiRegister', function() {
  gallery.pswp.ui.registerElement({
    name: 'custom-caption',
    order: 9,
    isButton: false,
    appendTo: 'root',
    html: 'Caption text',
    onInit: (el, pswp) => {
      gallery.pswp.on('change', () => {
        const currSlideElement = gallery.pswp.currSlide.data.element;
        let captionHTML = '';
        if (currSlideElement) {
          const hiddenCaption = currSlideElement.querySelector('.hidden-caption-content');
          if (hiddenCaption) {
            // get caption from element with class hidden-caption-content
            captionHTML = hiddenCaption.innerHTML;
          } else {
            // get caption from alt attribute
            captionHTML = currSlideElement.querySelector('img').getAttribute('alt');
          }
        }
        el.innerHTML = captionHTML || '';
      });
    }
  });
});


export default gallery;