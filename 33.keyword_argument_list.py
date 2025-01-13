# ceritanya mau bikin fungsi generate tag html yang attributenya dinamis.

def createTagHtml(tag, text, **attr):
  html = f'<{tag}'
  for key, val in attr.items():
    html += f" {key}='{val}'"
  html += f'>{text}</{tag}>'
  return html

print(createTagHtml('p', 'Ini adalah text', style='width: 5px'))
print(createTagHtml('div', 'Ini adalah div', clas='mr-2', onClick='goToLink()'))
