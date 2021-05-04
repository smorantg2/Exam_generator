from newspaper import Article
import re
import tkinter as tk

def button(prep):
    global count, text_with_blanks, correction, correct

    text_with_blanks = text_with_blanks.replace('____', solutions[count].upper(), 1)
    exam.config(text=text_with_blanks)

    if prep.lower() == solutions[count].lower():
        correct += 1
        correction_msg = "\nCORRECT!\n\nCurrent score: {}/{}".format(correct,count+1)

    else:
        correction_msg = "\nI'm sorry, the correct preposition was: {}. You wrote: {}\n\nCurrent score: {}/{}".format(solutions[count].upper(), prep.upper(),correct,count+1)
    correction.config(text = correction_msg)

    count += 1

def get_article(url):
    global solutions, text_with_blanks, count, correct

    article = Article(url = url)
    article.download()
    article.parse()

    big_regex = re.compile(' | '.join(map(re.escape, prepositions_list)))
    text_with_blanks = big_regex.sub(" ____ ", article.text)
    solutions = big_regex.findall(article.text)
    solutions = [x.replace(" ", "") for x in solutions]

    exam.config(text = text_with_blanks)

    count = 0
    correct = 0


prepositions_list = ["aboard", "about", "above", "across", "after", "against", "along", "among", "anti", "around", "as", "at" , "before",
                         "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by" , "concerning", "considering",
                         "despite", "down", "during", "except", "excepting", "excluding", "following", "for", "from", "in", "inside",
                         "into", "like", "minus", "near", "of", "off", "on", "onto", "opposite", "outside", "over", "past", "per", "plus",
                         "regarding", "round", "since", "than", "through", "to", "toward", "towards", "under", "underneath", "unlike", "until",
                         "up", "upon", "versus", "via", "with", "within", "without"]

#### TKINTER GUI #####

count = 0
correct = 0

root = tk.Tk()
root.title("Sergio's exam generator")

root.geometry("800x950")
title = tk.Label(root, text = "\nWELCOME TO SERGIO'S EXAM GENERATOR\n", font = "fixedsys 20 bold")
title.pack()

label_url = tk.Label(root, text="Please, enter the article's URL",wraplength=700)
label_url.place(anchor = 'center')
label_url.pack()

input_url = tk.Entry(root,width=100)
input_url.pack(pady=30)

btn1 = tk.Button(root,text="Get article",command=lambda:get_article(input_url.get()))
btn1.pack()


exam = tk.Label(root, text="",wraplength=700)
exam.place(anchor = 'center')
exam.pack()

input_prep = tk.Entry(root)
input_prep.pack(pady=30)

btn2 = tk.Button(root,text="CHECK PREPOSITION",command=lambda:button(input_prep.get()))
btn2.pack()

correction = tk.Label(root, text="\n",wraplength=700)
correction.place(anchor = 'center')
correction.pack()

root.mainloop()

exit()