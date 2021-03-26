from __future__ import absolute_import
__author__ = 'katharine'

import time


class Performance(object):
    # This is an approximation for now
    def __init__(self, runtime):
        self.runtime = runtime
    
    def setup(self):
        self.runtime.context.eval("""
            (function(_time) {
                this.performance = new (function() {
                    var start = _time();

                    this.now = function() {
                        return (_time() - start) * 1000;
                    };
                })();
            })
        """)(lambda: time.time())