"""
This is a modified version of the MIT licensed echo kernel
in the Jupyter docs.
http://jupyter-client.readthedocs.org/en/latest/wrapperkernels.html#example

MIT License (c) Murat Knecht 2016

"""
import codecs
import subprocess

from ipykernel.kernelbase import Kernel


class BehaveKernel(Kernel):
    implementation = 'Behave'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {'mimetype': 'text/plain', 'name': 'behave'}
    banner = "Behave yourself!"

    def __init__(self, *args, **kw):
        super(BehaveKernel, self).__init__(*args, **kw)
        self.history = []

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if store_history:
            self.history.append(code)

        if not silent:
            reply = self._maybe_run_and_get_reply(code)
            stream_content = {'name': 'stdout', 'text': reply}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            # The base class increments the execution count
            'name': 'Behave',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }

    def do_complete(self, text, cursor_pos):
        matches = []
        if text.strip().startswith("Given"):
            matches += [
                " we have 1 black hole",
                " we have 2 black holes",
                " black holes are out of stock",
            ]
        elif text.strip().startswith("When"):
            matches += ["the holes collide"]

        return {
            # The list of all matches to the completion request, such as
            # ['a.isalnum', 'a.isalpha'] for the above example.
            'matches': matches,

            'matched_text': text,

            # # Information that frontend plugins might use for extra display information about completions.
            # 'metadata' : dict,

            # status should be 'ok' unless an exception was raised during the request,
            # in which case it should be 'error', along with the usual error message content
            # in other messages.
            'status': 'ok'
        }

    def _maybe_run_and_get_reply(self, code):
        if "That's it." not in code:
            return ""

        filepath = "features/notebook.feature"
        with codecs.open(filepath, "w+", encoding="utf-8") as f:
            f.write(u"\n".join(self.history[:-1]))

        stdout, _ = subprocess.Popen("behave {}".format(filepath), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        return stdout


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=BehaveKernel)
