$(document).ready(function() {
    $(".read-more").click(function() {
        var blogId = $(this).data("blogid");
        $("#description_" + blogId).css("height", "auto");
        $(this).hide();
        $(".read-less[data-blogid='" + blogId + "']").show();
    });

    $(".read-less").click(function() {
        var blogId = $(this).data("blogid");
        $("#description_" + blogId).css("height", "4em");
        $(this).hide();
        $(".read-more[data-blogid='" + blogId + "']").show();
    });
});
