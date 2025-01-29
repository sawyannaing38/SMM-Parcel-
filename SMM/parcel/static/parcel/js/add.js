const nameInput = document.querySelector(".name");
const phoneInput = document.querySelector(".phone");
const itemInput = document.querySelector(".item");
const countInput = document.querySelector(".count");
const costInput = document.querySelector(".cost");
const statusInput = document.querySelector(".status");
const message = document.querySelector(".message");
const form = document.querySelector("form");

// Adding event on form 
form.addEventListener("submit", function(event)
{
    event.preventDefault();

    const status = ["pick", "unpick", "busy", "close", "unconnect"];

    if (!nameInput.value)
    {
        message.textContent = "Missing Name";
        return;
    }

    if (!phoneInput.value)
    {
        message.textContent = "Missing Phone Number";
        return;
    }

    if (!itemInput.value)
    {
        message.textContent = "Missing Item";
        return;
    }

    if (!countInput.value)
    {
        message.textContent = "Missing Count";
        return;
    }

    if (!costInput.value)
    {
        message.textContent = "Missing Cost";
        return;
    }

    if (!statusInput.value)
    {
        message.textContent = "Missng Status";
        return;
    }

    if (!Number(countInput.value))
    {
        message.textContent = "Invalid Count Input";
        return;
    }

    if (!Number(costInput.value))
    {
        message.textContent = "Invalid Cost Input";
        return;
    }

    if (Number(costInput.value) < 0)
    {
        message.textContent = "Invalid Cost Input";
        return;
    }

    if (!status.includes(statusInput.value))
    {
        message.textContent = "Invalid Status Input";
        return;
    }

    message.textContent = "";
    form.submit();

})