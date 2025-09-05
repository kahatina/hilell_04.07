import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
           clean_text = ''
           is_inside_tag = False

           for char in html:
               if char == "<":
                   is_inside_tag = True
               elif char == ">":
                   is_inside_tag = False
               else:
                   if is_inside_tag == False:
                       clean_text += char

      with codecs.open(result_file, 'w', 'utf-8') as file:
          file.write(clean_text)