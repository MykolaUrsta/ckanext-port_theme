
function myFunction() {
    $("#field-format").removeClass("form-control");
    $("#field-tag_string").removeClass("form-control");
}

(window.location.pathname);

if (window.location.pathname === "/blog") $('#content').css("padding-left", "30px");;
if (window.location.pathname === "/pages") $('#content').css("padding-left", "30px");;
if (window.location.pathname === "/blog_edit" || "/blog_edit/")
    var fullDate = new Date()
var twoDigitMonth = ((fullDate.getMonth().length + 1) === 1) ? (fullDate.getMonth() + 1) : '0' + (fullDate.getMonth() + 1);
var currentDate = fullDate.getFullYear() + "-" + twoDigitMonth + "-" + fullDate.getDate();
$('#field-publish_date').val(currentDate);;

$('#open-filter span').text('Відкриті');
$('#closed-filter span').text('Закриті');
$('#visible-filter span').text('Публічні');
$('#hidden-filter span').text('Приховані');

$('.issue-header-status.open').html('<i class="icon-unlock fa fa-unlock"></i> Відкрита');
$('.issue-header-status.closed').html('<i class="icon-lock fa fa-lock"></i> Закрита');

var child3 = $('.issue-show');
if (child3.length > 0) {
    var user_url = $('.issue-header-text').find('a:first').attr('href');
    var new_user_url = user_url.replace('user_datasets?id=', '/user/');
    $('.issue-header-text').find('a:first').attr("href", new_user_url);
    $('.issue-comment-wrapper').find('a:first').attr("href", new_user_url);;
}


if (window.location.pathname === "/") $("div[role='main'] a:not(.label)").css("color", "#333333");;
if (window.location.pathname === "/group") $(".media-grid a").css("color", "#333333");;
if (window.location.pathname === "/organization") $(".media-grid a").css("color", "#333333");;

