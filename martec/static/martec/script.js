// Allow end user have search ignoring special characters, very common in portoguese
function removeDiacritics(str){
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function scrollToProduct(){
    var input = document.getElementById('productSearch').value.toLowerCase();
    // Remove "weird" characters from user input.
    input = removeDiacritics(input);

    // Get product name from user input.
    var productName = document.querySelectorAll('.product-name');

    // Search for product
    for (var i = 0; i < productName.length; i++) {
        var name = productName[i].textContent.toLowerCase();
        name = removeDiacritics(name);

        // Returning the first product that matches the user input.
        if (name.includes(input)){
            var card = productName[i].parentNode.parentNode.parentNode;
            // Scroll the website to the desired product.
            card.scrollIntoView({ behavior: 'smooth', block: 'start'});
            card.style.border = '2px solid';

            setTimeout(function(c) {
                c.style.border = '';
            }, 2000, card);

            return
        }
    }

    // Portuguese alert message "Product not found".
    alert("Produto não encontrado");
}

function showToast(message, isSucess = true){
    const toastEl = document.getElementById('liveToast');
    const toastBody = document.getElementById('toastMessage');

    toastBody.textContent = message;

    // Different toast colors according to the message.
    toastEl.classList.remove('bg-success', 'bg-danger');
    toastEl.classList.add(isSucess ? 'bg-success' : 'bg-danger');

    const toast = new bootstrap.Toast(toastEl);
        toast.show();
}

document.addEventListener("DOMContentLoaded", () => {
    // Get form using element id.
    const form = document.getElementById("contactForm");
    // Return nothing if form is invalid/empty.
    if (!form) return;

    const status = form.dataset.formStatus;

    // If-statement for form input error check.
    if (status === "error"){
        let message = "Erros no formulário:\n";
        const errors = document.querySelectorAll(".is-invalid");
        errors.forEach(input => {
            const label = input.closest(".mb-3")?.querySelector("label")?.textContent || "Campo";
            const errorText = input.nextElementSibling?.textContent || "Invalido";
            message += `${label}: ${errorText}\n`;
        });

        showToast(message,false);
    } else if (status === "success"){
        showToast("Mensagem recebida! Em breve, nossa equipe entrará em contato com as melhores soluções para você.")
    }
})