from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch
from content import CV_DATA
import os

def generate_cv_pdf(lang: str, output_path: str, user_name: str = "Foydalanuvchi"):
    """Generates a personalized premium PDF CV."""
    doc = SimpleDocTemplate(
        output_path, 
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    
    # --- Custom Styles ---
    primary_color = colors.HexColor("#2563EB") # Modern Blue
    secondary_color = colors.HexColor("#64748B") # Slate Gray
    
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        fontSize=28,
        textColor=primary_color,
        fontName='Helvetica-Bold',
        spaceAfter=5
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=secondary_color,
        fontName='Helvetica',
        spaceAfter=20
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Normal'],
        fontSize=16,
        textColor=primary_color,
        fontName='Helvetica-Bold',
        spaceBefore=20,
        spaceAfter=10,
        borderPadding=5,
        borderWidth=0,
    )
    
    item_title_style = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontSize=12,
        fontName='Helvetica-Bold',
        spaceAfter=2
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.black
    )
    
    elements = []
    
    # --- Header Section ---
    elements.append(Paragraph(CV_DATA["name"].upper(), header_style))
    elements.append(Paragraph("Mobilographer | Developer | AI Expert", subtitle_style))
    
    # Contact Info Table
    contact_text = [
        [f"📍 {CV_DATA['location']}", f"📞 {CV_DATA['contacts']['telegram']}"],
        [f"📧 abdulloh@ai.uz", f"📸 Instagram: {CV_DATA['contacts']['instagram']}"]
    ]
    contact_table = Table(contact_text, colWidths=[3*inch, 3*inch])
    contact_table.setStyle(TableStyle([
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TEXTCOLOR', (0,0), (-1,-1), secondary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ]))
    elements.append(contact_table)
    elements.append(Spacer(1, 10))
    elements.append(Table([[primary_color]], colWidths=[7.5*inch], rowHeights=[2])) # Horizontal Line
    
    # --- About Me ---
    about_titles = {"uz": "MEN HAQIMDA", "ru": "ОБО МНЕ", "en": "ABOUT ME"}
    elements.append(Paragraph(about_titles[lang], section_style))
    
    about_texts = {
        "uz": f"Men {CV_DATA['age']} yoshli zamonaviy texnologiyalar ishqiboziman. Hozirda {CV_DATA['education']['university']}da {CV_DATA['education']['major']} yo'nalishi bo'yicha tahsil olmoqdaman. Vizual san'at va dasturlashni uyg'unlashtirish orqali innovatsion yechimlar yaratish - mening asosiy maqsadim.",
        "ru": f"Я 18-летний энтузиаст современных технологий. В настоящее время учусь в {CV_DATA['education']['university']} по направлению {CV_DATA['education']['major']}. Моя цель - создавать инновационные решения, объединяя визуальное искусство и программирование.",
        "en": f"I am an 18-year-old tech enthusiast currently studying {CV_DATA['education']['major']} at {CV_DATA['education']['university']}. My goal is to create innovative solutions by combining visual arts and programming."
    }
    elements.append(Paragraph(about_texts[lang], body_style))
    
    # --- Experience ---
    exp_titles = {"uz": "ISH TAJRIBASI", "ru": "ОПЫТ РАБОТЫ", "en": "EXPERIENCE"}
    elements.append(Paragraph(exp_titles[lang], section_style))
    
    for exp in CV_DATA["experience"]:
        elements.append(Paragraph(f"{exp['title']} | {exp['duration']}", item_title_style))
        desc = exp['desc'][lang] if isinstance(exp['desc'], dict) else exp['desc']
        elements.append(Paragraph(desc, body_style))
        elements.append(Spacer(1, 8))
        
    # --- Skills & Education (2 Columns) ---
    skills_titles = {"uz": "KO'NIKMALAR", "ru": "НАВЫКИ", "en": "SKILLS"}
    edu_titles = {"uz": "TA'LIM", "ru": "ОБРАЗОВАНИЕ", "en": "EDUCATION"}
    
    # Prepare Skills Text
    tech_skills = "<b>Technical:</b> " + ", ".join(CV_DATA["skills"]["technical"])
    soft_list = CV_DATA["skills"]["soft"][lang] if isinstance(CV_DATA["skills"]["soft"], dict) else CV_DATA["skills"]["soft"]
    soft_skills = "<b>Soft:</b> " + ", ".join(soft_list)
    
    # Prepare Education Text
    edu_info = f"<b>{CV_DATA['education']['university']}</b><br/>{CV_DATA['education']['major']} ({CV_DATA['education']['year']})"
    
    col1 = [
        Paragraph(skills_titles[lang], section_style),
        Paragraph(tech_skills, body_style),
        Spacer(1, 5),
        Paragraph(soft_skills, body_style)
    ]
    
    col2 = [
        Paragraph(edu_titles[lang], section_style),
        Paragraph(edu_info, body_style)
    ]
    
    # Nested table for 2-column layout
    col_table = Table([[col1, col2]], colWidths=[3.7*inch, 3.7*inch])
    col_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    elements.append(col_table)
    
    # --- Footer ---
    elements.append(Spacer(1, 0.5*inch))
    footer_text = f"<i>Maxsus {user_name} uchun tayyorlandi | Generated by {CV_DATA['name']} AI Assistant</i>"
    elements.append(Paragraph(footer_text, ParagraphStyle('Footer', parent=body_style, alignment=1, textColor=secondary_color)))
    
    doc.build(elements)
