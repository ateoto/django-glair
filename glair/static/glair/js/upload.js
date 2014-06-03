$(function() {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  function send_form(element) {
    var form = $(element).parentsUntil('.basic-edit').parent();
    var api_uri = $(form).parent().attr('data-glair-uri');
    $.ajax({ 
      url: api_uri, 
      data: $(form).serialize(), 
      type: 'PUT'
    }).done(function(data) {
        console.log(data);
    });
  }

  Dropzone.options.djangodropzone = {
    paramName: "image",
    init: function() {
      this.on('sending', function(file, xhr, formData) { 
        formData.append('name', file.name);
      });
      this.on('success', function(file, response) {
        $('#photo-editor').append(response.html);
      });
    }
  }

  $('#edit-modal').modal({
    keyboard: true,
    show: false
  });

  $('#edit-save').click(function(){
    $.ajax({ 
      url: $('#basic-edit').attr('action'),
      data: $('#basic-edit').serialize(),
      type: 'PUT'
    }).done(function(data) {
        console.log(data);
        $('#edit-modal').modal('hide');
    });
  });

  $('body').on('click', '.photo-thumb', function(){
    var action_uri = $(this).attr('href');
    $.get(action_uri, function(data){
      $('#basic-edit').attr('action', action_uri);
      $('#id_name').val(data.name);
      $('#id_is_private').prop('checked', data.is_private);
      $('#id_description').val(data.description);
      var cs_tags = '';
      var tag_count = data.tags.length;
      data.tags.forEach(function(element, index, array){
        cs_tags += element + ', ';
      });
      cs_tags = cs_tags.slice(0, -2);
      $('#id_tags').val(cs_tags);
      $('#edit-modal').modal('show');
    });
    return false;
  });
  
});