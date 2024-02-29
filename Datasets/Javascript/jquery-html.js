$('#new').on('click', function() {
    let data = {
        'title': $('#title').get(0).value,
        'content': $('#content').get(0).value,
    };
    $.ajax({
        type: 'POST',
        url: '/api/new',
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: (data) => {
            if (data.result == 'OK') {
                location.reload();
            } else {
                UIkit.notification({
                    message: "<span uk-icon='icon: error'></span> Error: " + data.reason,
                    status: 'danger'
                });
            }
        },
        error: (data) => {
            UIkit.notification({
                message: "<span uk-icon='icon: error'></span> Request error",
                status: 'danger'
            });
        }
    });
});

$('#export').on('click', function() {
    $.ajax({
        type: 'GET',
        url: '/api/export',
        dataType: 'json',
        success: (data) => {
            if (data.result == 'OK') {
                let blob = new Blob([data.export], {"type": "text/plain"});
                console.log(blob);
                $('<a>', {
                    href: window.URL.createObjectURL(blob),
                    download: 'backup.db'
                }).get(0).click();
            } else {
                UIkit.notification({
                    message: "<span uk-icon='icon: error'></span> Error: " + data.reason,
                    status: 'danger'
                });
            }
        },
        error: (data) => {
            UIkit.notification({
                message: "<span uk-icon='icon: error'></span> Request error",
                status: 'danger'
            });
        }
    });
});

$('#import').on('click', function() {
    $('<input>', {
        type: 'file',
    }).on('change', function(e) {
        let reader = new FileReader();
        reader.readAsText(e.target.files[0]);
        reader.onload = (re) => {
            let data = {'import': re.target.result};
            $.ajax({
                type: 'POST',
                url: '/api/import',
                dataType: 'json',
                data: JSON.stringify(data),
                contentType: 'application/json',
                success: (data) => {
                    if (data.result == 'OK') {
                        location.reload();
                    } else {
                        UIkit.notification({
                            message: "<span uk-icon='icon: error'></span> Error: " + data.reason,
                            status: 'danger'
                        });
                    }
                },
                error: (data) => {
                    UIkit.notification({
                        message: "<span uk-icon='icon: error'></span> Request error",
                        status: 'danger'
                    });
                }
            });
        }
    }).get(0).click();
});

$('button[id="delete"]').on('click', function(e) {
    let data = {'id': $(this).get(0).name};
    e.preventDefault();
    e.target.blur();
    UIkit.modal.confirm('Are you sure you want to delete "<b>'+data.id+'</b>"?').then(() => {
        $.ajax({
            type: 'POST',
            url: '/api/delete',
            dataType: 'json',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: (data) => {
                if (data.result == 'OK') {
                    location.reload();
                } else {
                    UIkit.notification({
                        message: "<span uk-icon='icon: error'></span> Error: " + data.reason,
                        status: 'danger'
                    });
                }
            },
            error: (data) => {
                UIkit.notification({
                    message: "<span uk-icon='icon: error'></span> Request error",
                    status: 'danger'
                });
            }
        });
    });
});

$('#login').on('click', ()=>{
let data = {
    'username': $('#username')[0].value,
    'password': $('#password')[0].value
};
$.ajax({
    type: 'POST',
    url: '/api/login',
    dataType: 'json',
    data: JSON.stringify(data),
    contentType: 'application/json',
    success: (data) => {
        location.reload();
    },
    error: (data) => {
        UIkit.notification({
            message: "<span uk-icon='icon: error'></span> Request error",
            status: 'danger'
        });
    }
});
});
