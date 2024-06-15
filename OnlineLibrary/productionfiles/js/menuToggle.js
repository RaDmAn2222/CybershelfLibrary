(function($) {
    var $window = $(window),
        $body = $('body');

    // Breakpoints.
    breakpoints({
        xlarge:   [ '1281px',  '1680px' ],
        large:    [ '981px',   '1280px' ],
        medium:   [ '737px',   '980px'  ],
        small:    [ '481px',   '736px'  ],
        xsmall:   [ '361px',   '480px'  ],
        xxsmall:  [ null,      '360px'  ]
    });

    // Play initial animations on page load.
    $window.on('load', function() {
        window.setTimeout(function() {
            $body.removeClass('is-preload');
        }, 100);
    });

    // Touch?
    if (browser.mobile)
        $body.addClass('is-touch');

    // Menu toggle.
    var $menuToggle = $('#menuToggle'),
        $menu = $('#menu');

    $menuToggle.on('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        
        $body.toggleClass('is-menu-visible');
    });

    $menu.on('click', function(event) {
        event.stopPropagation();
    });

    $body.on('click', function(event) {
        $body.removeClass('is-menu-visible');
    });

    $window.on('keydown', function(event) {
        if (event.keyCode === 27) {
            $body.removeClass('is-menu-visible');
        }
    });

})(jQuery);
