from __future__ import absolute_import
__author__ = 'katharine'

from .geolocation import Geolocation, prepare_geolocation


class Navigator(object):
    def __init__(self, runtime):
        self._runtime = runtime

    def setup(self):
        prepare_geolocation(self._runtime)
        self._runtime.context.eval("""
        (function(_internal_location) {
            this.navigator = new (function() {
                this.language = 'en-GB';
    
                var location = _internal_location;
                if(true) { // TODO: this should be a check on geolocation being enabled.
                    this.geolocation = new (function() {
                        _make_proxies(this, location, ['getCurrentPosition', 'watchPosition', 'clearWatch']);
                    })();
                }
            })();
        })""")(Geolocation(self._runtime))
