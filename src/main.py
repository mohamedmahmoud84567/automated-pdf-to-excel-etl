import os
import pandas as pd
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """الخطوة 1: استخراج النصوص من ملف الـ PDF"""
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    return full_text

def clean_and_convert_to_dataframe(raw_text):
    """الخطوة 2: تحويل النص إلى جدول وتنظيفه من المكررات"""
    lines = raw_text.strip().split('\n')
    data_list = []
    
    for line in lines:
        # تجاهل السطور غير المهمة مثل العنوان والخطوط الفاصلة
        if "Sample Invoice" in line or "---" in line or "ID, Name" in line:
            continue
        
        parts = line.split(',') 
        if len(parts) >= 4: # التأكد من وجود الأعمدة الأربعة كاملة
            data_list.append([p.strip() for p in parts])
            
    # تحويل البيانات إلى جدول بايثون (Dataframe)
    columns = ["ID", "Customer_Name", "Product", "Price"]
    df = pd.DataFrame(data_list, columns=columns)
    
    # هنا السحر! إزالة الصفوف المكررة تماماً بضغطة زر
    df.drop_duplicates(inplace=True)
    
    return df

def run_etl_pipeline():
    """الخطوة 3: تشغيل خط الأنابيب بالكامل وحفظ الملف"""
    input_pdf = os.path.join("data", "raw", "sample.pdf")
    output_excel = os.path.join("data", "processed", "cleaned_invoice_data.xlsx")
    
    print("⏳ [1/3] جاري قراءة ملف الـ PDF واستخراج النصوص...")
    raw_text = extract_text_from_pdf(input_pdf)
    
    print("🧹 [2/3] جاري معالجة البيانات وإزالة المكررات تلقائياً...")
    cleaned_df = clean_and_convert_to_dataframe(raw_text)
    
    print("💾 [3/3] جاري تصدير البيانات النظيفة إلى ملف Excel...")
    os.makedirs(os.path.dirname(output_excel), exist_ok=True)
    cleaned_df.to_excel(output_excel, index=False)
    
    print("\n✅ [Success] تم الانتهاء بنجاح! الملف النظيف جاهز في مجلد processed.")

if __name__ == "__main__":
    run_etl_pipeline()
