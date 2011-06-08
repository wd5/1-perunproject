 $(document).ready(function() {
    jQuery('.htabs li a:not(:first)').css('color','gray');
    jQuery('.tab:not(:first)').hide();     //if this is not the first tab, hide it
    jQuery('.tab:first').show();     //to fix u know who

    //when we click one of the tabs
    jQuery(".htabs li a").click(function(){
    stringref = jQuery(this).attr("href").split('#')[1];     //get the ID of the element we need to show
    jQuery('.tab:not(#'+stringref+')').hide();      //hide the tabs that doesn't match the ID

    //fix for ie6
    if (jQuery.browser.msie && jQuery.browser.version.substr(0,3) == "6.0") {
	    jQuery('.tab#' + stringref).show();
    }
    else
	    jQuery('.tab#' + stringref).fadeIn();     //display our tab fading it in
    jQuery('.htabs li a#' + stringref).css('color','#FFAE5E');
    jQuery('.htabs li a:not(#' + stringref+')').css('color','gray');
    return false;     //stay with me
    });
 });                         

