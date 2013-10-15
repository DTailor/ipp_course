$(document).ready(function () {
//     Task 1_1
    $('#problem_1_1 > li').each(function () {
        $(this).click(function () {
            var video_name = $(this).text();
            var video_url = $(this).attr('data-url');
            console.log(video_name + ' <- start');

            var request = $.ajax({
                url: "task1/",
                type: "GET",
                data: { 'url': video_url  },
                dataType: "html"
            });

            request.done(function (msg) {
//                console.log(video_name + '<- downloaded')
                console.log(msg)
            });

            request.fail(function (jqXHR, textStatus) {
                console.log(video_name + ' <- failed to download');
            });
        });
    });

});
