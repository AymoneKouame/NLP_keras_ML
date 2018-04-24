import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wd= CleanSentences(raw_text)

wc1 = WordCloud(max_font_size=40).generate(str(wd))
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
