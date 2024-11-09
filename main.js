// Each thing has a: description, year, image

years = [
    {
        year: 3,
        description: "Hello",
        image: "img/PanoBlueIPad.png"
    },
    {
        year: 27,
        description: "Goodbye",
        image: "img/PanoOrangeIPad.png"
    }
    ,
    {
        year: 5,
        description: "Image 5",
        image: "img/PanoPurpIPad.png"
    }
];

addEventListener("wheel", (event) => {
    let slide = document.getElementById("slidebar")
    let old_slide_value = slide.value;
    if (event.wheelDelta > 0) {
        slide.value++;
    } else if (event.wheelDelta < 0) {
        slide.value--;
    }
    if (slide.value !== old_slide_value)
        slider_update(slide.value)
});

function sort_years() {
    years = years.sort((a, b) => {
        return a.year - b.year;
    })
}

function slider_update(y) {
    current_year = years[y];

    let description = document.getElementById("desc");
    description.innerHTML = "";

    let year_title = document.createElement("h2");
    year_title.innerHTML = current_year.year;
    description.append(year_title);

    let desc_desc = document.createElement("p");
    desc_desc.innerHTML = current_year.description;
    description.append(desc_desc);

    // description.innerHTML = current_year.description;


    Array.from(document.getElementsByClassName("background")).forEach(e => {
        e.style.zIndex = -11
    });


    let last_image = document.getElementById(`bg_${last_year.year}`);
    last_image.style.zIndex = -10;

    let top_image = document.getElementById(`bg_${current_year.year}`);
    top_image.style.zIndex = -9;
    top_image.animate({
        opacity: [0, 1],
    }, 1000);

    last_year = current_year
}

let current_year = years[0];
let last_year = years[1];

document.addEventListener("DOMContentLoaded", () => {
    let slider = document.getElementById("slidebar");
    slider.max = years.length - 1;

    sort_years();

    years.forEach(e => {
        let image = document.createElement("img");
        image.src = e.image;
        image.id = `bg_${e.year}`;
        image.classList.add("background");
        document.getElementById("bg").append(image);
    });


    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        slider_update(this.value)
    }
});