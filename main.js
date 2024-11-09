// Each thing has a: description, year, image

years = [
    {
        year: 3,
        description: "Hello",
        image: "img/PanoBlueIPad.png"
    },
    // {
    //     year: 27,
    //     description: "Goodbye",
    //     image: "img/PanoPurpIPad.png"
    // }
    // , 
    {
        year: 5,
        description: "Image 5",
        image: "img/PanoPurpIPad.png"
    }
]

function sort_years() {
    years = years.sort((a, b) => {
        return a.year - b.year;
    })
    console.log(years)
}

document.addEventListener("DOMContentLoaded", (event) => {
    let slider = document.getElementById("slidebar");
    slider.max = years.length - 1;

    let output = document.getElementById("demo");
    output.innerHTML = slider.value; // Display the default slider value

    sort_years()

    years.forEach(e => {
        let image = document.createElement("img");
        image.src = e.image
        image.id = `bg_${e.year}`
        image.classList.add("background")
        document.getElementById("bg").append(image)
    });


    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        current_year = years[this.value]
        output.innerHTML = current_year.description;


        Array.from(document.getElementsByClassName("background")).forEach(e => {
            e.style.zIndex = -10
            e.animate({
                opacity: [1, 0],
            }, 1000)
        })

        let top_image = document.getElementById(`bg_${current_year.year}`)
        top_image.style.zIndex = -9
        top_image.animate({
            opacity: [0, 1],
        }, 1000)
    }
});