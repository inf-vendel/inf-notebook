let content = document.querySelector(".file");
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
      `<a href="#" class="nav-link" onclick="load('${line}')">${line}</a>`
    );
  }
  sidebar.insertAdjacentHTML("beforeend", "</ul>");
}
