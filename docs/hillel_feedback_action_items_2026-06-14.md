# Hillel Feedback Action Items - 2026-06-14

מקורות:
- תמלול שיחת Zoom: `הלל צברי 14062026`
- תמלול המשך: `חלק 2 הילל צברי 14062026`
- Google Sheet: `עותק של עותק של HMHW Official Creative Offer Oven - Scripts & Pipeline`
- צילומי מסך שסומנו במהלך השיחה
- נקודות ידניות שנרשמו אחרי השיחה

## טבלת מעקב תיקונים

| אזור | מה צריך לעשות | סטטוס | הערות |
|---|---|---|---|
| אתר ראשי | להחליף `Hilel 1 LLC` ל-`Hilel Steam`, לעדכן CTA, להוסיף מלל ולעדכן עיצוב | לא בוצע | דורש מעבר בכל קבצי האתר |
| גישה למחשבון | להוסיף הגנת username/password ולהסתיר קישור מהעמוד הראשי | בוצע בקוד | משתמש ב-Netlify Edge Function וב-hash/salt דרך env |
| Property Type | למחוק `Condo` ו-`Commercial`; להשאיר `Townhouse` | בוצע | `Calculator.html` שורה ~600: נמחקו `Condo / Townhouse` ו-`Commercial`, נוסף `Townhouse`. נשארו Single Family / Multi-Family / Townhouse |
| Property Photos / PDF | להכניס תמונות לדוח PDF הסופי | לא בוצע | וידאו לא נדרש |
| Assignment Fee | להשאיר פנימי בלבד ולא להציג בדוח הסופי | לא בוצע | חשוב לבדוק גם Share/Print/PDF |
| Title Costs | להחליף `Title, escrow, recording` ל-`Title` בלבד | לא בוצע | לפי צילום המסך שסומן |
| Repairs | למחוק עמוד Repairs מלא ולהחליף בבחירת Light/Medium/Heavy | לא בוצע | Light 10k-45k, Medium 45k-85k, Heavy 85k+ |
| Buy & Hold / Excel Inputs | לנקות שדות Excel פנימיים וכפילויות | לא בוצע | דורש החלטה סופית על `Cash In Deal` |
| שדות דיפולטיביים | לאפס מספרים ולהוסיף סימון אדום לשדות שלא נגעו בהם | לא בוצע | אינדיקציית touched/untouched |
| Hard Money / Flip | להשאיר Hard Money Rates/Points ולנקות שדות לא ברורים | לא בוצע | לוודא שהחישובים נשארים תקינים |
| Seller Finance | להוסיף Seller Finance ו-Subto לפי ה-Google Sheet | לא בוצע | כולל Buyer Entry Fee ו-Balloon Balances |
| Strategy / Results | לשמר/לבנות המלצת אסטרטגיה ותוצאות יצוא | לא בוצע | לבדוק שלא חושף נתונים פנימיים |
| Comps | להוסיף עמוד Comparables עם חישוב ARV לפי קומפים | לא בוצע | בשלב ראשון ידני, בלי חיבור Base44 |
| SEO / Deployment | Search Console, metadata, sitemap/robots וחיבור Netlify ל-GitHub | חלקית | GitHub כבר חובר והקוד נדחף; SEO/Search Console עדיין לא |

## אתר ראשי

- להחליף בכל האתר את `Hilel 1 LLC` / `Hillel-1 LLC` / וריאציות דומות בשם `Hilel Steam`.
- לוודא שהשם הישן לא מופיע גם בטפסים, תנאי הסכמה, Footer, עמוד About, Contact, Appointment, Privacy/Terms וכל טקסט משפטי או שיווקי.
- לעדכן את עמוד הבית בהשראה מהעיצוב שהוצג בשיחה:
  - עיצוב יותר מושך עין ומקצועי.
  - להבליט שהעסק קונה נכסים ב-cash, as-is, כולל נכסי fixer-upper ונכסים במצב בעייתי.
  - להימנע מתמונות בתים שנראים יוקרתיים מדי ולא משדרים fixer-upper.
  - לשלב שפה ויזואלית שמבדלת את האתר מאתרי wholesaling דומים.
- להכניס לעמוד הראשי את המלל/מבנה שהלל ישלח בוואטסאפ.
- להחליף CTA מסוג `Book a call` לניסוח יותר מתאים:
  - `Schedule a meeting`
  - `Speak with the decision maker`
  - להשאיר/להדגיש מסרים כמו `No repairs`, `No commission`, `Cash offer in 24 hours`.
- לוודא שקריאה לפעולה לקביעת שיחה מופיעה בכל עמוד ובמיקומים בולטים, במיוחד בתחילת עמודים.
- בעמוד Contact:
  - להוסיף Secondary Phone כשהלל יספק מספר.
  - ליד ה-Secondary Phone לכתוב שהוא `Only for texting`.
- בעמוד About:
  - להחליף `About Hillel-1 LLC` ל-`About Hilel Steam`.
  - להוסיף עוד מלל על מי העסק, איך הוא עובד, ולמה מוכרים יכולים לסמוך עליו.

## גישה למחשבון

- המחשבון צריך להיות מוגן בסיסמה.
- לא צריך מנגנון הרשמה מלא.
- ליצור כניסה פשוטה עם username/password שמיועדת להלל בלבד.
- לא לשים קישור גלוי למחשבון מהעמוד הראשי.
- הלל יקבל קישור ישיר וספציפי למחשבון.

## מחשבון - Property Details

- בשדה `Property Type` למחוק:
  - `Condo`
  - `Commercial`
- להשאיר:
  - `Single Family`
  - `Multi-Family`
  - `Townhouse`
- ✅ בוצע: ב-`Calculator.html` `<select id="ptype">` הוסר `Condo / Townhouse` והוסר `Commercial`, ונוסף `Townhouse`. השדה אינו משמש שום חישוב אז השינוי בטוח.
- להשאיר את שדות Bedrooms, Bathrooms, Square Footage, Year Built.
- להשאיר את `Select Situation`, כי זה חשוב לסינון מוטיבציה של מוכרים.
- להשאיר `Closing As-Is`.
- להשאיר `Property Notes`.

## Property Photos ו-PDF

- לאפשר העלאת תמונות תחת `Property Photos`.
- התמונות צריכות להיכנס לדוח ה-PDF הסופי באזור מתאים.
- אין צורך להכניס וידאו ל-PDF.
- אם יש וידאו, הלל יעביר אותו חיצונית.
- לוודא שה-PDF מציג תמונות בצורה נקייה ומסודרת לקונה.

## Purchase / Deal Inputs

- להשאיר:
  - `Purchase Price`
  - `After Repair Value / ARV`
  - `Closing Cost`
- `Wholesale Assignment Fee`:
  - להשאיר כנתון פנימי שהלל רואה ומשתמש בו.
  - לוודא שהוא לא מופיע בדוח הסופי לקונה.
  - בדוח החיצוני אסור שהקונה יראה כמה הלל מרוויח בעסקה.
- בשדה/טקסט `Title, escrow, recording`:
  - למחוק את `escrow, recording`.
  - להשאיר רק `Title`.

## Repairs

- למחוק את עמוד ה-Repairs הנוכחי כולו.
- לא להשתמש בפירוט קטגוריות תיקון כמו drywall, contractors וכו'.
- במקום זה, להכניס את חלק ה-Repairs בעמוד השני/באזור Purchase כפי שהוסבר בשיחה.
- המבנה החדש צריך להיות פשוט:
  - `Light`
  - `Medium`
  - `Heavy`
- טווחים:
  - `Light`: 10,000-45,000 דולר.
  - `Medium`: 45,000-85,000 דולר.
  - `Heavy`: 85,000 דולר ומעלה.
- כאשר בוחרים `Heavy`, המשתמש חייב להזין מספר תיקונים בפועל.
- המטרה: לא לפרט תיקונים כמו קבלן, אלא לסמן רמת שיפוץ ולתת מספר שמזין את החישובים.

## Buy & Hold / Excel Buy & Hold Inputs

- להשאיר את הנתונים התפעוליים הרלוונטיים:
  - Rent Monthly
  - Property Tax
  - Insurance
  - HOA
  - Management Fee
  - Vacancy Rate
  - Airbnb Cleaning / Supplies, אם עדיין רלוונטי לאסטרטגיה
- למחוק/להעיף את כל החלק שסומן כ-`Excel Buy & Hold Inputs` אם הוא כפילות או נתוני Excel פנימיים שלא צריכים להיות בממשק.
- למחוק שדות שמגיעים מה-Excel ולא ברורים למשתמש, לדוגמה:
  - `Excel Purchase`
  - `Excel Repairs`
  - `Selected Scenario`, אם אין לו משמעות ברורה בממשק.
- לבדוק האם `Cash In Deal` נדרש להצגה; אם נשאר, לוודא שהוא לא גורם ל-ROI/CoC להיראות שבור כשהוא 0.

## ברירות מחדל וסימון שדות שלא נגעו בהם

- לא להשאיר במחשבון מספרים דיפולטיביים מבלבלים מעסקאות קודמות.
- שדות מספריים צריכים להתחיל ב-0 או ריק, לפי מה שנכון לחישוב.
- להוסיף אינדיקציה ויזואלית לשדות שהלל עדיין לא נגע בהם:
  - שדה שלא נגעו בו יסומן באדום.
  - אחרי הזנה/עריכה, הסימון האדום ייעלם.
- המטרה היא שהלל ידע מייד אם מספר הוא דיפולטיבי או מספר שהוא הזין בפועל.

## Hard Money / Flip / Leverage

- להשאיר `Hard Money Rates` ו-`Hard Money Points`; הם קריטיים.
- לבדוק את אזור `Excel Flip + Leverage Inputs`.
- למחוק או להסתיר שדות Excel פנימיים שלא מובנים למשתמש:
  - `Excel Purchase`
  - `Excel Repairs`
  - `Selected Scenario`, אם אינו משרת חישוב ברור.
- שדות כמו `Purchase`, `Repair`, `Hard Money Loan`, `Service Fee` צריכים להתחיל ב-0 אם אין נתון אמיתי.
- לוודא שכל החישובים עדיין עובדים אחרי ניקוי השדות.

## Seller Finance

- להוסיף למחשבון את אפשרות `Seller Finance`.
- להוסיף גם את אפשרות `Subto` / `Subject To`, לפי השיחה.
- החישובים צריכים להתבסס על ה-Google Sheet שנשלח.
- להכניס את החישובים/מספרים של `Buyer Entry Fee`; זה קריטי.
- `Buyer Entry Fee` צריך לכלול:
  - Down Payment
  - Rehab
  - Assignment Fee
  - Closing / Title
- להכניס את חישובי `Balloon Balances`; זה קריטי.
- `Balloon Balances` צריך להציג:
  - At end of Year
  - Date
  - Interest Paid
  - Principal Paid
  - Outstanding Balance
  - Total Paid
- לתמוך בהזנת:
  - Purchase Price
  - Listed Price
  - Loan Amount
  - Down Payment
  - Annual Interest Rate
  - Amortization
  - First Payment Date
  - Interest Only: Yes/No
  - Monthly Payment
  - Annual Payment
  - Balloon Due in years
- לתמוך בחישובי Cash Flow ו-Cash-on-Cash Return לפי המודל ב-Sheet.
- לוודא שאם משנים נתון כמו Down Payment, המספרים מתעדכנים.
- לוודא שיש מקום להזין/לחשב את המספרים שסומנו באדום ב-Sheet.

## Strategy / Results

- לשמר או לבנות תוצאה שמראה מה האסטרטגיה הכי טובה לעסקה.
- ב-Sheet מופיע `Airbnb best strategy for this`; לבדוק איך לתרגם את זה למחשבון.
- אחרי הזנת נתונים, צריך לבדוק האם התוצאה הגיונית ולעשות fine-tuning עד שהחישובים מתאימים להלל.
- להשאיר אפשרויות:
  - Generate Share
  - Export CSV
  - Print
- לוודא ש-Share/Print/PDF לא חושפים נתונים פנימיים כמו Assignment Fee אם הם מיועדים רק להלל.

## Comps / Comparables

- להוסיף עמוד חדש בשם `Comps` / `Comparables`.
- העמוד צריך לעזור להצדיק את ה-ARV לקונה.
- לא חובה לחבר אוטומטית ל-Base44 בשלב הראשון.
- אם רוצים חיבור ל-Base44 בהמשך, צריך לקבל מהלל גישת עריכה/API ולדעת בדיוק אילו נתונים למשוך.
- בשלב הראשון אפשר לבנות חישוב ידני בתוך המחשבון.
- לכל Comp צריך לאפשר להזין:
  - Address
  - Square Footage
  - Sold Price
  - Sold Date
  - Bedrooms/Bathrooms
  - Distance from subject property
  - Notes / features, אם צריך
- לחשב לכל Comp:
  - Sold Price / Square Footage = Price per Sqft
- לחשב ממוצע Price per Sqft מכל ה-Comps.
- לחשב ARV:
  - Average Price per Sqft * Subject Property Square Footage
- להציג את הממוצע ואת ה-ARV בצורה ברורה.
- הקריטריונים שהלל ציין לקומפים:
  - נכסים קרובים, בערך עד מייל-מייל וחצי.
  - Square footage דומה, בערך 200 sqft למעלה או למטה.
  - Sold date חשוב מאוד; עדיף מכירות עדכניות, לא ישנות מדי.
  - דמיון בסוג הנכס, חדרים, גודל, תוספות, שנת בנייה ומצב.
- אפשר להסתכל על iComps כהשראה בלבד, אבל הלל לא סומך עליו כמקור אמת.
- הלל רוצה לבצע בדיקה ידנית של קומפים ולא להסתמך על AI או שירות חיצוני בלי אימות.

## SEO / Deployment

- לחבר את הפרויקט ל-GitHub repo שהלל פתח.
- לחבר את Netlify ל-repo כך שכל עדכון בקוד יתעדכן באתר.
- להגדיר Google Search Console לדומיין.
- להכניס לאתר את קוד האימות של Google Search Console כשיתקבל.
- לשפר תשתית SEO באתר:
  - metadata
  - titles
  - descriptions
  - robots/sitemap אם חסר
  - מבנה headings
  - טקסטים רלוונטיים לרובוטים של Google
- לאחר החיבור, לוודא שהדומיין מאומת ומתחיל להיסרק.

## פריטים שדורשים מידע נוסף מהלל

- כתובת אימייל/פרטי מיתוג מדויקים שיופיעו תחת `Hilel Steam`.
- מספר Secondary Phone והניסוח המדויק סביב texting.
- המלל שהלל אמר שישלח בוואטסאפ לעמוד הראשי ולעמוד About.
- החלטה סופית האם להשאיר את `Cash In Deal` בממשק או להסתיר/לחשב מאחורי הקלעים.
- החלטה סופית אילו שדות מתוך `Excel Buy & Hold Inputs` נשארים ואילו נמחקים.
- גישה/מידע ל-Base44 אם רוצים חיבור נתונים במקום הזנה ידנית של Comps.
- קוד Google Search Console לאחר פתיחת הנכס.

## סדר עדיפות מוצע

1. להחליף בכל האתר את `Hilel 1 LLC` ל-`Hilel Steam`.
2. להגן על המחשבון בסיסמה ולהסיר קישור גלוי מהאתר.
3. לנקות את Property Type, Repairs, Excel Inputs ושדות דיפולטיביים.
4. לתקן PDF כך שיכלול תמונות ולא יציג Assignment Fee.
5. להוסיף Seller Finance ו-Balloon Balances לפי ה-Google Sheet.
6. להוסיף Comps ידני עם חישוב ARV.
7. לעבור fine-tuning על כל החישובים מול הלל.
8. להשלים SEO ו-Google Search Console.
