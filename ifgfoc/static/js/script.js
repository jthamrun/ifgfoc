$(document).ready(function() {
    $.get(
        "https://www.googleapis.com/youtube/v3/channels", {
            part: 'contentDetails',
            id: 'UCnlbFb18WzWfsiYnmH10IWg',
            key: 'AIzaSyBxiln-oRK55Qz_Wh0sbAX1xbeH9oUen_k' },
            function(data) {
                $.each(data.items, function(i, item) {
                    console.log(item);
                    pid = item.contentDetails.relatedPlaylists.uploads;
                    getVids(pid);
                })
            }
    );

    function getVids(pid) {
        $.get(
            "https://www.googleapis.com/youtube/v3/playlistItems", {
                part: 'snippet',
                maxResults: 2,
                playlistId: pid,
                key: 'AIzaSyBxiln-oRK55Qz_Wh0sbAX1xbeH9oUen_k' },
                
                function(data) {
                    var output;
                    $.each(data.items, function(i, item) {
                        console.log(item);
                        vidTitle = item.snippet.title;
                        vidThumbnails = item.snippet.thumbnails.high.url;
                        vidURL = item.snippet.resourceId.videoId;

                        output = '<div class="row"><div class="col l6 s8 push-s2 center-align"><a href="https://www.youtube.com/watch?v=' + vidURL + '"><img src="' + vidThumbnails + '" width=450vw height=400vh></a></div></div>';

                        $('#results').append(output);
                    })
                }
        );
    }
});