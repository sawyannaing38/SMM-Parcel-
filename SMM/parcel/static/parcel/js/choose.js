const senderInputs = document.querySelectorAll(".sender");
const continueBtn = document.querySelector(".continueBtn");
const message = document.querySelector(".message");
const form = document.querySelector("form");

// Adding event on each sender
senderInputs.forEach(function(senderInput) 
{
    senderInput.addEventListener("change", function()
    {
        // Getting the value of it 
        const sender = this.value;

        // if sender is not empty / disabled other 2 inputs
        if (sender)
        {
            // Diabled other select
            senderInputs.forEach(function(send)
            {   
                if (send != senderInput)
                {
                    send.disabled = true
                }
            })
        }

        // if sener is empty
        else 
        {
            senderInputs.forEach(function(senderInput)
            {
                senderInput.disabled = false 
            })
        }
    })
})

// Adding event on continueBtn
form.addEventListener("submit", function(event)
{   
    event.preventDefault();

    // Getting value from input
    let sender = "";

    senderInputs.forEach(function(senderInput)
    {
        // if the input value is not empty, set them as sender 
        if (senderInput.value)
        {
            sender = senderInput.value;
        }
    })

    // if sender is still empty warm the user 
    if (!sender)
    {
        message.textContent = "Missing Sender";
        return false;
    }
    form.submit()
})