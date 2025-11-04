# Episode 2 uses centralized points system from points_system.rpy
default gemmy_kiss = False
default watched_horror_movie = False

label episode_2:

    play music "ES_2 Broken Hearts - Particle House.mp3" volume 0.2

    scene home_morning
    show mc at mc_convo
    with Fade(0.5, 5.0, 0.5)

    if nancy_outcome_prologue == "best" or nancy_outcome_prologue == "good":
        $ update_character_state("mc", CharState.HAPPY)
        mc "Hm…" # [1]

        $ update_character_state("bull", CharState.HAPPY)
        show bull at bull_convo
        with pixellate

        bull_phone "Good morning, sleeping princess." # [1]
        mc "Nancy didn't come back." # [1]
        bull_phone "Of course she isn't. Do you think she'd move in with you just because she wanted a quick fuck?" # [1]
    else:
        $ update_character_state("mc", CharState.SAD)
        mc "Yaaawn!" # [1]

        $ update_character_state("bull", CharState.ANGRY)
        show bull at bull_convo
        with pixellate

        bull_phone "Wake up, coomer." # [1]
        mc "Don't call me that, man, come on." # [1]
        bull_phone "I had to watch as you jerked the entire night thinking about those girls." # [1]
        bull_phone "If you want me to stop calling you this, you better get back to hunting and see some real pussy action!" # [1]

    bull_phone "If you want to get more pussy, you better get back at hunting!" # [2]
    mc "Hunting, eh?" # [2]
    mc "Yeah. I should. I won't let myself fall back to that sad state I was in before." # [2]
    bull_phone "That's what I like to hear!" # [2]
    mc "…How should I do that, though?" # [2]
    bull_phone "Boy, believe me, if I had lungs, I'd be sighing loud right now…" # [2]
    bull_phone "You should know what to do! This sort of thing is ingrained deep within your very DNA, man!" # [2]
    mc "My DNA?" # [2]
    bull_phone "Yeah, how did homo sapiens do back then? They'd stalk their prey for hours, and days, and weeks, until they couldn't resist anymore!" # [2]
    mc "Persistent hunting…" # [3]
    bull_phone "That's right. If you think you already got on the good side of that girl… Lauren, you're already halfway there." # [3]
    bull_phone "You threw your spear on her, now you mustn't let her leave! Corner her up, and get that juicy meet all for yourself!" # [3]
    mc "But… what if I didn't get on her good side?" # [3]
    bull_phone "Then, at least you can make friends with her or something." # [3]
    bull_phone "Even in this sad ass case, she'd help clear your reputation, at the very least." # [3]
    mc "I see." # [3]

    mc "S-Should I invite her on a second date, then?" # [4]

    play sound "ES_Telephone Ringback Tone - Epidemic Sound.mp3"

    bull_phone "I'm already calling her." # [4]
    mc "Wait, I'm not ready yet!" # [4]

    menu:
        "Grab the phone":
            label test_choice_v7eop:
            mc "Eh-?!" # [cite: 1]

    with fade

    lauren "[player_name]…?" # [4]
    mc "Ugh?!" # [4]
    mc "H-Hi, Lauren." # [4]
    lauren "…Hi." # [4]
    mc "So, uhm, I was just thinking…" # [4]
    "My heart was beating fast." # [4]
    "So fast, in fact, that it could very well fail me depending on the answer I'd end up getting from her." # [4]
    "I asked myself if I could really end up becoming the man that the phone wanted me to be…" # [4]
    mc "I-I had lots of fun on our last date, so how about we go on a second one? Maybe? Any of these days? When you're free? And only if you'd like to, of course." # [4]

    # Branch based on previous date outcome (assuming it's a variable from prior gameplay)
    if lauren_outcome_episode_1 == "worst":
        lauren "You had fun with that…?" # [5]
        lauren "Then you're weirder than I thought." # [5]
        lauren "…But I suppose I could at least give you a second chance. For the sake of the old times." # [5]
        lauren "Otherwise, that frog we dissected would have died in vain." # [5]
        mc "Yes! Thank you!" # [5]
        mc "We can meet up at my place, tomorrow, maybe?" # [5]
        lauren "…Fine." # [5]
        lauren "Just make sure your house isn't smelling like used tissue paper and there won't be potato chips lying everywhere." # [5]
        mc "M-My house isn't that bad, okay…?" # [5]
        lauren "We'll see." # [6]
        $ win_sound()
        $ lauren_love += 5 # Acknowledge a small positive for getting the second date
    else: # Assuming "good", "neutral", "best" or other positive outcomes lead to this
        lauren "…I-If you want to." # [6]
        mc "I-I do. I really want to meet up with you again." # [6]
        mc "Maybe we could meet up at my house tomorrow?" # [6]
        lauren "Your house…?" # [6]
        mc "Yes. Will you be able to make it?" # [6]
        lauren "I'll have to shave…" # [6]
        mc "What?" # [6]
        lauren "Nothing! Hm… Yes, I'll be knocking on your door tomorrow." # [6]
        lauren "Now, I need to… prepare some stuff." # [6]
        mc "Ah, yeah, me too. Goodbye, see you tomorrow, haha." # [6]
        mc "Sigh!" # [6]
        $ win_sound()
        $ lauren_love += 10 # More positive for a direct "yes"

    menu:
        "Hang up the phone":
            label test_choice_p7oug:
            play sound "ES_Mobile Phone, Hang Up Beeps - Epidemic Sound.mp3"
            "Beep, beep, beep…" # [cite: 1]

    scene home_morning
    show mc at mc_convo
    with fade

    $ update_character_state("bull", CharState.HAPPY)
    $ update_character_state("mc", CharState.HAPPY)
    show bull at bull_convo
    with pixellate

    bull_phone "See? It worked up in the end, right?" # [6]
    mc "Yeah, I guess so." # [7]
    bull_phone "Don't forget it, though: if you mess up three times, I'll be gone, and you'll be left all alone to be bullied and humiliated by everyone around you for the rest of your life!" # [7]
    mc "I… I'll start making preparations for tomorrow immediately!" # [7]

    $ update_character_state("bull", CharState.HAPPY)
    bull_phone "Hehe, good." # [7]

    hide bull
    with pixellate

    "First, I researched an easy, yet delicious recipe on the internet, and more tips about dates and male beauty." # [7]
    mc "It seems the thing that the mostly unanimously recommended thing about man's fashion is to have a nice, athletic body…" # [7]
    mc "Maybe I should start to work on that." # [8]
    mc "Still, I can't grow some muscles in just one day, I should focus on what I can do right now, and that is: clean my house, and buy some food ingredients!" # [8]
    mc "I can sweep the floors whenever, but the market will close up eventually, so I'd better prioritize it first." # [8]
    "I noted down a short list of ingredients for a creamy garlic pasta recipe, and headed out." # [8]

    scene mall_interior_morning
    show mc at mc_convo
    with Fade(0.5, 5.0, 0.5)

    "It took me two whole hours to get to the mall and buy most of the necessary ingredients. That wasn't due to a hard time finding them or something, however…" # [8]

    $ update_character_state("mc", CharState.SAD)

    mc "Urgh…" # [9]
    mc "(I feel sick just by coming to this place.)" # [9]
    "I really tried my best to find substitutes for the chicken, but unless I wanted to go fully vegan (and I didn't), there was no other choice: I had to come to the butcher shop… and face the butcher." # [9]
    mc "(I feel nauseous…)" # [9]

    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate

    bull_phone "Don't even DARE to throw up right now, dude." # [9]
    bull_phone "This guy fucked that bitch of an ex-girlfriend of yours, you just can't show any more weakness before him!" # [9]
    mc "I know, dammit…" # [9]
    "Finally finding enough courage in me to talk to the butcher and buy some chicken, I came out from behind the fridges, and walked towards the counter." # [9]

    scene butcher_shop_morning
    $ update_character_state("gemmy", CharState.ANGRY)
    $ update_character_state("craig", CharState.ANGRY)
    show gemmy at gemmy_right_pos
    show craig at craig_left
    with fade

    stop music fadeout 2
    play music "ES_Summer '15 - Maybe.mp3" volume 0.2

    mc "Ummm..."
    mc "What's going on here."

    gemmy "I'm not going to ask again, you asshole! Pay the damn child support at once, or I WILL sue you!" # [10]
    craig "You mean you're going to ask that stupid cousin of yours to sue me? That idiot wouldn't be able to get Hitler behind jail, do you really think he'll get me to give you a penny, you bitch?" # [10]
    "And it turned out, I showed up right as the butcher was having a fight with his ex-wife." # [10]
    "Unfortunately, the annoyed man seemed to be looking for any way possible to get out of that situation, change topics and be left at peace, when his eyes lay on me." # [10]
    craig "Hehe, look who it is." # [11]
    craig "It's been so long since you last came here, I thought you had gone vegetarian." # [11]
    craig "Well, I suppose if you buy some sausage, you're to find a way to use it nevertheless, hehehe." # [11]

    menu:
        "Instead of running away from her, shouldn't you be answering your ex-wife now?":
            label test_choice_qxv44:
            $ lose_sound()
            craig "And who the fuck said that I'm running away from anything?!" # [11]
            gemmy "Craig Jason Smith: you ARE running away from me! And from your duties! Pay your fucking child support right now!" # [11]
            craig "Gemmy, you bitch! Are you that broke that you need to squeeze every penny out of me, hu?!" # [11]
            mc "(And they're fighting again.)" # [12]
            jump butcher_continue
        "I-I don't even want a sausage, though…":
            label test_choice_kwedf:
            $ lose_sound()
            gemmy "Craig, if you think you can avoid me by bull_phoneying that boy, you're completely wrong!" # [12]
            craig "Gleemy, won't you shut the fuck up already?" # [12]
            mc "(And they're fighting again.)" # [12]
            jump butcher_continue
        "If you cut down the pig, then who will work as the butcher?":
            label test_choice_smq15:
            $ lose_sound()
            craig "What…?" # [12]
            gemmy "Pft! Hahaha!" # [12]
            gemmy "The boy is right, you fat pig! I don't want your oily, disgusting ass meat, I want your money!" # [13]
            craig "You ain't getting shit from me today, Glemmy!" # [13]
            craig "I've got it all figured out... I've been researching ways to avoid paying..."
            
            menu:
                "Research? What kind of research?":
                    label test_choice_7ky05:
                    outline "Craig thinks he's so smart with his schemes..."
                    outline "What do people do when they test theories and conduct research?"
                    jump outfit_41_puzzle
                    label outfit_41_puzzle_success:
                        outline "Too bad his experiments in being a deadbeat dad are failing!"
                    label outfit_41_puzzle_failure:
                        outline "Craig's not as smart as he thinks he is..."
                "Keep arguing with Gemmy":
                    label test_choice_31dkw:
                    "The argument continues..."
            gemmy "What about your son?!" # [13]
            mc "…" # [13]
            gemmy "Do you really think you can buy me with a slice of meat…?!" # [13]
            craig "You've always been a cheap whore, so don't pretend this shouldn't be enough." # [13]
            gemmy "You asshole! You don't even care about your son!" # [13]
            craig "Our son this, our son that…" # [14]
            craig "Our son can come visit me when he got a pretty girlfriend…" # [14]
            craig "So I can fuck her just like I did with this loser's girlfriend right here! Hahaha!" # [14]
            jump butcher_continue
        "Embarrass him.":
            label test_choice_utfvb:
            "Ba-Dum!" # [14]
            mc "Abandoning and mistreating your beautiful ex-wife for that cheap prostitute, you're helpless, Craig." # [14]
            $ update_character_state("gemmy", CharState.AROUSED)
            gemmy "B-Beautiful?" # [14]
            mc "What next? Will you say that you fell in love with her too?" # [14]
            mc "You know damn well [girl_friend] never loved you, Mr. Pig., you were just an easy-to-fool old man from whom to get some easy money." # [14]
            craig "You little-!" # [14]
            mc "I don't want to hear complaints from a fat old man who still fantasizes about his college years." # [14]
            mc "Now, Glemmy, would you mind giving me your number?" # [15]
            mc "We have a common enemy in Craig, and, well, I just can't resist but to ask for the contact of such a beautiful mature woman." # [15]
            craig "WHAT?!" # [15]
            craig "Glemmy, I swear, if you-!" # [15]
            gemmy "Hahaha!" # [15]
            gemmy "Of course, sweety, here you go… And I have something else to give you too." # [15]
            "Much to Craig's surprise, and my own surprise as well, Glemmy held my cheeks with both hands and…" # [15]

            play sound "ES_Loud - Epidemic Sound.mp3"

            gemmy "Hyum!" # [15]
            mc "Hm?!" # [15]
            craig "Glemmy?!" # [15]
            "She kissed me in front of her ex-husband." # [15]
            "And that was no superficial peck on the lips at all." # [16]
            gemmy "Hyum… ughn…" # [16]
            mc "Nghn… nghnn…!" # [16]
            "The older woman's tongue moved over the entire surface of the inside of my mouth, no piece of tongue, lips or gums was left untouched by her." # [16]
            "Not only was she good at what she was doing (really good at that), the fact that we were rubbing that kiss all over Craig's face was just so extremely satisfying…" # [16]
            "By the time our mouths came apart, I was popping up a huge and visibly apparent boner." # [16]
            craig "Y-You shameless whore!" # [17]
            $ gemmy_kiss = True
            jump butcher_continue_kiss

label butcher_continue:
    craig "Jeez, if you're so fucking desperate for something, I'll give you a slice of pig, alright?" # [12]
    craig "Then you better get the fuck out of here before I lose my patience, you miserable woman." # [12]
    gemmy "You ain't getting shit from me today, Glemmy!" # [13]
    gemmy "What about your son?!" # [13]
    mc "…" # [13]
    gemmy "Do you really think you can buy me with a slice of meat…?!" # [13]
    craig "You've always been a cheap whore, so don't pretend this shouldn't be enough." # [13]
    gemmy "You asshole! You don't even care about your son!" # [13]
    craig "Our son this, our son that…" # [14]
    craig "Our son can come visit me when he got a pretty girlfriend…" # [14]
    craig "So I can fuck her just like I did with this loser's girlfriend right here! Hahaha!" # [14]
    # No kiss path for Glemmy
    gemmy "Tch! You're helpless, Craig, bullying a guy like him." # [17]
    gemmy "Here, sweety, take my number. Call me if this pig bothers you again, and I'll scream my lungs out at him, okay?" # [17]
    mc "O-Okay. Thanks." # [17]
    gemmy "And don't think this is over yet, Craig! I WILL get my money!" # [17]

    stop music fadeout 1.0
    hide gemmy

    show craig at craig_convo
    with fade

    jump butcher_post_fight

label butcher_continue_kiss:
    gemmy "I don't wanna hear about shame from you, Craig, you pig!" # [17]
    gemmy "I'll come back again to get my money." # [17]
    gemmy "And you, sweety, call me if you need anything, okay?" # [17]
    mc "Of course, ma'am." # [17]

    stop music fadeout 1.0
    hide gemmy
    show craig at craig_convo
    with fade

    jump butcher_post_fight

label butcher_post_fight:

    show bull at bull_convo
    with pixellate

    bull_phone "Heh, this was interesting." # [17]
    bull_phone "It's always good to make new allies… and that Glemmy is a hell of a milf!" # [18]

    hide bull
    with pixellate

    craig "Greedy bitch, money this, money that…" # [18]
    craig "It's MY money!" # [18]
    craig "I've been investigating all the legal loopholes... searching for clues to avoid paying..."
    
    menu:
        "What do you search for when investigating?":
            label test_choice_fx2mb:
                outline "Craig thinks he's so clever with his investigations..."
                outline "What do detectives search for when solving mysteries?"
                jump outfit_42_puzzle
                label outfit_42_puzzle_success:
                    outline "Too bad the biggest clue is that he's a deadbeat!"
                label outfit_42_puzzle_failure:
                    outline "Craig's investigation skills are lacking..."
        "Stop avoiding your responsibilities":
            label test_choice_e8s9k:
            craig "I'm not avoiding anything!"
    mc "For now it is. Anyway, can I get my meat now?" # [18]
    craig "Aren't you embarrassed, asking for my services after everything?" # [18]
    mc "Don't you want to get paid?" # [18]
    craig "…Just tell me what you want." # [18]
    scene home_afternoon
    hide craig
    show mc at mc_convo
    with fade
    "After the unexpected event at the butcher shop, I returned home with all the necessary ingredients for a nice meal." # [18]
    mc "Now that everything is in the freezer, it's time to clean the house!" # [18]
    "I got a mop, a bucket, cleaning products, and started mopping." # [19]
    $ update_character_state("mc", CharState.SAD)
    "Ten minutes into that, however…" # [19]
    mc "Urgh… Phone, can't you possess my body right now and do the cleaning in my steady?" # [19]
    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate
    bull_phone "Why the hell would I do that?" # [19]
    mc "I don't know, to show me how it should be properly done?" # [19]
    bull_phone "You got it right, yeah, I'm a teacher of some sort…" # [19]
    bull_phone "And I shall teach you patience and discipline right now: clean your own goddamn house!" # [19]
    mc "(Stupid useless phone…)" # [19]
    "It took me a whole one and a half hours to finish cleaning my entire place, and by the time I was done, I was exhausted." # [19]
    mc "*Sigh!" # [20]
    mc "I just want to watch some random poor-quality show and fall asleep midway through…" # [20]
    "As I said that and envisioned the scene in my mind, my eyelids got heavier and heavier." # [20]
    scene black
    with fade
    "Before I fell asleep, however, a vision in particular did exactly the opposite of calming me down, but got my heart to beat faster." # [20]
    show scene_4
    with fade
    $ persistent.scene_4 = True
    lauren "*Suck, suck, suck!" # [20]
    mc "*Gulp!" # [20]
    "I couldn't stop thinking about her mouth, her lips and tongue. I imagined the two of us sitting on that bench in the park, and having Lauren working miracles down my shaft right then and there." # [20]
    "My hands slowly moved down my abdomen and to my-" # [21]
    scene home_night
    show mc at mc_convo
    show bull at bull_convo
    bull_phone "Hey! No jerking off the day before your date, fool!" # [21]
    mc "Tch! Do you really have to keep an eye on me all the time like this?!" # [21]
    bull_phone "I'll have to keep an eye on you for as long as you are willing to make a fool of yourself, yes." # [21]
    bull_phone "If you have that much energy, why don't you direct it at something useful, hu?" # [21]
    mc "Like what? The house is clean, the food ingredients are in the freezer, and I have decided what to wear for the date already." # [21]
    bull_phone "Aren't you forgetting something?" # [22]
    mc "Forgetting…?" # [22]
    bull_phone "You're not following the most basic tip that you've read a million times on the net, dude!" # [22]
    bull_phone "Do some goddamn exercises!" # [22]
    mc "Eh? B-But I don't even have the proper equipment yet, and I don't have gym clothes either, so…" # [22]
    bull_phone "That's unnecessary. Now, unless you want me to send all your dick pics to your family, you better get down to make some push-ups right now" # [22]
    mc "Gah?! I-I thought you were my ally!" # [22]
    bull_phone "Sometimes a good teacher must be hated, and I hope one day you'll understand it. Now, push-ups!" # [23]
    bull_phone "I'm fixing what's broken in you... rebuilding you from the ground up..."
    menu:
        "What do you use to fix broken things?":
            label test_choice_un2av:
            if lauren_love >= 35:
                bull_phone "I'm rebuilding you from the ground up..."
                bull_phone "What's the essential tool for fixing anything broken?"
                jump outfit_39_puzzle
                label outfit_39_puzzle_success:
                    bull_phone "I'm the mechanic fixing your broken spirit!"
                    bull_phone "With the right tools and work, anything can be repaired!"
                label outfit_39_puzzle_failure:
                    bull_phone "Tools and hard work fix everything, remember that..."
        "Just do the exercises":
            label test_choice_q8kjt:
            bull_phone "That's the spirit! Work builds character!"
    "I got closer to the floor and followed the phone's instructions." # [23]
    mc "(Damn phone! I'll never forget this! I won't lower my guard ever again!)" # [23]
    mc "Shit, my… arms…!" # [23]
    bull_phone "Come on, you can do at least a couple more." # [23]
    "Spoiler alert: we didn't stop at just a couple more." # [23]
    "That night, I fell asleep more soundly than I've had slept in all the past few months combined." # [23]
    scene black
    with fade
    "The next day, as soon as I woke up, I started making sure everything was just fine, and after examining and re-examining every inch of my living space and my own body for the hundredth time…" # [23]
    play sound "ES_Knocking On The Inside - Epidemic Sound.mp3"
    "Knock, knock!" # [24]
    scene home_morning
    $ update_character_state("mc", CharState.AROUSED)
    show mc at mc_convo
    with fade
    mc "(Someone is at the door? Is it the time for the date already?!)" # [24]
    mc "I-I'm coming!" # [24]
    mc "Lauren!" # [24]
    scene home_morning
    show lauren at lauren_convo
    with fade
    play music "ES_You - SRA.mp3" volume 0.2
    lauren "…Hello. I've come, as per agreed." # [24]
    mc "Yes, yes, I'm happy to see that. Uh, p-please, come in!" # [24]
    mc "This is the living room, the bathroom is right there, the kitchen is that way, and my bedroom is over there." # [24]
    lauren "It's… cleaner than I expected." # [24]
    mc "Oh, really? And what exactly did you expect?" # [24]
    lauren "Your ex told everyone that you had used tissue paper and porn magazines rolling all around your place…" # [24]
    lauren "No, that was nonsensical to begin with. Of course, she would try to make you look as bad as possible." # [25]
    mc "Haha, thank you for understanding that." # [25]
    mc "Anyway, do you want some water, or something?" # [25]
    lauren "…I'm fine." # [25]
    mc "Well then, shall we pick up a movie to watch?" # [25]
    lauren "…Yes." # [25]
    scene black
    with fade
    "We sat down on the sofa, and I struggled while asking myself what was an appropriate distance to sit away from her." # [25]
    mc "(Should I put my arm around her back or something?)" # [25]
    lauren "[player_name]? The movie." # [25]
    mc "Ah, yes!" # [25]
    mc "Uhm… So, do you have any preference for any genera?" # [26]
    lauren "…Comey." # [26]
    mc "Really?" # [26]
    lauren "Yes. Please, show me your favorite comedy movie." # [26]
    mc "Ah, yes. I'll pick just the right movie for us to watch!" # [26]
    menu:
        "HORROR AND BLOODSHED IN THE SLAUGHTERHOUSE 2!":
            label test_choice_hrcv3:
            $ lose_sound()
            $ watched_horror_movie = True
            "I picked a certain movie with a bloodred title, and we watched it in silence." # [26]
            "One and a half hours later, I turned to Lauren, excited to listen to her opinion on the pick." # [26]
            mc "S-So, what did you think?" # [26]
            lauren "This… wasn't funny at all." # [26]
            lauren "There was so much gore and jumpscares. I thought I told you to pick a comedy movie, not a horror one." # [26]
            mc "Yeah, well, I heard you, but I thought I could do just so much better picking something that would surprise you…" # [27]
            lauren "Indeed, it was a surprising choice. The worst possible kind." # [27]
            mc "(Noted: she doesn't like scary movies at all.)" # [27]
            mc "(Though... maybe some people do like spooky things... just not Lauren.)"
            jump continue_date
        "6 Weeks in the Savana: Life of a Starving Male Hyena":
            label test_choice_7pnnh:
            $ lose_sound()
            "I selected a calm and informative-looking production, and we watched it in its entirety." # [27]
            mc "Wow, I never thought I'd sympathize with a hyena. I mean, I hated them in Lion Monarch." # [27]
            lauren "Me too… I just wished I could have laughed at something. Why didn't you pick a comedy movie like I told you to?" # [28]
            mc "I-I thought I could do better than that." # [28]
            lauren "Documentaries are interesting, but they are not relaxing at all. It just reminded me of my studies…" # [28]
            lauren "*Sigh." # [28]
            lauren "Please, next time just do as I say." # [28]
            mc "Y-Yeah, sorry." # [28]
            jump continue_date
        "Male Model Against the Evil":
            label test_choice_ab459:
            "I picked a comedy movie and we watched it together." # [28]
            "Lauren didn't exactly laugh, but her lips curved up in the slightest, and I found that even more captivating than the show on TV." # [28]
            "I almost couldn't take my eyes away from her." # [28]

            scene home_afternoon
            show lauren at lauren_convo
            with fade

            "Before I knew it, the movie had ended." # [29]
            mc "So, yeah, I quite like this one. What did you think?" # [29]
            lauren "It was entertaining, indeed." # [29]
            lauren "It was so ridiculous that when I thought I couldn't be surprised anymore by nothing that the movie threw at me, they went ahead and showed something even crazier and I couldn't stop smiling." # [29]
            lauren "I… liked this movie. Thank you." # [29]
            mc "Hey, you don't need to thank me, I invited you here today because I wanted to see you happy." # [29]
            mc "If you had fun, I had fun too." # [29]
            lauren "T-Thank…" # [30]
            $ win_sound()
            $ lauren_love += 5
            jump continue_date

label continue_date:
    mc "Hey, what do you think of having something to eat something now?" # [30]
    lauren "Sounds… good." # [30]
    mc "Great! Do you like pasta?" # [30]
    lauren "Yes… Are we getting delivery? Italian food, maybe?" # [30]
    mc "Hehehe, better!" # [30]
    lauren "Better…?" # [30]
    mc "I'm cooking us something!" # [30]
    lauren "I didn't know you could cook. Your ex…" # [30]
    lauren "No, I should stop comparing the real you to the version of you your ex has been spreading around." # [30]
    mc "Yeah, I'd be thankful if you did that." # [31]
    mc "Anyway, give me half an hour, and I'll prepare something nice for the two of us to eat." # [31]
    mc "You can watch anything you want on the TV meanwhile." # [31]
    lauren "Alright." # [31]

    scene black
    with fade

    "I went to the kitchen, and opened my laptop to check the recipe I had saved." # [31]
    mc "Okay! Now I just need to follow the recipe…" # [31]
    mc "Or, maybe, I could try something else to really impress her?" # [31]
    mc "I mean, she already was impressed enough when she learned that I could cook, if I pulled out something really fancy…" # [31]
    mc "Hehehe, I can already imagine her panties falling down to her ankles!" # [31]
    "That's when I opened my fridge and noticed that I still had a package of uneaten takeaway food from a local restaurant." # [31]
    mc "Wait, maybe I could use this too? It seems quite good, maybe even better than the pasta I was about to prepare…" # [32]

    menu:
        "Follow the recipe.":
            label test_choice_nmy1s:
            "I shook my head from side to side." # [32]
            mc "No, these ideas are so scummy, they're not like me at all." # [32]
            mc "I'll just stick to the recipe as I intended, and give my best at this." # [32]
            mc "I mean, who knows? Maybe love IS the most delicious ingredient." # [32]
            "Step by step, I followed the recipe religiously, and slowly put together quite a good-looking creamy garlic pasta dish." # [32]
            mc "Yep, it appears to be good enough for a first try!" # [33]
            
            # Lauren Spooky outfit during cooking reflection
            if lauren_love >= 40:
                mc "Lauren mentioned she likes spooky things... that's actually pretty cool."
                mc "Most people are scared of scary movies and Halloween..."
                
                menu:
                    "Think about what makes Halloween special":
                        label test_choice_bkp18:
                        mc "What holiday celebrates all things spooky and mysterious?"
                        jump outfit_14_puzzle
                        label outfit_14_puzzle_success:
                            mc "Maybe I should suggest watching a horror movie sometime... carefully."
                        label outfit_14_puzzle_failure:
                            mc "I should learn more about her spooky interests..."
                    "Focus on cooking":
                        label test_choice_tqhot:
                        mc "Right now, I should focus on making this meal perfect."
            "I took the dish to the dining table, and invited Lauren in for a meal." # [33]
            scene home_afternoon
            show lauren at lauren_convo
            with fade
            lauren "…Did you cook this?" # [33]
            mc "Yes… Does it look bad?" # [33]
            lauren "No. Let's eat." # [33]
            scene black
            with fade
            "I was so nervous that I could feel my heart beating in my throat." # [33]
            "We ate together, and my heart grew anxious. Her silence was just a result of her awkwardness, or was my cooking that bad?" # [33]
            "To my own taste buds, the pasta was fine…" # [33]
            "We finished our meal." # [33]
            scene home_night
            show lauren at lauren_convo
            with fade
            mc "So, uhm… What's the opinion of tonight's critic on the pasta?" # [34]
            lauren "It was… delicious, actually." # [34]
            lauren "I did not expect you to be this talented with cooking, [player_name]." # [34]
            mc "Haha, it isn't really about talent. The secret is love, you see?" # [34]
            lauren "LOV-?!" # [34]
            lauren "*Cough, cough!" # [34]
            mc "Are you okay?" # [34]
            lauren "Y-Yes." # [34]
            lauren "I see. Even then, I greatly enjoyed eating your dish. Thank you again." # [34]
            $ win_sound()
            $ lauren_love += 5
            jump post_meal_talk
        "Try making something fancy.":
            label test_choice_k03xm:
            $ lose_sound()
            mc "You know what? Fuck that simple ass recipe!" # [34]
            mc "I'll follow my heart's voice and prepare something truly special for Lauren." # [34]
            mc "Oh, man, she'll be so impressed, hehehe!" # [35]
            "I picked a little bit of this and a little bit of that, a pinch of that thing, and a handful of that other thing…" # [35]
            "And one hour later I had a bizarre object that may or may not have been edible." # [35]
            mc "Shit… I don't even have the courage to give this a taste test." # [35]
            lauren "[player_name]? Is it done already?" # [35]
            mc "Ah! Y-Yeah, I'll be taking the meal to the dining table in just a minute!" # [35]
            mc "Shit, I don't even have the time to call a delivery now…!" # [35]
            mc "Kuh, there's no other way, I have to bet everything on this meal!" # [35]
            mc "Maybe it is one of those foods that have a terrible look to it, but actually taste kinda good, like nato or something?" # [36]
            "I took the dish to the dining table, where Lauren was waiting…" # [36]
            lauren "This smells like death…" # [36]
            "And her reaction wasn't good at all." # [36]
            mc "B-But the taste is amazing! I promise it, haha. Why don't you give it a try?" # [36]
            lauren "…" # [36]
            "She brought just a tiny bit of a fraction of a nearly empty spoonful to her mouth…" # [36]
            lauren "Pftuh!" # [36]
            "And she spat everything." # [36]
            lauren "It tastes like death too…!" # [37]
            mc "I-It's just high very highbrow cosine, you wouldn't understand." # [37]
            lauren "No, it's just a high-level shit food, and I understand it perfectly." # [37]
            lauren "*Sigh." # [37]
            lauren "It's just as [girl_friend] said, you're hopeless in the kitchen..." # [37]
            lauren "After getting a taste of this, maybe even the worse stories she used to talk about and were so hard to believe…" # [37]
            mc "L-Let's think about something else before making hasty assumptions!" # [37]
            mc "This was a failure, yes, but, you know…" # [37]
            mc "Things only turned out like this because one of the ingredients must have spoiled and I didn't notice it." # [37]
            lauren "…Of course." # [38]
            lauren "But I just lost my appetite." # [38]
            $ lauren_love -= 5  # Penalty for mess up
            jump post_meal_talk
        "Pretend that you cooked the takeaway food.":
            label test_choice_t64ue:
            $ lose_sound()
            "I spend one hour playing on my phone alone in the kitchen, and when the right time came around, I just heated up the meal in the microwave, and transferred it to two separate plates." # [38]
            mc "Dinner is ready!" # [38]
            lauren "It smells… nice." # [38]
            mc "Hehe, thank you, thank you. Why don't you give it a taste too? I swear its flavor is even better than its smell." # [38]
            lauren "…!" # [39]
            mc "So? What do you say?" # [39]
            mc "(It's delicious, of course. I know it because I constantly order food from this place!)" # [39]
            lauren "[player_name]… did you really cook this meal?" # [39]
            mc "Hm? Well, of course I did. Why do you ask?" # [39]
            lauren "Because there's a receipt in my food listing the meal name and restaurant from which you bought it." # [39]
            mc "GAH!?" # [39]
            mc "(I can't believe I fucking forgot to throw away the receipt!)" # [39]
            mc "Well, that… you see…" # [39]
            lauren "I'd be really disappointed with you, [player_name]… if this wasn't a bit funny." # [39]
            lauren "So, I'm just a little bit disappointed." # [39]
            mc "Sorry…" # [39]
            "We finished our meal in an embarrassing silence." # [39]
            $ lauren_love -= 5  # Penalty for mess up
            jump post_meal_talk

label post_meal_talk:

    scene black
    with fade

    "After the meal, I took the dishes to the kitchen and washed them." # [39]
    "With that done with, the two of us returned to the sofa and sat down before the smart TV." # [39]

    scene home_night
    show lauren at lauren_convo
    with fade

    mc "Go ahead, you can choose something that you like now, the remote controller is in your hands." # [40]
    lauren "…Right." # [40]
    "Lauren scrolled down the list of movies for quite a while, until she stopped the selecting box over one piece in specific." # [40]
    mc "The Weird Girl… Do you want to see it?" # [40]
    lauren "…I'm not sure." # [40]
    mc "Why is that?" # [40]
    lauren "When they make a movie about a girl not fitting in with those around her, there's a 50 percent chance that the plot will revolve around her changing completely." # [40]
    lauren "Her clothes, hair, voice, the topics she talks about, her mannerisms." # [41]


    lauren "I… Don't like this sort of movie." # [41]
    lauren "Do you like them, [player_name]?" # [41]

    menu:
        "I don't like them either.":
            label test_choice_04jko:
            mc "If the other characters don't like her how she really is, then they should just go away and leave her alone." # [41]
            lauren "…" # [42]
            lauren "You're right. I think just the same." # [42]
            lauren "But I'm surprised. I didn't think you'd agree with me." # [42]
            mc "What do you mean?" # [42]
            lauren "I mean… You've been changing, [player_name]." # [42]
            lauren "Becoming more confident, talkative, direct. I thought you had decided that everyone should change." # [42]
            mc "…You shouldn't try to fix what isn't broken." # [42]
            lauren "Does this mean…" # [42]
            lauren "No, I'm sorry. You're right." # [42]
            $ win_sound()
            $ lauren_love += 5
            jump lauren_feelings_talk
        "I like them.":
            label test_choice_wc522:
            $ lose_sound()
            lauren "…Of course you do." # [43]
            lauren "You've been trying so hard to change lately, right?" # [43]
            mc "Haha, I-Is it that obvious?" # [43]
            lauren "It is. And let me tell you this, [player_name]…" # [43]
            lauren "You'll fail." # [43]
            mc "Eh…? W-What?" # [43]
            lauren "You'll never get better. You'll never improve. No one will ever love you." # [43]
            mc "Lau…ren…?" # [43]
            lauren "And if you think I have ever harbored any feelings for you, you couldn't be further from the truth." # [43]
            lauren "I never loved you, [player_name]. And I never will love you." # [43]
            lauren "But you're right about something: you need a change." # [43]
            lauren "I'd recommend playing crosswords on your wrists. If you're lucky enough, you might get the right answer for you on your first try." # [43]
            lauren "Let me give you a tip: five letters, and happens to everyone eventually." # [43]
            mc "T-That's a bit-" # [43]
            lauren "It's not too much… for you." # [43]
            lauren "I'm out now. I don't need to hear any more of your crap." # [43]
            "Just like that, Lauren called our date off early and went away." # [44]
            jump skip_here_2

label lauren_feelings_talk:
    mc "This isn't about the movie, is it?" # [45]
    lauren "…" # [45]
    mc "Lauren, do you hate yourself?" # [45]
    lauren "Everyone else sure seems to hate me… so why shouldn't I?" # [45]
    mc "I don't hate you." # [45]
    lauren "You don't really mean it…" # [45]
    mc "How could I prove to you that's not really the case?" # [45]
    lauren "…T-Tell me all that you love about me, then." # [46]
    mc "What?" # [46]
    lauren "If you want to prove to me that you don't hate me… tell me what you love about me." # [46]
    mc "Alright." # [46]

    menu:
        "Your voice.":
            label test_choice_e0n4b:
            lauren "But… I speak so weirdly." # [46]
            lauren "Whenever I open my mouth… I have to go all over the dialogue I'm about to have in my head." # [46]
            lauren "I just can't bring myself to… speak so confidently as everyone else." # [47]
            lauren "…And few are the ones with the patience to wait for me to get ready to speak." # [47]
            mc "Well, if you showed a Luthier Stradivarius around, most people would say it's just a normal violin." # [47]
            mc "You mean so much, Lauren… to me." # [47]
            lauren "…!!" # [47]
            $ win_sound()
            $ lauren_love += 5
            jump mc_broken_talk
        "Your big toes.":
            label test_choice_o8t4t:
            $ lose_sound()
            lauren "What…?" # [47]
            mc "D-Din't you like the compliment?" # [48]
            lauren "I know that I'm not a girl who fits in as well as other…" # [48]
            lauren "But even I know that was a weird as hell compliment, [player_name]." # [48]
            mc "Sorry, I just wanted to make you smile, I thought it would be a funny thing to say. You know, since you mentioned liking comedy and all." # [48]
            lauren "…It subverted my expectations, I'll give you that." # [48]
            $ lauren_love -= 5  # Penalty for mess up
            jump mc_broken_talk
        "Your cold bloodness.":
            label test_choice_fvne4:
            $ lose_sound()
            lauren "…I'm not cold-blooded." # [48]
            mc "You look like you are. I can't ever tell what's going on in your head, haha." # [48]
            lauren "…I'll probably have nightmares about this attempt of you to compliment me, [player_name]." # [48]
            mc "Damn, was it that bad?!" # [48]
            $ lauren_love -= 5  # Penalty for mess up
            jump mc_broken_talk

label mc_broken_talk:
    lauren "[player_name]…" # [48]
    mc "Yes?" # [48]
    lauren "You're trying to change, right? That's what you implied with not fixing what isn't broken." # [48]
    mc "…Yeah." # [49]
    lauren "But… You aren't broken, [player_name]. Not to me. You have never been." # [49]
    lauren "I've always wanted to help people... to heal their pain..." # [49]
    lauren "Maybe that's why I'm drawn to you... I want to take care of you."
    lauren "I actually volunteered at the campus health clinic last semester..."
    lauren "I love the feeling of helping others feel better."
    
    menu:
        "That's really admirable of you":
            label test_choice_ixkdr:
            lauren "Thank you... not many people appreciate that side of me."
            lauren "I even kept the volunteer uniform they gave me..."
            lauren "It made me feel like I was really making a difference."
            if lauren_love >= 45:
                lauren "What do you think drives people to heal and comfort others?"
                jump outfit_13_puzzle
                label outfit_13_puzzle_success:
                    lauren "That's what I felt wearing that nurse uniform..."
                    lauren "Like I could really take care of people who needed it..."
                label outfit_13_puzzle_failure:
                    lauren "I just want to help people feel better..."
        "You have a caring heart":
            label test_choice_4xj81:
            lauren "Thank you... that means everything to me."
    mc "I am broken, Lauren. Because…" # [49]
    menu:
        "I had never made a move on you until now.":
            label test_choice_mp11z:
            lauren "[player_name]…!" # [49]
            lauren "I… I…" # [49]
            lauren "If that makes you broken, then the same applies to me." # [49]
            lauren "After all, I have never… even though what I feel for you is…" # [49]
            mc "Yes?" # [49]
            $ win_sound()
            $ lauren_love += 5
            jump lauren_confession
        "I can't stop thinking about sex.":
            label test_choice_0ab6g:
            $ lose_sound()
            lauren "Well, that's…" # [50]
            lauren "Expected from a man of your age, I guess." # [50]
            mc "Haha, yeah, except I'm having a hard time getting the pussy that I want so much." # [50]
            lauren "No comments." # [50]
            lauren "*Sigh." # [50]
            lauren "And to think that, for a guy like this I…" # [50]
            mc "Hm?" # [50]
            $ lauren_love -= 5  # Penalty for mess up
            jump lauren_confession

label lauren_confession:
    lauren "[player_name], I have to tell you something." # [50]
    mc "What is it?" # [50]

    # Different intros to Lauren's confession based on first date outcome
    if lauren_outcome_episode_1 == "worst":
        lauren "I know things between us…" # [50]
        lauren "Didn't really go that well the first time we met after so long…" # [51]
        lauren "Both of us had a lot of things in mind, for sure." # [51]
        mc "Y-Yeah, of course…" # [51]
        mc "It wasn't a good moment, I was still a bit shaky from the breakup and all." # [51]
        lauren "And I was just… confused. I didn't know how to react when meeting you after so long." # [51]
        lauren "But that doesn't matter now. I'm no longer confused. What happened here today solidified my opinion of you definitely." # [51]
        mc "And… what is that opinion?" # [51]
    else: # Neutral, good or best result on first date
        lauren "I know I may have behaved a bit… unsightly on our first date." # [51]
        lauren "But that was just because I was so nervous when meeting up with you after so long." # [51]
        mc "Haha, come on, Lauren, don't worry, I had lots of fun that day." # [52]
        lauren "It's alright, I… didn't know what to do when I saw you for the first time after so long." # [52]
        lauren "But now I do." # [52]
        mc "You do?" # [52]
        lauren "Yes…" # [52]

    lauren "[player_name], I…" # [52]

    if lauren_love >= 40:
        jump sex_scene_69
    elif lauren_love >= 35:
        jump sex_scene_69
    elif lauren_love >= 30:
        # Neutral result
        lauren "After thinking about our relationship and what I feel for you…" # [52]
        mc "*Gulp!" # [52]
        mc "Y-Yes…?!" # [53]
        lauren "I understood that what I really feel for you is…" # [53]
        mc "Y-YES?!" # [53]
        lauren "A strong sense of respect and appreciation. You're a good friend, after all. You have always been, even if you messed up sometimes." # [53]
        mc "Oh…" # [53]
        mc "I... I see." # [53]
        jump skip_here_1
    elif lauren_love >= 25:
        # Bad result
        lauren "What I have to tell you is…" # [53]
        mc "Yeah?" # [53]
        mc "(Hehe, here we go, boy! My dick is already throbbing, let's go, I'm ready!)" # [53]
        lauren "I fucking hate you, after all." # [53]
        mc "…What?" # [54]
        lauren "I just want to let you know that I fucking hate you. And I'm saying all of this so quickly because I don't even need to think too much about it, that's how certain I am of this affirmation." # [54]
        mc "But… But why?!" # [54]
        lauren "Do you want me to write you a fucking list? Why don't you use that head of yours at least once in your life and think about it yourself? Or are you too stupid to do even this simple task?" # [54]
        mc "No- Wait- P-Please, this can't be-" # [54]
        lauren "It is real, and this is happening right now. Now listen here." # [54]
        lauren "As soon as I get out of here, I'm going to let everyone know that every rumor [girl_friend] spread about you is true, and I'll even add to the story she told everyone about you." # [54]
        lauren "She told everyone you used to cum on your own food and eat it? Well, I'm going to say your favorite meal is dog food too." # [54]
        mc "WHAT?!" # [54]
        lauren "She told everyone that you were a submissive cuckold? Well, I'll add that you begged me to spit on your face and step on your balls too." # [55]
        mc "What the fuck, that's a lie!" # [55]
        lauren "Having gotten to know you and how pathetic you truly are? Honestly, I bet most of these things would, eventually, become true anyway." # [55]
        lauren "Now, please, never again contact me. If you try to do that, I'll tase you, strip you naked, and shove up a dildo in your asshole in plain daylight in the middle of the street." # [55]
        mc "You fucking…!" # [55]
        lauren "I hope you choke up on dog food and die, [player_name]. This is the end of anything that ever existed between the two of us." # [55]
        jump skip_here_2
    else: # lauren_love < 25 (Worse result)
        lauren "What I want you to know is…" # [56]
        lauren "How do you think my feet taste?" # [56]
        mc "…What?" # [56]
        lauren "Are you too stupid to understand such a subtle request? In this case, let me put it in a way that your deficient mind will comprehend me: kiss my feet, vermin." # [56]
        mc "What? No, I- I'm supposed to be the bull!" # [56]
        lauren "Do it right now, you vermin! Or I'm going to call Justin, your ex's new boyfriend, to fuck me in front of you right here right now!" # [57]
        mc "N-No way?! That guy?!" # [57]
        lauren "You better not test me, [player_name]…" # [57]
        mc "A-Alright! Alright, I got it, I'll do it, okay? Just… save me from this humiliation…" # [57]
        "I got on my knees and held her foot, but that didn't seem good enough to Lauren, apparently." # [57]
        lauren "No, not like that. I want to see you on all fours." # [57]
        mc "Kuh…!" # [57]
        "I lowered myself even more, so much so that I could feel my pride getting dragged in the mud." # [57]
        "Then, I picked up her foot and kissed it. But just in time…" # [57]
        "Ka-tch!" # [57]
        mc "Eh? D-Did you just take a picture of me kissing your foot?" # [58]
        lauren "Yes, and I'm posting it on social media with the caption 'he asked me to treat him like the dog he truly is'." # [58]
        lauren "Now, let's continue to part 2…" # [58]
        "Lauren pressed a button on her phone and turned it at me once more." # [58]
        lauren "Tell me that you want to be hard fucked in the ass like a little bitch." # [58]
        mc "N-No way! I'd never-" # [58]
        "Though I wished to die before saying such a humiliating thing, though I'd rather have both legs broken… Lauren's stare carried a threat much greater than physical damage." # [59]
        "And so, I lowered my eyes, and…" # [59]
        mc "I-I want to be fucked in the ass like a little bitch…" # [59]
        lauren "By whom?" # [59]
        mc "…" # [59]
        lauren "Say his name." # [59]
        mc "Eh… Mi-?" # [59]
        lauren "No. It starts with 'J', you know it." # [59]
        mc "Kuh…!" # [59]
        mc "I-I want to be fucked in the ass like a little bitch by Justin!" # [60]
        lauren "Why?" # [60]
        mc "B-Because…" # [60]
        "I had no instructions from Lauren, but my mind worked on its own to come up with the most self-degrading thing I had ever spoken." # [60]
        mc "Because when I saw him fucking my girlfriend and cuckolding me, I grew so jealous of her!" # [60]
        lauren "…Holy shit." # [60]
        "Lauren turned off her phone." # [60]
        lauren "…" # [60]
        lauren "At this point I can't even feel angry at you anymore. Just… sad. Not for you, but for your poor mother, who had to gestate such a shameful… creature in her belly for nine months." # [60]
        lauren "You should be ashamed for being born." # [60]
        lauren "Getting back home, I'll upload this video to my social media too. And you should seriously consider committing suicide." # [60]
        jump skip_here_2


label sex_scene_69:
    # (69 scene) # [52]
    lauren "I love you." # [79]
    lauren "I love you so, so, so much…" # [79]
    lauren "I want to have you, no matter what it takes. I'll do anything you want me to." # [79]
    mc "Anything…?" # [79]
    lauren "*Gulp!" # [79]
    lauren "Yes…" # [79]
    "I placed my hands on her shoulders…" # [79]
    "And my lips on her lips." # [79]
    "As we exchanged sighs and saliva, our bodies telling each other so much more than words could ever transmit…" # [79]
    # (scene with you eating Lauren) # [79]

    stop music fadeout 1.0
    scene scene_9_initial
    with fade
    
    $ persistent.scene_9 = True

    "Soon, we found ourselves naked, and with our faces positioned right against each other's genitals." # [79]
    mc "What a beautiful pussy you have, Lauren." # [80]
    lauren "T-Thank you." # [80]
    mc "I don't want to let these lips stay jealous of your mouth, though. They deserve a little kiss too." # [80]\

    scene scene_9
    
    "I followed up my promise by placing my lower lip right against her clit, and thrust my tongue into her pussyhole." # [80]
    $ play_vagina_insertion_sound()
    lauren "Nghn! Nghnn!" # [80]
    $ play_woman_pleasure_sound()
    "I moved my jaw, eating her juicy, wet pussy away, teasing her hardened clitoris and playing with her inside with my tongue." # [80]
    $ play_vagina_insertion_sound()
    lauren "Gahn! Ughnn…!" # [81]
    $ play_woman_pleasure_sound()
    "Every time my taste buds scraped her vaginal walls, I felt her thighs and ass shaking and tensing up against my hands, and each of her moans sounded just a bit louder than the last." # [81]
    lauren "Aaghn! Hu-Huunn…!" # [81]
    $ play_woman_pleasure_sound()
    "And as I ate Lauren's pussy, she also sucked me off, and each time she brought her throat down my cock, her body moved on my tongue and lips, and she felt even more pleasure from my blowjob." # [81]
    $ play_blowjob_sound()
    lauren "Guhn! Kughn…!" # [82]
    $ play_woman_pleasure_sound()
    mc "(I can feel her heartbeat through my tongue, and she's simply going crazy…)" # [82]
    mc "(God, I love this.)" # [82]
    mc "(This girl just promised to do anything for me, and now I'm eating her pussy as she sucks me off…)" # [82]
    mc "(I've never been harder in my entire life!)" # [82]
    mc "(This is completely different from when that bitch [girl_friend] made me suck her, I'm in complete control right here!)" # [82]
    mc "(And knowing this, that I'm the one to make the calls here… It only makes me more excited!)" # [82]

    scene scene_8
    with fade
    
    $ persistent.scene_8 = True

    lauren "Kughn!" # [82]
    $ play_woman_pleasure_sound()
    "My cock twitched in Lauren's mouth so violently that I almost escaped from her lips." # [82]
    "She moved like a bubblehead, taking my dick deep inside her mouth, running her tongue all over my glans." # [83]
    $ play_blowjob_sound()
    mc "Argh…!" # [83]
    $ play_man_pleasure_sound()
    "Her saliva leaked off her lips and ran down my shaft, still hot, and her moving mouth squelched and squirted, pleasing not only for my dick, but my ears too." # [83]
    $ play_mouth_sound("SALIVA")
    lauren "Nghn! Nghn! Nghn!" # [83]
    $ play_woman_pleasure_sound()
    "Lauren's tits rubbed against my abs whenever she lowered her head, and I could feel her soft breasts brushing against my skin like delicate silk." # [83]
    lauren "Nghnn! Aaghnn!" # [83]
    mc "Ughn! Aargh!" # [83]
    "And each time her tits touched my abdomen, her nipples hardened, turned more sensitive, and she splashed more sweat and natural lubricants over me." # [84]
    "The more she sucked me off, the more the two of us grew excited." # [84]
    mc "(Telling me that she would do anything for my sake, and then quickly getting naked and sucking me off…)" # [84]
    mc "(Honestly, that bitch ass [girl_friend] could learn a couple of things from her!)" # [84]
    mc "(That's how a girl should really behave! She should be down to suck me off whenever, to follow my every wish!)" # [84]
    "The more I relished in my power over that awkward, and now completely enticed Lauren, a lonely girl who'd follow me to Hell and back- no, someone who I could drag to hell and back by her hair, and she still thank me for that…" # [84]
    "The more my cock twitched, splashed precum, and throbbed hard." # [85]
    lauren "Ughnn! Ughnn! Aaghnn!" # [85]
    "Her mouth was delicious, more than just delicious, brain-melting…" # [85]
    "But I needed more. So much more." # [85]
    lauren "Hmm! Hmm! Aghnn!" # [85]
    $ play_woman_pleasure_sound()
    $ play_blowjob_sound()
    "As the fire inside of Lauren burned brighter, hotter, she tried to take more and more of my dick inside her mouth…" # [85]
    "And I could listen to her moans growing louder as her hardened nipples send shivers of pleasure up her spine whenever they brushed against my skin." # [86]
    mc "(I see, I'm not the only one getting stocked by this.)" # [86]
    mc "(She's eager for more just as I am. She's eager to be USED, to be FUCKED HARD.)" # [86]
    mc "(And I'll give her just what she wants.)" # [86]
    "I paid close attention to every signal that Lauren's body gave, and waited until just the right moment, just as she was about to climax, so I could finally…" # [86]

    scene scene_8_final
    play sound "ES_Female, Gasp 02 - Epidemic Sound.mp3"
    with fade

    lauren "Ah! W-Wait!" # [86]
    lauren "AAAGHNNNNN!!" # [86]
    $ play_woman_pleasure_sound()
    $ play_vagina_insertion_sound()
    "With one last skillful use of my tongue, I got Lauren to cross the line, and her whole body shook." # [87]
    "Her nectar tasted so much sweeter, then." # [87]
    "I untangled myself from her, her eyes showing off all the pent-up heat she could barely contain, the need for just a little further push, her mind and body standing at the very edge." # [87]

    jump skip_here_1

label skip_here_1:

    scene home_night
    show lauren at lauren_convo
    with fade

    "After cleaning up the mess, Lauren and I stood before one another by the exit door, the two of us with silly smiles on our faces." # [62]
    mc "So, uhm… I-I hope you had fun today. I certainly had." # [62]
    lauren "I did. Believe me." # [62]
    lauren "[player_name]…" # [62]
    mc "Yeah?" # [62]
    lauren "I… Just want to let you know one more thing." # [62]
    mc "What is it?" # [63]
    lauren "I… am fine now." # [63]
    lauren "After spending time with you, I realized that I don't need to… fix anything about myself, after all." # [63]
    lauren "If ain't broken, don't fix it, right?" # [63]
    mc "That's right. And I'm glad that you finally realized it." # [63]
    lauren "And there's something more…" # [63]
    mc "Yeah?" # [63]
    lauren "I don't know how much you want to change, where exactly you want to get to, but… You're on the right path, [player_name]." # [63]
    mc "Thanks. Really." # [63]
    jump skip_here_3

label skip_here_2:
    "I waited on the sofa, staring down at my own two feet while Lauren went away." # [63]
    mc "…" # [64]
    mc "Goddammit!" # [64]
    bull_phone "Are you angry?" # [64]
    mc "Of course I am, fuck! This was a disaster!" # [64]
    bull_phone "Good that you know it… and good that you feel enraged." # [64]
    bull_phone "You better channel all of this frustration into your own self-improvement, then." # [64]
    mc "Self-improvement?" # [64]
    bull_phone "Of course! If she was this bitchy with you, it only means you have yet another reason to get better, right? Another person to prove wrong about you." # [64]
    mc "…You're right. I can't let things end like this." # [65]
    jump skip_here_3

label skip_here_3:

    scene home_night
    $ update_character_state("mc", CharState.HAPPY)
    show mc at mc_convo
    with fade

    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate

    bull_phone "Hehehe, it seems like I'm no longer the only one seeing potential in you, mc." # [65]
    bull_phone "You're starting to get the hang of this…" # [65]
    bull_phone "And it may be time to take the next big step." # [65]
    mc "The next big step? What is it, do you have someone else in my contact list whom I could call?" # [65]
    bull_phone "Fool! Becoming a real man isn't about lazing around in your room doing nothing but filling up random cumdumps!" # [65]
    bull_phone "If you do that, soon enough you'll run out of girls interested in you, and it'll be practically impossible to find new people." # [65]
    bull_phone "It will be even less likely that you'll ever get your revenge on that bitch [girl_friend] and her son of a bitch of her new boyfriend!" # [65]
    bull_phone "No, your next big step now that you're growing more determined, confident, serious about all of this is…" # [66]
    bull_phone "Go back to college!" # [66]
    mc "C-College…?!" # [66]
    mc "But… Everyone in there thinks that I'm a loser…" # [66]
    bull_phone "That's not true, right? Not EVERYONE in there." # [66]
    bull_phone "If I'm still by your side, it means you successfully got at least a little bit of favor from SOMEONE." # [66]
    bull_phone "And friends defend friends, hehehe." # [66]

    $ update_character_state("mc", CharState.SAD)

    mc "What do you mean?" # [66]
    bull_phone "I mean that I just checked your college internet pages and chat rooms, and your new friends are defending you on them, you know?" # [67]
    bull_phone "They may still be a minority, but it's enough to make people think twice before mocking you." # [67]
    bull_phone "Which means, now is your big debut." # [67]
    bull_phone "Go back to college, and show everyone that you're NOTHING like what your bitch ex-girlfriend describes!" # [67]
    mc "…Yeah. Yeah, right. You're goddamn right!" # [67]
    "I felt a fire burning bright and hot in my heart, and then it wasn't just lust." # [67]
    "There was pride, determination, hope!" # [67]
    mc "I'll go back to college with my head up, and finally start fighting those lies spread by [girl_friend] face on!" # [68]
    bull_phone "Hehehe, that's what I wanted to hear." # [68]
    bull_phone "So you better start making some preparations, right?" # [68]
    bull_phone "You don't want to get back there and fumble all your classes." # [68]
    mc "Of course. I'll get back to studying- no! I'll study like never before for the next week. And when I step back in that classroom…" # [68]
    "When I thought about my classroom at college, at least a few people who had contributed to my tainted reputation came to my mind…" # [68]
    "Professor Benjamin, another one of the men with whom [girl_friend] cheated on me…" # [69]
    "Emma, a popular girl who didn't think twice before stepping on other people so as to get more attention and a better reputation for herself…" # [69]
    "And all of the strangers who repeated [girl_friend]'s lies about me in whispered…" # [69]
    mc "I'll do it, Bull phone. I'll prove everyone wrong." # [69]
    bull_phone "Well, if that's the case, you better get down to it as soon as possible." # [69]
    bull_phone "From what I've read online, your college library requires a reservation to grant entrance, and with tests just around the corner…" # [69]
    mc "You're right. I'll see that through right now." # [70]
    "For the rest of that night, I made a reservation for the library, and researched which books would help me the most to get back to my studies." # [70]
    "Then, after some exercises I went to sleep." # [70]

    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate

    bull_phone "Peep-peep-peep, motherfucker! It's time to wake up!" # [70]
    mc "Guh… can't you wake me up a normal way for once?" # [70]
    bull_phone "I just want to make sure my buddy won't miss his oh-so-important reservation." # [70]
    mc "*Sigh." # [70]
    mc "(Right. He's a bit… alright, REALLY annoying, but this phone wants what's better for me… I think.)" # [71]
    mc "Okay, let's go! I have half a dozen books to borrow." # [71]

    scene university_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade

    "In the college's corridors." # [71]
    "Thankfully, that was a day off for most students, so when I visited the library, I didn't stumble on anyone that I knew." # [71]
    "I had spent the last three hours looking for the books I researched online, and luckily enough, I managed to get all of them." # [71]
    mc "Alright, if I just manage my time correctly, I'll be able to finish them in time for the tests to come!" # [71]

    if lauren_love >= 35: # If you got good, or best results with Lauren in date 2

        scene university_morning
        show lauren at lauren_convo
        play music "ES_You - SRA.mp3" volume 0.2
        with fade

        lauren "[player_name]?" # [72]
        mc "Lauren? Hey, I didn't expect to see you today. Could it be, are you going to the library to get some books too?" # [72]
        lauren "Library…? Are you studying for the tests to come?" # [72]
        mc "Haha, well, yeah." # [72]
        lauren "I see..." # [72]
        lauren "You really… changed." # [72]
        mc "Haha, for better or worse?" # [72]
        lauren "Better… Definitely better." # [72]
        mc "Good. So, about the place you were going right now…?" # [72]
        lauren "Back to my apartment… I just came here to return a book to a classmate." # [72]
        mc "Cool, I'm happy to see you've got new friends already." # [73]
        lauren "Yeah…" # [73]
        lauren "Uhm… [player_name]?" # [73]
        mc "Yes?" # [73]
        lauren "Do you want to… follow me back home?" # [73]
        bull_phone "Even an idiot should know the right answer for this, hehe!" # [73]
        mc "Yes, of course." # [73]

        scene lauren_apartment_morning
        show lauren at lauren_convo
        with fade

        "I followed Lauren back to her apartment." # [73]
        lauren "Bathroom there… Bedroom here…" # [73]
        lauren "Do… you need anything else?" # [74]
        lauren "I have some... special clothes in my closet... costumes and such..."
        lauren "From theme parties and events..."
        
        menu:
            "What kind of costumes?":
                label test_choice_31ze0:
                if lauren_love >= 50:
                    lauren "Well... I have this spooky Halloween one..."
                    lauren "What holiday celebrates mystery and scares?"
                    jump outfit_14_puzzle_apt
                    label outfit_14_puzzle_success_apt:
                        lauren "Yes! Halloween! I love dressing up for it..."
                    label outfit_14_puzzle_failure_apt:
                        lauren "Well... it's for Halloween..."
            "Show me your bedroom":
                label test_choice_dkcwb:
                lauren "O-okay... if you want to see it..."
        mc "Yeah. Yeah, actually I do." # [74]
        "I pulled her closer, and feeling the feverishly hot mood in the air, I planted a deep wet kiss in her mouth." # [74]
        "Our lips only let go of one another briefly and while we took our clothes off." # [74]
        scene black
        stop music fadeout 1.0
        with fade
        mc "Turn around." # [92]
        scene scene_5
        with fade
        $ persistent.scene_5 = True
        "She'd get what she wanted, but the way wanted it, when I wanted it." # [92]
        lauren "Yes!" # [92]
        "She eagerly obeyed me, positioning herself just right to welcome me inside of her." # [92]
        "I grabbed her hair, listening to her irregular respiration and taking a good look at her most precious treasure." # [92]
        mc "Your pussy is so swollen and wet right now… I can see it contracting, as if begging for me to get in already." # [93]
        lauren "I… I…" # [93]
        "I brushed my cock against her wet pussy, mixing up the saliva that coated my member with her natural lubricants." # [93]
        mc "Do you want it?" # [93]
        lauren "Yes! Please! I… I want you inside of me!" # [93]
        lauren "AAAGHNNNN!" # [93]
        "She didn't need to ask twice: I shoved my hips forward and gave her the cock she longed for so much." # [93]
        "And her insides were even better than anything I could have ever imagined." # [93]
        lauren "Gahn! Kaaghnn!" # [94]
        lauren "God! Aah! Ahh! Y-You're splitting me in half! Ughnn!" # [94]
        lauren "T-This pleasure… Ughnnn!" # [94]
        lauren "It's like you're scrambling my brains with your cock, mc! Aaghnn!" # [94]
        "She wasn't lying, I could tell by the way her pussy squeezed my dick, the way her vaginal walls pulled me in deeper and deeper, how her body involuntarily was trying so hard to milk my dick off." # [94]
        lauren "Gahnn! Aaaghn!" # [94]
        lauren "[player_name]! Aghn! I-I can't keep living on without you! Not any longer!" # [94]
        lauren "I can't keep living on without feeling this dick inside of me every day! Aaah!" # [94]
        mc "Hehe, it seems you're no longer that slow talker, hu?" # [94]
        lauren "Ughnn! H-How could I be? When you're fucking me this hard, this fast, I… I'm out of my mind! I can't even think once about what I'm saying, much less twice!" # [95]
        mc "Good, I like it this way, obedient to this dick of mine." # [95]
        mc "Keep behaving like this, like a good girl, and I'll make you feel really good." # [95]
        lauren "I-I will! I'll be a good girl! Aagh! Ughn!" # [95]
        lauren "I-I'll give you whatever you want, w-whenever you want! Ughnn! Aagh!" # [95]
        mc "Hehehe, is that so? And why are you so well-lbehaved all of a sudden?" # [95]
        lauren "Because I love your cock!" # [96]
        lauren "Aah! I love the way you throb inside of me, and how you push my lips aside! Ughnn! W-When you get in and out… my mind goes blank! Aahh!" # [96]
        mc "Good! Good!" # [96]
        mc "Saying these dirty things when your pussy feels so good…" # [96]
        mc "You squeeze me so hard with your wet pussy, you throw your hips against mine so wildly, you moan so deliciously…" # [96]
        mc "You deserve a reward. And here it here it comes!" # [96]
        scene scene_5_final
        with fade
        lauren "Aaaguhnn!" # [96]
        "Lauren came, and even harder than the first time." # [96]
        mc "Kurgh…!" # [96]
        "And so did I." # [96]
        "For a moment, we were one…" # [96]
        "And I wished that brief moment would never end." # [96]        "But everything comes to an end, and with nightfall, I found myself getting dressed back up, and then saying goodbye." # [74]
        scene lauren_apartment_night
        show lauren at lauren_convo
        with fade
        lauren "Bye, [player_name]… It was fun." # [74]
        mc "It sure was. Goodbye, Lauren. Give me a call if you need anything." # [74]
        lauren "You too." # [74]
        "Standing there, looking at her flushed face, my heart skipped a bit, even though I had just filled her up not long ago." # [74]
        mc "(This isn't good, I must get back home and focus on my studies!)" # [75]
        "I waved goodbye, gave Lauren my back, and walked back home." # [75]
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.SAD)
    with fade
    "Returning to my own bedroom, I placed the books I had borrowed on my desk, sat down, and started reading through them." # [75]
    mc "Damn, I can't barely understand any of this…" # [75]
    show bull at bull_convo
    with pixellate
    bull_phone "Well, you lost MONTHS worth of classes while stuck in here, after all." # [75]
    mc "*Sigh." # [75]
    mc "I guess you can't possess my body to make me study hard, can you?" # [75]
    bull_phone "Hahaha! Why would I do such a thing? No, the boring part is entirely your responsibility." # [75]
    bull_phone "Actually, why you're at this…" # [76]
    bull_phone "*Yaaawwnn!" # [76]
    bull_phone "I'm going to sleep. G'night!" # [76]
    mc "Selfish phone…" # [76]
    if lauren_love >= 40: # If you got a perfect 1st and 2nd date with Lauren
        "The more I read the lines printed on the books before me, the more I got distracted." # [76]
        "I relived everything that I had gone through that far." # [76]
        "Especially the events with Lauren." # [77]
        mc "Lauren…" # [77]
        "I looked at my phone, asking myself if she was feeling the same at that time of the night too." # [77]
        "Part of me even expected a message from her." # [77]
        mc "Hehe, how silly-" # [77]
        play sound "ES_Knocking On The Inside - Epidemic Sound.mp3"
        "*Knock, knock, knock!" # [77]
        mc "Eh? There's… someone at the door?" # [77]
        "Curious, yet cautious, I went to investigate the mysterious late-night visitor." # [77]
        scene home_front_night
        show lauren at lauren_convo
        play music "ES_You - SRA.mp3" volume 0.2
        with fade
        lauren "Hi…" # [77]
        mc "Lauren?! What are you doing here at this time?" # [77]
        lauren "I… I…" # [77]
        lauren "I couldn't hold myself back, mc!" # [78]
        "She practically jumped on me, kissing me just as passionately as I had done to her at her apartment." # [78]
        lauren "I need you… More than ever!" # [78]
        mc "Then you came just in time." # [78]
        lauren "What?" # [78]
        mc "I was thinking about you too." # [78]
        scene scene_6
        stop music fadeout 1.0
        with Fade(0.5, 0.5, 0.5)
        $ persistent.scene_6 = True
        lauren "Aah! Aghnn!" # [87]
        lauren "T-This is intense! Too intense! Way too intense!" # [87]
        lauren "Aaghnn!" # [87]
        lauren "I can feel you… so deep!" # [87]
        lauren "You're crashing against my very uterus!" # [87]
        lauren "I…! I…! I am…!" # [87]
        lauren "I'm cumming!!!!!" # [87]
        lauren "Aaaaghhh!!" # [87]
        "As I thrusted into her hole from her backside, I felt Lauren's body tensing up in its entirety, her vaginal walls squeezing me than a juicer, thirstier for my seed than a desert for water." # [88]
        lauren "Gahn?!" # [88]
        mc "But I'm not done just yet!" # [88]
        "As I told her, I kept thrusting forward, fucking her nonstop even through her climax." # [88]
        "And with each thrust, she seemed to reach higher highs, new levels of pleasure that she didn't even know existed." # [88]
        lauren "God! Aaagh!" # [88]
        "Her moans were liking the singing of a siren, her face melting from pleasure, hypnotizing, and her body…" # [89]
        mc "Fuck, you're way too hot! I want to make my cock's house out of this pussy of yours!" # [89]
        "Lauren wasn't the only one feeling like her spirit was being raptured: after each second that passed by during that activity, my balls grew heavier, my heart beat faster," # [89]
        "and my lungs struggled to supply enough oxygen to my body, which was being taken to its limit." # [89]
        lauren "Yes, yes! T-This pussy belongs to your cock! This hole is your cock house! It should always find its way inside of me, forever!" # [89]
        mc "Do you like this warmth inside of you that much, eh?" # [89]
        lauren "Yes! Aaghn! I LOVE it!" # [89]
        mc "Then, I'll give you something to keep inside for a lot longer after we're done!" # [89]
        mc "Arrgh! It's coming! Your parting gift!" # [89]
        lauren "Yes, yes, please! I-I want my parting gift! I want to feel your warmth inside for much, much longer!" # [89]
        mc "It's… coming…!" # [90]
        scene scene_6_final
        with fade
        mc "AAARGHHH!!!" # [90]
        lauren "Hyaaaghnnn!!!" # [90]
        "With one last thrust, pushing my dick head the closest to her uterus and deepest place, I finally released the weight of the world that I was carrying in my balls." # [90]
        "A whole tsunami of semen flowed out of my dick and washed over Lauren's hole, quickly flooding her to the brim and leaking off her entrance." # [90]
        lauren "Aagh! Aaghnn!" # [90]
        "And at the same time I finally peaked, Lauren climaxed a second time, her womanly parts stimulating my member and getting even more man-milk out of me." # [91]
        lauren "Ughn! Aaghn! Aagh!" # [91]
        lauren "So… much! I feel… so heavy!" # [91]
        "I believe in her, for the life that once weighed me down was now almost entirely out of her, the exception being the white splashes on the ground, the excess which she was unable to contain." # [91]
        lauren "Ah… ah…" # [92]
        lauren "It feels… warm…" # [92]
        mc "I told you." # [92]
        "When we finally came apart, I stood still for a couple of minutes staring at Lauren's twitching shape just like an artist stares at his work once finished." # [92]
        "We were both drenched in sweat, she looked so spent, she didn't seem to have the necessary physical or mental energy to even speak." # [92]
        "And I was pleased." # [92]
        "At the end of it all, I had a beautiful cum-filled Lauren lying on my bed, sleeping soundly…" # [78]
        "But instead of finding myself even more tired and distracted than before, I was re-empowered." # [78]
        mc "I guess I just needed to spend that steam somewhere." # [78]
        mc "Anyway!" # [78]
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    with fade
    mc "Let's focus! I'll read through all this, watch as many video lessons as I can, and I'll ace the test to come!" # [78]
    mc "I'll show everyone I'm not the man they think I am…" # [78]
    mc "But that I'm so much better!" # [78]
    # Single outfit opportunity based on perfect date
    if perfect_first_and_second_date:
        outline "This perfect evening with Lauren was so romantic..."
        outline "I should aspire to be more refined, more sophisticated..."
        outline "A gentleman should dress the part for such special occasions..."
        menu:
            "Reflect on proper gentleman behavior":
                label test_choice_l7yz3:
                outline "What defines a cultured, well-mannered man in formal settings?"
                jump outfit_4_puzzle
                label outfit_4_puzzle_success:
                    outline "I should get a tuxedo for special occasions like this perfect date."
                    outline "Lauren deserves to be with someone who dresses the part."
                label outfit_4_puzzle_failure:
                    outline "Formal occasions require proper attire..."
            "Just enjoy the memory":
                label test_choice_si6iw:
                outline "This perfect moment with Lauren is enough for now."
    # Grant episode 2 completion achievement
    call grant_episode_achievement(2) from _call_grant_episode_achievement
    $ check_love_achievements()

    jump episode_3


label check_game_over:
    if lauren_love <= 10:  # Too many mess ups
        bull_phone "That's it, I give up." # [44]
        mc "W-What do you mean?" # [61]
        bull_phone "I mean that you're helpless, the biggest loser in this whole wide world, [player_name]." # [61]
        bull_phone "Not even I can possibly get you to growl into a proper human being." # [61]
        mc "I am a human being already!" # [61]
        bull_phone "No, you're not. You're not better than a shit-eating fly, honestly." # [61]
        bull_phone "And maybe you like it, eh? The disrespect, the humiliation, the disgust on the face of everyone…" # [61]
        bull_phone "You're the biggest fucking cuckold masochist I've ever seen. You can't even be considered a failure, as that would be an insult to all the failures." # [61]
        bull_phone "I'm out." # [61]
        mc "W-Wait! Bull Phone! D-Don't give up on me just yet! I swear I'll grow better at this! I'll do anything you tell me to!" # [45]
        "I held my phone with both hands, despair filling up my heart, and tears my eyes, and begged for the return of that promised exit from the situation I had found myself in, the rock bottom." # [45]
        "But he never replied... ever again." # [45]
        "And I never again left my bedroom." # [45]
        "Game over." # [45]
        return # End of game
    else:
        bull_phone "Well, you messed up this time, but hopefully you have learned your lesson for when the next time comes around." # [44]
        return # Return to wherever you called from