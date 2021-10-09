
function subvisa(link)
{
alert("Called");
link = "/visa/"+link;
location.href = link;
}


function sendMail()
{
    function sendEmail() {
        Email.send({
          Host: "smtp.gmail.com",
          Username: "ashish.adhikari727@gmail.com",
          Password: "icanbenumber1",
          To: 'ashishadhikari.be18cse@pec.edu.in',
          From: "ashish.adhikari727@gmail.com",
          Subject: "Sending Email using javascript",
          Body: "Well that was easy!!",
        })
          .then(function (message) {
            alert("mail sent successfully")
          });
      }
}