let content = document.querySelector(".file");
let input = document.querySelector("#input-holder");
(async function getItems() {
  fetch(`/data`)
    .then((response) => response.json())
    .then((data) => setSidebar(data));
})();

function setContent(page) {
    content.innerHTML="";
    content.insertAdjacentHTML("afterbegin", page);
}

async function load(page) {
    fetch(`/${page}`)
    .then((response) => response.json())
    .then((data) => setContent(data));
}

function setSidebar(data) {
  sidebar = document.querySelector(".sidebar-content");
  sidebar.innerHTML = "<ul>";
  for (let line of data) {
    sidebar.insertAdjacentHTML(
      "afterbegin",
      `<div style="display: inline-block"><a href="/remove/${line}"><span class="bi bi-file-x-fill"></span></a><a style="display: inline" href="#" class="nav-link" onclick="load('${line}')">${line}</a> </div>`
    );
  }
  sidebar.insertAdjacentHTML("beforeend", "</ul>");
}
function unhideInput() {
  content.innerHTML="";
  input.style.display="block";
}
function hideInput() {
  input.style.display='none';
}
function showDeleteButtons() {

}
