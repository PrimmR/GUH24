// Each thing has a: description, year, image

years = [
    {
        year: 3,
        description: "Hello",
        image: "PanoBlueIPad.png"
    },
    {
        year: 27,
        description: "Goodbye",
        image: "PanoPurpIPad.png"
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
    slider.max = years.length;

    let output = document.getElementById("demo");
    output.innerHTML = slider.value; // Display the default slider value

    sort_years()


    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        output.innerHTML = this.value;

        document.getElementById("bg_img2").style.opacity = this.value
    }
});