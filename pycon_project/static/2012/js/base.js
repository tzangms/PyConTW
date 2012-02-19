jQuery.fn.autoscroll = function() {
    $('html,body').animate({scrollTop: this.offset().top}, 500);
}

$(function() {
    $(".alert .close").click(function() {
        $(this).parent().fadeOut();
        return false;
    });
});
