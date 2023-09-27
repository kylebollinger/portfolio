import * as bootstrap from 'bootstrap';
import PhotoSwipe from 'photoswipe';
import PhotoSwipeLightbox from 'photoswipe/lightbox';


window.bootstrap = bootstrap;
window.PhotoSwipeLightbox = PhotoSwipeLightbox;
window.PhotoSwipe = PhotoSwipe;


const options = {
    gallery:'#my-gallery',
    children:'.pswp-gallery__item',
    pswpModule: () => import('photoswipe')
};
const lightbox = new PhotoSwipeLightbox(options);
lightbox.on('uiRegister', function() {
lightbox.pswp.ui.registerElement({
    name: 'custom-caption',
    order: 9,
    isButton: false,
    appendTo: 'root',
    html: 'Caption text',
    onInit: (el, pswp) => {
    lightbox.pswp.on('change', () => {
        const currSlideElement = lightbox.pswp.currSlide.data.element;
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
lightbox.init();