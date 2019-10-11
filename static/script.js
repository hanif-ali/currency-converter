function load_data(){

    const request = new XMLHttpRequest();

    var source = document.querySelector("#source").value;
    var target = document.querySelector("#target").value;
    var amount = document.querySelector("#amount").value;

    request.open("POST", "/convert");

    request.onload = ()=>{
        const results = JSON.parse(request.responseText);

        var result = document.createElement("div");
        result_wrapper = document.querySelector("#result_wrapper");
        result_wrapper.innerHTML = "";

        if(results.success){
 

            result_html = `<strong>1</strong> ${results.source} IS <strong>${results.rate}</strong> ${results.target}<br>`;
            result_html += `<strong>${results.amount} </strong>${results.source} IS <strong>${results.target_amount}</strong> ${results.target}<br>`;
            
            result.innerHTML = result_html;

            result.setAttribute("class", "results alert alert-success");

            result_wrapper.appendChild(result);

        }
        else{
            result.setAttribute("class", "results alert alert-danger")
            result_html = "Sorry, The Application incurred some internal error."
            result.innerHTML = result_html
            result_wrapper.appendChild(result);

        }

    }
    const data = new FormData()
    data.append("source", source)
    data.append("target", target)
    data.append("amount", amount)

    request.send(data)

}

document.addEventListener("DOMContentLoaded", ()=>{
    var conv_form = document.querySelector("#conv_form");
    var amount_field = conv_form.querySelector('#amount');
    var submit_btn = conv_form.querySelector("#submit");
    conv_form.addEventListener("submit", (e)=>{
        e.preventDefault()
        load_data()
    });

    amount_field.addEventListener("keyup", ()=>{
        if(!amount_field.value){
            submit_btn.setAttribute("disabled", "disabled");
        }
        else{
            submit_btn.removeAttribute("disabled");
        }


    });

});


