document.addEventListener("DOMContentLoaded", function () {
  // Drag and drop logic
  const dropZone = document.getElementById("drop-zone");
  const contentInput = document.getElementById("content-input");
  const styleInput = document.getElementById("style-input");
  const contentPreview = document.getElementById("content-preview");
  const stylePreview = document.getElementById("style-preview");
  const form = document.getElementById("upload-form");
  const loading = document.getElementById("loading");

  // Helper to preview image
  function previewImage(input, preview) {
    if (input.files && input.files[0]) {
      const reader = new FileReader();
      reader.onload = function (e) {
        preview.src = e.target.result;
        preview.style.display = "block";
      };
      reader.readAsDataURL(input.files[0]);
    }
  }

  // Drag and drop events
  if (dropZone) {
    dropZone.addEventListener("click", function () {
      if (!contentInput.files.length) {
        contentInput.click();
      } else if (!styleInput.files.length) {
        styleInput.click();
      } else {
        contentInput.click(); // fallback
      }
    });
    dropZone.addEventListener("dragover", function (e) {
      e.preventDefault();
      dropZone.classList.add("dragover");
    });
    dropZone.addEventListener("dragleave", function (e) {
      dropZone.classList.remove("dragover");
    });
    dropZone.addEventListener("drop", function (e) {
      e.preventDefault();
      dropZone.classList.remove("dragover");
      const files = e.dataTransfer.files;
      if (files.length) {
        if (!contentInput.files.length) {
          contentInput.files = files;
          previewImage(contentInput, contentPreview);
        } else if (!styleInput.files.length) {
          styleInput.files = files;
          previewImage(styleInput, stylePreview);
        }
      }
    });
  }

  // File input change events
  if (contentInput) {
    contentInput.addEventListener("change", function () {
      previewImage(contentInput, contentPreview);
    });
  }
  if (styleInput) {
    styleInput.addEventListener("change", function () {
      previewImage(styleInput, stylePreview);
    });
  }

  // Show spinner on submit
  if (form && loading) {
    form.addEventListener("submit", function () {
      loading.style.display = "flex";
    });
    loading.style.display = "none";
  }
});
