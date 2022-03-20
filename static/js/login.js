function messageUser (text) {
    $('#content').html(text)
    $('#exampleModal').modal('show')
  }
    function login () {
      const loginForm = $('#login_form')
      const formData = new FormData(loginForm[0])
      $.ajax({
        url: '/forum/login/',
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
                window.location.href =  formData.get("next")
            }, 1000)

          }
        }
      })
  }