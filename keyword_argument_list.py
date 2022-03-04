# Belajar keyword argument list

# ** = keyword argument list
def create_html(tag, text, **attribute):
    html = f'<{tag}'

    for key, value in attribute.items():
        html = html + f"> {key}='{value}'"
    
    html = html + f'>{text}</{tag}>'
    return html

html = create_html('p', 'hello world')
print(html)
html = create_html('a', 'ini link', href='www.google.com')
print(html)