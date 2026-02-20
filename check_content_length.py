#!/usr/bin/env python3
import os
import glob
import re

def analyze_book_content(filepath):
    """分析书籍HTML文件的内容长度"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 移除HTML标签，提取纯文本
    text_content = re.sub(r'<[^>]+>', ' ', content)
    text_content = re.sub(r'\s+', ' ', text_content).strip()
    
    # 统计字符数
    char_count = len(text_content)
    
    # 统计段落数（以<p>标签为准）
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
    p_count = len([p for p in paragraphs if re.sub(r'<[^>]+>', '', p).strip()])
    
    # 统计section数
    sections = re.findall(r'<div[^>]*class="[^"]*section[^"]*"[^>]*>', content)
    section_count = len(sections)
    
    return {
        'file': os.path.basename(filepath),
        'char_count': char_count,
        'paragraph_count': p_count,
        'section_count': section_count
    }

# 分析所有HTML文件
books_dir = 'books'
results = []

for filepath in glob.glob(os.path.join(books_dir, '*.html')):
    try:
        result = analyze_book_content(filepath)
        results.append(result)
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# 按字符数排序
results.sort(key=lambda x: x['char_count'])

# 输出结果
print("=" * 100)
print(f"{'书籍文件名':<50} {'字符数':<10} {'段落数':<10} {'Section数':<10}")
print("=" * 100)

for r in results:
    print(f"{r['file']:<50} {r['char_count']:<10} {r['paragraph_count']:<10} {r['section_count']:<10}")

print("=" * 100)
print(f"\n总计: {len(results)} 本书籍")

# 找出内容较少的书本（字符数少于6000的）
print("\n⚠️ 内容较少的书本（字符数 < 6000）:")
print("=" * 100)
print(f"{'书籍文件名':<50} {'字符数':<10} {'段落数':<10} {'Section数':<10}")
print("=" * 100)

short_books = [r for r in results if r['char_count'] < 6000]
for r in short_books:
    print(f"{r['file']:<50} {r['char_count']:<10} {r['paragraph_count']:<10} {r['section_count']:<10}")

if short_books:
    print(f"\n共发现 {len(short_books)} 本内容较少的书籍需要补充")
else:
    print("\n✅ 所有书籍内容都足够丰富")