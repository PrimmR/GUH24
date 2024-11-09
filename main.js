// Each thing has a: description, year, image

years = [
    {
        year_name: "4.6 Billion Years Ago",
        year: -4600000001,
        description: "Beginning of the solar system and the formation of the Earth. During this time, the surface of the Earth is extremely hot and the Earth is basically a giant magma ball floating in space.",
        image: "img/PanoPurpIPad.png"
    }
    ,
    {
        year_name: "4.6 Billion Years Ago - Eon: Hadean",
        year: -4600000000,
        description: "The start of the Hadean eon. This is the first and oldest eons of the Earth's history. During this period, the Earth's surface cooled, vaporized atmospheric water condensed into liquid water and eventually a superocean covering nearly all of the planet was formed, turning Earth into an ocean planet. Volcanic outgassing and asteroid bombardments further altered the Hadean atmosphere eventually into the nitrogen- and carbon dioxide-rich.",
        image: "img/PanoPurpIPad.png"
    }
    ,
    {
        year_name: "4 Billion Years Ago - Eon: Archean",
        year: -4000000001,
        description: "This marks the end of the Hadean eon and the start of the second eon - Archean. Archean eon lasted for 1.5 billion years. In this period, the Earth was still mostly a water world: there was continental crust, but much of it was under an ocean deeper than today's oceans. Except for some rare relict crystals, today's oldest continental crust dates back to the Archean. Much of the geological detail of the Archean has been destroyed by subsequent activity. The Earth's atmosphere was also vastly different in composition from today's: the prebiotic atmosphere was a reducing atmosphere rich in methane and lacking free oxygen. The earliest known life, mostly represented by shallow-water microbial mats called stromatolites, started in the Archean and remained simple prokaryotes (archaea and bacteria) throughout the eon. The earliest photosynthetic processes, especially those by early cyanobacteria, appeared in the mid/late Archean and led to a permanent chemical change in the ocean and the atmosphere after the Archean.",
        image: "img/PanoPurpIPad.png"
    }
    ,
    {
        year_name: "4.6 Billion Years Ago - Era: Eoarchean",
        year: -4000000000,
        description: "This is the start of the Eoarchean era which lasted about 400 million years. In this period, the Earth began to cool down, the atmosphere of the Earth was without oxygen and the pressure values ranged from 10 to 100 bar.",
        image: "img/PanoPurpIPad.png"
    }
    ,
    {
        year_name: "Future",
        year: 2025,
        description: "Future",
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
    year_title.innerHTML = current_year.year_name;
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