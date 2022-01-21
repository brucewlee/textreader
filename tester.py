# -*- coding: utf-8 -*-
import textreader

text = "Here we go again. We were all standing in line waiting for breakfast when one of the caseworkers came in and taptap-tapped down the line. Uh-oh, this meant bad news, either they’d found a foster home for somebody or somebody was about to get paddled. All the kids watched the woman as she moved along the line, her high-heeled shoes sounding like little fire-crackers going off on the wooden floor.Shoot! She stopped at me and said, “Are you Buddy Caldwell?”I said, “It’s Bud, not Buddy, ma’am.”She put her hand on my shoulder and took me out of the line. Then she pulled Jerry, one of the littler boys, over.“Aren’t you Jerry Clark?” He nodded.“Boys, good news! Now that the school year has ended, you both have been accepted in new temporary-care homes starting this afternoon!”Jerry asked the same thing I was thinking, “Together?”She said, “Why no, Jerry, you’ll by in a family with three little girls…”Jerry looked like he’d just found out they were going to dip him in a pot of boiling milk.“…and Bud…” She looked at some papers she was holding. “Oh, yes, the Amoses, you’ll be with Mr. and Mrs. Amos andtheir son, who’s twelve years old, that makes him just two years older than you, doesn’t it, Bud?”“Yes, ma’am.”She said, “I’m sure you’ll both be very happy.”Me and Jerry looked at each other.The woman said, “Now, now, boys, no need to look so glum, I know you don’t understand what it means, but there’s a depression going on all over this country. People can’t find jobs and these are very, very difficult times for everybody.We’ve been lucky enough to find two wonderful families who’ve opened their doors for you. I think it’s best that we show our new foster families that we’re very…”She dragged out the word very, waiting for us to finish her sentence for her.Jerry said, “Cheerful, helpful and grateful.” I moved my lips and mumbled. dsfkdsjfklj"

text_object = textreader.request(text)
print(text_object.flesch_kincaid_grade_level(adjusted=False))
print(text_object.fog_index(adjusted=False))
print(text_object.smog_index(adjusted=False))
print(text_object.coleman_liau_index(adjusted=False))
print(text_object.automated_readability_index(adjusted=False))

print('-'*30)

print(text_object.FKGL(texttype='poetry'))
print(text_object.FOGI(texttype='poetry'))
print(text_object.SMOG(texttype='poetry'))
print(text_object.COLE(texttype='poetry'))
print(text_object.AUTO(texttype='poetry'))

print(text_object.calculate_tree_height())
print(text_object.count_content_word())
print(text_object.count_noun_phrases())
print(text_object.count_word_familiarity())
print(text_object.count_content_word())
