var help_text = 'Commands:<br>' +
'apps_list<br>' +
'models_list<br>' +
'model_fields<br>' +
'clear<br>' +
'help<br>' +
'theme<br>' +
'version<br>';

var terminal = null;

var call_terminal = function(command, method, nosync, arguments){
    var error = 'Error!';
    var res = null;
    var nsync = null;
    var args = null;
    if(typeof arguments === "undefined") {
        args = {};
    }
    else{
        args = arguments;
    }
    $.ajax({
        url: '/' + command + '/',
        type: method,
        data: args,
        success: function(result) {
            res = result;
        },
        error: function(result) {
            res = 'Error';
        },
        async: nosync
    });
    return res;
}

var parse_command = function(cmd, args) {
    var res = null;
    switch (cmd) {
        case 'apps_list':
            return call_terminal('apps_list', 'get', false);
        case 'models_list':
            var args = {
                    'app_label': args[0],
                }
            return call_terminal('models_list', 'get', false, args);
        case 'model_fields':
            var args = {
                    'model_name': args[0],
                }
            return call_terminal('model_fields', 'get', false, args);
        case 'model_instance':
            var args = {
                    'model_name': args[0],
                    'args': args[1],
                }
            return call_terminal('model_instance', 'get', false, args);
        case 'clear':
            terminal.clear();
            return '';
        case 'help':
            return help_text;
        case 'theme':
            if (args && args[0]) {
                if (args.length > 1) return 'Too many arguments';
                else if (args[0].match(/^interlaced|modern|white$/)) { terminal.setTheme(args[0]); return ''; }
                else return 'Invalid theme';
            }
            return terminal.getTheme();
        case 'ver':
        case 'version':
            return '1.0.0';
        default:
            // Unknown command.
            return false;
    };
}