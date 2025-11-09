# Episode 1 uses centralized points system from points_system.rpy

image hold_hands = At("images/non_sex_scenes/hold_hands.png", ai_zoom)

label park_date:
    scene park_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.AROUSED)
    show screen empty_interactions
    with Fade(0.5, 5.0, 0.5)

    outline "I ask myself how Lauren is right now."
    outline "She used to be really pretty, the reason why I – foolishly – chose [girl_friend] over her was because I was painfully in love with the one who turned out to be a bitch, and also…"

    scene park_morning
    play music "ES_You - SRA.mp3" volume 0.2
    show lauren at lauren_convo
    $ update_character_state("lauren", CharState.NORMAL)

    lauren "Good morning."
    mc "Ah! Good morning, Lauren! You’re early."
    $ update_character_state("lauren", CharState.SAD)
    lauren "I've heard showing up to a date one hour earlier is the polite thing to do."
    lauren "But since you're already here, it seems I failed."
    mc "Haha… well, usually, the man is the one who has to wait, so I wouldn’t call it a failure. Shall we get going?"
    lauren "Indeed."

    "Slowly, I took Lauren to stroll around the park."
    mc "So… how you’ve been?"
    lauren "Good."
    mc "That’s cool, that’s cool. Uhm… And you’ve done anything interesting lately?"
    lauren "I’ve finished a new crossword book."
    mc "Ah… of course."
    outline "Yeah, other than my feelings for [girl_friend], this is the reason why I didn’t choose Lauren: she is just so hard to read! I never know what she’s feeling, or how I should treat her."
    bull_phone "Do not despair yet, dude: however you used to treat her back then, she liked it enough to ask you to date her, right? So, you must have done something right. You just need to look for the clues and try to remember that."

    menu:
        "You must hate small talk, right?":
            label test_choice_0bi3o:
            $ lose_sound()
            lauren "Why do you say that?"
            mc "I mean, you’re all about short answers, yes or no. Am I wrong?"
            lauren "I… like… talking."
            lauren "See? I’m perfectly able to hold appropriately normal conversations."
            mc "I wouldn’t call that normal, but whatever you say, dude."
        "You're looking pretty cute today.":
            label test_choice_fx0sd:
            $ win_sound()
            $ lauren_love += 5
            $ update_character_state("lauren", CharState.HAPPY)
            lauren "…T-Thank you."
            lauren "Uhm… you too. Your attire is fitting of you."
            mc "Thanks!"
            mc "I spent quite a lot of time thinking about what I should wear to see you, haha."
            lauren "…Me too."
        "It’s been years since I last played with crossed words.":
            label test_choice_uwntx:
            $ lose_sound()
            lauren "You used to play with them?"
            mc "Yeah, there was a time when my phone got broken, and so I started to go to the bathroom with a booklet of crossed words."
            lauren "Oh…"
            mc "Yeah, I mean, it’s better than nothing, but when it comes to entertainment, I definitely wouldn’t put it very high on my list."
            lauren "…I see."

    "We were almost leaving the park when I stopped to look at the plant life of the place."
    mc "Still, it’s been so long since we last walked through here together, right?"
    lauren "Yes."
    mc "We were so naïve back then."
    mc "While these trees haven’t changed a bit, to me, it’s almost as if a whole lifetime has passed by, and I’m a completely different person now."
    lauren "…I wish I could say the same."
    mc "What do you mean?"
    $ update_character_state("lauren", CharState.SAD)
    lauren "Even now… I find myself alone in college."
    lauren "I thought I could change. I tried to change. But, in the end, I'm still…"

    menu:
        "Perfect the way you are.":
            label test_choice_13loc:
            $ win_sound()
            $ lauren_love += 5
            $ update_character_state("lauren", CharState.AROUSED)
            lauren "Eh…!"
            lauren "D-Do you really think so?"
            lauren "I mean… we’ve been walking for almost forty minutes, and I have barely spoken anything."
            lauren "I don’t know where to look at, or what to do with my hands."
            lauren "I’m just so-"
            mc "Perfect."
            lauren "…!"
            mc "We were in a place filled with assholes, and that’s why you didn’t have that many friends back then."
            mc "And now I can confidently say that it’s just the same with our college."
            mc "But you’re a nice girl, Lauren."
            mc "You may not speak much, but you also don’t lie, and every word that leaves your mouth is genuine, just like you are."
            mc "You’re a breath of fresh air here, and I wish we had kept contact through everything that has gone on."
            lauren "I…"
            $ update_character_state("lauren", CharState.HAPPY)
            lauren "Thank you. I will use your name to train my calligraphy."
            mc "Haha, sure, that sounds like an honor!"
            $ win_sound()
            $ lauren_love += 5
        "You'll become normal one day.":
            label test_choice_qjnxp:
            $ lose_sound()
            $ update_character_state("lauren", CharState.SAD)
            lauren "Normal…"
            mc "Yeah, yeah. Maybe you’ll be able to hold proper conversations, and have hobbies appropriate for your age and shit."
            mc "If you do all of this, I’m sure you’ll eventually fit in!"
            lauren "…That wouldn’t be me."
            mc "Hey, sacrifices must be made for a good social life."
        "I wish you luck in your transformation.":
            label test_choice_x2g6x:
            $ lose_sound()
            $ update_character_state("lauren", CharState.ANGRY)
            lauren "Luck? I don't even know what I should do, or where I should begin."
            mc "I can help you with that. Do you want me to make a list with everything wrong with you?"
            lauren "No."
            mc "Hey, you’re already improving! See how you answered quick this time? The only mistake of yours now was how short your answer was."
            lauren "I already told you I don’t want you to list everything wrong with me."

    mc "Anyway, it’s still early, so what do you think about going to a coffee shop and eating something?"
    lauren "…Sounds good."

    scene coffee_shop
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    with fade

    mc "This place has some pretty nice vibes, hu?"

    hide mc
    show lauren at lauren_convo
    $ update_character_state("lauren", CharState.NORMAL)
    with fade
    lauren "I like the decoration."
    mc "Good!"
    mc "And have you decided what you want already?"
    lauren "Coffee, black, and a slice of water pie."
    mc "Water pie…"
    mc "I-I mean, cool! I will place our orders then."
    "I placed the orders, and a couple minutes later, our food and drinks arrived at our table."
    mc "The pastries aren’t the best, but the coffee is delicious."
    lauren "The meal contained a substantial quantity of caffeine, sugar, and fats. It was satisfying."
    mc "Is that how you measure the worth of food?"
    lauren "The nutritional value of edibles is the perfect measure of quality."
    mc "I guess you can say so in a way, haha."
    mc "Hey, could it be, your grades at college are really good?"
    lauren "…Average."
    mc "I see. And your course is…?"
    lauren "Nutrition."
    mc "That makes sense. Either that, or piloting giant robots, haha."
    lauren "What?"
    mc "Nothing."
    lauren "I also enjoy... other interests. Like Halloween and spooky things."
    lauren "Most people think that's weird for someone studying nutrition."
    lauren "I also love swimming... there's something so freeing about being in water."
    
    menu:
        "Halloween sounds fun! I love mystery and magic":
            label test_choice_vl662:
            lauren "Really? Most people think I'm weird for liking spooky stuff..."
            lauren "You know, I actually have this old costume from last Halloween..."
            lauren "It's a witch outfit... complete with pointed hat and everything."
            
            if lauren_love >= 15:  # best outcome
                lauren "Since you appreciate the spooky theme..."
                lauren "What do witches create with their cauldrons and spells?"
                jump outfit_12_puzzle
                label outfit_12_puzzle_success:
                    lauren "Maybe... maybe you'd like to see me in the witch costume sometime?"
                    lauren "For Halloween, of course..."
                label outfit_12_puzzle_failure:
                    lauren "Well, I thought you might get it... but that's okay."
            else:
                lauren "Maybe next Halloween you could see it..."
        "Swimming does sound relaxing":
            label test_choice_i5ihq:
            lauren "It really is! There's something so freeing about being in the water..."
            lauren "I have this cute bikini I bought but never had anyone to go swimming with..."
            lauren "What's the best activity for hot summer days in the water?"
            jump outfit_15_puzzle
            label outfit_15_puzzle_success:
                lauren "Maybe we could go to the beach together sometime?"
                lauren "I'd love to show you how much I enjoy the water..."
            label outfit_15_puzzle_failure:
                lauren "I hope we can swim together sometime..."
        "Everyone has different interests":
            label test_choice_u2kjt:
            lauren "Thank you for not judging me..."
            lauren "Most people think I'm strange for liking both nutrition science and spooky things."
    menu:
        "You must be single, right?":
            label test_choice_cweqf:
            $ lose_sound()
            lauren "I MUST be? Why so?"
            mc "Well, haha. Come on. Do I really have to say it?"
            lauren "I’m vexed. [player_name], you’re vexing me."
            mc "Oh. Sorry…"
            lauren "…But I am single, indeed."
        "I doubt you care about love.":
            label test_choice_cbin6:
            $ update_character_state("lauren", CharState.ANGRY)
            lauren "What do you mean by that?"
            mc "I don’t know, you just don’t seem to be the type of person who cares about love."
            lauren "And what would be that type of person?"
            mc "You know, someone like… girly?"
            lauren "…"
            lauren "You must care a lot about love, then."
            mc "D-Did you just call me…"
            mc "(Shoot, have I offended her?)"
        "Have you found a boyfriend yet?":
            label test_choice_sucle:
            lauren "No..."
            mc "Lucky me, hehe."
            $ update_character_state("lauren", CharState.AROUSED)
            lauren "Lucky?"
            mc "You must really be surrounded by idiots, if no one has noticed how great of a woman you are."
            lauren "Woman…!"
            lauren "Y-You think so?"
            mc "I mean, am I wrong? I think you’re quite cute in your own way."
            mc "Plus… well, you’re quite attractive. Very much so, actually."
            lauren "!!"
    $ update_character_state("lauren", CharState.SAD)
    lauren "And- And what about you?"
    lauren "Your girlfriend… [girl_friend]. Do you still love her?"
    menu:
        "I do.":
            label test_choice_1b4q9:
            $ lose_sound()
            mc "Of course I do."
            lauren "…"
            lauren "Then, why haven’t you invited her out today?"
            mc "That’s-"
            lauren "Oh, yes. I almost forgot. It’s because she’s too busy jumping on someone else’s cock right now."
            mc "L-Lauren…?"
            lauren "And maybe I should be doing the same instead of wasting my time here with you."
            lauren "My college life is already hard enough without being associated with a cuckold loser like you anyway."
            lauren "I'd say 'goodbye' to be polite, but maybe 'farewell' is a better word choice."
            jump end_episode
        "I do not.":
            label test_choice_nfv3n:
            mc "Of course I don't."
            mc "I gave her my everything, I chose to believe in her…"
            mc "And she chose to throw it all away and prove me wrong."
            mc "I… I've been thinking about you ever since [girl_friend] and I broke up."
            mc "About the choices that I made. About the mistakes that I committed. And how much happier I could have been."
            $ update_character_state("lauren", CharState.AROUSED)
            lauren "We."
            mc "Hm?"
            lauren "How much happier WE could have been."
            lauren "I, too, have thought long and hard about those days."
            lauren "Asking myself just where I had gone wrong, at what point I messed up."
            lauren "But I- I…"
            lauren "You know me, [player_name]. People are just so hard to understand. One word can have a thousand different meanings."
            lauren "Yes can mean no, love can mean hate, pretty can mean ugly."
            lauren "And it doesn’t matter how hard I study this, I just find it so hard to navigate through these conversations…"
            mc "(That’s why the crosswords, hu?)"
            mc "I know what you mean."
            lauren "Do you?"
            mc "Yeah. After all, I ended up making even myself confused and taking all the wrong choices."
            mc "Lauren, you didn’t do anything wrong. Not now, not back then."
    menu:
        "Yeah, it was disgusting.":
            label test_choice_v5lk8:
            lauren "Oh…"
            lauren "Y-Yes. Disgusting."
            lauren "That’s exactly what I was about to say."
            mc "I mean, right? It was so slimy and cold and stinky..."
            mc "As if it wasn’t bad enough being hated by the whole class for being a nerd, I had to be paired up with the weird g-"
            mc "*Cough, cough!"
            mc "I mean, I hated that day."
            lauren "…Yes. I hated that day too. Being paired with the nerd boy was the worst."
        "Nah, I don’t.":
            label test_choice_92r6v:
            $ lose_sound()
            lauren "I see…"
            lauren "I had fun that day… It’s a shame you don’t remember anything about it."
            mc "Sorry."
            lauren "It’s fine."
        "Yes, it was so fun!":
            label test_choice_rdo12:
            lauren "I agree."
            lauren "Up to that point, I had done everything alone. Even when I ended up in group projects, I was assigned to do everything by myself due to being the ‘weird girl’."
            lauren "But then you stood by my side, and were just so… helpful. Understanding. Careful…"
            lauren "I believe the word for that would be ‘cool’."
            mc "Me? Cool? Haha, thanks."
            lauren "You were cool, [player_name]. You still are."
            mc "You know, I had a similar thought about you that day."
            mc "While we were working together, and I looked to my side and at you, I thought: damn, this girl is cute. And differently from everyone else, she’s not an asshole about it."
            lauren "T-Thank you."
            mc "And I still think the same."
            $ win_sound()
            $ lauren_love += 5
    mc "Anyway, we’ll end up bothering the owners if we stay here for much longer."
    mc "Want to head back to the park? Chill in there, talk for a bit?"
    lauren "Let us."
    scene park_night
    show lauren at lauren_convo
    with fade
    mc "Uhm… Want- Want to hold hands while at it?"
    lauren "…Yes."
    $ update_character_state("lauren", CharState.HAPPY)
    hide lauren
    with fade
    outline "Trying to feign naturality while holding a woman's hand after so long, I took her back to the park with a smile on my face and chit-chatting about anything irrelevant."
    outline "At some point, we found ourselves sitting down on the bench of the park, but still holding each other's hands."
    mc "And then she said: so close, that's actually a shape! Haha."
    # MC Ninja outfit opportunity during stealth moment
    if mc_stealth_points == 0:
        outline "I notice I'm naturally moving quietly, staying in shadows..."
        outline "Almost like I'm developing stealth instincts..."
        menu:
            "Practice moving silently":
                label test_choice_tqz1w:
                outline "What do ninjas use to stay hidden?"
                jump outfit_1_puzzle
                label outfit_1_puzzle_success:
                    outline "My stealth skills are definitely improving!"
                label outfit_1_puzzle_failure:
                    outline "I need to work on my stealth techniques..."
            "Move normally":
                label test_choice_guh0g:
                outline "Just walking casually for now..."
    play sound "ring.mp3"
    "Ring!"
    scene park_night
    show mc at mc_convo
    with fade
    mc "My phone is vibrating. Sorry, I’ll just check this message real quick."
    scene park_night
    show lauren at lauren_convo
    $ update_character_state("lauren", CharState.NORMAL)
    with fade
    lauren "Your phone vibrated? I didn't even notice it."
    $ update_character_state("bull", CharState.ANGRY)
    show bull at bull_convo
    show mc at mc_convo, bull_glow_effect
    stop music fadeout 0.5
    $ update_character_state("mc", CharState.AROUSED)
    play sound "Male, Evil, Gravel Laugh, Male Laughs 02.mp3"
    play music "ES_Moonlight Mystery - Alexandra Woodward.mp3"
    hide lauren
    show mc at mc_convo
    with pixellate
    bull_phone "It’s good you’re enjoying this little date and all, but you haven’t forgotten your mission, have you?"
    mc "I know it, dammit."
    hide bull
    hide mc
    show lauren at lauren_convo
    with fade
    lauren "Are you alright?"
    mc "A-Ah, yes. It was just a spam message. You know it, extended warranty and stuff."
    outline "It’s time already, isn’t that what you wanted to let me know?"
    outline "I must approach the subject already."
    outline "Gulp!"
    mc "You know…"
    lauren "Yes?"
    outline "Shit, I haven’t had this sort of talk with anyone other than my ex-girlfriend before!"
    outline "What should I say?"
    menu:
        "SUCK ME OFF RIGHT NOW!":
            label test_choice_efpfw:
            $ lose_sound()
            mc "SUCK ME OFF RIGHT NOW!"
            lauren "…"
            mc "…?"
            lauren "…"
            mc "J-Just joking! Haha… ha…"
            lauren "Good. Because even a woman madly in love with you would be put off by that sort of speech."
        "Haven't you been feeling lonely lately?":
            label test_choice_ktog5:
            $ update_character_state("lauren", CharState.SAD)
            lauren "I've been mostly focusing on crosswords."
            mc "Yeah, having a hobby is cool, it’s a good thing, and I experimented with it myself too…"
            mc "But what about human warmth?"
            mc "When night falls, and you find yourself in your bed, too mentally tired to distract yourself with anything else, and your mind keeps wondering about everyone and everything else…"
            mc "How do you deal with it?"
            lauren "I… think about the good days."
            mc "Which ones?"
            $ update_character_state("lauren", CharState.HAPPY)
            lauren "The ones we spent together."
            $ win_sound()
            $ lauren_love += 5
        "T-The grass is looking so green, right?":
            label test_choice_ojuau:
            $ lose_sound()
            lauren "Grass is always green this time of the year."
            mc "Yeah…"
            outline "Speaking of grass, is YOUR yard trimmed, or you let it wild?"
            outline "As if I’d be able to say that!"
            mc "*Sigh…"
    mc "Haha."
    lauren "What are you laughing at?"
    mc "it’s just that… You know, after everything that I went through recently, going out with you today was like realizing seeing half of my dreams coming into reality."
    lauren "Just half?"
    mc "Yes. In bed, often I found myself daydreaming about going on a date with you, and that was the first half…"
    mc "In the second half, however…"
    menu:
        "We shook hands and parted ways.":
            label test_choice_hvr6t:
            $ lose_sound()
            lauren "If things continue like this, we’ll probably realize that last part of your dream anyway, so there’s no need to despair."
            mc "Y-Yeah…"
        "We found a frog to dissect again!":
            label test_choice_9v4mf:
            $ lose_sound()
            lauren "[player_name], even if I enjoyed that day…"
            lauren "Going around hunting for frogs isn’t exactly what I consider an especially roman- I mean, interesting meeting."
            mc "Haha, yes, I was… just joking, of course."
        "That's the part when I usually start to jerk off thinking about you.":
            label test_choice_a2fba:
            $ win_sound()
            $ update_character_state("lauren", CharState.AROUSED)
            lauren "*Gasp!"
            lauren "I… Uhm… Well…"
            lauren "By ‘jerk off’, you mean…?"
            mc "I masturbate thinking of you."
            lauren "O-Of course. It’s not like that expression has any other meaning, right?"
            lauren "…We really had good times together, so, I guess that’s not really that weird."
            $ lauren_love += 5
    if lauren_love >= 25:  # 5+ correct choices
        jump date_outcome_best
    elif lauren_love >= 15:  # 3+ correct choices
        jump date_outcome_good
    elif lauren_love >= 10:  # 2 correct choices
        jump date_outcome_neutral
    else:
        jump date_outcome_worst

label date_outcome_best:
    $ update_character_state("lauren", CharState.AROUSED)
    mc "It isn't weird? Really?" 
    mc "Isn’t it weird that, every night I regret not having chosen you, and then beat my meet for hours on end, cumming hard thinking about you being the one to touch me?" 
    lauren "I-I mean… we did have something special." 
    mc "We did, didn’t we?" 
    mc "Then, it wouldn’t be weird if this dream of mine turned into reality either, right?" 
    lauren "I don’t understand, [player_name]…"
    mc "I want you to jerk me off right now." 
    $ update_character_state("lauren", CharState.AROUSED)
    lauren "Eh?!"
    mc "We have something special, don't we?"
    lauren "…"
    mc "We do." 
    "Taking a look around and confirming that there was no one around, I unzipped my pants, and let my cock spring up, already half chubby from all the dirt talk." 
    mc "Then, go ahead. Let us DO something special too." 
    lauren "Wha-What should I even…?" 
    mc "Suck me off." 
    lauren "Suck…"

    scene black
    show scene_4_initial
    stop music fadeout 1.0
    with fade

    "Lauren took off her shirt, lied down, and gobbled up my dick, wrapping her lips around it voraciously."
    mc "Good girl, I'll fuck your mouth now."
    $ play_man_pleasure_sound()

    scene black
    show scene_4

    lauren "Hmm, hmm…" 
    $ play_woman_pleasure_sound()
    $ play_blowjob_sound()
    mc "Aah. That's right."
    $ play_man_pleasure_sound() 
    mc "Can you feel a different taste now? That's my pre-cum filling up your mouth. It means you're doing a good job. Keep going." 
    lauren "*Suck, suck, suck..." 
    $ play_mouth_sound("SUCK")
    lauren "*Slurp, slurp, lick!" 
    $ play_mouth_sound("SALIVA")
    mc "Aagh…"
    $ play_man_pleasure_sound() 
    mc "You're pretty good with your mouth. Could it be, you've been thinking about this too?" 
    lauren "Uhm-hm." 
    $ play_woman_pleasure_sound()
    $ play_blowjob_sound()
    lauren "Mufu-fuh, ughn- fuhn…" 
    $ play_woman_pleasure_sound()
    mc "Haha, I can't understand a think of what you say when you have my dick in your mouth, but it feels nice when you try to speak." 
    $ play_man_pleasure_sound()
    mc "I guess you've been touching yourself every night thinking about me, right? About this moment." 
    mc "You lay on your bed, close your eyes, and imagine that boy on who you had a crush getting inside of you, spreading that tight wet pussy of yours." 
    mc "Damn, I should have fucked you ages ago." 
    lauren "Nghnn…!" 
    $ play_woman_pleasure_sound()
    "Either growing more confident in her skills or reckless due to extreme excitement, Laure's tongue started to work together with her mouth, complimenting her lips and throat work." 
    lauren "Suck, suck, suck, slurp!" 
    $ play_mouth_sound("SUCK")
    $ play_blowjob_sound()
    "(Lauren sucks and slurps.)"
    "Her heard bobbed up and down faster, splashing saliva and precum all around." 
    $ play_mouth_sound("SALIVA")
    mc "Fuck, you must have dreamed of the day you'd be able to suck me off like this, didn't you?" 
    $ play_man_pleasure_sound()
    lauren "Uhm-hm! Uhm-hm!"
    $ play_woman_pleasure_sound() 
    "The suction noises, her breathin, our heartbeat, everything grew immensely louder." 
    $ play_woman_breathing_sound()
    $ play_blowjob_sound()
    lauren "Cock… [player_name]'s cock…!"
    $ play_woman_pleasure_sound()
    "With each piston-like movement Lauren executed with her neck, I spilled more pre-cum, and wettened her lips and face even further, she glided across my length more easier, more pleasing." 
    $ play_mouth_sound("SALIVA")
    mc "Aagh!" 
    $ play_man_pleasure_sound()
    mc "Fuck, Lauren, you may not be that good with people, but you certainly are with dicks!"
    $ play_man_pleasure_sound() 
    mc "(I can’t believe I’m doing this in the middle of the park.)" 
    "(I can’t believe I’m doing this in the middle of the park.)" # Narration for internal thought
    mc "(If someone come around…!)" 
    "(If someone come around…!)" # Narration for internal thought
    mc "Holly…!" 
    mc "Fuck, I almost wish someone would actually come around and catch us like this!" 
    lauren "Hyumm!!" 
    mc "Suck me good, Lauren, get me higher than ever, you shameless slut!" 
    lauren "Gyuhnn! Hyum!" 
    mc "Enjoy be called a slut that much, eh?" 
    mc "I might start to treat you as one, then, put those tight holes of yours to good use." 
    lauren "Ughnn! Gyhn!" 
    mc "If you’re getting wet from sucking me off, you have no idea the damage I’d make to that pussy of yours, Lauren..." 
    mc "You’d get addicted to my dick, so much so that sucking me off in public would be the least embarrassing thing you’d be willing to do." 
    lauren "Nghnn! Guhnn!?" 
    mc "Aargh!“" 
    mc "But we got to train them first, right? Make you learn how to behave like my bitch to begin with." 
    lauren "Aaghn… Ughnn…!" 
    $ play_woman_pleasure_sound()
    $ play_blowjob_sound()
    mc "I am- Agh! H-Here it comes, bitch! The meal you worked so hard to get!" 
    $ play_man_pleasure_sound()
    mc "Keep going on like this, and… ughn…!" 
    $ play_man_pleasure_sound()
    mc "I will… cum!" 
    mc "Yes! Faster! J-Just a little more! Agh! Urgh! I-I'm almost there!" 
    $ play_man_pleasure_sound()
    $ play_blowjob_sound()
    mc "Can you feel me throbbing inside your throat? My hardness?" 
    lauren "Hmm! Hm-Aaghn!"
    $ play_woman_pleasure_sound()

    scene scene_4_final
    with fade

    mc "Aah! I'm cumming!" 
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    mc "Aaah!!"
    $ play_man_pleasure_sound()
    lauren "Kyahnn!"
    $ play_woman_pleasure_sound()
    "She pulled her head away from my tired cock, cheeks puffed up, holding all my cum." 
    $ play_mouth_sound("SALIVA")
    mc "Look at you, all sticky in the face." 
    mc "You can't head back home like that, right? Everyone is going to know exactly where that hand has been." 
    mc "I guess you must eat it, then." 
    lauren "Hm?" 
    mc "Eat it. Eat all my cum, swallow it." 
    lauren "…" 
    lauren "*Gulp… Gulp… Gulp…!" 
    $ play_mouth_sound("SWALLOW")
    "Drinking the sperm contained in her mouth, Lauren moved her tongue all around her lips, gathering all the seed that I spilled in them and drinking them too."
    $ play_mouth_sound("SALIVA") 
    "She slurped it all up, until there was nothing else, and seemed quite satisfied not only by what she tasted, but by her good job too." 
    lauren "There." 
    mc "Good girl."

    scene park_night
    show lauren at lauren_convo
    with fade

    $ update_character_state("lauren", CharState.HAPPY)
    lauren "Oh, my god, I-I have to head back home."
    lauren "I just remembered that I have something to do."
    mc "(She definitely just wants to masturbate.)" 
    lauren "Goodbye!" 
    mc "Goodbye Lauren." 
    jump end_episode
    
label date_outcome_good:
    $ update_character_state("lauren", CharState.HAPPY)
    mc "Lauren. I just want to let you know… Thank you. For everything."
    mc "I had lots of fun today, and I really wanted to see you again. For a long time now. I missed you."
    lauren "Me too, [player_name]."
    "We exchanged honest smiles, heart to heart, connected."
    "Even though the one who spoke those words was the Bull Phone and not me, they were honest, and true."
    "We hugged, and it felt natural. It felt good."
    "…But someone wanted to feel better."
    mc "…I’m sorry, I haven’t been completely honest with you."
    lauren "What haven’t you told me, then?"
    mc "I didn’t miss only your presence, Lauren. But also your warmth, your embrace… your body."
    mc "My hands, controlled by an entity much more audacious than myself, moved down Lauren’s back, and over her asscheeks."
    lauren "Nghn!"
    mc "I have been wanting to feel you up for so long, Lauren. Not having done this before is my biggest regret."
    $ update_character_state("lauren", CharState.AROUSED)
    lauren "I… I have been longing for this too."
    "After exchanging glances full of desire, we finally kissed."
    "And my hands got right back to work: lowering her pants, I started to tease her already wet pussy through her panties, rubbing my fingers up and down her slit."
    lauren "Nghn! Hmm…"
    "She may have had difficulties reading people and expressing herself, but at that moment there was no doubt about what either of us was feeling: we were horny."
    "Even through the thin, drenched fabric of her underwear, I could feel her heat, her throbbing, swollen pussy mounds gripping onto my digits, hungry for more."
    lauren "Aughn…!"
    "And those were not the only lips starving for attention."
    "Lauren’s tongue threw itself against my own wildly."
    "She didn’t kiss me as much as she swallowed me, sucking me inside her mouth, as if without me she couldn’t keep living on."
    mc "Hyun! Hyamm!"
    "The bull in control of my body wrapped our tongues around each other’s, bit her lips, held her asscheeks tight and rubbed her good."
    "While I wasn’t in control of my body then, I felt everything which my physical self experienced just as vividly as if I was truly the one master of my being."
    "And it was ecstatic."
    lauren "I-If you keep going- ughn! Gahn!"
    mc "If I keep going, then what?"
    lauren "Then I- I will- Ughnn! Kahnn…!"
    "Her cute expression and voice, and even cuter twitches and jolts only made me move my fingers faster, massage her asscheeks harder."
    mc "You’ll what?"
    lauren "I will… I will…"
    lauren "I will cum!"
    lauren "Hyaaahnnn!"
    "With a final brush of my fingers, her pussy quivered, as well as the whole rest of her body."
    "And in the next moment, she leaned on me, weak."
    lauren "*Panting… Panting…"
    mc "It seems like you got really happy from seeing me today. Good. I promise you, the feeling is mutual."
    "Straightening herself back up, she dressed herself back again."
    $ update_character_state("lauren", CharState.HAPPY)
    lauren "I-I have to go back home. This damp spot is going to show through my pants in no time."
    mc "Haha, I get it. Goodbye, Lauren."
    lauren "Goodbye, [player_name]."
    jump end_episode

label date_outcome_neutral:
    $ update_character_state("lauren", CharState.NORMAL)
    mc "Welp! That was pretty nice."
    "We both got up from the bench and exchanged a half smile."
    lauren "It was mildly entertaining, I guess."
    lauren "But I have to go now, and I imagine so do you."
    mc "Yeah, yeah, I’m, like, super busy back home."
    mc "See you later?"
    lauren "…Maybe."
    lauren "Goodbye, [player_name]."
    mc "Goodbye, Lauren."
    jump end_episode

label date_outcome_worst:
    $ update_character_state("lauren", CharState.NORMAL)
    mc "Lauren, I… need to tell you something."
    "We got up from the bench, and I stepped closer to the girl who once had a crush on me."
    mc "No, I need to DO something with you."
    lauren "Yes, me too. I must do something with you too."
    mc "Really?! Great! We’re on the same wavelength here, then, hehe."
    mc "Then, come here and give me a kiiiiisss…!"
    mc "Guwah-?!"
    "Instead of a peck on my lips, however, what Lauren ended up giving me was a kick on my balls."
    "My breath escaped my lungs, my entrails churned up, and I immediately fell down on the ground, agonizing."
    $ update_character_state("lauren", CharState.ANGRY)
    lauren "I can't believe that I loved you once, [player_name]. I must have been truly desperate."
    lauren "Loneliness is really a poison, it fogs your mind and makes you act strangely."
    mc "W-What are you-"
    mc "Kaah!"
    "Right as I was managing to catch my breath, Lauren stepped on my balls, pressing them between her sole and the hard ground below with such a might, that I felt as if they could explode at any moment."
    "The pain was so intense, I almost felt as if I could faint, and yet, her words were so sharp, they cut through the red veil of agony that paralyzed me:"
    $ update_character_state("lauren", CharState.ANGRY)
    lauren "But I'm thankful for this date today."
    lauren "If not for this, I would have never realized how pathetic you truly are, [player_name]."
    lauren "You’re not a worthless man, but a worthless human being."
    lauren "I despise you, and the highest point of my day today is to see you squirming in agony like the worm you are."
    lauren "…I might even have found a new hobby other than crosswords: seeing you in pain. I ask myself what could I do to make you cry?"
    mc "P-Please… S-Stop…!"
    lauren "Maybe I should look into your life, see if you have a father I can fuck? A rival?"
    outline "Fuck! She won’t stop just because I’m bagging her!"
    lauren "Oh, yes, that douche who stole your girl. I bet he’d be happy to fuck me too, and brag to your whole college about it."
    mc "P-People are coming!"
    lauren "What?!"
    "In the brief moment in which Lauren looked behind her, I crawled into the wild side of the park."
    "She didn’t seem determined enough to follow me through leaves and dirt, and so I escaped."
    jump end_episode

label end_episode:
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with Fade(0.5, 5.0, 0.5)

    mc "*Sigh."
    bull_phone "Tired?"
    mc "Who wouldn’t be? All of this was at least a bit taxing."

    if lauren_love >= 15:
        bull_phone "I get you, I get you. After all, I was there too! Haha!"
        bull_phone "You’ve done good, [player_name]. And you’re turning into a real man now."
    elif lauren_love >= 10 and lauren_love < 15:
        bull_phone "Not that you did much to get yourself tired to begin with; retired old man seen more action while listening to the radio than you did today."
        mc "Shut up."
    else:
        bull_phone "Christ, [player_name], that was such a huge mess up, I would pity you, if I didn’t want to beat you myself."
        bull_phone "If you get shit to this point a third time, I’ll seriously leave you to struggle alone."

    bull_phone "Anyway, I think you really should take a break."
    bull_phone "Think about your recent experiences, and steel up your heart!"
    bull_phone "Because we’re just beginning, hehehe."
    mc "Just beginning?"
    bull_phone "Of course! You don’t really think our final objective is to just get some kisses and feel up a couple breasts, right?"
    bull_phone "No, I’ll get you to FUCK. And sooner than you think."
    mc "*Gulp!"
    "That was it. I wasn’t only determined to change my life around, to get back at everyone who hurt me before, but I was actually working on it."
    mc "Yeah. Let’s do it."

    if nancy_key_question_passed:
        if nancy_love >=18:
            jump nancy_returns_knock
    else:
            label end_episode_1:
    # Grant episode 1 completion achievement  
    # call grant_episode_achievement(1)
    # $ check_all_achievements()

    jump episode_2

    # Grant episode 1 completion achievement
    # call grant_episode_achievement(1)
    # $ check_all_achievements()

label nancy_returns_knock:

    play sound "ES_Knocking On The Inside - Epidemic Sound.mp3"
    "Knock, knock!"
    mc "Hm? Who could it be? I didn’t invite anyone here today…"

    hide mc
    show nancy at nancy_convo
    $ update_character_state("nancy", CharState.AROUSED)
    play music "ES_Pillow (Instrumental Version) - SCENE.mp3" volume 0.1
    with fade

    nancy "H-Hi, [player_name]..."
    mc "Nancy? Hi. What are you doing here?"
    nancy "It’s just that I- I have been thinking of what happened between the two of us back in the mall, and… and…"
    nancy "[player_name], I just can’t study anymore, I can’t focus on any text any longer… and it’s all your fault."
    mc "My fault?"
    nancy "Yes… Because you made me horny like this."
    mc "Nghn?"
    "She suddenly jumped on my arms, her mouth closing on mine like a Gungnir, the spear that never misses its target."
    nancy "Hyumm…!"
    mc "Hughn!!"
    "And it was no sweet, easy, and easily misinterpreted kiss either, but a lustful surrendering to her most primitive desires."
    "There was no room for interpretation in that."
    nancy "[player_name]… fuck me."
    outline "Ba-dum!"
    mc "Hehehe… with pleasure."

    scene black
    show scene_3_initial
    stop music fadeout 1.0
    with fade

    $ update_character_state("lauren", CharState.AROUSED)
    outline "We quickly stripped down, and in a matter of seconds, we got ourselves in the right position."
    outline "Lauren's perked-up nipples pointed straight at me, her wet pussy dripping down on my cock."
    outline "W-We're about to fuck…!"
    outline "Nancy's juice wetted my tip and ran down my shaft, lubricating me further and stoking the flames of lust inside of me."
    $ play_vagina_insertion_sound()
    bull_phone "Yes, and look how she's eager… We can't let her waiting any longer, right?"
    nancy "Huaaam!!"
    $ play_woman_pleasure_sound()
    nancy "Aagh! Aagh!"
    $ play_woman_pleasure_sound()

    scene black
    show scene_3
    with fade


    outline "Oh, God! It's been ages since I felt this good!"
    $ play_penetration_sound()
    $ play_man_pleasure_sound()
    mc "You got quite a tasty pussy right here, Nancy."
    mc "And I'll show you that you made the right choice coming here to alleviate yourself."
    nancy "Humm!"
    $ play_woman_pleasure_sound()
    nancy "I did! I can tell it already!"
    nancy "Aghn! Nghnn!"
    $ play_woman_pleasure_sound()

    nancy "This cock is nothing like what that bitch of your ex has been telling everyone!"
    $ play_woman_pleasure_sound()
    nancy "Oh, God! Y-You've got a mast for a cock, you're impaling me! Hughnn!"
    $ play_penetration_sound()
    $ play_woman_pleasure_sound()

    outline "These words… the way she's moaning…"

    bull_phone "What you're seeing, what you're experiencing is the body of a woman who isn't a loose, controlling whore. What do you think?"

    outline "I-I love it. I need more. More!"

    outline "Maybe because we shared the same body at that instant, maybe because he was indeed my ally, whatever the reason, the Bull Phone heard me:"
    mc "Faster, bitch!"
    $ play_man_pleasure_sound()
    mc "You'll never get to feel my spunk filling you up this way! To your back into it, and I'll make you cum hard!"
    "Words which I would never dare to say to my ex left my mouth, and the result were instantaneous: her pussy quivered, her pupils dilatated, and she picked up her speed."
    $ play_vagina_insertion_sound()

    nancy "Oh, my God, yes! Yes! C-Call me more slurs!"
    $ play_woman_pleasure_sound()
    "Each time she lowered herself onto me, I reached deeper into her than the last time, she leaked more of her juices, and the squelching noises were louder."
    $ play_penetration_sound()
    $ play_vagina_insertion_sound()

    mc "You better start to come here more often, bitch, because after tasty this pussy of yours, I won't leave you any rest."
    mc "And you'll like it, do you hear me?"
    $ play_man_pleasure_sound()

    nancy "Yes! Yes! I like it already, aghnn!"
    $ play_woman_pleasure_sound()

    mc "Good, I'll make you my bitch and you'll be thankful for that."

    nancy "I-I am so thankful! T-Thank you for fucking me, [player_name]!"
    $ play_woman_pleasure_sound()

    mc "Is that all you've got to say, you bitch?"

    nancy "P-Please, fuck me as many times as you can! As often as you can! Aaghn! I want to feel your cock everyday, all day long! Aaghn!"
    $ play_woman_pleasure_sound()
    $ play_penetration_sound()

    nancy "There's no way I'll ever be able to go back to my routine after experiencing this!"
    nancy "You make me… you make me…"
    nancy "CUM SO HARD!!!"
    nancy "Aaghnnnnnnn!!!!!"
    $ play_woman_pleasure_sound()
    $ play_vagina_insertion_sound()

    outline "She climaxed, splashing her love juices all over my hips."
    outline "And those final pussy contractions and her lewd promises was all that I needed to cum as well."

    mc "Gaahn!"
    $ play_man_pleasure_sound()

    scene scene_3_final
    with fade

    outline "I held nothing back, and allowed myself to shoot my thing straight into her womb."
    $ play_cum_sound()
    $ play_man_pleasure_sound()

    nancy "Hmm… God…"
    $ play_woman_pleasure_sound()
    $ play_woman_breathing_sound()

    outline "With her eyes rolling up inside her skull, Nancy slumped down beside me."
    outline "She seemed so tired, so satisfied, the overworked girl fell asleep immediately, leaking my semen from her pussyhole."
    
    $ persistent.scene_3 = True

    bull_phone "So, what do you think? Enjoyed the feeling of power?"

    outline "If I enjoyed it?! Fuck, I can't go back to that submissive shit my ex made me go through ever again!" # Narration for internal thought

    mc "No.. that's not all either. I need more pussy. Right now."

    bull_phone "Ha! Now we're starting to look eye to eye…"
    bull_phone "You're right in that, buddy, you do need more pussy. And I'll help you get them."
    
    # MC's thoughts about Lauren after the experience with Nancy
    if lauren_love >= 15:
        outline "Thinking about Lauren now... she's so different from Nancy..."
        outline "There's something pure about her... innocent and genuine..."
        outline "She sees past my awkwardness, accepts who I really am inside..."
        outline "Lauren makes me want to be better, to protect that innocence..."
        
        menu:
            "Reflect on Lauren's pure nature":
                label test_choice_qe6ff:
                outline "What word captures Lauren's beautiful innocence and goodness?"
                jump outfit_11_puzzle
                label outfit_11_puzzle_success:
                    outline "Like an angel... something precious that should be protected..."
                    outline "She deserves someone who appreciates her purity..."
                    jump end_episode_1
                label outfit_11_puzzle_failure:
                    outline "Lauren's innocence is something special..."
                    jump end_episode_1
            "Focus on the present moment":
                label test_choice_mp4rg:
                outline "Right now, I should focus on what just happened with Nancy..."
    
    label end_episode_1:
    # Grant episode 1 completion achievement  
    # call grant_episode_achievement(1)
    # $ check_all_achievements()

    jump episode_2
