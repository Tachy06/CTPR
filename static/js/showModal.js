var card = document.querySelector('.card');
var modalTrigger = card.dataset.target;
                
card.addEventListener('click', function() {
    $(modalTrigger).modal('show');
});