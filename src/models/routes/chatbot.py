from flask import Blueprint, request, jsonify
from sic. models. government_entities import GovernmentEntity, Announcement, db
from datetime import datetime, date, timedelta import json import openai import os
chatbot bp = Blueprint ( 'chatbot',
_name_
OpenAl إعداد #
os. geten( OPENAI API BASE'
'https://api.openai.com/v1'/
# قاعدة معرفة شقردي
SHAORADI_KNOWLEDGE = """
أنا شقردي، مساعدك الذكي للخدمات الحكومية الكويتية. أقدر أساعدك في :
الجهات الحكومية المتاحة :
1. الهيئة العامة للمعلومات المدنية -
البطاقة المدنية والجنسية
2. بلدية الكويت - التراخيص
والخدمات البلدية
3. المؤسسة العامة للإسكان - الإسكان
الحكومي والقروض
4. ديوان الخدمة المدنية -
الوظائف الحكومية
5. وزارة الأشغال العامة - رخص
البناء والمقاولات
6. الهيئة العامة للصناعة -
التراخيص الصناعية
7. الإدارة العامة للإطفاء -
تر اخيص السلامة
8. وزارة التجارة والصناعة - السجل
التجاري والشركات
9. وزارة الإعلام الكويتية - التراخيم
الإعلامية والنشر الإلكتروني
10. منصة سهل للخدمات الحكومية -
التطبيق الحكومي الموحد
11. جريدة كويت اليوم الرسمية -
الإعلانات والقوانين الرسمية
الخدمات الرئيسية :
- معلومات عن الخدمات الحكومية
- إرشادات للمعاملات الرسمية
- آخر الإعلانات الحكومية
- معلومات الاتصال بالجهات المختصا
- مواعيد العمل والمتطلبات
أتحدث باللهجة الكويتية المحلية وأقدم
المساعدة بطريقة ودية ومفيدة .
@chatbot_bp. route(' /chat', methods=[ 'POST' ])
def chat () :
try:
data = request. get_json ()
user_message =
data. get ('message',
'')
if not user message:
return jsonify({'error':
400 ({ الرسالة مطلوبة )
# إنشاء السياق
للذكاء الاصطناعي
context =
E" ( SHAORADI_KNOWLEDGE} |n\n المستخدم :
{user_message} \nشقردي: "
OpenAI استدعاء
#
response =
openai.Completion.create (
engine="text-
davinci-003"
        prompt=context, max_tokens=500, temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0
)
bot response =
response. choices [0] .text.strip ()
return jsonifyl{
' response':
bot _response! status': 'success'
}), 200
except Exception as e:
return jsonifyl{
'response' : ' عذراً ، حدث
خطأ في النظام . يرجى المحاولة مرة
' . أخرى
'error': str (e)
}) , 500
@chatbot_bp.route(' /entities',
methods=[ 'GET' ]) def get entities () :
try:
entities =
GovernmentEntity query.all ()
return
jsonify(lentity.to_dict () for entity
in entities]),
200
except Exception as e:
return jsonify({'error':
str (e)}), 500
@chatbot bp. route (' /announcements' methods=[ 'GET' ])
def get_announcements ( ):
try:
days =
request.args.get get ('days', 7, type=int)
start_date = date. today () -
timedelta (days=days)
announcements =
Announcement. query. filter (
Announcement. announcement_date ›= start_date,
Announcement. announcement_date <=
date. today ( )
) . order_by (Announcement. anno
uncement_date. desc ()) •all ( )
return
jsonify( [announcement.to_dict() for
announcement in announcements]), 200
except Exception as e:
return jsonify({'error':
str (e)}) , 500