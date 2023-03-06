let img_elements;
let num_of_images;
let current_image_index;
let prev_link;
let next_link;
let count_display;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    img_elements = document.querySelectorAll('.slideshow img');
    num_of_images = img_elements.length;

    for (let image of img_elements) {
        image.style.display = 'none';
    }

    let control_div_left = create_control_div_left();
    let control_div_right = create_control_div_right();
    let aside_element = document.querySelector('.detailmain');
    aside_element.appendChild(control_div_left);
    aside_element.appendChild(control_div_right);

    current_image_index = 0;
    goto_image(null);
}

function create_control_div_left() {
    prev_link = document.createElement('img');
    prev_link.src = "left1.jpg";

    prev_link.addEventListener('click', goto_image, false);

    let control_div_left = document.createElement('div');
    control_div_left.className="left";
    control_div_left.appendChild(prev_link);

    control_div_left.style.textAlign = "center";
    return control_div_left;
}

function create_control_div_right() {
    next_link = document.createElement('img');
    next_link.src = "right1.jpg";

    next_link.addEventListener('click', goto_image, false);

    let control_div_right = document.createElement('div');
    control_div_right.className="right";
    control_div_right.appendChild(next_link);

    control_div_right.style.textAlign = "center";
    return control_div_right;
}

function goto_image(event) {
    img_elements[current_image_index].style.display = 'none';

    if (! event) {
        // don't change slide
    } else if (event.target === prev_link) {
        current_image_index -= 1;
    } else if (event.target === next_link) {
        current_image_index += 1;
    }
    img_elements[current_image_index].style.display = 'inline';

    if (current_image_index === 0) {
        prev_link.style.visibility = 'hidden';
    } else {
        prev_link.style.visibility = 'visible';
    }

    if (current_image_index === num_of_images - 1) {
        next_link.style.visibility = 'hidden';
    } else {
        next_link.style.visibility = 'visible';
    }


}
