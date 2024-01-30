const dropdownItems = document.querySelectorAll('.dropdown-item');
        const selectedImage = document.getElementById('selected-image');
        dropdownItems.forEach(item => {
          item.addEventListener('click', e => {
            e.preventDefault();
            const imgSrc = e.target.dataset.imgSrc;
            selectedImage.setAttribute('src', imgSrc);
          });
        });