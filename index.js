
document.addEventListener('DOMContentLoaded', function(){

    let resumeButton = document.getElementById("resumeButton");

    resumeButton.addEventListener("click", function()
    {
        location.href = "page2.html";
    });

    let mediaButton = document.getElementById("mediaButton");

    mediaButton.addEventListener("click", function()
    {
        location.href = "page3.html";
    });
});


