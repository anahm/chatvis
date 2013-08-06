/*
 * formInput.js
 */

$(document).ready(function() {

    // Need something for form input
    $('form[name=chatInfo]').on('submit', function(e) {
        e.preventDefault();

        var form = $(this);
        var inputs = form.find("input");
        var serializedData = form.serialize();

        console.log(serializedData);

        // disable inputs for the duration of the ajax request
        inputs.prop("disabled", true);
        $('[type=submit]').val("waiting...");

        var request = $.ajax({
            type: "POST",
            url: '/chatvisForm',
            data: serializedData,
            dataType: 'json'
        });

        request.done(function (resp, textStatus, jqXHR) {
            console.log(resp);
            $('div#output').html('<p># of chats: ' + resp.convoLen + '</p>');
            $('div#output').append('<p># occurrences of '
                + $('input[name=searchText]').val()
                + ': ' + resp.strCounter + '</p>');

            $('<div id="outputList">').appendTo('#output');
            $.each(resp.strList, function(index, item) {
                $('div#outputList').append('<p>' + item + '</p>');
            })
        });

        request.fail(function (jqXHR, textStatus, errorThrown) {
            console.error("boo sadface: " + textStatus, errorThrown);
        });

        request.always(function () {
            inputs.prop("disabled", false);
            $('[type=submit]').val("Get It!");
        });

        return false;
    });

    // Need something to render to the screen

});

