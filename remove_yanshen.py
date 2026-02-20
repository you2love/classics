#!/usr/bin/env python3
import os
import re
import glob

def remove_yanshen_yuedu(content):
    # 删除独立的延伸阅读section
    pattern1 = r'\s*<div class="section">\s*<h2 class="section-title">📚 延伸阅读</h2>\s*<p class="content-text">.*?</p>\s*</div>'
    content = re.sub(pattern1, '', content, flags=re.DOTALL)
    
    # 删除学习建议与延伸阅读section
    pattern2 = r'\s*<div class="section">\s*<h2 class="section-title">📚 学习建议与延伸阅读</h2>.*?</div>\s*</div>'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)
    
    # 删除core-point-card中的延伸阅读
    pattern3 = r'\s*<div class="core-point-card">\s*<h4>延伸阅读</h4>\s*<p>.*?</p>\s*</div>'
    content = re.sub(pattern3, '', content, flags=re.DOTALL)
    
    # 删除subsection-title延伸阅读
    pattern4 = r'\s*<div class="subsection-title">延伸阅读</div>\s*<p class="content-text">.*?</p>'
    content = re.sub(pattern4, '', content, flags=re.DOTALL)
    
    return content

# 处理books目录下的所有HTML文件
for filepath in glob.glob('books/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = remove_yanshen_yuedu(content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {filepath}')

print('Done!')
