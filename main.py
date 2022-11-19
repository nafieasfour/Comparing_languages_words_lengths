import string
from matplotlib import pyplot as plt
import nltk

German = 'Die Staats- und Regierungschefs der APEC-Staaten verabschieden auf ihrem Gipfeltreffen in Bangkok eine Erklärung zum Krieg in der Ukraine. Darin heißt es, die meisten Mitglieder der Asiatisch-Pazifischen Wirtschaftsgemeinschaft hätten den Krieg scharf verurteilt und betont, "dass er immenses menschliches Leid verursacht und die bestehenden Schwächen der Weltwirtschaft verschärft". Es habe aber auch "andere Ansichten und unterschiedliche Einschätzungen der Situation und der Sanktionen" gegeben. Die APEC sei kein Forum zur Lösung von Sicherheitsproblemen. Sie erkenne aber an, dass diese erhebliche Konsequenzen für die Weltwirtschaft haben könnten. Man habe gesehen, dass sich der Krieg in der Ukraine nachteilig auf die globale Wirtschaft auswirke.'
German_without_punctuation = German.translate(str.maketrans('', '', string.punctuation))
German_tokens = nltk.word_tokenize(German_without_punctuation)
print(German_tokens)

German_word_length = [len(w) for w in German_tokens]
plt.hist(German_word_length, align='mid')
plt.xlabel("number of characters in each word")
plt.ylabel("number of words")
plt.title("German")
plt.show()

English = "I have something I want to ask you.' David searched her eyes to see if she guessed what was coming. Her smile was reassuring. She squeezed his hand. 'You needn't worry. Whatever it is, I'm sure I'll say yes!' A huge wave of excitement went through him as he prepared to ask the most important question of his life. From the corner of the restaurant, a strange man watched them. He sat, stiff and unmoving, at his table, pretending to read a menu. But all the while, he stared with cold eyes at the young couple. Back at their table, David suddenly felt his nerves return.'Excuse me,' he said to Emma. He pushed his chair back and went to the toilet. As he looked at his reflection in the mirror, he took a deep breath and told himself: 'Come on, David, come on! You can do this, mate! She's crazy about you!'"
English_without_punctuation = English.translate(str.maketrans('', '', string.punctuation))
English_tokens = nltk.word_tokenize(English_without_punctuation)
print(English_tokens)

English_word_length = [len(w) for w in English_tokens]
plt.hist(English_word_length, align='mid')
plt.xlabel("number of characters in each word")
plt.ylabel("number of words")
plt.title("English")
plt.show()


Arabic = "أما مازن وعديّ وأمجد فارتبكوا بعض الشيء ، وباقي التلاميذ في الفصل يفكرون بكلمات بحرف الراء. نظر المعلم لتلاميذه وبدأ يشرح نطق حرف الراء وكلماته وكيف يُكتب؟ لكنه لاحظ عدم مشاركة عدنان وهو الولد المتميّز ، وسرعان ماربط المعلم بين الحصة ومشكلته مع حرف الراء لكنه استغرب حال أقرانه فسأل المعلّم : مابكم ياأعزائي ؟ أجابوا : فليرحل حرف الراء ! استغرب المعلّم : وقال كيف يرحل وهو موجود بالأسماء والحركات بالأفعال والتمييز. وآخر كلمة مسرور وهي حالة فرح نسعى لها جميعًا همهم الأطفال وأومأوا برؤسهم تأكيدًا على الكلام لكنه ليس بسعادة فنظر المعلم لعدنان : وقال زدت حرف الراء جمالا حين تتلعثم فيه فهذا ليس ذنبك ولا نب حرف الراء  ، هذا اختبار الله فينظر هل تصبر وترضى أم تقنت ؟ سكت عدنان وقال: حقيقي ياأستاذي لكني أخجل أن أتلعثم أمام أحد فيسخر مني سكت المعلم ثم قال : من يتتعتع في القرآن وهو بين يدي الله تعالى يكافئه الله بأجرين ، فهل تخجل من الناس ؟! شعر عدنان ببعض الثقة مع الندم أنه يفكر في خجله من الناس . ونظر للأولاد الثلاث وقال هل يرحل أم يظل الراء لتكونوا سعداء قال الأولاد : يظل ولكن يرحل من كلمة واحدة فقد جاء في النصف يفصل حرفين نحبهم جميعا"
Arabic_without_punctuation = Arabic.translate(str.maketrans('', '', string.punctuation))
Arabic_tokens = nltk.word_tokenize(Arabic_without_punctuation)
print(Arabic_tokens)

Arabic_word_length = [len(w) for w in Arabic_tokens]
plt.hist(Arabic_word_length, align='mid')
plt.xlabel("number of characters in each word")
plt.ylabel("number of words")
plt.title("Arabic")
plt.show()
