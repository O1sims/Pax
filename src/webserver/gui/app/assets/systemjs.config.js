/**
 * System configuration for Angular 2 samples
 * Adjust as necessary for your application needs.
 */

(function(global) {

  var plugin = 'bootstrap';

  var config = {
    map: map,
    baseURL: '/gui/',
    packages: packages
  };

  // map tells the System loader where to look for things
  var map = {
    'app': 'app', // 'dist',
    '@angular': 'app/node_modules/@angular',
    'angular2-in-memory-web-api': 'app/node_modules/angular2-in-memory-web-api',
    'rxjs': 'app/node_modules/rxjs',
    'ng2-charts': 'app/node_modules/ng2-charts/bundles/ng2-charts.umd.js',
    'underscore': 'app/node_modules/underscore/underscore.js',
    '@swimlane/ngx-datatable': 'app/node_modules/@swimlane/ngx-datatable/release/index.js',
    'leaflet': 'app/node_modules/leaflet/dist',
    '@asymmetrik/ngx-leaflet': 'app/node_modules/@asymmetrik/ngx-leaflet/src/leaflet/leaflet.module.js',
    '@asymmetrik/ngx-leaflet-draw': 'app/node_modules/@asymmetrik/ngx-leaflet-draw/src/leaflet-draw/leaflet-draw.module.js',
    'ng2-nvd3': 'app/node_modules/ng2-nvd3/build/lib',
    'angular2-modal': 'app/node_modules/angular2-modal',
    'ngx-popover': 'app/node_modules/ngx-popover',
    'survey-angular': 'app/node_modules/survey-angular',
    'ng2-file-upload': 'app/node_modules/ng2-file-upload'
  };

  // packages tells the System loader how to load when no filename and/or no extension
  var packages = {
    'app' : {
      main: 'main.js',
      defaultExtension: 'js'
    },
    'rxjs' : {
      defaultExtension: 'js'
    },
    'angular2-in-memory-web-api' : {
      main: 'index.js',
      defaultExtension: 'js'
    },
    'leaflet' : {
      main: 'leaflet-src.js',
      defaultExtension: 'js'
    },
    '@asymmetrik/ngx-leaflet' : {
      defaultExtension: 'js'
    },
    '@asymmetrik/ngx-leaflet-draw' : {
      defaultExtension: 'js'
    },
    'ng2-charts' : {
      defaultExtension: 'js'
    },
    'ng2-nvd3' : {
      main: "ng2-nvd3.js",
      defaultExtension: "js"
    },
    'angular2-modal' : {
      main: 'bundles/angular2-modal.umd',
      defaultExtension: 'js'
    },
    'ngx-popover': {
      main: "index.js",
      defaultExtension: "js"
    },
    'survey-angular': {
      main: "survey.angular.js",
      defaultExtension: "js"
    },
    'ng2-file-upload': {
      main: "ng2-file-upload.js",
      defaultExtension: "js"
    }
  };

  var ngPackageNames = [
    'common',
    'compiler',
    'core',
    'forms',
    'http',
    'platform-browser',
    'platform-browser-dynamic',
    'router',
    'router-deprecated',
    'upgrade'
  ];

  // UMD bundles
  map[`angular2-modal/plugins/${plugin}`] = map['angular2-modal'] + '/bundles';
  packages[`angular2-modal/plugins/${plugin}`] =  { defaultExtension: 'js', main: `angular2-modal.${plugin}.umd` };

  // Individual files (~300 requests):
  ngPackageNames.forEach(function (pkgName) {
      // Bundled (~40 requests):
      //packages['@angular/' + pkgName] = { main: pkgName + '.umd.js', defaultExtension: 'js' };

      // Individual files (~300 requests):
      packages['@angular/'+pkgName] = { main: 'index.js', defaultExtension: 'js' };
  });

  // Bundled (~40 requests):
  function packUmd(pkgName) {
    packages['@angular/'+pkgName] = { main: '/bundles/' + pkgName + '.umd.js', defaultExtension: 'js' };
  }

  // Most environments should use UMD; some (Karma) need the individual index files
  var setPackageConfig = System.packageWithIndex ? packIndex : packUmd;

  // Add package entries for angular packages
  ngPackageNames.forEach(setPackageConfig);

  var config = {
    map: map,
    packages: packages
  };

  System.config(config);
})(this);
