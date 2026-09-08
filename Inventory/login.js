// ===========================
// SLIDES
// ===========================

const slides = [

    {

        image: "images/1.jpg",

        title: "Inventory Management",

        text:
            "Track materials, suppliers, inventory levels and production from one centralized platform."

    },

    {

        image: "images/2.jpg",

        title: "Production Planning",

        text:
            "Monitor stock availability and manage manufacturing with real-time inventory visibility."

    },

    {

        image: "images/3.jpg",

        title: "Sales Catalogue",

        text:
            "Provide your sales team with up-to-date material information and landed costs instantly."

    },

    {

        image: "images/4.jpg",

        title: "Erith Global",

        text:
            "Erith Global Inventory - Procurement, Order Management."

    }

];

let currentSlide = 0;

const currentImage =
    document.getElementById("slideCurrent");

const nextImage =
    document.getElementById("slideNext");

const title =
    document.getElementById("slideTitle");

const text =
    document.getElementById("slideText");

const dots =
    document.querySelectorAll(".dot");

// ===========================
// PRELOAD ALL IMAGES
// ===========================

slides.forEach(slide => {

    const img = new Image();

    img.src = slide.image;

});

// ===========================
// INITIAL SLIDE
// ===========================

currentImage.src = slides[0].image;

nextImage.src = slides[1].image;

title.textContent = slides[0].title;

text.textContent = slides[0].text;

dots[0].classList.add("active");

// ===========================
// CHANGE SLIDE
// ===========================

function showSlide(index) {

    // Fade text out

    title.style.opacity = 0;
    title.style.transform = "translateY(10px)";

    text.style.opacity = 0;
    text.style.transform = "translateY(10px)";

    // Preload the next image first

    const preload = new Image();

    preload.onload = () => {

        nextImage.src = preload.src;

        nextImage.style.transition = "none";
        nextImage.style.transform = "translateX(100%)";

        requestAnimationFrame(() => {

            requestAnimationFrame(() => {

                currentImage.style.transition =
                    "transform .7s ease";

                nextImage.style.transition =
                    "transform .7s ease";

                currentImage.style.transform =
                    "translateX(-100%)";

                nextImage.style.transform =
                    "translateX(0)";

            });

        });

        setTimeout(() => {

            currentImage.src = preload.src;

            currentImage.style.transition = "none";
            currentImage.style.transform = "translateX(0)";

            nextImage.style.transition = "none";
            nextImage.style.transform = "translateX(100%)";

        }, 700);

    };

    preload.src = slides[index].image;

    // Update text

    setTimeout(() => {

        title.textContent =
            slides[index].title;

        text.textContent =
            slides[index].text;

        title.style.opacity = 1;
        title.style.transform = "translateY(0)";

        text.style.opacity = 1;
        text.style.transform = "translateY(0)";

    }, 250);

    dots.forEach(dot =>
        dot.classList.remove("active")
    );

    dots[index].classList.add("active");

}

// ===========================
// AUTO ROTATE
// ===========================

window.addEventListener("load", () => {

    setInterval(() => {

        currentSlide++;

        if (currentSlide >= slides.length)
            currentSlide = 0;

        showSlide(currentSlide);

    }, 5000);

});

// ===========================
// ENTER KEY
// ===========================

document
    .getElementById("password")
    .addEventListener("keypress", function (e) {

        if (e.key === "Enter") {

            login();

        }

    });

// ===========================
// BETTER LOGIN()
// ===========================

const originalLogin = window.login;

window.login = function () {

    const username =
        document
            .getElementById("username")
            .value
            .trim();

    const password =
        document
            .getElementById("password")
            .value;

    const message =
        document.getElementById("loginMessage");

    message.textContent = "";

    if (!username || !password) {

        message.textContent =
            "Please enter your username and password.";

        return;

    }

    try {

        originalLogin();

    }

    catch {

        message.textContent =
            "Invalid username or password.";

    }

};