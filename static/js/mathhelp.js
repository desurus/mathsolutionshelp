var MATHHELP = MATHHELP || {};

/**
 * MATHHELP - mathsolutionshelp.com namespace and functionality
 *
 * @package Bonapick
 * @author Oleksandr Kryshchenko <okryshchenko@gmail.com>
 */
MATHHELP = function(mathhelp, $){
	var _self = mathhelp;
	var _initialized = false;
	
	/**
	 * Public init - initialize the javascript object
	 */
	_self.init = function(){
        // Carousel on the index page
        var main_carousel = $('#slider-carousel').carousel();

        $('#carousel-slide-left').click(function(){
            main_carousel.carousel('prev');
            return false;
        });
        $('#carousel-slide-right').click(function(){
            main_carousel.carousel('next');
            return false;
        });

        _self.slide_carousel_to = function(slide_number){
            main_carousel.carousel(slide_number);
            return false;
        }

        _self.pause_carousel = function(){
            main_carousel.carousel('pause');
            console.log('carousel paused');
            return false;
        }

		$('#slider-carousel').on('slid.bs.carousel', function (){
			var experts_slide_state = $('#experts_slide').attr('data-state');
			/* counter */
			if (experts_slide_state !== 'started'){
				var numAnim = new countUp("problems-solved-counter", '0', '88', '0', '4.5');
				numAnim.start(function(){
					// callback after counter animation is done
					
					$('#experts_slide').attr('data-state', 'started');	
				});
			}
		});
    }

    // bind a call of the init routine to DOM ready event
	$(document).ready(function(){
		_self.init();
	});
	return _self;
}(MATHHELP, jQuery);