let content = document.querySelector(".content");
(async function getItems() {
    fetch(`/data`)
      .then((response) => response.json())
      .then((data) => setSidebar(data));
	
})();
async function load(page){};
function setSidebar(data){};