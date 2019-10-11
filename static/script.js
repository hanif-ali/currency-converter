function load_data(){
    const request = new XMLHttpRequest();
    var source = document.querySelector("#source").value;
    var target = document.querySelector("#target").value;
    var amount = document.querySelector("#amount").value;
    console.log(`${amount} in ${source} to ${target}`)

    request.open("POST", "/convert");
    request.onload = ()=>{
        const results = JSON.parse(request.responseText);
        if(results.success){
            var result = document.createElement("div");

            result_html = `<strong>1</strong> ${results.source} IS <strong>${results.rate}</strong>${results.target}<br>`;
            result_html += `<strong>${results.amount} </strong>${results.source} IS <strong>${results.target_amount}</strong> ${results.target}<br>`;
            
            result.innerHTML = result_html;

            result.setAttribute("class", "results alert alert-success");

            result_wrapper = document.querySelector("#result_wrapper");
            result_wrapper.innerHTML = "";
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
    var submit_btn = document.querySelector("#conv_form")
    submit_btn.addEventListener("submit", (e)=>{
        e.preventDefault()
        load_data()
    })
})
