jq(document).ready(function() {
    jq('.cmrs-news img, .portlet-image img')
        .prepOverlay({
            subtype: 'image',
            urlmatch: '/image_.+$',
            urlreplace: '/image_large'
        });
});
