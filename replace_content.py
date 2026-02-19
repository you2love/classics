#!/usr/bin/env python3
import re
import os

books = [
    ('books/行政发包制：大一统的制度密码.html', '行政发包制：大一统的制度密码'),
    ('books/筚路维艰：中国社会主义路径的五次选择.html', '筚路维艰：中国社会主义路径的五次选择'),
    ('books/改革的逻辑.html', '改革的逻辑'),
    ('books/传奇医学：改变人类命运的医学成就.html', '传奇医学：改变人类命运的医学成就'),
    ('books/国富论.html', '国富论'),
    ('books/就业、利息和货币通论.html', '就业、利息和货币通论'),
    ('books/经济学原理.html', '经济学原理'),
    ('books/资本论.html', '资本论'),
    ('books/利息与价格.html', '利息与价格'),
    ('books/宏观经济学史：从凯恩斯到卢卡斯及其后.html', '宏观经济学史：从凯恩斯到卢卡斯及其后'),
]

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

for book_file, book_name in books:
    if os.path.exists(book_file):
        with open(book_file, 'r', encoding='utf-8') as f:
            book_html = f.read()
        
        start_marker = '<div class="section">'
        end_marker = '</div>\n    </div>\n</body>'
        
        start_idx = book_html.find(start_marker)
        end_idx = book_html.find(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            content = book_html[start_idx:end_idx]
            content = content.rstrip()
            
            old_pattern = f'<div class="section">\\s*<h3 class="section-title">🔗 完整内容</h3>\\s*<p>点击下方链接查看完整的书籍内容：</p>\\s*<a href="books/{re.escape(book_name)}.html"[^>]*>[^<]*</a>\\s*</div>'
            
            new_section = f'''<div class="section">
                    <h3 class="section-title">📖 完整内容</h3>
                    {content}
                </div>'''
            
            index_content = re.sub(old_pattern, new_section, index_content, flags=re.DOTALL)
            print(f'处理完成: {book_name}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print('全部完成!')
