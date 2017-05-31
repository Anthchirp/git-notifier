import cgi
import re

_separator = '>' + ('-'*63) + '\n'
_pattern = re.compile('(  +)')

def _mangle_line(line):
  content = cgi.escape(line)
  m = _pattern.finditer(content)
  for i in reversed(list(m)):
    (start, end) = i.span()
    content = content[:start] + ('&nbsp;' * (end-start)) + content[end:]

  if content.startswith('-'):
    return '<tt style="color:#800">%s</tt>' % (content)
  if content.startswith('+'):
    return '<tt style="color:#008">%s</tt>' % (content)
  return content

def htmlify(text):
  blocks = text.split(_separator)

  if len(blocks) == 3:
    caption, commitinfo, changes = blocks

    output = [_mangle_line(l) for l in caption.splitlines()]
    output.append('<hr>')
    output.extend([_mangle_line(l) for l in commitinfo.splitlines()])
    output.append('<hr>')
    output.extend([_mangle_line(l) for l in changes.splitlines()])

  else:
    lines = text.splitlines()
    output = [_mangle_line(l) for l in lines]

  return '<html><body><tt>%s</tt></body></html>' % "<br>".join(output)
