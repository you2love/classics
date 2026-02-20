#!/usr/bin/env python3
import os
import glob

# 定义需要补充内容的书籍及其补充内容
books_to_supplement = {
    "置身事内.html": {
        "sections": [
            {
                "title": "📚 全书章节结构",
                "content_type": "table",
                "data": [
                    ["上篇 微观机制", "第1章 中央与地方", "地方政府的事权与财权"],
                    ["", "第2章 土地财政", "土地出让与土地金融"],
                    ["", "第3章 政府投融资", "城投债与政府融资平台"],
                    ["", "第4章 工业化", "招商引资与产业政策"],
                    ["下篇 宏观现象", "第5章 城市化", "城市化的经济逻辑"],
                    ["", "第6章 地区差异", "区域发展的不平衡"],
                    ["", "第7章 风险挑战", "地方债务与金融风险"],
                    ["", "第8章 全球视野", "中国模式的国际比较"]
                ]
            },
            {
                "title": "💡 核心观点",
                "content_type": "cards",
                "data": [
                    ["1", "土地财政", "土地出让收入成为地方政府重要财源，推动了城市化发展"],
                    ["2", "城投公司", "地方政府通过城投公司融资，绕过预算约束"],
                    ["3", "产业政策", "地方政府通过产业政策引导投资，推动工业化"],
                    ["4", "风险累积", "地方债务快速累积，需要防范金融风险"],
                    ["5", "改革方向", "需要完善地方财政体制，规范地方政府融资行为"]
                ]
            },
            {
                "title": "📊 重要数据",
                "content_type": "cards",
                "data": [
                    ["土地出让", "土地出让收入占地方财政收入比重超过50%"],
                    ["城投债务", "城投债券余额超过40万亿元"],
                    ["地方政府", "中国有300多个地级市，2000多个县级政府"],
                    ["经济贡献", "地方政府投资对GDP增长的贡献率超过40%"]
                ]
            }
        ]
    },
    "税收学(第三版).html": {
        "sections": [
            {
                "title": "📚 全书章节结构",
                "content_type": "table",
                "data": [
                    ["第1章 税收基本理论", "税收的本质、特征、职能"],
                    ["第2章 税收原则", "公平原则、效率原则、财政原则"],
                    ["第3章 税收负担", "税收负担的衡量与影响因素"],
                    ["第4章 税收转嫁与归宿", "税收转嫁机制与最终承担者"],
                    ["第5章 税收制度", "税收制度的设计与评价"],
                    ["第6章 流转税", "增值税、消费税、营业税"],
                    ["第7章 所得税", "企业所得税、个人所得税"],
                    ["第8章 财产税", "房产税、遗产税、赠与税"],
                    ["第9章 资源税与行为税", "资源税、环境保护税"],
                    ["第10章 国际税收", "国际税收关系与协调"]
                ]
            },
            {
                "title": "💡 核心概念",
                "content_type": "cards",
                "data": [
                    ["税收中性", "税收不应扭曲资源配置和经济决策"],
                    ["税收公平", "相同情况相同纳税，不同情况不同纳税"],
                    ["税收效率", "以最小的征收成本获得最大的税收收入"],
                    ["税收法定", "税收必须由法律明确规定"],
                    ["量能负担", "根据纳税能力确定税收负担"]
                ]
            }
        ]
    },
    "中国税收制度(2025).html": {
        "sections": [
            {
                "title": "📚 全书章节结构",
                "content_type": "table",
                "data": [
                    ["第1章 中国税收制度概述", "税收制度的历史演变与基本框架"],
                    ["第2章 流转税制度", "增值税、消费税改革"],
                    ["第3章 所得税制度", "企业所得税、个人所得税优化"],
                    ["第4章 财产税制度", "房地产税改革探索"],
                    ["第5章 资源环境税", "绿色税收体系建设"],
                    ["第6章 税收征管", "税收征管现代化"],
                    ["第7章 国际税收", "国际税收合作与竞争"],
                    ["第8章 税收政策", "税收政策与宏观调控"]
                ]
            },
            {
                "title": "💡 最新改革",
                "content_type": "cards",
                "data": [
                    ["增值税改革", "增值税税率简并，降低企业税负"],
                    ["个税改革", "综合所得税制，提高起征点"],
                    ["房地产税", "探索房地产税立法与试点"],
                    ["绿色税收", "完善环境保护税，促进绿色发展"],
                    ["数字化征管", "推进税收征管数字化改革"]
                ]
            }
        ]
    },
    "新中国税收70年.html": {
        "sections": [
            {
                "title": "📚 全书章节结构",
                "content_type": "table",
                "data": [
                    ["第一编", "第1章 新中国成立初期", "税收制度的建立"],
                    ["", "第2章 计划经济时期", "统一税制的形成"],
                    ["第二编", "第3章 改革开放初期", "利改税与税制改革"],
                    ["", "第4章 市场经济转型", "分税制改革"],
                    ["第三编", "第5章 新世纪以来", "税收制度完善"],
                    ["", "第6章 新时代税收", "现代化税收体系"],
                    ["第四编", "第7章 国际税收", "国际税收合作"],
                    ["", "第8章 未来展望", "税收制度改革方向"]
                ]
            },
            {
                "title": "💡 重要里程碑",
                "content_type": "cards",
                "data": [
                    ["1950年", "统一全国税政，建立新中国税收制度"],
                    ["1980年", "建立涉外税收制度，吸引外资"],
                    ["1983年", "第一步利改税，税利分流"],
                    ["1984年", "第二步利改税，完善税制"],
                    ["1994年", "分税制改革，建立分税制体系"],
                    ["2016年", "营改增全面推开，完善增值税制"],
                    ["2019年", "个人所得税改革，建立综合税制"]
                ]
            }
        ]
    }
}

# 生成HTML补充内容的函数
def generate_section(section):
    if section["content_type"] == "table":
        table_rows = ""
        for row in section["data"]:
            if len(row) == 3:
                table_rows += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>\n'
            elif len(row) == 2:
                table_rows += f'<tr><td>{row[0]}</td><td>{row[1]}</td></tr>\n'
        return f'''
        <div class="section">
            <h2 class="section-title">{section["title"]}</h2>
            <table class="data-table">
                <tr><th>编/章</th><th>章节</th><th>主要内容</th></tr>
                {table_rows}
            </table>
        </div>
        '''
    elif section["content_type"] == "cards":
        cards = ""
        for card in section["data"]:
            num = card[0] if len(card) > 0 else ""
            title = card[1] if len(card) > 1 else ""
            desc = card[2] if len(card) > 2 else ""
            cards += f'''
                <div class="core-point-card">
                    <div class="point-number">{num}</div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
            '''
        return f'''
        <div class="section">
            <h2 class="section-title">{section["title"]}</h2>
            <div class="core-points-grid">
                {cards}
            </div>
        </div>
        '''
    return ""

# 处理每本书
for book_file, book_data in books_to_supplement.items():
    filepath = os.path.join("books", book_file)
    if not os.path.exists(filepath):
        print(f"文件不存在: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 在最后一个section之后插入新内容
    new_sections = ""
    for section in book_data["sections"]:
        new_sections += generate_section(section)
    
    # 在footer之前插入新内容
    if "</footer>" in content:
        content = content.replace("</footer>", new_sections + "\n    </footer>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"已更新: {book_file}")
    else:
        print(f"未找到footer标签: {book_file}")

print("批量补充完成!")