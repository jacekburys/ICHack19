// This file is part of server.
// https://github.com/someuser/somepackage

// Licensed under the MIT license:
// http://www.opensource.org/licenses/MIT-license
// Copyright (c) 2018, Jacek Burys <jacekburys@gmail.com>

var bower = require('./node_modules/bower');
var organizeSources = require('./node_modules/organize-bower-sources');
var fs = require('fs');

var writeDependenciesFile = function(file, content) {
    fs.writeFile(file, content, function(err) {
        if (err) {
            console.log('Could not create ' + file + '. ' + err);
        } else {
            console.log('File ' + file + ' created successfully!');
        }
    })
};

bower.commands.list({json: true})
.on('end', function(list){
    var bowerSources = organizeSources( list );
    writeDependenciesFile('./server/static/bower_dependencies.json', JSON.stringify(bowerSources));
})
