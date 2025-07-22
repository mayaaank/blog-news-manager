// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // ===== Expand Search Input =====
  const searchInput = document.querySelector(".search-input");
  const searchBtn = document.querySelector(".search-btn");

  // Focus input on button click
  if (searchBtn && searchInput) {
    searchBtn.addEventListener("click", (e) => {
      e.preventDefault();
      searchInput.focus(); // Focus input
    });
  }

  // ===== Dropdown Hover (already handled in CSS) =====
  // For mobile click support or JS-only dropdowns, you can do this:
  const dropdownToggle = document.querySelector(".dropdown-toggle");
  const dropdownMenu = document.querySelector(".dropdown-menu");

  if (dropdownToggle && dropdownMenu) {
    dropdownToggle.addEventListener("click", (e) => {
      e.preventDefault();
      dropdownMenu.classList.toggle("show");
    });

    // Hide dropdown when clicking outside
    document.addEventListener("click", (e) => {
      if (!dropdownMenu.contains(e.target) && !dropdownToggle.contains(e.target)) {
        dropdownMenu.classList.remove("show");
      }
    });
  }
});
