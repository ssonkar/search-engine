function getParameterByName(target) {
   
    let url = window.location.href;
 
    target = target.replace(/[\[\]]/g, "\\$&");

  
    let regex = new RegExp("[?&]" + target + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';

    
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}


function handleResult(resultData) {

    console.log("handleResult: populating result table from resultData");
    let queryTable = jQuery("#results_table");
    console.log(resultData[0]);
    var count = 0;
    for (let i = 0; i < resultData.length; i++) {
        if(count == 10){
            break;
        }
         let rowHTML = "";
         rowHTML += "<tr>";
         rowHTML += "<th>" +

         '<a href = http://' + resultData[i]+ '>' + resultData[i] +
         '</a>' +
         "</th>";
         rowHTML += "</tr>";
              
         // Append the row created to the table body, which will refresh the page
         queryTable.append(rowHTML);
         count = count + 1;
         
    } 
}

$("#search").keyup(function(event) {
    if (event.keyCode === 13) {
        $("#btn").click();
    }
});

  $(document).ready(function(){
  let query= getParameterByName('query');
  console.log(query);

  jQuery.ajax({
     
    cache: false,
      method: "GET",
      url: "http://127.0.0.1:4996/search/" + query, 
      success: function(resultData){
      	handleResult(resultData) ;    
      },
      error:function(response){
    	  alert("error");
      }
      
  });  
   
  });
   