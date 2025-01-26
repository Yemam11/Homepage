
document.addEventListener('DOMContentLoaded', function(){

    var images = document.querySelectorAll(".row > img");
    var lightbox = document.getElementById("lightbox");
    var spotlightImg = document.getElementById("spotlightImg");
    var index;

    function nextImg()
    {
        if (index == images.length-1)
        {
            spotlightImg.src = images[0].src;
            index = 0;
        }
        else
        {
            spotlightImg.src = images[index+1].src;
            index = index+1;
        }
    }

    function prevImg()
    {
        if (index == 0)
        {
            spotlightImg.src = images[images.length-1].src;
            index = images.length-1;
        }
        else
        {
            spotlightImg.src = images[index-1].src;
            index = index-1;
        }
    }


    images.forEach(image => {
        image.addEventListener("click", function(){
            let newImg = image.src;
            spotlightImg.src = newImg;
            lightbox.style.display = "flex";
            for (var i = 0; i < images.length; i++)
            {
                if (images[i].src === spotlightImg.src)
                {
                    index = i;
                    break;
                }
            }
        });
    });



    let closeButton = document.getElementById("closeButton");
    closeButton.addEventListener("click", function()
    {
        lightbox.style.display = "none";
    });


    let nextButton = document.getElementById("nextButton");
    nextButton.addEventListener("click", nextImg);

    let prevButton = document.getElementById("prevButton");
    prevButton.addEventListener("click", prevImg);

});


