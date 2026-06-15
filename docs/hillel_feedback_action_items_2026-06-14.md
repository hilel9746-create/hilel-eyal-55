# Hillel Feedback Action Items - 2026-06-14

מקורות:
- תמלול שיחת Zoom: `הלל צברי 14062026`
- תמלול המשך: `חלק 2 הילל צברי 14062026`
- Google Sheet: `עותק של עותק של HMHW Official Creative Offer Oven - Scripts & Pipeline`
- צילומי מסך שסומנו במהלך השיחה
- נקודות ידניות שנרשמו אחרי השיחה

## מה נשאר לתקן

- להחליף בכל האתר את `Hilel 1 LLC` / `Hillel-1 LLC` ל-`Hilel Steam`.
- להשלים את עמוד הבית וה-About עם המלל שהלל ישלח בוואטסאפ.
- להוסיף Secondary Phone עם ניסוח `Only for texting`.
- להחליט אם `Cash In Deal` נשאר בממשק או מוסתר/מחושב מאחורי הקלעים.
- לסגור את `Excel Buy & Hold Inputs` ולמחוק שדות Excel פנימיים לא ברורים.
- ✅ בוצע: `Wholesale Assignment Fee` מוסתר מכל הפלטים החיצוניים (Share/Print/CSV) ונשאר פנימי בחישובים.
- לוודא ש-SEO, `Google Search Console`, metadata, sitemap ו-robots הושלמו.
- להשלים גישת Base44 אם רוצים חיבור נתוני Comps אוטומטי בעתיד.

## טבלת מעקב תיקונים

| אזור | מה צריך לעשות | סטטוס | הערות |
|---|---|---|---|
| אתר ראשי | להחליף `Hilel 1 LLC` ל-`Hilel Steam`, לעדכן CTA, להוסיף מלל ולעדכן עיצוב | לא בוצע | דורש מעבר בכל קבצי האתר |
| Assignment Fee | להשאיר פנימי בלבד ולא להציג בדוח הסופי | בוצע | מסונן מ-Share (`genLink`), מ-Print (`collectFormSections`) ומ-CSV (`collectCsvInputRows`) דרך `INTERNAL_ONLY_FIELDS`. נשאר בחישובים הפנימיים |
| Title Costs | להשאיר רק `Title` בלי פירוט נוסף | בוצע | `Title, escrow, recording` הוחלף ל-`Title` בלבד |
| Buy & Hold / Excel Inputs | לנקות שדות Excel פנימיים וכפילויות ולשמור רק מה שנחוץ | בוצע | שדות Excel פנימיים וכפילויות הוסרו מהטופס; נשארה החלטה פתוחה רק לגבי `Cash In Deal` אם צריך להציגו |
| Hard Money / Flip | להשאיר Hard Money Rates/Points ולנקות שדות לא ברורים | בוצע | `Excel Flip + Leverage Inputs`, `Excel Purchase` ו-`Select Scenario` נמחקו מהטופס; נשארו Hard Money Rates/Points והחישובים ממשיכים לעבוד |
| Strategy / Results | לשמר/לבנות המלצת אסטרטגיה ותוצאות יצוא | בוצע | המלצת אסטרטגיה + טבלת השוואה קיימות. נוספה רשימה מרכזית `INTERNAL_ONLY_FIELDS` (`n-fee`, `sf-assignment`) שמסוננת מ-Share, Print ו-CSV. ה-Assignment Fee נשאר בחישובים הפנימיים בלבד ולא חושף לקונה |
| SEO / Deployment | Search Console, metadata, sitemap/robots וחיבור Netlify ל-GitHub | חלקית | GitHub כבר חובר והקוד נדחף; SEO/Search Console עדיין לא |
| גישה למחשבון | להוסיף הגנת username/password ולהסתיר קישור מהעמוד הראשי | בוצע ונפרס | Netlify Edge Function פעיל בפרודקשן; hash/salt שמורים ב-Netlify env; הסיסמה לא נשמרה בקוד |
| Property Type | למחוק `Condo` ו-`Commercial`; להשאיר `Townhouse` | בוצע | `Calculator.html` שורה ~600: נמחקו `Condo / Townhouse` ו-`Commercial`, נוסף `Townhouse`. נשארו Single Family / Multi-Family / Townhouse |
| Property Photos / PDF | להכניס תמונות לדוח הסופי (דרך Print) | בוצע | מסלול Export PDF הוסר לחלוטין. התמונות מ-Property Photos מוצגות בדוח ההדפסה בסקשן `Property Photos`, ממוקם מיד אחרי Property Details (כמו מיקום ההעלאה בטופס). וידאו לא נדרש |
| Repairs | למחוק עמוד Repairs מלא ולהחליף בבחירת Light/Medium/Heavy | בוצע | עמוד p3 (Repair Items) נמחק כולו. נוסף בורר `Repair Level` (Light/Medium/Heavy) + שדה `Repair Budget` בסוף עמוד Purchase. Heavy מחייב הזנת מספר ≥85k. המספר מזין את כל החישובים |
| שדות דיפולטיביים | לאפס מספרים ולהוסיף סימון אדום לשדות שלא נגעו בהם | בוצע | כל שדה מספרי מתחיל ריק (חוץ מהנחות: ריביות/אחוזים/תקופות) ומסומן באדום עד עריכה ראשונה. מנגנון JS גלובלי (`initDefaultFields`) |
| Seller Finance | להוסיף Seller Finance ו-Subto לפי ה-Google Sheet | בוצע בקוד | נמצא ב-`Calculator.html` בעמוד `Creative`, כרטיס `Seller Financing`; כולל Buyer Entry Fee ו-Balloon Balances |
| Comps | להוסיף עמוד Comparables עם חישוב ARV לפי קומפים | בוצע | נוסף step חדש `Comps` (שלב 3) במחשבון. טבלת קומפים ידנית, $/sqft אוטומטי, ממוצע, ARV = ממוצע×subject sqft. תואם בדיוק ללשונית "Fix & Flip Calc" באקסל. בלי חיבור Base44. כפתור "Use this ARV in the deal" מזין את ה-ARV ל-`n-arv`. (MAO 70/75% הוסר — לא דובר בשיחה בהקשר Comps) |

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

- בוצע: המחשבון מוגן בסיסמה באמצעות Netlify Edge Function ו-HTTP Basic Auth.
- בוצע: לא נוצר מנגנון הרשמה מלא.
- בוצע: נוצרה כניסה פשוטה עם username/password שמיועדת להלל בלבד.
- בוצע: קישורי `Calculator` גלויים הוסרו מהניווט בעמודים הציבוריים.
- בוצע: המחשבון נשאר נגיש דרך קישור ישיר בלבד.
- בוצע: הסיסמה הגולמית לא נשמרה בקוד; ב-Netlify env נשמרים רק username, salt ו-password hash.
- אומת בפרודקשן: בלי פרטים מתקבל `401`, עם פרטים שגויים מתקבל `401`, ועם פרטים נכונים המחשבון נטען.

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
- ✅ בוצע: ב-`Calculator.html` נוסף סקשן `Property Photos` ל-`renderPrintReport()`, מוצג רק דרך **Print** (`window.print()`). התמונות מגיעות ממערך `photos` (data URLs מ-Property Photos), בגריד 3 עמודות (`.report-photos`) עם `break-inside:avoid`. הסקשן ממוקם מיד אחרי סקשן `Property Details` בדוח — בדיוק כמו מיקום ההעלאה בטופס. אם אין תמונות הסקשן לא מופיע. וידאו לא נכלל.
- ✅ בוצע: מסלול **Export PDF** הוסר לחלוטין — נמחקו הפונקציה `exportPdf()`, ה-`<script>` של `html2pdf` מ-CDN, וה-CSS של `.report-export-mode`. לא היה לו כפתור בממשק ממילא; היצוא היחיד לדוח מודפס הוא דרך Print.

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
  - ✅ בוצע: נשאר רק `Title`.
  - `escrow, recording` נמחקו.

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
- ✅ בוצע ב-`Calculator.html`:
  - עמוד ה-Repairs הישן (page `p3`, "Repair Items" עם קטגוריות/קבלן/סטטוס) נמחק כולו, והוסר מה-stepper (הצעדים מוספרו מחדש 1–8).
  - בסוף עמוד **Purchase** (p2) נוסף card חדש `Repairs`: בורר `Repair Level` עם Light / Medium / Heavy + שדה `Repair Budget` (`#n-rehab`).
  - בחירת Light ממלאת 27,500 (אמצע 10k–45k), Medium ממלאת 65,000 (אמצע 45k–85k) — שניהם ניתנים לעריכה. Heavy מנקה את השדה ומחייב הזנת מספר; אם <85k מוצגת אזהרה אדומה.
  - הסכום מ-`#n-rehab` מזין את כל החישובים דרך `getRepairs()` (כמו קודם, רק שעכשיו קורא מספר אחד במקום סכימת טבלה).
  - נוקו כל ההתליות הישנות: `addRow`/`sumRepairs`/`rtbody`/יבוא CSV של שורות repair/סקשן "Repairs Log" בדוח. בדוח ההדפסה רמת השיפוץ והתקציב מופיעים תחת סקשן Purchase.

## Buy & Hold / Excel Buy & Hold Inputs

- להשאיר את הנתונים התפעוליים הרלוונטיים:
  - Rent Monthly
  - Property Tax
  - Insurance
  - HOA
  - Management Fee
  - Vacancy Rate
  - Airbnb Cleaning / Supplies, אם עדיין רלוונטי לאסטרטגיה
- ✅ בוצע: הוסר כל החלק שסומן כ-`Excel Buy & Hold Inputs` כשהוא כפילות או נתוני Excel פנימיים.
- ✅ בוצע: שדות Excel לא ברורים הוסרו מהטופס, כולל `Excel Purchase`, `Excel Repairs` ו-`Select Scenario`.
- נשאר לבדוק רק אם `Cash In Deal` צריך להופיע למשתמש או להישאר מאחורי הקלעים.

## ברירות מחדל וסימון שדות שלא נגעו בהם

- לא להשאיר במחשבון מספרים דיפולטיביים מבלבלים מעסקאות קודמות.
- שדות מספריים צריכים להתחיל ב-0 או ריק, לפי מה שנכון לחישוב.
- להוסיף אינדיקציה ויזואלית לשדות שהלל עדיין לא נגע בהם:
  - שדה שלא נגעו בו יסומן באדום.
  - אחרי הזנה/עריכה, הסימון האדום ייעלם.
- המטרה היא שהלל ידע מייד אם מספר הוא דיפולטיבי או מספר שהוא הזין בפועל.
- ✅ בוצע ב-`Calculator.html` (מנגנון JS גלובלי, בלי לערוך ~100 שדות ידנית):
  - `initDefaultFields()` רץ ב-load ועובר על כל `input[type=number]`:
    - מאפס (משאיר ריק) את כל השדות הדולריים הספציפיים-לעסקה (purchase, ARV, repairs, hard money loan, service fee, שכירויות/מיסים/ביטוח מעסקאות קודמות וכו').
    - שומר רק שדות-הנחה (ריביות, אחוזים, תקופות, counts) דרך `KEEP_DEFAULTS` — כדי לא לשבור חישובים סבירים.
  - כל שדה מספרי מקבל class `untouched` → מסגרת אדומה + רקע אדמדם + פס אדום משמאל. ברגע שהלל מקליד/משנה (`input`/`change`) הסימון האדום נעלם.
  - שדה `Repair Budget` מאבד את הסימון האדום כשבוחרים Repair Level (לא רק בהקלדה ידנית).
  - טעינת deal מ-share-link מנקה אוטומטית את הסימון האדום מהשדות שמולאו.
  - שורות ה-Comps לא מסומנות (הלל ממלא אותן ממילא).

## Hard Money / Flip / Leverage

- להשאיר `Hard Money Rates` ו-`Hard Money Points`; הם קריטיים.
- ✅ בוצע: האזור `Excel Flip + Leverage Inputs` נמחק מהטופס.
- ✅ בוצע: השדות `Excel Purchase`, `Excel Repairs` ו-`Select Scenario` הוסרו.
- ✅ בוצע: `Hard Money Rates` ו-`Hard Money Points` נשארו.
- ✅ בוצע: החישובים נבדקו אחרי הניקוי והמשיכו לעבוד.

## Seller Finance

- בוצע בקוד: החלק נמצא בתוך המחשבון ב-`Calculator.html`, בעמוד מספר 7 `Creative`, בכרטיס `Seller Financing`.
- בוצע בקוד: נוספה בחירת `Offer Type` עם אפשרויות `Seller Finance` ו-`Subto`.
- בוצע בקוד: החישובים מבוססים על מבנה ה-Google Sheet שנשלח, כולל Buyer Entry Fee ו-Balloon Balances.
- בוצע בקוד: הוכנסו החישובים/מספרים של `Buyer Entry Fee`; זה קריטי לפי השיחה.
- `Buyer Entry Fee` כולל:
  - Down Payment
  - Rehab
  - Assignment Fee
  - Closing / Title
- בוצע בקוד: הוכנסו חישובי `Balloon Balances`; זה קריטי לפי השיחה.
- `Balloon Balances` מציג:
  - At end of Year
  - Date
  - Interest Paid
  - Principal Paid
  - Outstanding Balance
  - Total Paid
- בוצע בקוד: נתמך בהזנת:
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
- בוצע בקוד: נתמכים חישובי Cash Flow ו-Cash-on-Cash Return לפי המודל ב-Sheet.
- בוצע בקוד: שינוי נתון כמו Down Payment, Monthly Payment, Rehab או Assignment Fee מעדכן את התוצאות.
- בוצע בקוד: יש מקום להזין/לחשב את המספרים שסומנו באדום ב-Sheet.

## Strategy / Results

- לשמר או לבנות תוצאה שמראה מה האסטרטגיה הכי טובה לעסקה.
- ב-Sheet מופיע `Airbnb best strategy for this`; לבדוק איך לתרגם את זה למחשבון.
- אחרי הזנת נתונים, צריך לבדוק האם התוצאה הגיונית ולעשות fine-tuning עד שהחישובים מתאימים להלל.
- להשאיר אפשרויות:
  - Generate Share
  - Export CSV
  - Print
- ✅ בוצע: Share/Print/CSV לא חושפים נתונים פנימיים. נוספה רשימה מרכזית אחת `INTERNAL_ONLY_FIELDS` (כרגע `n-fee` ו-`sf-assignment`); כל מסלולי הייצוא מדלגים על שדות ברשימה, אך הם ממשיכים להשתתף בכל החישובים הפנימיים. כדי להוסיף שדה סודי בעתיד — מספיק להוסיף את ה-id לרשימה הזו.

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
- ✅ בוצע: ב-`Calculator.html` נוסף step חדש `Comps` (שלב 3, בין Purchase ל-Repairs; page id `pcomps`). העיצוב מבוסס על מסך ה-COMPS ב-CRM של הלל (witty-estate-flow-crm.base44.app):
  - שדה `Subject Property Sqft` שמסונכרן אוטומטית מ-Property Details (`#sqft`), ניתן לעריכה.
  - טבלת `Comparable Sales` עם Add Comp / מחיקת שורה. עמודות: #, Address, Sqft, Sold Price, **$/sqft (מחושב אוטומטית = Sold/Sqft)**, Sold Date, Bd/Ba, Distance.
  - שורת `Average (N comps) $X / sqft`.
  - 2 כרטיסי תוצאה: `Avg $/Sqft` ו-`ARV` (=ממוצע $/sqft × subject sqft) — בדיוק מה שהלל תיאר בשיחה, ותואם ללשונית `Fix & Flip Calc` באקסל (כל קומפ `K=J/I`, ממוצע `K18=AVERAGE`, `Total ARV (E8)=D8*C8`).
  - כפתור `Use this ARV in the deal →` שמזין את ה-ARV המחושב לשדה `n-arv` בעמוד Purchase (כדי להצדיק את ה-ARV מול הקונה).
  - הקריטריונים של הלל (עד ~מייל-מייל וחצי, ±200 sqft, תאריך מכירה עדכני, דמיון חדרים/בנייה/מצב) מוצגים כהערה. הזנה ידנית בלבד — אין משיכה אוטומטית מ-Base44/iComps.
  - 3 שורות קומפים ריקות נטענות בברירת מחדל.
  - הערה: כרטיסי `MAO 70%`/`MAO 75%` שהיו במסך ה-CRM הוסרו מהעמוד — הלל לא הזכיר אותם בשיחה בהקשר Comps. באקסל ה-MAO הוא חלק מ-Fix & Flip (`(ARV×%) − Rehab − closing`, ואז `Your Offer = MAO − Assignment Fee`), לא מעמוד הקומפים.

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
2. ✅ להגן על המחשבון בסיסמה ולהסיר קישור גלוי מהאתר. (בוצע)
3. לנקות את Property Type, Repairs, Excel Inputs ושדות דיפולטיביים. (Property Type ✅ + Repairs ✅ + דיפולטים/סימון אדום ✅ בוצעו; Excel Inputs פתוח)
4. ✅ לתקן PDF/הדפסה כך שיכלול תמונות ולא יציג Assignment Fee. (תמונות בהדפסה ✅ + הסתרת Assignment Fee מ-Share/Print/CSV ✅ בוצעו)
5. להוסיף Seller Finance ו-Balloon Balances לפי ה-Google Sheet.
6. ✅ להוסיף Comps ידני עם חישוב ARV. (בוצע)
7. לעבור fine-tuning על כל החישובים מול הלל.
8. להשלים SEO ו-Google Search Console.
