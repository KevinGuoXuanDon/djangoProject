// pass the message to views
function messageUser (text) {
    $('#content1').html(text)
    $('#exampleModal1').modal('show')
  }
    function register () {
      const loginForm = $('#user_form')
      const formData = new FormData(loginForm[0])
      $.ajax({
        url: '/forum/register/',
        method: 'post',
        data: formData,
        contentType:false,
        processData: false,
        success (res) {
          if (res.code !== 0) {
            messageUser(res.msg)
          } else {
            messageUser(res.msg)
            setTimeout(function () {
                window.location.href = res.data.url
            }, 1000)
          }
        }
      })
      return false
  }