import fanstatic
import js.jquery

library = fanstatic.Library('ember', 'resources')

hb = fanstatic.Resource(library, 'handlebars-1.0.0.js')

ember = fanstatic.Resource(
    library,
    'ember-1.0.0-rc.8.js',
    minified='ember-1.0.0-rc.8.min.js',
    depends=[js.jquery.jquery, hb])
