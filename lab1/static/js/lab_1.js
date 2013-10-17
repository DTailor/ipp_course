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

//    Task 1_2

    function task2() {
        console.log('Fire up batch download');
        console.log(links.yt);
        $.ajax({

            url: "task1/",
            type: "POST",
            data: {'links': JSON.stringify(links.yt)},
            dataType: 'json',
            error: function () {
                proxy_on = false;
                links.yt = {'url': []};
            },
            success: function () {
                proxy_on = false;
                links.yt = {'url': []};
            }
        });
    }

    var links = {};
    links.yt = {'url': []};
    var proxy_on = false;

    $('#problem_1_2 > li').each(function () {
        $(this).click(function () {

            var video_name = $(this).text();
            console.log(video_name)
            var video_url = $(this).attr('data-url');
            links.yt['url'].push(video_url);
            console.log('link added');

            if (!proxy_on) {
                proxy_on = true;
                setTimeout(task2, 10000);
            }

        })

    });

});
