
    function validate_is_like(url, id, likes) {
        // get the data from local storage
        let storage = window.localStorage;
        const storage_str_data = storage.getItem("my_blog_data");
        let storage_json_data = JSON.parse(storage_str_data);
        if (!storage_json_data) {
            storage_json_data = {}
        };

        const status = check_status(storage_json_data, id);
        $('span#likes_number').text(likes + 1).css('color', '#dc3545');

        $.post(
            url,
  
            {},
            function(result) {
                if (result === 'success') {
                    try {
                        storage_json_data[id] = true;
                    } catch (e) {
                        window.localStorage.clear();
                    };
                    // change it to string
                    const d = JSON.stringify(storage_json_data);
                    // try to save into the form
                    try {
                        storage.setItem("my_blog_data", d);
                    } catch (e) {
                        // full local storage error
                        if (e.code === 22) {
                            window.localStorage.clear();
                            storage.setItem("my_blog_data", d);
                        }
                    };
                } else {
                    layer.msg("failed to connect");
                }
 
            }
        );
    };
 
    // check if this like button is pressed
    function check_status(data, id) {
        try {
            if (id in data && data[id]) {
                return true;
            } else {
                return false;
            }
        } catch (e) {
            window.localStorage.clear();
            return false;
        };
    };
