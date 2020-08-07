$(document).ready(function(){
    $.get(
        "https://www.googleapis.com/youtube/v3/channels", {
            part: 'contentDetails',
            id: 'UCnlbFb18WzWfsiYnmH10IWg', 
            key: 'AIzaSyDON8FOVrai8e6OlrnNKN5-r9_xktaUEI8' },
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
                maxResults: 24,
                playlistId: pid,
                key: 'AIzaSyDON8FOVrai8e6OlrnNKN5-r9_xktaUEI8' },
                function(data) {
                    var output = "";
                    var count = 1;
                    
                    output.concat("<div class='row'>")

                    $.each(data.items, function(i, item) {
                        console.log(item);
                        vidTitle = item.snippet.title;
                        thumbnails_pic = item.snippet.thumbnails.high.url;
                        vidUrl = item.snippet.resourceId.videoId;
                        var vidtemp = '<div style="margin-bottom: 50px" class="col l4"><a href="https://www.youtube.com/watch?v='+ vidUrl +'"><img src= "https://img.youtube.com/vi/' + vidUrl + '/mqdefault.jpg">'+ vidTitle +'</a></div>';
                        
                        
                        if (count%3 == 0) {
                            output.concat(vidtemp).concat('</div><div class="row">');
                        }
                        else {
                            output.concat('<div style="margin-bottom: 50px" class="col l4"><a href="https://www.youtube.com/watch?v='+ vidUrl +'"><img src= "https://img.youtube.com/vi/' + vidUrl + '/mqdefault.jpg">'+ vidTitle +'</a></div>');
                        }

                        if(count==24) {
                            output = output.substr(output.length - 17);
                        }
                        
                        count += 1;

                        // output = '<div class="col l4"><a href="https://www.youtube.com/watch?v='+ vidUrl +'"><img src= "' + thumbnails_pic + '" width="300px" height="300px"></a></div>';

                        
                        $('#results').append(output);
                  })
              }
        );
    }
});