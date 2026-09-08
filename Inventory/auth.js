// ===========================
// USERS
// ===========================

const USERS = {

    SCM: {

        password: "Inventory123",
        role: "inventory"

    },

    Inside_Sales: {

        password: "InsideSales123",
        role: "sales"

    },
    Sales: {
        password: "EISales123",
        role: "sales"

    }

};

// ===========================
// LOGIN
// ===========================

window.login = function () {

    const username =
        document.getElementById("username")
            .value
            .trim()
            .toLowerCase();

    const password =
        document.getElementById("password")
            .value;

    const user = USERS[username];

    if (!user || user.password !== password) {

        const msg = document.getElementById("loginMessage");

        if (msg) {

            msg.textContent = "Invalid username or password.";

        }

        return;

    }

    localStorage.setItem("loggedIn", "true");
    localStorage.setItem("username", username);
    localStorage.setItem("role", user.role);

    if (user.role === "inventory") {

        window.location.href = "Main_Inv_Page.html";

    }
    else {

        window.location.href = "Sales_Page.html";

    }

};

// ===========================
// LOGOUT
// ===========================

window.logout = function () {

    localStorage.clear();

    window.location.href = "index.html";

};

// ===========================
// AUTH CHECK
// ===========================

window.checkAccess = function (allowedRoles) {

    const loggedIn =
        localStorage.getItem("loggedIn");

    const role =
        localStorage.getItem("role");

    if (loggedIn !== "true") {

        window.location.href = "index.html";
        return;

    }

    if (!allowedRoles.includes(role)) {

        alert("You are not authorized to access this page.");

        logout();

    }

};

// ===========================
// SHOW USERNAME
// ===========================

window.showLoggedInUser = function () {

    const label =
        document.getElementById("usernameLabel");

    if (!label) return;

    label.textContent =
        localStorage.getItem("username");

};
