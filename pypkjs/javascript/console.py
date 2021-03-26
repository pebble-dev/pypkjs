from __future__ import absolute_import
__author__ = 'katharine'

import STPyV8 as v8


class Console(object):
    def __init__(self, runtime):
        self.runtime = runtime

    def setup(self):
        self.runtime.context.eval("""
        (function (_internal_console) {
            this.console = new (function() {
                _make_proxies(this, _internal_console, ['log', 'warn', 'info', 'error']);
            })();
        })""")(self)

    def log(self, *params):
        # kOverview == kLineNumber | kColumnOffset | kScriptName | kFunctionName
        trace_str = str(v8.JSStackTrace.GetCurrentStackTrace(2, v8.JSStackTrace.Options.Overview))
        try:
            frames = v8.JSError.parse_stack(trace_str.strip())
            caller_frame = frames[0]
            filename = caller_frame[1]
            line_num = caller_frame[2]
            file_and_line = u"{}:{}".format(filename, line_num)
        except:
            file_and_line = u"???:?:?"
        log_str = u' '.join([x.toString() if hasattr(x, 'toString') else str(x) for x in params])
        self.runtime.log_output(u"{} {}".format(file_and_line, log_str))

    def warn(self, *params):
        self.log(*params)

    def info(self, *params):
        self.log(*params)

    def error(self, *params):
        self.log(*params)