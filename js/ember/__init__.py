import fanstatic
import js.jquery

library = fanstatic.Library('ember', 'resources')

hb = fanstatic.Resource(library, 'handlebars-1.0.0.beta.6.js')

ember = fanstatic.Resource(library, 'ember.js', minified='ember.min.js',
                 depends=[js.jquery.jquery, hb])
