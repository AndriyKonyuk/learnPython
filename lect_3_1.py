import cgi

def html_p(s: str) -> str:
    new_s = '<p>{}<p>'.format(s)
    return new_s


def html_b(s: str) -> str:
    new_s = '<b>{}<b>'.format(s)
    return new_s


def html_i(s: str) -> str:
    new_s = '<i>{}<i>'.format(s)
    return new_s


def html_u(s: str) -> str:
    new_s = '<u>{}<u>'.format(s)
    return new_s


def writer(mes):
    def writer_wraper(f):
        def wrapper(s):
            pat = {'p': html_p, 'b': html_b, 'i': html_i, 'u': html_u}
            for i in mes:
                if i in pat:
                    s = pat[i](s)
            return f(s)

        return wrapper
    return writer_wraper

@writer('bpx')
def html_printer(s: str) -> str:
    return cgi.escape(s).encode('ascii', 'xmlcharrefreplace')

if __name__ == '__main__':
    print(html_printer('I\'ll give  you +++ cash for this -> struff.'))
    print('&lt;p&gt;&lt;b&gt;I&#x27;ll give you +++ cash for this -&gt; struff.&lt;b&gt;&lt;p&gt;')

