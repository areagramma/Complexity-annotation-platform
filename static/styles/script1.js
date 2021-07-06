

    //preventing form from being sent if the token is not valid
      var el = document.getElementById('token-form');
        if(el){
          el.addEventListener('click', swapper, false);
        }
        else{
            alert("e NULL");
        }
        el.addEventListener("submit", function(event) {
        var token = document.getElementById("token").value;
        if (token != "test123"){
          alert("Incorrect token!");
          event.preventDefault();
        }
      });


