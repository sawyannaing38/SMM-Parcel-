const takenContainer = document.querySelector(".taken-container");
const showBtn = document.querySelector(".show-btn");

showBtn.addEventListener("click", function()
{
    takenContainer.classList.toggle("hidden");

    this.textContent = this.textContent == "Show Taken Parcels"? "Hide Taken Parcels" : "Show Taken Parcels"
})