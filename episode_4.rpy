# Episode 4 uses centralized points system from points_system.rpy
default butcher_blackmail_success = False
default gemmy_standing_ride_scene = False
default ersa_reverse_cowgirl_scene = False
default double_licking_scene = False
default gemmy_otaku_bond = 0
default ersa_exotic_interest = 0
default gemmy_right = 0
default ersa_right = 0
default gemmy_outcome = None
default ersa_outcome = None

label episode_4:
    
    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    # MUSIC PLACEHOLDER: Upbeat morning theme - MC feeling confident after previous victories
    play music "ES_All That I Want - Brendon Moeller.mp3" volume 0.2
    with Fade(0.5, 5.0, 0.5)
    
    outline "Things have been going pretty well lately."
    outline "Nancy was incredible, Lauren and I had some great dates, and I even managed to tame Emma."
    outline "My reputation is slowly recovering, and people are starting to see [girl_friend]'s stories for the bullshit they were."
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    bull_phone "Morning, stud. You've been on quite the winning streak lately, but you know what would really cement your status as a true alpha?"
    mc "What's that?"
    bull_phone "Remember that conversation between Gemmy and Craig at the butcher shop? That bitch ex-wife of his who's struggling to get child support?"
    mc "Yeah, I remember - she was pretty pissed off."
    bull_phone "Well, what if I told you there's an opportunity there? Two opportunities, actually - Craig has TWO ex-wives."
    mc "Two ex-wives? Jesus, that guy really can't keep it in his pants."
    bull_phone "Or keep a marriage together, apparently. But here's the thing - both of them hate his guts, and you know what they say: the enemy of my enemy..."
    mc "...is my friend?"
    bull_phone "Is your potential fuck buddy, in this case."
    
    $ update_character_state("mc", CharState.NORMAL)
    mc "So you want me to seduce Craig's ex-wives? That's... actually pretty devious."
    bull_phone "It's brilliant! Think about it - Craig fucked your ex-girlfriend and he's been spreading rumors about you."

    bull_phone "What better revenge than to fuck not one, but BOTH of his ex-wives, film it, and use it to make him stop his bullshit?"
    mc "That's... that's actually not a bad plan, but how do I even approach them?"
    bull_phone "Gemmy's easy - you already heard her complaining about child support."
    bull_phone "So offer to help her with that and be the knight in shining armor Craig never was."
    bull_phone "As for the other one... her name's Ersa."
    bull_phone "She's college educated, bitter about how Craig treated her."
    bull_phone "Use your college boy charm and do some 'research' about failed marriages or something."
    mc "Alright, let's start with Gemmy then."
    
    hide bull
    with pixellate
    
    "I pull out my phone and search for Gemmy's contact information."
    "It doesn't take long - she runs a small bakery near the mall, and her number is listed on the business page."
    "Taking a deep breath, I dial the number."
    
    play sound "ES_Telephone Ringback Tone - Epidemic Sound.mp3"
    
    "Ring... ring... ring..."
    
    gemmy "Gemmy's Gourmet Goods, how can I help you?"
    mc "Hi, Gemmy? This is [player_name]. We met briefly at Craig's butcher shop the other day?"
    gemmy "Oh... you're that guy Craig was making fun of."
    gemmy "What do you want? If you're calling to order a cake, we're booked solid this week."
    
    menu:
        "I wanted to ask if you're getting your child support from Craig.":
            label test_choice_0z1gz:
            $ win_sound()
            $ gemmy_love += 5
            mc "Actually, I wanted to ask if you're getting your child support from Craig."
            mc "I couldn't help but overhear your conversation, and it sounded like he's being difficult."
            gemmy "...Why do you care?"
            mc "Because Craig's an asshole who deserves to pay what he owes."
            mc "And because I might be able to help."
            gemmy "Help? How?"
            mc "I have some connections - good lawyers who specialize in this kind of thing, lawyers who know how to make deadbeat dads pay up."
            gemmy "Really? And what's in it for you?"
            mc "Let's just say Craig and I have our own issues, and helping you would be... mutually beneficial."
            gemmy "Craig always acts like he knows everything... like he's teaching everyone..."
            
            menu:
                "What does Craig think he knows so much about?":
                    label test_choice_bn3np:
                    if gemmy_love >= 5:
                        gemmy "He lectures everyone about responsibility while avoiding his own!"
                        gemmy "What do people who teach and share wisdom do?"
                        jump outfit_43_puzzle
                        label outfit_43_puzzle_success:
                            gemmy "Professor Craig, teaching everyone how to be a deadbeat!"
                            gemmy "His degree in being an asshole is showing!"
                        label outfit_43_puzzle_failure:
                            gemmy "He thinks he knows everything but he knows nothing!"
                "Craig's not qualified to teach anyone":
                    label test_choice_3yvoa:
                    gemmy "Exactly! He's the one who needs education!"
            gemmy "Hmm... interesting."
        "Craig mentioned you're struggling financially.":
            label test_choice_yzvsf:
            $ lose_sound()
            mc "Craig mentioned you're struggling financially, and I thought maybe I could help somehow."
            gemmy "Craig said WHAT?! That lying piece of shit!"
            gemmy "I'm not struggling, I just want what's legally mine!"
            gemmy "How dare he spread rumors about me!"
            mc "Sorry, I didn't mean to-"
            gemmy "No, no, it's not your fault - it's just like Craig to badmouth me to strangers. What exactly did he say?"
            mc "Just that you were asking for child support."
            gemmy "Asking? ASKING?! I'm DEMANDING what the court ordered him to pay!"
        "I have a business proposition for you.":
            label test_choice_zkcmo:
            $ lose_sound()
            mc "I have a business proposition for you."
            gemmy "If this is some MLM bullshit, I'm hanging up."
            mc "No, no! Nothing like that - it's about Craig and getting him to pay what he owes you."
            gemmy "I'm listening, but this better not be a waste of my time."
            mc "It won't be. Can we meet to discuss it?"
            gemmy "You have thirty seconds to convince me."
    gemmy "You know what? Fine, I could use all the help I can get with that deadbeat - he's three months behind on payments and my lawyer cousin is useless."
    gemmy "When can you meet?"
    mc "How about tomorrow afternoon? I can pick you up and we can go see the lawyer together."
    gemmy "Downtown, right? These good lawyers you mentioned?"
    mc "The best. They've handled cases like this before."
    gemmy "Alright. Tomorrow at 2 PM. Don't be late."
    gemmy "And listen? If this is some kind of joke or scam, you'll regret it."
    mc "It's not, I promise. See you tomorrow, Gemmy."
    play sound "ES_Mobile Phone, Hang Up Beeps - Epidemic Sound.mp3"
    "Beep, beep, beep..."
    scene home_morning
    show mc at mc_convo
    with fade
    $ update_character_state("mc", CharState.HAPPY)
    mc "(Step one complete. Now I need to prepare for tomorrow.)"
    mc "(I should research some actual lawyers, just in case she asks for specifics.)"
    mc "(But the real plan... that's going to require some finesse.)"
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    bull_phone "Nice work! You've got her hooked."
    bull_phone "Now remember, the lawyer thing is just a pretense."
    bull_phone "What you really want is to get her comfortable with you."
    bull_phone "Show her you're everything Craig wasn't - attentive, helpful, caring."
    bull_phone "Make her feel appreciated. Make her feel desired."
    bull_phone "And when the moment's right..."
    mc "I know, I know. But we have to be careful."
    mc "She's not some college girl. She's a grown woman with a child."
    mc "If I push too hard too fast, she'll see right through it."
    bull_phone "That's why you're playing the long game."
    bull_phone "Tomorrow, be the perfect gentleman. Listen to her problems."
    bull_phone "Let her vent about Craig. Build that trust."
    bull_phone "The seduction comes later."
    mc "Got it. I should probably look up some actual law firms too."
    mc "Just in case she wants to actually visit one."
    bull_phone "Smart thinking. Cover all your bases."
    bull_phone "This is why you're becoming a true player, my friend."
    hide bull
    with pixellate
    scene black
    with fade
    stop music fadeout 1.0
    "I spend the rest of the day researching family law attorneys and child support laws."
    "By evening, I have enough knowledge to hold a convincing conversation about the topic."
    "Tomorrow's going to be interesting..."
    # NEXT DAY - GEMMY DATE
    scene mall_front_afternoon
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with Fade(0.5, 5.0, 0.5)
    "I arrive at the mall where Gemmy's bakery is located."
    "Her shop is in one of the smaller retail spaces near the food court, but it's cozy with the smell of fresh bread and pastries wafting through the mall corridors."
    "The mall location probably helps with foot traffic, but the rent must be killing her - no wonder she needs that child support."
    show gemmy at gemmy_convo
    $ update_character_state("gemmy", CharState.NORMAL)
    hide mc
    play music "ES_In the Evening - Guustavv.mp3" volume 0.2
    with fade
    gemmy "You're actually on time. That's already better than Craig ever was."
    mc "I said I'd be here, didn't I?"
    mc "Ready to go see that lawyer?"
    gemmy "Just let me grab my documents. I've got three years worth of missed payments documented."
    gemmy "Bank statements, court orders, text messages where he promises to pay and never does..."
    mc "Sounds like you've been thorough."
    gemmy "I've had to be. Nobody else is looking out for me and my daughter."
    $ update_character_state("gemmy", CharState.ANGRY)
    gemmy "You know what the worst part is?"
    gemmy "It's not even about the money. Not really."
    gemmy "It's about the disrespect. The way he acts like we don't matter."
    gemmy "Like his son doesn't matter."
    menu:
        "Craig's a fool for not appreciating what he had.":
            label test_choice_i94k3:
            $ win_sound()
            $ gemmy_love += 5
            mc "Craig's a fool for not appreciating what he had."
            mc "A beautiful wife, a family, a son to carry on his name..."
            mc "And he threw it all away for what? To fuck around?"
            $ update_character_state("gemmy", CharState.NORMAL)
            gemmy "...You really think so?"
            mc "I know so. Any man would be lucky to have what he had."
            mc "But he was too stupid to see it."
            gemmy "You know, you're pretty insightful for someone your age."
            gemmy "Most young guys just think with their dicks."
            gemmy "My daughter loves anime... especially the magical girl shows..."
            gemmy "She says they're about protecting people you love..."
            menu:
                "Tell me about magical girls":
                    label test_choice_9s9sq:
                    if gemmy_love >= 10:
                        gemmy "They're so inspiring! Regular girls who gain special powers..."
                        gemmy "What happens when they gain their magical abilities?"
                        jump outfit_22_puzzle
                        label outfit_22_puzzle_success:
                            gemmy "I actually have this cute magical girl costume from a theme party..."
                            gemmy "My daughter loves when I wear it... makes me feel young again..."
                        label outfit_22_puzzle_failure:
                            gemmy "I thought you might understand the appeal..."
                "You're a protective mother":
                    label test_choice_hmje1:
                    gemmy "I try to be... it's not easy doing it alone."
            mc "Maybe. But I've learned the hard way what happens when you don't appreciate what you have."
            mc "You lose it. And sometimes, you never get it back."
        "He's missing out on seeing his son grow up.":
            label test_choice_m1pu0:
            $ win_sound()
            $ gemmy_love += 5
            mc "He's missing out on seeing his son grow up."
            mc "That's time he'll never get back."
            $ update_character_state("gemmy", CharState.ANGRY)
            gemmy "Exactly! Little Marcus just turned seven."
            gemmy "He's starting to ask questions about why daddy never comes around."
            gemmy "What am I supposed to tell him? That his father cares more about his new girlfriends than his own son?"
            mc "That must be incredibly hard."
            mc "You're doing an amazing job raising him on your own."
            gemmy "...Thank you. It's nice to hear that sometimes."
            gemmy "Most people just see a bitter ex-wife. They don't see the struggling single mom."
        "Well, that's what lawyers are for, right?":
            label test_choice_pinh8:
            $ lose_sound()
            mc "Well, that's what lawyers are for, right?"
            mc "To make deadbeats pay up."
            gemmy "If only it were that simple."
            gemmy "You know how many times I've been to court?"
            gemmy "How many judgments I've won that he just ignores?"
            gemmy "The system is broken."
            mc "Then we need to find a better way."
            gemmy "That's what I'm hoping your lawyers can do."
    "We walk outside to find a quieter place to talk."
    "She seems surprised by my gentlemanly gestures - another thing Craig probably never did."
    scene park_afternoon
    show gemmy at gemmy_convo
    $ update_character_state("gemmy", CharState.NORMAL)
    with fade
    gemmy "So, these lawyers of yours - what firm are they with?"
    mc "Morrison & Associates. They specialize in family law and have a great track record with child support cases."
    mc "(Thank god I did my research.)"
    gemmy "Never heard of them. How do you know about them?"
    mc "A friend of mine used them when her ex was being difficult."
    mc "They got her eighteen months of back payments plus interest."
    gemmy "Sounds too good to be true."
    mc "Well, they're not cheap. But they work on contingency for cases like yours."
    mc "They only get paid if you get paid."
    $ update_character_state("gemmy", CharState.HAPPY)
    gemmy "Now that's what I like to hear!"
    gemmy "You know, [player_name], I misjudged you."
    gemmy "When I saw you at Craig's shop, I thought you were just another one of his loser customers."
    gemmy "But you're actually trying to help me. Why?"
    menu:
        "Because I hate seeing good people get screwed over.":
            label test_choice_kg43h:
            $ win_sound()
            $ gemmy_love += 5
            mc "Because I hate seeing good people get screwed over."
            mc "You're working hard, raising a daughter, running a business..."
            mc "And Craig's sitting pretty in his butcher shop, acting like he owes you nothing."
            mc "It's not right."
            gemmy "You really get it, don't you?"
            gemmy "Most people just tell me to move on, find closure, all that bullshit."
            gemmy "But it's not about closure. It's about justice."
            mc "Exactly. And maybe a little revenge wouldn't hurt either."
            $ update_character_state("gemmy", CharState.HAPPY)
            gemmy "Haha! Now you're speaking my language!"
        "Because Craig and I have our own issues.":
            label test_choice_vh1h5:
            $ lose_sound()
            mc "Because Craig and I have our own issues."
            mc "Let's just say he's done some things that pissed me off."
            mc "Helping you is a way to get back at him."
            gemmy "So you're using me to get revenge?"
            mc "No, no! I mean, helping you helps me, but-"
            gemmy "Relax, man. I get it."
            gemmy "Enemy of my enemy and all that."
            gemmy "As long as I get my money, I don't care about your motivations."
        "Because you deserve better than how he treated you.":
            label test_choice_fif7m:
            $ win_sound()
            $ gemmy_love += 10
            mc "Because you deserve better than how he treated you."
            mc "No woman should be discarded like that, especially not the mother of his child."
            $ update_character_state("gemmy", CharState.NORMAL)
            gemmy "..."
            gemmy "You know, no one's said anything like that to me in a long time."
            gemmy "Everyone just sees the angry ex-wife."
            gemmy "They don't see the woman who was betrayed, abandoned, left to pick up the pieces."
            mc "I see her."
            mc "And she's a lot stronger than Craig ever gave her credit for."
            gemmy "Damn, you're going to make me cry."
            gemmy "And I just did my makeup."
    "We walk in comfortable silence for a while."
    "I can see Gemmy stealing glances at me, reassessing her initial impression."
    "This is going better than I expected."
    scene mall_front_afternoon
    show gemmy at gemmy_convo
    $ update_character_state("gemmy", CharState.NORMAL)
    with fade
    "We're back at the mall parking lot - I told her the law firm has an office in the business complex attached to the mall."
    "I'm banking on her not actually wanting to go to the office right away."
    mc "The firm's office is in the business tower connected to the mall. Third floor."
    gemmy "Actually... before we go there..."
    gemmy "Can we grab a coffee or something? I'm suddenly nervous."
    gemmy "It's been so long since anyone actually tried to help me with this."
    gemmy "I guess I'm scared to get my hopes up."
    mc "Of course. There's a nice coffee shop inside the mall, near your bakery actually."
    mc "(Perfect. Just as planned.)"
    scene coffee_shop
    show gemmy at gemmy_convo
    $ update_character_state("gemmy", CharState.NORMAL)
    with fade
    "We settle into a quiet corner booth."
    "Gemmy orders a latte and a chocolate croissant - 'stress eating,' she calls it."
    "I get a black coffee, trying to seem mature."
    gemmy "You know what the really fucked up part is?"
    gemmy "I actually loved that asshole once."
    gemmy "Can you believe that? I was young, stupid, thought he was this rugged, manly provider type."
    gemmy "Turns out he was just a selfish prick who happened to be good with a cleaver."
    mc "How long were you married?"
    gemmy "Six years. Six fucking years of my life."
    gemmy "The first two were good, I'll give him that."
    gemmy "He was attentive, romantic even. Brought me flowers every Friday."
    gemmy "Then I got pregnant, and it all changed."
    $ update_character_state("gemmy", CharState.ANGRY)
    gemmy "Suddenly I wasn't his sexy young wife anymore."
    gemmy "I was just the mother of his child. The ball and chain."
    gemmy "He started staying out late, coming home smelling like other women's perfume."
    gemmy "When I confronted him, he'd gaslight me. Say I was being hormonal, paranoid."
    menu:
        "He didn't deserve you. You're beautiful and strong.":
            label test_choice_9lp1n:
            $ win_sound()
            $ gemmy_love += 10
            mc "He didn't deserve you. You're beautiful and strong."
            mc "Any man should be proud to have you as his wife."
            $ update_character_state("gemmy", CharState.HAPPY)
            gemmy "Beautiful? You think I'm beautiful?"
            gemmy "I'm thirty-two with stretch marks and bags under my eyes from single motherhood."
            mc "And you're still stunning. Those marks just show you're a warrior."
            mc "You brought life into this world. That's incredible."
            mc "Craig was an idiot for not worshipping the ground you walk on."
            gemmy "Jesus, where did you learn to talk like that?"
            gemmy "Most guys your age just grunt and ask for nudes."
            gemmy "Or they just want to talk about video games and anime..."
            mc "Maybe I'm not like most guys my age."
            menu:
                "Are you into gaming and anime?":
                    label test_choice_toai5:
                    if gemmy_love >= 10:
                        gemmy "Actually... yeah. I am a bit of a gamer."
                        gemmy "Are you a real gamer? What's the most famous cheat code?"
                        jump outfit_24_puzzle
                        label outfit_24_puzzle_success:
                            gemmy "I actually have this awesome gamer girl setup at home..."
                            gemmy "Streaming gear, RGB everything... maybe you'd like to see it sometime?"
                        label outfit_24_puzzle_failure:
                            gemmy "Well, you tried. Most guys don't even know what I'm talking about."
                "I prefer mature conversation":
                    label test_choice_yxqcu:
                    gemmy "That's refreshing. Most young guys are so immature."
            gemmy "No... no, you're definitely not."
            "She's looking at me differently now. There's a heat in her eyes that wasn't there before."
        "Men like Craig don't know what they have until it's gone.":
            label test_choice_kd092:
            $ win_sound()
            $ gemmy_love += 5
            mc "Men like Craig don't know what they have until it's gone."
            mc "They take their families for granted, chase after cheap thrills."
            mc "Then they end up alone, paying child support to the woman they should have cherished."
            gemmy "Exactly! But he's not even paying the support!"
            gemmy "He's got a new girlfriend every month, driving a nice truck..."
            gemmy "Meanwhile, I'm working sixty-hour weeks just to keep the lights on."
            mc "That's going to change. I promise you that."
            gemmy "You seem pretty confident for someone so young."
            mc "I've learned that age doesn't always equal wisdom."
            mc "Sometimes it just means more years of being an asshole."
            gemmy "Ha! True that."
        "That's rough. My ex cheated on me too.":
            label test_choice_bnhmo:
            $ lose_sound()
            mc "That's rough. My ex cheated on me too."
            mc "I know how much it hurts."
            gemmy "Your ex? You mean that [girl_friend] girl Craig mentioned?"
            gemmy "The one who fucked half the town?"
            mc "...Yeah. That one."
            gemmy "No offense, but that's not quite the same thing."
            gemmy "You didn't have a child with her. You didn't build a life together."
            gemmy "Getting cheated on in college is like... a rite of passage."
            gemmy "Getting cheated on when you're married with a baby? That's devastation."
            mc "You're right. I'm sorry."
    gemmy "But enough about my sob story."
    gemmy "Tell me about these lawyers. What's their strategy going to be?"
    mc "Well, first they'll review all your documentation."
    mc "Then they'll probably file a motion for contempt, since he's violating court orders."
    mc "They might also look into garnishing his wages directly from the butcher shop."
    gemmy "Can they do that?"
    mc "If he owns the business, absolutely. They can put a lien on it if necessary."
    mc "But honestly, Gemmy..."
    mc "Sometimes the best revenge isn't legal. It's personal."
    $ update_character_state("gemmy", CharState.NORMAL)
    gemmy "What do you mean?"
    mc "I mean, Craig cares about his reputation, right?"
    mc "His tough guy image, his ability to get women..."
    mc "What if we could hit him where it really hurts?"
    gemmy "I'm listening..."
    mc "What would piss him off more - paying child support, or knowing his ex-wife moved on to someone better?"
    mc "Someone younger, more attentive... someone who actually appreciates what he threw away?"
    $ update_character_state("gemmy", CharState.AROUSED)
    gemmy "Are you... are you suggesting what I think you're suggesting?"
    menu:
        "I'm suggesting we give Craig something to really be mad about.":
            label test_choice_63unp:
            $ win_sound()
            $ gemmy_love += 10
            mc "I'm suggesting we give Craig something to really be mad about."
            mc "Show him that discarding you was the biggest mistake of his life."
            mc "And maybe have some fun in the process."
            gemmy "You're... you're seriously hitting on me right now?"
            gemmy "I'm ten years older than you!"
            mc "So? That just means you know what you want."
            mc "And you're experienced enough to teach me a thing or two."
            mc "Unless you're not interested in a younger man who actually knows how to treat a woman..."
            $ update_character_state("gemmy", CharState.AROUSED)
            gemmy "Fuck. You're dangerous, you know that?"
            gemmy "I came here thinking we were seeing lawyers..."
            gemmy "And now you've got me thinking about... other things."
            mc "Why not both? We can still see the lawyers."
            mc "But maybe we could also explore... other options for making Craig regret his choices."
        "I'm suggesting you deserve to be happy.":
            label test_choice_ywyed:
            $ win_sound()
            $ gemmy_love += 5
            mc "I'm suggesting you deserve to be happy."
            mc "And if that happiness happens to make Craig insanely jealous, well..."
            mc "That's just a bonus, isn't it?"
            gemmy "You're playing with fire here."
            gemmy "I'm a single mom. I have responsibilities."
            gemmy "I can't just... fool around with college boys."
            mc "Who said anything about fooling around?"
            mc "Maybe I genuinely think you're an incredible woman who deserves better."
            mc "Maybe I want to show you how a real man treats a lady."
            gemmy "A real man? You're barely old enough to buy beer!"
            mc "And yet here I am, doing more for you in one day than Craig did in years."
            gemmy "...Fuck. You have a point."
        "Never mind. Let's just focus on the lawyers.":
            label test_choice_sdjyk:
            $ lose_sound()
            mc "Never mind. Let's just focus on the lawyers."
            mc "I got carried away."
            gemmy "No, no. Don't backtrack now."
            gemmy "You were suggesting something. Say it."
            mc "I just... I think you're attractive, okay?"
            mc "But you're right, it's inappropriate."
            gemmy "Jesus, grow some balls already."
            gemmy "If you're going to make a move, make it."
            gemmy "Don't half-ass it like everything else in your life."
            mc "I... okay. I want you."
            gemmy "Better. But your timing sucks."
            gemmy "Let's deal with the lawyer first."
    $ update_character_state("gemmy", CharState.NORMAL)
    gemmy "You know what? Fuck the lawyers."
    gemmy "I've been to plenty of lawyers. They all say the same thing."
    gemmy "'We'll file motions, we'll send letters, we'll threaten legal action.'"
    gemmy "And Craig just laughs and keeps not paying."
    mc "So what do you want to do?"
    $ update_character_state("gemmy", CharState.ANGRY)
    gemmy "I want to make him suffer."
    gemmy "I want him to know what it feels like to be humiliated, discarded, replaced."
    gemmy "I want him to see me happy with someone else and BURN with jealousy."
    mc "I can help with that."
    mc "But it might require doing something... dramatic."
    $ update_character_state("gemmy", CharState.NORMAL)
    gemmy "How dramatic are we talking?"
    mc "What if we filmed something? Something that would drive him absolutely insane?"
    mc "Something that shows you've moved on to someone younger, better..."
    mc "Someone who actually knows how to please a woman?"
    $ update_character_state("gemmy", CharState.AROUSED)
    gemmy "You want to make a sex tape? To send to my ex-husband?"
    gemmy "That's... that's fucking insane."
    mc "Is it? He humiliated you for years."
    mc "He cheated, he abandoned you and your son, he refuses to support his own child."
    mc "Don't you think he deserves a little humiliation in return?"
    menu:
        "We could start with something simple. Just to test the waters.":
            label test_choice_hy6cb:
            $ win_sound()
            $ gemmy_love += 10
            mc "We could start with something simple. Just to test the waters."
            mc "Maybe just... a preview. Something to let him know you're not the desperate ex-wife he thinks you are."
            mc "Something that shows you're desired, wanted, pursued by men who aren't idiots."
            gemmy "What kind of preview?"
            mc "Come back to my place. We'll figure it out together."
            mc "No pressure. We can stop anytime you want."
            mc "But I promise you... Craig will never look at you the same way again."
            gemmy "This is crazy. This is absolutely fucking crazy."
            gemmy "I'm a mother. I have a reputation to maintain."
            gemmy "I can't just... make porn with a college student!"
            mc "It's not porn. It's revenge."
            mc "And your reputation? Craig already destroyed that with his lies."
            mc "This is about taking back your power."
            mc "Showing him - and yourself - that you're not his victim anymore."
            $ update_character_state("gemmy", CharState.NORMAL)
            gemmy "..."
            gemmy "Fuck it. You're right."
            gemmy "I've been the good girl for too long, and where has it gotten me?"
            gemmy "Let's do this."
        "Think about it - anonymous video, threatening to show his buddies...":
            label test_choice_nj86w:
            $ win_sound()
            $ gemmy_love += 5
            mc "Think about it - we film something hot, send it anonymously."
            mc "Tell him if he doesn't pay the child support, all his drinking buddies get to see it."
            mc "All his customers at the butcher shop..."
            mc "Everyone will know his ex-wife upgraded to a younger model."
            gemmy "That's... blackmail."
            mc "No, it's leverage. He's been using his financial power against you for years."
            mc "Time to use something else against him."
            gemmy "And you think he'd actually pay?"
            mc "His ego couldn't handle the humiliation."
            mc "Trust me, men like Craig would rather pay than have everyone know their ex is getting better dick elsewhere."
            gemmy "God, you're crude."
            gemmy "But... you might have a point."
            gemmy "He always was insecure about his performance."
        "Forget I said anything. This was a stupid idea.":
            label test_choice_onaf2:
            $ lose_sound()
            $ gemmy_love -= 5
            mc "Forget I said anything. This was a stupid idea."
            mc "Let's just go see the lawyers like we planned."
            gemmy "No, wait. I want to hear this out."
            gemmy "You can't just suggest something like that and then chicken out."
            gemmy "Are you a man or a boy?"
            mc "I just... I don't want to pressure you."
            gemmy "Pressure me? I'm the one who's been pressured for years."
            gemmy "By Craig, by the courts, by society telling me to just accept my situation."
            gemmy "For once, I want to do something for ME."
            gemmy "So either commit to this plan or admit you're all talk."
    scene park_night
    show gemmy at gemmy_convo
    $ update_character_state("gemmy", CharState.NORMAL)
    with fade
    "We walk through the park as evening falls, and this time the energy is completely different."
    "There's a tension in the air - sexual, dangerous, exciting."
    "Gemmy keeps fidgeting with her purse, stealing glances at me."
    gemmy "I can't believe I'm doing this."
    gemmy "What would my mother think? What would Marcus think if he knew?"
    mc "Marcus would think his mother is a badass who doesn't let anyone walk over her."
    mc "And your mother? She'd probably be proud you're finally standing up for yourself."
    gemmy "By making a sex tape with someone barely out of college?"
    mc "By taking control of your narrative."
    mc "For years, Craig's been telling everyone you're the bitter ex-wife."
    mc "Time to show them you're the sexy, confident woman who's moving on to better things."
    $ update_character_state("gemmy", CharState.HAPPY)
    gemmy "You know, you're either the smoothest talker I've ever met..."
    gemmy "Or you actually believe this bullshit you're spouting."
    mc "Why not both?"
    mc "I think you're hot, Gemmy. I have since I saw you in that butcher shop."
    mc "The way you stood up to Craig, the fire in your eyes..."
    mc "I wanted you right then and there."
    $ update_character_state("gemmy", CharState.AROUSED)
    gemmy "Fuck. You can't just say things like that."
    gemmy "I'm wet already and we haven't even done anything."
    mc "Good. That means you want this as much as I do."
    mc "The question is... what are you willing to do about it?"
    scene home_night
    show gemmy at gemmy_convo
    $ update_character_state("gemmy", CharState.NORMAL)
    with fade
    "We arrive at my place, and I can see Gemmy's nervousness returning."
    "She's probably reconsidering this whole thing."
    "I need to keep her focused on the revenge aspect."
    mc "Want something to drink? Water? Coffee? Something stronger?"
    gemmy "Definitely something stronger. This is crazy enough sober."
    mc "I've got whiskey. Craig's least favorite brand, coincidentally."
    gemmy "Perfect. Pour me a double."
    "I fix us both drinks, making hers strong enough to calm her nerves but not so strong she'll regret this."
    "We sit on the couch, close but not quite touching."
    $ update_character_state("gemmy", CharState.NORMAL)
    gemmy "So how do we do this? Do we just... start fucking?"
    gemmy "I haven't been with anyone since Craig. I don't even remember how this works."
    mc "We take it slow. Build up to it."
    mc "The anticipation will drive Craig even crazier."
    mc "Besides, I want to savor this. It's not every day I get to be with a gorgeous woman like you."
    $ update_character_state("gemmy", CharState.HAPPY)
    gemmy "There you go with that silver tongue again."
    gemmy "Alright, smooth talker. Show me what you've got."
    gemmy "But remember - this is about revenge, not romance."
    mc "Of course. Pure, delicious revenge."
    mc "Now, let me set up the camera..."
    menu:
        "Start with just kissing and touching, build the tension.":
            label test_choice_tft7n:
            $ win_sound()
            $ gemmy_love += 5
            mc "Let's start slow. Just kissing and touching."
            mc "We want Craig to see what he's missing, not just jump to the main event."
            mc "Come here."
            "I pull Gemmy close, my hands sliding around her waist."
            "She's tense at first, but as our lips meet, I feel her relax into me."
            "The kiss starts gentle, exploratory, but quickly deepens."
            "Her hands tangle in my hair as years of frustration pour out."
            $ update_character_state("gemmy", CharState.AROUSED)
            gemmy "Mmm... fuck, I forgot how good this feels."
            gemmy "Craig never kissed me like this, not even in the beginning."
            mc "That's because he's an idiot who didn't appreciate what he had."
            "I trail kisses down her neck, feeling her pulse race under my lips."
            "My hands explore her curves, appreciating every inch Craig neglected."
            gemmy "The camera... is it recording?"
            mc "Every second. Want me to adjust the angle?"
            gemmy "No... no, this is perfect. Let him see how desired I am."
            gemmy "Let him see another man worship his ex-wife."
        "Let's go straight to sex - really shock him.":
            label test_choice_d1oe6:
            $ win_sound()
            $ gemmy_love += 10
            $ gemmy_standing_ride_scene = True
            mc "I have an idea. Something that will really get under his skin."
            mc "Craig always bragged about his dick, right? Classic overcompensation."
            mc "What if we showed him his ex-wife enthusiastically enjoying someone else?"
            $ update_character_state("gemmy", CharState.AROUSED)
            gemmy "You want me to... ride you? On camera?"
            gemmy "That's so dirty. So wrong. So..."
            gemmy "So fucking perfect. He always complained I didn't do it enough."
            gemmy "Said I was a prude, that other women would appreciate him more."
            mc "Then let's show him what he missed out on."
            mc "Show him that you weren't the problem - he was."
            gemmy "Fuck yes. Get those pants off."
            gemmy "I'm going to give you the best ride of your life."
            gemmy "And Craig's going to watch every second of it."
        "Maybe we should think about this more...":
            label test_choice_v9ozi:
            $ lose_sound()
            $ gemmy_love -= 5
            mc "Maybe we should think about this more..."
            mc "I mean, once we do this, there's no taking it back."
            $ update_character_state("gemmy", CharState.ANGRY)
            gemmy "Are you fucking kidding me?"
            gemmy "You get me all worked up, bring me here, and now you're backing out?"
            gemmy "What are you, gay? Or just a pussy?"
            mc "No! I just... I want to make sure you're comfortable."
            gemmy "I was comfortable until you started acting like a little bitch."
            gemmy "Either fuck me or take me home. But don't waste my time."
            mc "You're right. I'm sorry. Let's do this."
            gemmy "That's better. Now stop thinking and start acting."
    if gemmy_standing_ride_scene:
        "Gemmy stands before me, her eyes locked on the camera with wicked intent."
        "She slowly strips, revealing her curvy MILF body that Craig abandoned."
        $ update_character_state("gemmy", CharState.AROUSED)
        gemmy "Make sure you get a good angle. I want Craig to see everything."
        gemmy "Want him to see me ride a real man who can actually satisfy me."
        "She pulls me to standing position, my back against the wall."
        gemmy "Holy shit. You're so hard already."
        gemmy "Craig would be jealous. You're much bigger than him."
        mc "Stop talking about Craig and show him what he's missing."
        gemmy "Mmm, demanding. I love it."
        scene scene_10_initial
        stop music fadeout 1.0
        with fade
        "Gemmy positions herself, then lifts one leg up, wrapping it around my waist."
        "With impressive flexibility, she guides me inside her while standing."
        $ play_penetration_sound()
        play sound "ES_Female, Gasp 02 - Epidemic Sound.mp3"
        scene scene_10
        $ persistent.scene_10 = True
        play sound "ACTIONS_BODY_COLLIDE_NAKED_06.mp3" loop
        "She begins riding me against the wall, her body bouncing with each thrust."
        $ play_vagina_insertion_sound()
        gemmy "Fuck... yes... I forgot how good this could feel."
        $ play_woman_pleasure_sound()
        gemmy "Craig could never hold me up like this... never had the strength."
        mc "That's because... fuck... he didn't appreciate what he had."
        mc "You deserve to be fucked properly. Like this."
        $ play_man_pleasure_sound()
        "She increases her pace, using the wall for leverage as she rides me."
        play sound "VOICE_WOMAN_A_PLEASURE_MOAN_SHORT_01.mp3"
        $ update_character_state("gemmy", CharState.HAPPY)
        gemmy "You know what? I want him to see all of me."
        gemmy "Want him to see these tits bouncing as another man fucks me."
        gemmy "The tits he called 'ruined' after I had his baby."
        gemmy "And you know what else he never appreciated? My music!"
        gemmy "I used to DJ at parties before I met him... he made me stop..."
        menu:
            "Tell me about your music passion":
                label test_choice_r875l:
                if gemmy_love >= 20:
                    gemmy "I love electronic music... the energy, the beats..."
                    gemmy "What drives people on the dance floor?"
                    jump outfit_23_puzzle
                    label outfit_23_puzzle_success:
                        gemmy "I still have my DJ outfit... my turntables..."
                        gemmy "Maybe after we destroy Craig, I'll spin tracks again..."
                    label outfit_23_puzzle_failure:
                        gemmy "I thought you might understand music..."
            "Focus on showing Craig what he lost":
                label test_choice_owbvk:
                gemmy "You're right... let's give him a show..."
        mc "Show him everything he lost, Gemmy."
        mc "Every curve, every inch of skin he took for granted."
        "Gemmy grins wickedly and pulls off her top and bra in one smooth motion."
        "Her breasts are full and natural, with the slight sag of motherhood that makes them even more attractive."
        gemmy "These fed his son. And he called them 'saggy' and 'ruined.'"
        gemmy "Tell me what you think of them."
        mc "They're perfect. You're perfect."
        mc "Craig's a fucking moron."
        "Her breasts bounce freely as I thrust up into her."
        "The sight is incredible—this MILF riding me standing up while staring defiantly at the camera."
        gemmy "That's right, Craig. Look what you gave up."
        gemmy "Look what another man gets to enjoy because you're a selfish prick."
        "She rides me harder, her legs trembling from the exertion and pleasure."
        play sound "VOICE_WOMAN_A_PLEASURE_MOAN_SHORT_03.mp3"
        "I can feel her getting close, her pussy clenching around me."
        $ play_vagina_insertion_sound()
        mc "Gemmy... you're incredible..."
        $ play_man_pleasure_sound()
        gemmy "Don't stop. I'm going to cum."
        gemmy "Let Craig see me cum on another man's cock."
        $ play_woman_pleasure_sound()
        play sound "VOICE_WOMAN_A_PLEASURE_MOAN_SHORT_04.mp3"
        "I grip Gemmy's hips tightly, pressing her back against the wall as I thrust deeper."
        $ play_grab_sound()
        $ play_penetration_sound()
        gemmy "Oh fuck, yes! Harder—just like that!"
        $ play_woman_pleasure_sound()
        "Her nails dig into my shoulders, her head thrown back in ecstasy."
        mc "You feel so fucking good, Gemmy. So tight around me."
        $ play_man_pleasure_sound()
        gemmy "Don't hold back. I want you to ruin me for him."
        "I slam into her, the sound of skin on skin echoing in the room."
        $ play_penetration_sound()
        gemmy "God, yes! Let him see how a real man fucks me!"
        $ play_woman_pleasure_sound()
        "She wraps both arms around my neck, pulling me in for a hungry kiss."
        $ play_kiss_sound()
        gemmy "He never made me feel like this. Never."
        mc "He never deserved you."
        "Her moans grow louder, her body trembling as I keep up the relentless pace."
        $ play_woman_pleasure_sound()
        $ play_penetration_sound()
        gemmy "I'm so close... don't stop, please!"
        mc "I won't. I want you to cum for me. Show him what he lost."
        $ play_man_pleasure_sound()
        "She bites her lip, eyes locked on the camera, her breasts bouncing with every thrust."
        gemmy "Watch this, Craig. Watch me cum for someone who actually knows how to fuck me."
        $ play_woman_pleasure_sound()
        
        mc "I'm going to fill you up, Gemmy!"
        gemmy "Yes! Fill me completely!"
        
        scene scene_10_final
        with fade
        
        mc "Fuck!"
        $ play_cum_sound()
        $ play_man_pleasure_sound()
        "I explode inside her as she screams in ecstasy."
        gemmy "YESSSS! So much cum!"
        $ play_woman_pleasure_sound()
        play sound "VOICE_WOMAN_A_PLEASURE_MUTED_INTENSE_LONG_02.mp3"
        
        "We're both catching our breath, the camera still rolling."
        "Gemmy fixes her disheveled clothes, grinning wickedly."
        scene home_night
        $ all_naked = True
        with fade
        show gemmy at gemmy_convo
        $ update_character_state("gemmy", CharState.AROUSED)
        gemmy "Holy shit. I can't believe we just did that."
        gemmy "Did you see me riding you like that? Craig could never handle that position."
        mc "You were incredible. He's an idiot for letting you go."
        gemmy "Damn right he is."
        gemmy "So... what now? Do we send it to him?"
        mc "Not yet. First, we need to make sure he can't trace it back to us."
        mc "Anonymous email, maybe mention the child support..."
        mc "Make it clear this stops when he starts paying."
        gemmy "You've really thought this through, haven't you?"
        gemmy "This wasn't just spur of the moment."
        mc "I told you - I want to help you. And if we both get some pleasure out of it..."
        gemmy "Win-win, right?"
        gemmy "Though I have to say, that was more than 'some' pleasure."
        gemmy "I haven't cum that hard in years."
        mc "Who says we have to stop at just one video?"
        $ update_character_state("gemmy", CharState.AROUSED)
        gemmy "Oh? Already planning round two?"
        gemmy "What did you have in mind?"
        mc "Well, Craig has another ex-wife, doesn't he?"
        mc "What if we really drove the knife in?"
        gemmy "Ersa? That uptight college bitch?"
        gemmy "Oh my god, you're evil. I love it."
        gemmy "She always thought she was better than me because she has a degree."
        mc "Think she'd be interested in some revenge too?"
        gemmy "If you can crack that ice queen exterior? Absolutely."
        gemmy "She hates Craig even more than I do."
        gemmy "He promised her the world and gave her nothing but disappointment."
        mc "Perfect. Then phase two of our plan begins tomorrow."
        mc "But for now... want to make another video? Just for fun this time?"
        $ update_character_state("gemmy", CharState.HAPPY)
        gemmy "You know what? Why not."
        gemmy "Marcus is at his grandmother's until tomorrow."
        gemmy "I've got all night to be a bad girl."
        gemmy "And you've awakened something in me I thought was dead."
        mc "Then let's make the most of it."
        mc "By tomorrow, Craig will be begging to pay that child support."        
        jump gemmy_date_success
    
    else:
        "We make out passionately on the couch, hands exploring each other's bodies."
        "The camera captures every moment - every moan, every touch, every kiss."
        "Gemmy seems to forget about the recording, lost in the moment."
        
        $ update_character_state("gemmy", CharState.AROUSED)
        gemmy "God, I needed this. I needed to feel wanted again."
        gemmy "Do you want me, [player_name]? Really want me?"
        mc "More than you know. You're sexy as hell, Gemmy."
        mc "I've been hard since you got in my car."
        gemmy "Prove it. Show me how much you want me."
        
        "Things escalate quickly from there..."
        
        jump gemmy_date_success

label gemmy_date_fail:
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.SAD)
    with fade
    
    mc "(Fuck. I completely blew that.)"
    mc "(She was literally ready to do anything, and I chickened out.)"
    mc "(Now she thinks I'm just another weak loser like Craig said.)"
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate
    
    bull_phone "What the FUCK was that?!"
    bull_phone "She was on her knees, ready to suck your dick, and you STOPPED her?!"
    bull_phone "Are you gay? Impotent? Just stupid?"
    mc "I don't know! I just... panicked."
    bull_phone "You panicked. With a hot MILF's mouth around your cock."
    bull_phone "This is why you were a virgin for so long."
    bull_phone "This is why [girl_friend] cheated on you."
    bull_phone "Because you're a fucking coward!"
    mc "I know, okay? I fucked up."
    bull_phone "You did more than fuck up. You ruined our entire plan."
    bull_phone "Now Gemmy's going to tell Craig you're a pussy, and he'll laugh even harder."
    bull_phone "We're back to square one, you idiot."
    
    jump episode_4_continue_ersa

label gemmy_date_success:
    $ butcher_blackmail_success = True
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    $ all_naked = False
    with fade
    
    mc "(Holy shit. That actually worked.)"
    
    mc "(Gemmy was incredible. And now we have the perfect leverage against Craig.)"
    mc "(Time to edit this video and send it anonymously.)"
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    bull_phone "Now THAT'S what I'm talking about!"
    bull_phone "Did you see her face when you came? Pure victory!"
    bull_phone "Craig's going to shit himself when he sees this."
    mc "She really got into it, didn't she?"
    mc "I think she enjoyed the revenge aspect more than the sex."
    bull_phone "Who cares why she enjoyed it? The point is, she did."
    bull_phone "And now we have phase one complete."
    bull_phone "Time to move on to the ice queen - Ersa."
    mc "Right. Gemmy said she's uptight, educated..."
    mc "I'll need a different approach with her."
    bull_phone "Use that college boy charm. Do your research."
    bull_phone "Find out what makes her tick, what she missed with Craig."
    bull_phone "Then give her everything he didn't."
    mc "Already on it. Time to do some social media stalking."
    
    hide bull
    with pixellate

label episode_4_continue_ersa:
    
    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with Fade(0.5, 5.0, 0.5)
    
    "The next morning, I'm researching everything I can about Ersa."
    "LinkedIn, Facebook, Instagram - painting a picture of Craig's second ex-wife."
    "She's 28, has a master's degree in psychology, works as a guidance counselor."
    "Her social media is full of motivational quotes and bitter posts about 'narcissistic exes.'"
    
    mc "(Perfect. She's educated, analytical, and clearly still angry about Craig.)"
    mc "(The college research angle should work perfectly.)"
    mc "(Let me craft the perfect approach email...)"
    
    "I spend an hour writing and rewriting my message."
    "It needs to sound academic but personal, professional but intriguing."
    
    scene black
    with fade
    "To: ersa.thompson@westfield.edu"
    "Subject: Research Project on Post-Divorce Recovery Patterns"
    ""
    "Dear Ms. Thompson,"
    ""
    "I'm a psychology student at the local college conducting research on recovery patterns following difficult divorces, particularly those involving financial disputes and emotional manipulation."
    ""
    "Your name came up during my preliminary interviews as someone who might have valuable insights to contribute."
    "I understand you have personal experience with these challenges,"
    "and a professional background that could provide unique perspective."
    ""
    "Would you be willing to participate in a confidential interview? I could meet you at your convenience, perhaps over coffee?"
    ""
    "The research aims to help others going through similar situations, and your contribution would be invaluable."
    ""
    "Best regards,"
    "[player_name]"
    
    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    mc "(That should do it. Academic enough to seem legitimate, personal enough to pique her interest.)"
    mc "(And the mention of emotional manipulation will definitely resonate given what I've learned about Craig.)"
    mc "(I should dress professionally for this meeting... first impressions matter.)"
    
    menu:
        "Consider professional business attire":
            label test_choice_rypyi:
            if gemmy_love >= 10:
                mc "Academic meetings require the right image..."
                mc "What outfit conveys serious professional success?"
                jump outfit_58_puzzle
                label outfit_58_puzzle_success:
                    mc "Professional attire makes a strong impression..."
                    mc "This will help me look more mature and credible."
                label outfit_58_puzzle_failure:
                    mc "I'll stick with smart casual for now..."
        "Academic casual is fine":
            label test_choice_skvg4:
            mc "I don't need to overthink the clothing. Smart casual should work."
    "I hit send and wait. To my surprise, she responds within an hour."
    scene black
    with fade
    "From: ersa.thompson@westfield.edu"
    "Re: Research Project on Post-Divorce Recovery Patterns"
    ""
    "Hello [player_name],"
    ""
    "Your research topic is indeed close to my heart, both personally and professionally. I would be happy to contribute to your study."
    ""
    "I'm free Thursday afternoon at 3 PM. There's a quiet café near the college - The Book Nook. Would that work?"
    ""
    "I should mention that my ex-husband was particularly manipulative, so I have quite a bit to share on that subject."
    ""
    "Looking forward to our discussion."
    "Ersa Thompson, M.A."
    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    with fade
    mc "(Excellent. She's already opening up about Craig being manipulative.)"
    mc "(This is going to be easier than I thought.)"
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    bull_phone "Nice work with that email. Very smooth."
    bull_phone "You're learning to adapt your approach to different women."
    bull_phone "Gemmy needed a bad boy to make her feel young again."
    bull_phone "Ersa needs an intellectual equal who understands her pain."
    mc "The research angle gives me an excuse to ask personal questions too."
    mc "Find out exactly what Craig did wrong, then do the opposite."
    bull_phone "Exactly! You're becoming a real player."
    bull_phone "Just remember - the end goal is the same."
    bull_phone "We want both ex-wives on camera, together if possible."
    bull_phone "Can you imagine Craig's face?"
    mc "One step at a time. Let me win over Ersa first."
    mc "She seems more cautious than Gemmy."
    bull_phone "That's why you're playing the long game with her."
    bull_phone "Build trust, show empathy, be everything Craig wasn't."
    bull_phone "Then, when her guard is down..."
    mc "I know. I've got this."
    hide bull
    with pixellate
    # TIME SKIP TO THURSDAY
    scene coffee_shop
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with Fade(0.5, 5.0, 0.5)
    "I arrive at The Book Nook fifteen minutes early."
    "It's a cozy place - shelves of books, soft jazz playing, the perfect atmosphere for an intimate conversation."
    "I order a coffee and pull out a notebook and pen, trying to look like a serious researcher."
    hide mc
    show ersa at ersa_convo
    $ update_character_state("ersa", CharState.NORMAL)
    play music "ES_Things to Do - Dyalla.mp3" volume 0.2
    with fade
    ersa "You must be [player_name]."
    mc "Ms. Thompson! Thank you so much for coming."
    mc "Please, have a seat. Can I get you anything?"
    ersa "Just Ersa is fine. And I'll have a green tea, thank you."
    "I order her tea and take a moment to study her."
    "She's beautiful in a different way than Gemmy - more refined, intellectual."
    "Where Gemmy has curves and fire, Ersa has elegance and ice."
    "She's dressed professionally but fashionably, every detail carefully considered."
    ersa "So, tell me about your research."
    ersa "Post-divorce recovery patterns, particularly involving manipulation?"
    mc "Yes. I'm studying how people rebuild their lives after leaving toxic relationships."
    mc "Especially when financial control and emotional abuse were factors."
    mc "Your background in psychology gives you unique insight into these patterns."
    $ update_character_state("ersa", CharState.HAPPY)
    ersa "That's very perceptive. Most people just want to hear the dirty details."
    ersa "But you're right - understanding the psychology is crucial."
    ersa "Are you recording this?"
    mc "Only notes, if that's okay. I want this to feel like a conversation, not an interrogation."
    ersa "I appreciate that. Where should we start?"
    menu:
        "Tell me about the early warning signs you missed.":
            label test_choice_c6bao:
            $ win_sound()
            $ ersa_love += 5
            mc "Tell me about the early warning signs you missed."
            mc "In hindsight, what should have told you he wasn't who he pretended to be?"
            $ update_character_state("ersa", CharState.SAD)
            ersa "Oh, there were so many. But I was young, in love..."
            ersa "He love-bombed me at first. Flowers every day, constant texts, grand gestures."
            ersa "I thought it was romantic. Now I know it was manipulation."
            ersa "He was establishing control, making me dependent on his validation."
            mc "That must have been hard to recognize at the time."
            ersa "Exactly! Everyone said I was so lucky to have such an attentive boyfriend."
            ersa "But it was suffocating. He needed to know where I was every moment."
            ersa "If I didn't text back immediately, he'd accuse me of cheating."
            ersa "Classic narcissistic behavior - projection of his own infidelity."
        "What attracted you to him initially?":
            label test_choice_c4c7i:
            $ win_sound()
            $ ersa_love += 5
            mc "What attracted you to him initially?"
            mc "Before things went wrong, what drew you in?"
            ersa "He was so different from the men I'd dated before."
            ersa "I was used to intellectuals - soft-spoken, careful, perhaps a bit boring."
            ersa "Craig was raw, masculine, confident. He seemed so sure of himself."
            ersa "He made me feel protected, desired in a primal way."
            mc "The bad boy appeal?"
            $ update_character_state("ersa", CharState.NORMAL)
            ersa "Exactly. My therapist calls it 'repetition compulsion.'"
            ersa "We're drawn to what's familiar, even if it's unhealthy."
            ersa "My father was domineering too. I mistook control for strength."
            ersa "Craig knew exactly how to push those buttons."
        "How long were you together?":
            label test_choice_vh7p3:
            $ lose_sound()
            mc "How long were you together?"
            ersa "Three years total. One dating, two married."
            ersa "Though I'd say the real relationship ended after six months."
            ersa "The rest was just me trying to fix something irreparably broken."
            mc "That's a common pattern, right?"
            ersa "Very common. We call it the sunk cost fallacy."
            ersa "You've invested so much, you can't bear to walk away."
            ersa "Even when staying costs you more every day."
    ersa "But enough about the timeline. You want to know about the manipulation, right?"
    ersa "The real psychological warfare?"
    mc "Yes, please. Whatever you're comfortable sharing."
    $ update_character_state("ersa", CharState.ANGRY)
    ersa "Comfortable? I'm past comfortable. I'm angry."
    ersa "Do you know what it's like to have your reality constantly questioned?"
    ersa "Craig was a master gaslighter. He'd do something awful, then convince me I was crazy for being upset."
    ersa "He'd flirt with other women in front of me, then say I was paranoid and jealous."
    ersa "He'd spend our savings on stupid things, then blame me for being controlling about money."
    "She's getting worked up now, her professional composure cracking."
    "This is good - the more emotional she gets, the more she'll share."
    mc "That sounds incredibly damaging. How did it affect your sense of self?"
    $ update_character_state("ersa", CharState.SAD)
    ersa "I lost myself completely. I didn't trust my own perceptions anymore."
    ersa "I'd apologize for things that weren't my fault. I'd doubt my own memories."
    ersa "The worst part? I have a master's in psychology! I knew the signs!"
    ersa "But when you're in it, when it's happening to you..."
    ersa "Love makes you stupid. Or maybe it wasn't love at all."
    menu:
        "It wasn't love. It was trauma bonding.":
            label test_choice_ycc1e:
            $ win_sound()
            $ ersa_love += 10
            mc "It wasn't love. It was trauma bonding."
            mc "The intensity you felt was your nervous system trying to survive."
            $ update_character_state("ersa", CharState.NORMAL)
            ersa "Yes! Exactly! You understand!"
            ersa "The highs were so high because the lows were so low."
            ersa "That intermittent reinforcement is more addictive than any drug."
            mc "And he knew exactly when to give you just enough hope to keep you hooked."
            ersa "God, yes. Just when I'd work up the courage to leave..."
            ersa "He'd suddenly be the man I fell in love with again."
            ersa "Flowers, apologies, promises to change."
            ersa "And I'd fall for it every time like an idiot."
            mc "You weren't an idiot. You were being systematically broken down."
            mc "That takes incredible strength to survive, let alone escape."
            $ update_character_state("ersa", CharState.HAPPY)
            ersa "You know, you're very insightful for an undergrad."
            ersa "Most people your age don't understand these dynamics."
        "Sometimes smart people are the easiest to manipulate.":
            label test_choice_x65ff:
            $ win_sound()
            $ ersa_love += 5
            mc "Sometimes smart people are the easiest to manipulate."
            mc "You overthink, rationalize, give benefit of the doubt."
            ersa "That's... actually very true."
            ersa "I kept thinking I could fix him if I just understood him better."
            ersa "I'd analyze his behavior, make excuses, create elaborate psychological profiles."
            ersa "Meanwhile, he was just an asshole who wanted control."
            mc "Occam's razor - the simplest explanation is usually correct."
            ersa "Exactly. But I needed it to be complicated."
            ersa "Because if he was just an asshole, what did that say about me for choosing him?"
        "Love does make people blind to red flags.":
            label test_choice_a1s4z:
            $ lose_sound()
            mc "Love does make people blind to red flags."
            ersa "It wasn't love. I see that now."
            ersa "It was need, dependency, fear of being alone."
            ersa "Real love doesn't require you to lose yourself."
            mc "How do you know the difference?"
            ersa "Experience. Therapy. A lot of painful self-reflection."
            ersa "And learning to be alone without being lonely."
    $ update_character_state("ersa", CharState.NORMAL)
    ersa "But I'm curious - why this specific research topic?"
    ersa "Most undergrads study easier subjects. This is heavy material."
    mc "I... I've seen the damage these relationships can do."
    mc "Someone close to me went through something similar."
    mc "(Not entirely a lie. [girl_friend] was manipulative in her own way.)"
    ersa "I'm sorry. It's hard to watch someone you care about suffer like that."
    ersa "Is that person okay now?"
    mc "Getting better every day. Learning to trust again."
    mc "Actually, talking to you is helping me understand their experience better."
    $ update_character_state("ersa", CharState.HAPPY)
    ersa "I'm glad I could help. It's therapeutic for me too, honestly."
    ersa "I don't often get to discuss this with someone who actually understands."
    ersa "My friends just want me to 'move on' and 'find someone new.'"
    ersa "As if it's that simple."
    menu:
        "Healing isn't linear. You move at your own pace.":
            label test_choice_6vly9:
            $ win_sound()
            $ ersa_love += 10
            mc "Healing isn't linear. You move at your own pace."
            mc "And 'moving on' doesn't mean jumping into another relationship."
            mc "Sometimes it means learning to be whole on your own first."
            $ update_character_state("ersa", CharState.HAPPY)
            ersa "Yes! Thank you! Someone who gets it!"
            ersa "I've been single for two years and people act like I'm broken."
            ersa "But I'm not looking for someone to complete me anymore."
            ersa "I'm already complete. I just want someone to complement me."
            mc "That's beautiful. And incredibly healthy."
            mc "You've done the work most people avoid their entire lives."
            ersa "You really think so?"
            mc "I know so. Your self-awareness is remarkable."
            mc "Craig lost something precious when he lost you."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "That's... that's very kind of you to say."
            ersa "You know, you're nothing like I expected a college guy to be."
        "Maybe they're right. New experiences can help heal old wounds.":
            label test_choice_owwac:
            $ win_sound()
            $ ersa_love += 5
            mc "Maybe they're right, in a way."
            mc "New experiences can help heal old wounds."
            mc "Not necessarily a relationship, but connections, friendships..."
            mc "Reminders that not everyone is like your ex."
            ersa "I suppose. I've been very isolated."
            ersa "It's hard to trust anyone after what I went through."
            mc "Understandable. But isolation can become its own prison."
            mc "Maybe start small? Coffee with new people, casual conversations?"
            ersa "Like this one?"
            mc "Exactly like this one. See? You're already healing."
            ersa "You're sweet. Wise beyond your years."
        "Finding someone new might help you forget Craig.":
            label test_choice_a6fo0:
            $ lose_sound()
            mc "Finding someone new might help you forget Craig."
            ersa "Forget him? I don't want to forget."
            ersa "Those experiences, horrible as they were, shaped me."
            ersa "I want to integrate them, learn from them, not forget."
            mc "Sorry, I didn't mean-"
            ersa "It's fine. You're young. You think love fixes everything."
            ersa "But sometimes love is the problem, not the solution."
    ersa "Can I ask you something personal?"
    mc "Of course."
    ersa "Have you ever been in a manipulative relationship?"
    ersa "You seem to understand the dynamics very well."
    mc "I have, actually. My ex-girlfriend."
    mc "She cheated constantly but made me feel like it was my fault."
    mc "Said I wasn't man enough, that's why she needed others."
    mc "Classic manipulation - destroy your self-worth so you won't leave."
    $ update_character_state("ersa", CharState.ANGRY)
    ersa "Oh honey, I'm so sorry. That's awful."
    ersa "No one deserves that. How did you get out?"
    mc "She left me, actually. For someone with more money and status."
    mc "At the time I was devastated. Now I see it as a gift."
    mc "She showed me who she really was, finally."
    $ update_character_state("ersa", CharState.NORMAL)
    ersa "And now you're researching these patterns to understand what happened?"
    ersa "That's very brave. Most people just bury the pain."
    mc "I want to make sure I never fall for it again."
    mc "And maybe help others avoid the same mistakes."
    ersa "You will. You have the insight and empathy."
    ersa "Don't let her damage define you."
    "We continue talking for another hour."
    "Ersa opens up more and more, sharing intimate details about Craig's failures."
    "How he never complimented her intellect, only her body."
    "How he forgot anniversaries, birthdays, every meaningful date."
    "How he'd mock her education, call her 'too smart for her own good.'"
    "Each revelation is a roadmap for how to win her over."
    $ update_character_state("ersa", CharState.HAPPY)
    ersa "I can't believe I've talked this long. You're very easy to open up to."
    ersa "I feel like I've known you much longer than two hours."
    mc "I feel the same way. Your insights have been invaluable."
    mc "Both for my research and... personally."
    ersa "I'm glad I could help. This has been therapeutic for me too."
    menu:
        "Would you be willing to meet again? I have follow-up questions.":
            label test_choice_w9iok:
            $ win_sound()
            $ ersa_love += 10
            mc "Would you be willing to meet again? I have follow-up questions."
            mc "Plus, I really enjoyed our conversation."
            mc "You're brilliant, insightful, and surprisingly funny."
            ersa "Surprisingly? What did you expect?"
            mc "Honestly? Someone bitter and closed off."
            mc "Instead, I found someone who turned pain into wisdom."
            mc "Someone who refused to let a bad experience define them."
            $ update_character_state("ersa", CharState.HAPPY)
            ersa "That's... that's the nicest thing anyone's said to me in years."
            ersa "Yes, I'd love to meet again. For your research, of course."
            ersa "I have to admit, I've been quite cold to people lately..."
            ersa "Building walls, freezing people out..."
            menu:
                "Sometimes being cold protects us":
                    label test_choice_s13jn:
                    if ersa_love >= 20:
                        ersa "Exactly... but what happens when you're cold for too long?"
                        ersa "What state does water reach when it's too cold?"
                        jump outfit_27_puzzle
                        label outfit_27_puzzle_success:
                            ersa "But sometimes ice can be beautiful too..."
                            ersa "I have this elegant ice-themed outfit... represents my cold period."
                            ersa "Maybe it's time to start thawing..."
                        label outfit_27_puzzle_failure:
                            ersa "I thought you might understand the cold..."
                "You're warming up now":
                    label test_choice_q85nv:
                    ersa "Maybe I am... with the right person."
            mc "Of course. Purely academic interest."
            mc "Though I won't lie - I'm looking forward to it for more than just research."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "Me too, if I'm being honest."
            ersa "It's been a long time since I've connected with someone like this."
        "I'd love to continue this over dinner sometime.":
            label test_choice_i2pko:
            $ win_sound()
            $ ersa_love += 5
            mc "I'd love to continue this over dinner sometime."
            mc "Somewhere nicer than a coffee shop."
            mc "You deserve to be treated to a proper meal."
            ersa "Are you asking me on a date?"
            ersa "I'm quite a bit older than you..."
            mc "Age is just a number. Connection is what matters."
            mc "And I feel a real connection here. Don't you?"
            $ update_character_state("ersa", CharState.NORMAL)
            ersa "I... I do. But I'm not sure I'm ready for dating."
            ersa "It's been two years, but still..."
            mc "No pressure. Just dinner between two people who understand each other."
            mc "We can talk about whatever you want. Or not talk at all."
            ersa "That does sound nice. Okay. Dinner."
        "Thanks for your time. This was very helpful.":
            label test_choice_61vgc:
            $ lose_sound()
            mc "Thanks for your time. This was very helpful."
            mc "Good luck with everything."
            ersa "Oh. That's it?"
            ersa "I thought... never mind."
            mc "Did you want to add something?"
            ersa "No, no. Just... this was nice."
            ersa "I don't get to talk to people who understand very often."
            mc "Yeah, it was nice. Thanks again."
            ersa "Right. Well. Good luck with your research."
            "She seems disappointed as she gathers her things."
            "Did I misread the situation?"
    ersa "Before I go... can I give you some advice?"
    ersa "From someone who's been through the wringer?"
    mc "Please do."
    $ update_character_state("ersa", CharState.NORMAL)
    ersa "Don't let your ex define your future relationships."
    ersa "What she did was about her brokenness, not your worth."
    ersa "You're clearly intelligent, empathetic, and mature beyond your years."
    ersa "Any woman would be lucky to have someone who listens like you do."
    mc "Thank you, Ersa. That means a lot."
    mc "Especially coming from someone as remarkable as you."
    $ update_character_state("ersa", CharState.HAPPY)
    ersa "Flatterer. But I'll take it."
    ersa "I haven't felt remarkable in a very long time."
    "We exchange numbers and make plans to meet again in a few days."
    "As she leaves, she touches my arm gently - a small gesture, but significant."
    "I watch her walk away, already planning our next encounter."
    stop music fadeout 1.0
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    with fade
    mc "(That went perfectly. She's hooked.)"
    mc "(All those details about Craig - I know exactly what she needs now.)"
    mc "(Attention, validation, intellectual stimulation, respect...)"
    mc "(Everything that asshole denied her.)"
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    bull_phone "Smooth as silk! You played that beautifully."
    bull_phone "The research angle, the shared trauma, the emotional connection..."
    bull_phone "She's practically begging for someone to treat her right."
    mc "She's more complex than Gemmy. This will take time."
    mc "But I think the payoff will be worth it."
    bull_phone "Definitely. Did you hear all those things Craig did wrong?"
    bull_phone "Never complimented her mind, forgot important dates, mocked her education..."
    bull_phone "It's like he gave you a blueprint for seduction."
    mc "That's the plan. Be everything he wasn't."
    mc "Attentive, respectful, intellectually engaging."
    mc "Make her feel like the brilliant woman she is."
    bull_phone "And then?"
    mc "Then we film something even better than what we got with Gemmy."
    mc "And eventually... bring them together."
    bull_phone "Both ex-wives at once. Craig will have a heart attack."
    mc "He deserves it. And they deserve their revenge."
    hide bull
    with pixellate
    # SEVERAL DAYS LATER - SECOND MEETING WITH ERSA
    scene restaurant_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    with Fade(0.5, 5.0, 0.5)
    "I chose an upscale restaurant for our second meeting."
    "Not too fancy - that would seem try-hard - but nice enough to show respect."
    "I even bought a new shirt for the occasion."
    "When Ersa arrives, she takes my breath away."
    hide mc
    play music "ES_Things to Do - Dyalla.mp3" volume 0.2
    show ersa at ersa_convo
    $ update_character_state("ersa", CharState.HAPPY)
    with fade
    "She's dressed in a elegant black dress that hugs her slim figure."
    "Her hair is styled differently - softer, more romantic."
    "She's clearly put effort into her appearance."
    ersa "I hope I'm not overdressed. You said somewhere nice..."
    mc "You look absolutely stunning. That dress is perfect on you."
    mc "It brings out your eyes."
    $ update_character_state("ersa", CharState.AROUSED)
    ersa "Thank you. You clean up well yourself."
    ersa "I wasn't sure what to expect. This feels more like a date than research."
    mc "Maybe it's both? I did promise follow-up questions."
    mc "But I'd be lying if I said I wasn't more interested in getting to know you."
    mc "The brilliant woman behind the academic insights."
    ersa "Flatterer. But please, continue."
    ersa "It's been too long since someone appreciated my mind."
    "We're seated at a quiet corner table."
    "I make sure to pull out her chair - small gestures Craig probably never bothered with."
    "The waiter brings menus and I suggest wine."
    mc "What's your preference? Red? White?"
    ersa "You're old enough to order wine?"
    mc "I'm old enough for a lot of things."
    mc "But if it makes you uncomfortable..."
    ersa "No, no. Wine sounds perfect. Red, please."
    ersa "Something bold. I'm feeling adventurous tonight."
    "I order a bottle of Malbec, remembering from her social media that it's her favorite."
    "Her eyes widen slightly when I make the selection."
    $ update_character_state("ersa", CharState.HAPPY)
    ersa "How did you know I love Malbec?"
    menu:
        "Lucky guess. You seem like a woman who appreciates complexity.":
            label test_choice_6csfr:
            $ win_sound()
            $ ersa_love += 10
            mc "Lucky guess. You seem like a woman who appreciates complexity."
            mc "Malbec is sophisticated, layered, improves with age..."
            mc "Much like yourself."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "My god, you're dangerous with those lines."
            ersa "Do they usually work on college girls?"
            mc "I wouldn't know. I'm not interested in girls."
            mc "I prefer women. Intelligent, experienced, self-aware women."
            mc "Women who've lived, loved, learned, and emerged stronger."
            ersa "And where do you find these women?"
            mc "Apparently, researching post-divorce recovery patterns."
            mc "Who knew academic research could be so... stimulating?"
            $ update_character_state("ersa", CharState.HAPPY)
            ersa "Indeed. Very stimulating research."
        "I may have stalked your social media a little.":
            label test_choice_5bmxb:
            $ win_sound()
            $ ersa_love += 5
            mc "I may have stalked your social media a little."
            mc "For research purposes, of course."
            mc "You posted about a wine tasting last month."
            ersa "Checking up on me? Should I be flattered or concerned?"
            mc "Flattered, I hope. I wanted tonight to be perfect."
            mc "You deserve to have your preferences remembered."
            ersa "Craig never remembered anything I liked."
            ersa "He'd order for me without asking, always getting it wrong."
            mc "Then he was a fool. Your preferences matter."
            mc "Your opinions, your tastes, your desires... they all matter."
            ersa "My desires?"
            ersa "I love dramatic performances... the arts... especially opera..."
            ersa "The passion, the powerful voices reaching incredible heights..."
            menu:
                "Tell me about opera":
                    label test_choice_70n3t:
                    if ersa_love >= 30:
                        ersa "The emotion, the drama! What do opera singers perform with such passion?"
                        jump outfit_29_puzzle
                        label outfit_29_puzzle_success:
                            ersa "I actually have this gorgeous opera gown... from when I sang in college..."
                            ersa "Maybe I'll perform for you someday... privately..."
                        label outfit_29_puzzle_failure:
                            ersa "I thought you might appreciate the dramatic arts..."
                "All your desires matter":
                    label test_choice_ik8eq:
                    mc "All of them."
        "Red wine pairs well with red meat. Basic pairing.":
            label test_choice_f5s43:
            $ lose_sound()
            mc "Red wine pairs well with red meat. Basic pairing."
            ersa "Oh. Practical choice then."
            ersa "For a moment I thought..."
            ersa "Never mind. It's a good selection."
            mc "You thought what?"
            ersa "Nothing. Let's look at the menu."
            "The moment feels awkward. I've disappointed her somehow."
    "We order our meals - she chooses the salmon, I get the steak."
    "As we wait, I steer the conversation back to safer ground."
    mc "I've been thinking about our last conversation."
    mc "About healing and moving forward."
    mc "You mentioned not dating for two years. That must be lonely sometimes."
    $ update_character_state("ersa", CharState.SAD)
    ersa "It is. But loneliness is better than being with the wrong person."
    ersa "I'd rather be alone than diminished."
    mc "You shouldn't have to choose. The right person would elevate you, not diminish you."
    mc "They'd celebrate your intelligence, your accomplishments."
    mc "They'd be proud to be with someone so remarkable."
    $ update_character_state("ersa", CharState.NORMAL)
    ersa "You keep calling me remarkable. I'm starting to believe you mean it."
    mc "I absolutely mean it. Your strength, your insight, your resilience..."
    mc "The way you've rebuilt yourself after everything Craig put you through..."
    mc "You're not just remarkable. You're inspiring."
    $ update_character_state("ersa", CharState.HAPPY)
    ersa "Stop, you're going to make me cry."
    ersa "And I spent too long on my makeup for that."
    mc "Then let me make you smile instead."
    mc "Tell me something that makes you happy. Something Craig never asked about."
    ersa "I... I love to dance. Ballroom, specifically."
    ersa "I took lessons before I met Craig, competed even."
    ersa "He said it was stupid. A waste of time and money."
    ersa "So I stopped."
    menu:
        "Would you teach me? I'd love to learn from you.":
            label test_choice_azpwt:
            $ win_sound()
            $ ersa_love += 10
            mc "Would you teach me? I'd love to learn from you."
            mc "I can't imagine anything more elegant than dancing with you."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "You want to learn ballroom? Really?"
            mc "I want to learn what makes you happy."
            mc "If that's ballroom dancing, then yes, absolutely."
            mc "When can we start?"
            ersa "You're serious."
            mc "Completely. I bet you're an amazing teacher."
            mc "Patient, knowledgeable, graceful..."
            ersa "There's a studio near the mall. They have practice rooms."
            ersa "We could... we could go sometime. If you really want to."
            mc "It's a date. Though I should warn you, I might step on your toes."
            ersa "I'll risk it. It's been so long since I danced with anyone."
            ersa "Craig refused to even try. Said it was 'gay.'"
            mc "Craig's an insecure idiot. Real men aren't afraid of dancing."
            mc "Real men do whatever it takes to make their woman happy."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "Their woman?"
            mc "Figure of speech. Unless..."
        "That's beautiful. You should start dancing again.":
            label test_choice_u1s3j:
            $ win_sound()
            $ ersa_love += 5
            mc "That's beautiful. You should start dancing again."
            mc "Don't let his ignorance steal your joy forever."
            ersa "I've thought about it. But dancing alone feels sad."
            ersa "It's meant to be shared, you know?"
            mc "Then find a new partner. Someone who appreciates the art."
            mc "Someone who'd be honored to dance with you."
            ersa "Are you volunteering?"
            mc "If you'd have me. Though I'm a complete beginner."
            ersa "Everyone starts somewhere."
            ersa "The important thing is being willing to try."
        "Dancing? Isn't that kind of old-fashioned?":
            label test_choice_0ngf8:
            $ lose_sound()
            $ ersa_love -= 5
            mc "Dancing? Isn't that kind of old-fashioned?"
            $ update_character_state("ersa", CharState.ANGRY)
            ersa "Old-fashioned? It's classical, elegant."
            ersa "But I suppose to someone your age..."
            mc "No, I didn't mean it like that-"
            ersa "You sounded just like Craig for a moment."
            ersa "Dismissing something just because you don't understand it."
            mc "I'm sorry. You're right. Tell me more about it."
            ersa "The moment's passed. Let's talk about something else."
    "Our food arrives, and the conversation flows more easily."
    "I make sure to ask her opinion on everything - the wine, the ambiance, current events."
    "Each time she shares a thought, I listen intently, ask follow-up questions."
    "I can see her blooming under the attention."
    $ update_character_state("ersa", CharState.HAPPY)
    ersa "I have to say, this is the best evening I've had in years."
    ersa "You're an excellent conversationalist."
    mc "That's because you're fascinating to talk to."
    mc "Your perspectives on psychology, on life... I could listen for hours."
    ersa "Craig used to tell me I talked too much."
    ersa "Especially about my work. He said it was boring."
    mc "Then he missed out on understanding an incredible mind."
    mc "Tell me about your most interesting case - without violating confidentiality, of course."
    "She launches into a story about helping a student overcome trauma."
    "Her passion for her work is evident, her eyes lighting up as she speaks."
    "I maintain eye contact, nodding, asking thoughtful questions."
    "This is what she needed - someone who values her intellect."
    $ update_character_state("ersa", CharState.AROUSED)
    ersa "I'm sorry, I'm monopolizing the conversation."
    ersa "Craig always said I did that."
    mc "Stop apologizing for being interesting."
    mc "And stop bringing up Craig. He doesn't deserve space in your thoughts."
    mc "Tonight is about you. The brilliant, beautiful woman across from me."
    mc "Not the ghost of an insecure man who couldn't appreciate what he had."
    ersa "You're right. I'm sorry- no, I'm not apologizing anymore."
    ersa "Thank you for reminding me I don't need to shrink myself."
    mc "Never shrink yourself. Not for anyone."
    mc "You're perfect exactly as you are."
    "The waiter brings the dessert menu."
    "Ersa demurs at first - 'I shouldn't' - but I insist."
    mc "Life's too short to deny yourself pleasure."
    mc "What do you want? Really want?"
    $ update_character_state("ersa", CharState.AROUSED)
    ersa "The chocolate lava cake. I always want the chocolate lava cake."
    mc "Then you shall have it. Two spoons?"
    ersa "You want to share dessert with me?"
    mc "I want to share more than just dessert with you."
    mc "But let's start with chocolate."
    "We share the dessert, and the intimacy of it isn't lost on either of us."
    "She laughs when I get chocolate on my chin."
    "I love the sound - free, uninhibited, joyful."
    ersa "I feel like a teenager again."
    ersa "Is that weird? You make me feel young."
    mc "You are young. Twenty-eight is nothing."
    mc "Craig made you feel old because he's a bitter middle-aged man."
    mc "But you're in your prime. Brilliant, beautiful, accomplished."
    mc "Any man would be lucky to be here with you."
    menu:
        "I'm the luckiest man in this restaurant right now.":
            label test_choice_kook2:
            $ win_sound()
            $ ersa_love += 10
            mc "I'm the luckiest man in this restaurant right now."
            mc "Maybe in the whole city."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "You can't possibly mean that."
            mc "Look around. Every man here has noticed you."
            mc "But I'm the one who gets to hear your laugh, see your smile."
            mc "Learn what makes you tick, what brings you joy."
            mc "If that's not lucky, I don't know what is."
            ersa "I... I don't know what to say."
            mc "Say you'll let me see you again."
            mc "Say this doesn't have to end tonight."
            ersa "It doesn't have to end?"
            mc "Not unless you want it to."
            mc "We could go for a walk, have another drink..."
            mc "Or I could take you dancing right now, if you know a place."
            $ update_character_state("ersa", CharState.HAPPY)
            ersa "You really want to dance with me?"
            mc "More than anything."
        "Age really is just a number when the connection is real.":
            label test_choice_f00ij:
            $ win_sound()
            $ ersa_love += 5
            mc "Age really is just a number when the connection is real."
            mc "And this... this feels real to me. Does it to you?"
            ersa "It does. Surprisingly, wonderfully real."
            ersa "I came here expecting to help with research."
            ersa "Instead, I found..."
            mc "Found what?"
            ersa "I'm not sure yet. But something. Something good."
            mc "I know what I found."
            mc "Someone who challenges me, inspires me, makes me want to be better."
            ersa "Now you're just flattering me."
            mc "Is it working?"
            ersa "...Yes."
        "You're not that much older than me, really.":
            label test_choice_5pi86:
            $ lose_sound()
            mc "You're not that much older than me, really."
            mc "Just a few years."
            ersa "Six years. That's significant at our ages."
            ersa "You're still in college. I have a career, baggage..."
            mc "Everyone has baggage."
            ersa "Not like mine. I'm divorced, bitter, in therapy..."
            ersa "You should be with someone young, optimistic, undamaged."
            mc "I don't want undamaged. I want real."
            ersa "Real is messy."
            mc "Then let's be messy together."
    "The check comes, and I pay without hesitation."
    "She protests, but I insist - 'You honored me with your time.'"
    "As we leave the restaurant, she links her arm through mine."
    "The gesture is natural, comfortable."
    scene mall_interior_night
    show ersa at ersa_convo
    $ update_character_state("ersa", CharState.HAPPY)
    with fade
    "We walk through the nearly empty mall, most shops closed for the evening."
    "The soft lighting and quiet atmosphere makes it feel almost romantic."
    ersa "This has been wonderful. Really."
    ersa "I haven't felt this... alive in so long."
    mc "The night doesn't have to end. Unless you have somewhere to be?"
    ersa "I... no. No, I don't."
    ersa "What did you have in mind?"
    menu:
        "Come back to my place. We can talk more privately.":
            label test_choice_u4rnt:
            $ win_sound()
            $ ersa_love += 10
            mc "Come back to my place. We can talk more privately."
            mc "I have wine, comfortable couches, good music..."
            mc "And no waiters hovering."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "Your place? Isn't that a bit..."
            mc "Forward? Maybe. But I'm not ready for this evening to end."
            mc "Are you?"
            ersa "No. No, I'm not."
            ersa "But I haven't been to a man's place since... since Craig."
            mc "Then it's time to make new memories."
            mc "Better memories. With someone who actually appreciates you."
            ersa "You make it sound so simple."
            mc "It is simple. Two people who enjoy each other's company."
            mc "No pressure, no expectations. Just... possibility."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "Possibility. I like that."
            ersa "Okay. Your place. But just talking."
            mc "Of course. Whatever you're comfortable with."
            mc "I'm just happy to spend more time with you."
        "There's a wine bar nearby. We could continue our conversation.":
            label test_choice_4mbvc:
            $ win_sound()
            $ ersa_love += 5
            mc "There's a wine bar nearby. We could continue our conversation."
            mc "Quiet, intimate, great selection..."
            ersa "More wine? You're trying to get me drunk."
            mc "Never. I want you clear-headed and present."
            mc "I want you to remember every moment of tonight."
            ersa "I don't think I could forget if I tried."
            ersa "Wine bar sounds perfect."
            mc "Great. And after that, if you're not too tired..."
            mc "Maybe you could show me some basic dance steps?"
            ersa "You really want to learn?"
            mc "I really want to learn from you."
            ersa "Then I'll teach you. But I warn you, I'm a demanding instructor."
            mc "I wouldn't have it any other way."
        "I should probably get you home. It's getting late.":
            label test_choice_6ssyx:
            $ lose_sound()
            $ ersa_love -= 5
            mc "I should probably get you home. It's getting late."
            $ update_character_state("ersa", CharState.SAD)
            ersa "Oh. Yes, of course."
            ersa "I suppose it is late."
            mc "I had a wonderful time tonight."
            ersa "So did I. Thank you for dinner."
            ersa "And for listening. For seeing me."
            mc "Always. Can I call you?"
            ersa "Sure. For your research, right?"
            mc "Right. Research."
            "The energy has shifted. She seems disappointed."
            "I've moved too slowly, been too cautious."
    if ersa_right >= 4:
        jump ersa_seduction_success
    else:
        jump ersa_seduction_continued

label ersa_seduction_success:
    
    scene home_night
    show ersa at ersa_convo
    $ update_character_state("ersa", CharState.NORMAL)
    with fade
    
    "Back at my place, Ersa seems nervous but excited."
    "I pour us wine and put on soft jazz - sophisticated, romantic."
    "We sit on the couch, closer than before."
    
    ersa "Your place is nice. Cleaner than I expected from a college student."
    mc "I cleaned specifically for you."
    mc "I wanted everything to be perfect."
    ersa "You really planned all this? The restaurant, the wine, everything?"
    mc "I told you - you deserve to be treated well."
    mc "To have someone put in effort, remember details, make you feel special."
    
    $ update_character_state("ersa", CharState.AROUSED)
    ersa "Mission accomplished. I feel very special right now."
    ersa "Also a little scared."
    mc "Scared? Of me?"
    ersa "Of this. Of feeling things I thought were dead."
    ersa "You've awakened something in me tonight."
    
    "She sets down her wine glass and turns to face me fully."
    "There's hunger in her eyes now, mixed with vulnerability."
    
    ersa "I haven't been with anyone since Craig."
    ersa "Haven't wanted to be. Until now."
    mc "We don't have to do anything you're not ready for."
    ersa "That's the problem. I think I'm too ready."
    ersa "You've been perfect tonight. Attentive, respectful, engaging..."
    ersa "Everything he wasn't. Everything I needed."
    ersa "I love sophisticated events... elegant parties with mystery and intrigue..."
    ersa "The kind where people wear masks and beautiful gowns..."
    
    menu:
        "Tell me about these elegant parties":
            label test_choice_s1voa:
            if ersa_love >= 35:
                ersa "Masquerade balls... where secrets hide behind elegant facades..."
                ersa "What creates mystery and intrigue at such events?"
                jump outfit_28_puzzle
                label outfit_28_puzzle_success:
                    ersa "I have this stunning masquerade outfit... black silk and lace..."
                    ersa "Maybe you'd like to escort me to such an event someday..."
                label outfit_28_puzzle_failure:
                    ersa "I thought you might appreciate the elegance of mystery..."
        "Then let me keep being what you need.":
            label test_choice_e0aen:
            $ ersa_love += 10
            mc "Then let me keep being what you need."
            mc "Tonight, tomorrow, for as long as you'll let me."
            "I reach out and cup her face gently."
            "She leans into my touch, eyes fluttering closed."
            mc "You're so beautiful, Ersa. So brilliant and strong."
            mc "Any man who couldn't see that is a fool."
            $ update_character_state("ersa", CharState.AROUSED)
            ersa "Kiss me."
            ersa "Please. I need to know this is real."
            "Our lips meet, and it's electric."
            "All her pent-up desire pours out in that kiss."
            "Her hands tangle in my hair as she pulls me closer."
            "When we break apart, we're both breathing hard."
            ersa "Oh god. I'd forgotten what good kissing felt like."
            mc "That's just the beginning."
            mc "I want to worship every inch of you."
            mc "Show you how a real man treats a goddess."
        "You deserve to feel desired again.":
            label test_choice_gjhh7:
            $ ersa_love += 5
            mc "You deserve to feel desired again."
            mc "To remember what it's like to be wanted, cherished, adored."
            ersa "Is that what you're offering? Adoration?"
            mc "Among other things."
            mc "But yes, I adore your mind, your strength, your beauty."
            mc "Let me show you how much."
            "I lean in slowly, giving her time to pull away."
            "Instead, she meets me halfway."
            "The kiss is tender at first, then passionate."
            ersa "I want you. God help me, I want you so much."
            mc "Then have me. All of me."
        "Are you sure? I don't want to rush you.":
            label test_choice_7s49r:
            $ lose_sound()
            mc "Are you sure? I don't want to rush you."
            ersa "Rush me? We've been building to this all night."
            ersa "Unless... unless you don't want to?"
            mc "No! I do. I just want to be respectful."
            ersa "I'm a grown woman. I know what I want."
            ersa "The question is, do you?"
            mc "Yes. I want you."
            ersa "Then stop talking and show me."
    $ update_character_state("ersa", CharState.AROUSED)
    ersa "Wait. There's something I need to know first."
    ersa "This isn't just about your research, is it?"
    ersa "Or some conquest to brag about to your friends?"
    mc "No. This is about you and me."
    mc "About two people who understand each other's pain."
    mc "Who can maybe heal together."
    ersa "Together. I like the sound of that."
    ersa "But I need you to know - I'm not looking for another relationship."
    ersa "Not yet. Maybe not ever."
    mc "I'm not asking for forever. Just tonight."
    mc "Let me make you feel good. Let me erase his touch from your memory."
    mc "Let me show you what you've been missing."
    ersa "Yes. God, yes."
    ersa "But... can we film it?"
    mc "What?"
    ersa "I know it sounds crazy, but..."
    ersa "I want proof this happened. That someone wanted me like this."
    ersa "That I'm still desirable, still capable of passion."
    ersa "And maybe... maybe I want Craig to know too."
    menu:
        "I was thinking the same thing. Let him see what he lost.":
            label test_choice_l4l2d:
            $ ersa_love += 10
            $ ersa_reverse_cowgirl_scene = True
            mc "I was thinking the same thing. Let him see what he lost."
            mc "See his ex-wife in ecstasy with someone who actually appreciates her."
            ersa "You don't think I'm crazy?"
            mc "I think you're perfect."
            mc "And if documenting your liberation helps you heal, I'm all for it."
            mc "Besides, the thought of that asshole seeing you like this..."
            mc "Seeing what he can never have again... it's poetic justice."
            ersa "Set up the camera. I want him to see everything."
            ersa "Want him to see me beg for another man's touch."
            ersa "Want him to know he's been replaced by someone better."
            mc "With pleasure. But are you sure you're ready for this?"
            ersa "I've been ready for two years."
            ersa "I just needed someone worth breaking my celibacy for."
        "If that's what you want, I'm happy to help.":
            label test_choice_t9bcc:
            $ ersa_love += 5
            $ ersa_reverse_cowgirl_scene = True
            mc "If that's what you want, I'm happy to help."
            mc "Your pleasure, your rules."
            ersa "Really? Most men would be worried about being filmed."
            mc "I'm not most men."
            mc "And I have nothing to hide. Let the camera see how much I worship you."
            ersa "Worship? You really do know what to say."
            mc "It's not just words. Let me prove it."
            mc "Let me show you and the camera what real desire looks like."
            ersa "Yes. Show me. Show him. Show everyone."
            ersa "I want the world to know I'm desired."
        "That seems risky. What if it gets out?":
            label test_choice_8izs7:
            $ lose_sound()
            $ ersa_love -= 5
            mc "That seems risky. What if it gets out?"
            mc "Your career, your reputation..."
            ersa "You're right. It's a stupid idea."
            ersa "I'm just... I'm angry and horny and not thinking clearly."
            mc "We can still have fun without filming."
            ersa "No, the moment's ruined."
            ersa "You're being sensible and I'm being reckless."
            ersa "Maybe this whole thing is a mistake."
            mc "It's not a mistake. I want you."
            ersa "But not enough to risk anything for it."
            ersa "Just like Craig. Always playing it safe."
            jump ersa_seduction_fail
    
    if ersa_reverse_cowgirl_scene:
        "I set up my phone to capture the couch area."
        "Ersa watches, her breathing already heavy with anticipation."
        "When I return to her, she pulls me down for a fierce kiss."
        
        $ update_character_state("ersa", CharState.AROUSED)
        ersa "I want to show Craig something special."
        ersa "Something he never got to experience with me."
        ersa "I want to ride you... but in a way that shows him everything he's missing."
        mc "Whatever you want. This is your show."
        mc "I'm here to give you exactly what you need."

        scene black
        with fade
        
        "We start kissing passionately as clothes come off."
        "My hands explore her naked body, finding all her sensitive spots."
        "She moans when I tease her, already wet with anticipation."
        
        ersa "Yes... I need you inside me."
        ersa "Craig never made me feel this desperate."
        ersa "Never made me crave it like this."
        mc "Turn around. Show the camera everything."
        mc "Let him see what he lost."
        
        "She positions herself facing away from me."
        "Her perfect ass on display as she lowers herself onto my cock."
        "She gasps as I fill her completely."
        
        scene scene_17
        $ persistent.scene_17 = True
        stop music fadeout 1.0
        play sound "audio/VOICE_WOMAN_A_PLEASURE_MOAN_SHORT_03.mp3"
        with fade
        
        "Ersa begins riding me in reverse cowgirl, her movements confident and sensual."
        "As she bounces on my cock, she reaches back and starts fingering her ass."
        "The visual is incredible - and perfectly framed for the camera."
        
        ersa "Oh god... I'm so full. So fucking full."
        ersa "Craig never filled me like this. Never hit these spots."
        mc "You're incredible. The way you're taking me..."
        mc "And watching you play with yourself like that..."
        mc "Fuck, you're the sexiest woman I've ever seen."
        
        "She speeds up, her fingers working deeper into her ass."
        "Her moans grow louder as she pleasures both holes."
        "The sight of her touching herself while riding me is overwhelming."
        
        ersa "I'm close... fuck, having both holes stimulated..."
        ersa "Craig would never... he said it was dirty..."
        mc "It's perfect. You're perfect."
        mc "Come for me, beautiful. Show him what real pleasure looks like."
        $ play_man_pleasure_sound()
        
        "She screams as she climaxes, her body convulsing."
        $ play_woman_pleasure_sound()
        $ play_vagina_insertion_sound()
        "Her pussy clenches around me as she continues fingering her ass."
        "I hold her hips steady, letting her ride out the intense orgasm."
        
        scene scene_17_final
        with fade
        
        mc "I'm going to fill you, Ersa!"
        $ play_cum_sound()
        $ play_man_pleasure_sound()
        ersa "Yes! Yes! Give it all to me!"
        ersa "Show him what he's missing!"
        
        scene home_night
        show ersa at ersa_convo
        $ update_character_state("ersa", CharState.HAPPY)
        with fade
        
        ersa "Holy shit. That was intense."
        ersa "I've never come that hard. The dual stimulation was incredible."
        mc "That's because you're with someone who actually cares about your pleasure."
        mc "And we're just getting started."
        
        $ update_character_state("ersa", CharState.AROUSED)
        ersa "The camera... did it get everything?"
        mc "Every second. Want to make another?"
        ersa "Actually... I have a better idea."
        ersa "Does Gemmy still hate Craig as much as she used to?"
        mc "Gemmy? You know her?"
        ersa "We've commiserated a few times. Bonded over what an ass he is."
        ersa "What if... what if we really drove the knife in?"
        mc "You mean..."
        ersa "Both his ex-wives. Together. With you."
        ersa "Can you imagine his face?"
        
        $ update_character_state("mc", CharState.HAPPY)
        mc "That's... that's brilliant."
        mc "And I happen to have Gemmy's number."
        ersa "Really? You've been busy."
        ersa "Call her. Let's make this a night Craig will never forget."
        ersa "Or rather, never be able to forget."
        
        # Only proceed to double scene if Gemmy was also successfully seduced
        if gemmy_standing_ride_scene:
            jump double_licking_setup
        else:
            # Gemmy wasn't successful, so just Ersa scene
            "I consider calling Gemmy, but our earlier interactions didn't go well enough."
            "Instead, Ersa and I enjoy the rest of the evening together."
            jump episode_4_ending

label ersa_seduction_fail:
    
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.SAD)
    with fade
    
    "Ersa left shortly after, the mood completely ruined."
    "I fucked up by being too cautious, too concerned about the wrong things."
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate
    
    bull_phone "You fucking idiot!"
    bull_phone "She was literally asking to be filmed and you worried about her reputation?"
    bull_phone "She's a grown woman who can make her own choices!"
    mc "I know. I just... I actually like her."
    mc "I didn't want her to regret anything."
    bull_phone "The only thing she regrets is wasting her evening on you."
    bull_phone "We were so close to having both of them!"
    mc "Maybe I can fix this. Call her tomorrow, apologize..."
    bull_phone "It's too late. You showed her you're just another weak man."
    bull_phone "Just like Craig, playing it safe instead of giving her what she needs."
    
    jump episode_4_ending

label ersa_seduction_continued:
    
    scene wine_bar_night
    show ersa at ersa_convo
    $ update_character_state("ersa", CharState.HAPPY)
    with fade
    
    "At the wine bar, I work to rebuild the momentum."
    "I order us a flight of wines to taste, making it playful and interactive."
    
    mc "This one reminds me of you - complex, sophisticated, with hidden depths."
    ersa "Are you going to compare me to every wine?"
    mc "Only the exceptional ones."
    
    $ update_character_state("ersa", CharState.AROUSED)
    ersa "You're relentless with the compliments."
    mc "I'm relentless when I want something."
    mc "And I want you to see yourself the way I see you."
    ersa "And how's that?"
    mc "Brilliant. Beautiful. Wasted on a man who couldn't appreciate you."
    mc "But not wasted anymore."
    
    "After more wine and increasingly intimate conversation, I make my move."
    
    mc "Come home with me, Ersa."
    mc "Let me show you how a real man worships a woman like you."
    
    $ update_character_state("ersa", CharState.AROUSED)
    ersa "That's a dangerous proposition."
    mc "The best ones usually are."
    ersa "I haven't been with anyone since..."
    mc "I know. Let me help you remember what you've been missing."
    mc "Or better yet, let me show you something you've never had."
    
    ersa "You're very confident for someone so young."
    mc "Age has nothing to do with knowing how to please a woman."
    mc "Let me prove it to you."
    
    "She considers for a long moment, then nods."
    ersa "Okay. But if I change my mind..."
    mc "Then we stop. Your comfort is what matters most."
    mc "But I don't think you'll want to stop."
    
    jump ersa_seduction_success

label double_licking_setup:
    
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    with fade
    
    mc "Let me call Gemmy. This is going to be epic."
    
    play sound "ES_Telephone Ringback Tone - Epidemic Sound.mp3"
    
    gemmy "Hello? [player_name]? It's pretty late..."
    mc "Gemmy, I'm here with Ersa."
    gemmy "Ersa? Craig's other ex? What are you..."
    gemmy "Oh my god. You didn't."
    mc "I did. And she has an idea that I think you'll love."
    mc "How would you like to help us send Craig a message he'll never forget?"
    gemmy "What kind of message?"
    mc "The kind that shows him both his ex-wives have moved on."
    mc "To the same younger man. At the same time."
    gemmy "..."
    gemmy "Holy fuck. That's evil. I love it."
    gemmy "Marcus is at his grandmother's until Sunday."
    gemmy "Give me twenty minutes to get ready and text me your address."
    mc "You're amazing, Gemmy."
    gemmy "No, this is amazing. Two ex-wives fucking the same young stud?"
    gemmy "Craig's going to have a stroke."
    gemmy "Make sure that camera has a full battery."
    
    play sound "ES_Mobile Phone, Hang Up Beeps - Epidemic Sound.mp3"
    
    scene home_night
    show ersa at ersa_convo
    $ update_character_state("ersa", CharState.HAPPY)
    with fade
    
    ersa "She's coming?"
    mc "She'll be here in twenty minutes."
    mc "Are you sure about this?"
    ersa "I've never been more sure of anything."
    ersa "Gemmy and I have fantasized about getting revenge on Craig."
    ersa "We just never imagined it would be like this."
    mc "Life's full of surprises."
    ersa "The best ones, apparently."
    ersa "We should prepare. Make sure everything's perfect."
    ersa "I want this video to be something Craig can never forget."
    ersa "Every time he closes his eyes, I want him to see us."
    ersa "Happy, satisfied, moving on with our lives."
    
    $ update_character_state("mc", CharState.HAPPY)
    mc "You're incredible. Both of you."
    mc "Most women would never do something this bold."
    ersa "We're not most women."
    ersa "We're survivors. And tonight, we're taking our power back."
    
    # GEMMY ARRIVES
    
    "Twenty minutes later, there's a knock at the door."
    "Gemmy enters like a force of nature, dressed to kill."
    
    show gemmy at gemmy_right_pos
    show ersa at ersa_left
    $ update_character_state("gemmy", CharState.HAPPY)
    with fade
    
    gemmy "Ersa! Girl, you look amazing!"
    ersa "So do you! That dress is killer."
    gemmy "I figured if we're making a revenge porn, I should look my best."
    
    "The two women hug, bonded by their shared history."
    "Then they both turn to look at me with predatory smiles."
    
    gemmy "So you're the one who's been seducing Craig's ex-wives."
    ersa "Very successfully, I might add."
    gemmy "I can see why. He's got that sweet face but dirty mind combo."
    ersa "And he actually listens. Remembers things. Cares about our pleasure."
    gemmy "Everything Craig wasn't."
    ersa "Exactly."
    
    $ update_character_state("mc", CharState.AROUSED)
    mc "Ladies, you're making me blush."
    gemmy "Oh honey, we're going to make you do a lot more than blush."
    ersa "Should we discuss the plan?"
    gemmy "What's to discuss? We fuck this young stud senseless while the camera rolls."
    gemmy "Then we send it to Craig with a note about what he's missing."
    ersa "I was thinking we could be more... strategic."
    ersa "Really emphasize what he lost. Make him see what he gave up."
    
    menu:
        "Let's just see where the night takes us naturally.":
            label test_choice_px6xj:
            $ gemmy_love += 5
            $ ersa_love += 5
            mc "Let's just see where the night takes us naturally."
            mc "The best revenge is authentic pleasure."
            mc "Just be yourselves, enjoy each other, enjoy me..."
            mc "Let Craig see what happens when women are truly appreciated."
            gemmy "I like that. No script, just passion."
            ersa "And the camera captures it all."
            mc "Every moan, every kiss, every moment of ecstasy."
            mc "He'll see two goddesses being worshipped properly."
            gemmy "Goddesses. I like that."
    ersa "We are goddesses. We just forgot for a while."
    ersa "Like the phoenix... rising from the ashes of a terrible marriage..."
    
    menu:
        "Tell me about rising from ashes":
            label test_choice_rzndb:
            if ersa_love >= 35:
                ersa "Some things must burn to be reborn..."
                ersa "What mythical bird represents rebirth and renewal?"
                jump outfit_30_puzzle
                label outfit_30_puzzle_success:
                    ersa "I have this beautiful phoenix-themed outfit... feathers and fire..."
                    ersa "It represents my transformation... my rebirth!"
                    ersa "Maybe you'll see me wear it when I'm fully reborn..."
                label outfit_30_puzzle_failure:
                    ersa "I thought you'd understand the symbolism..."
        "You're both goddesses":
            label test_choice_8rdr5:
            mc "Then let me remind you. Both of you."
        "We should make it clear this is about him failing you both.":
            label test_choice_1o0nv:
            $ gemmy_love += 5
            $ ersa_exotic_interest += 5
            mc "We should make it clear this is about him failing you both."
            mc "Maybe mention specific things he did wrong during..."
            gemmy "Oh, like how he never went down on me?"
            ersa "Or how he lasted thirty seconds on a good day?"
            gemmy "How he called my post-baby body 'ruined'?"
            ersa "How he said my degree made me 'less feminine'?"
            ersa "He never appreciated my heritage, my culture, my background..."
            menu:
                "Tell me about your heritage":
                    label test_choice_bbq3r:
                    if ersa_exotic_interest >= 3:
                        ersa "My family comes from ancient lands..."
                        ersa "Where great rivers flow and pharaohs once ruled..."
                        ersa "What river do you think flows through my ancestral homeland?"
                        jump outfit_26_puzzle
                        label outfit_26_puzzle_success:
                            ersa "I have traditional outfits... royal Egyptian attire..."
                            ersa "Maybe I'll show you how a true queen dresses..."
                        label outfit_26_puzzle_failure:
                            ersa "I hoped you might appreciate my background..."
                "Craig was an idiot":
                    label test_choice_subxr:
                    ersa "Completely. He never valued what he had."
            mc "Exactly. Show him through contrast."
            mc "Every time I do something right, mention how he did it wrong."
            gemmy "Fuck yes. Rub his nose in his failures."
            ersa "While we enjoy someone who actually knows how to please women."
        "Maybe we should plan out specific positions and angles?":
            label test_choice_0c50o:
            $ lose_sound()
            mc "Maybe we should plan out specific positions and angles?"
            mc "Make sure we get the best shots..."
            gemmy "Are we making porn or having revenge sex?"
            ersa "He's got a point about the angles though..."
            gemmy "Fuck the angles. This is about feeling good."
            gemmy "About taking back our power, not making a professional film."
            mc "You're right. Sorry, I got carried away."
            gemmy "Just fuck us good and the rest will follow."
    $ update_character_state("gemmy", CharState.AROUSED)
    $ update_character_state("ersa", CharState.AROUSED)
    gemmy "So, shall we begin?"
    ersa "I'm ready if you are."
    mc "Ladies, I'm at your service."
    "They exchange a look, then move toward me in unison."
    "Gemmy kisses me first, fierce and demanding."
    "Then Ersa, softer but no less passionate."
    "Soon we're all tangled together on the couch."
    stop music fadeout 1.0
    scene scene_16_initial
    with fade
    "What follows is pure hedonistic pleasure."
    "Both women kneel before me, their faces close together as they begin to worship my cock."
    scene scene_16
    $ persistent.scene_16 = True
    "Their tongues dance along my shaft, sometimes meeting in the middle for a kiss before returning to their task."
    gemmy "Mmm, he tastes so good, doesn't he Ersa?"
    ersa "So much better than Craig ever did."
    gemmy "Look how hard he stays! Craig would have finished twice by now."
    ersa "Remember how he'd just roll over and snore after?"
    gemmy "Every fucking time. But this one..."
    gemmy "This one knows how to last while we both lick him."
    "They work in perfect harmony, their tongues synchronized as they pleasure me together."
    "Years of shared frustration with Craig turning into shared ecstasy with me."
    "The camera captures every moment - their tongues swirling together, lips meeting around my cock."
    mc "You're both so fucking beautiful doing this."
    mc "Craig's an idiot for letting either of you go."
    gemmy "His loss is your gain, baby."
    ersa "And our gain too. God, I love licking you with her."
    gemmy "We both needed this. Who knew the answer was sharing your cock?"
    ersa "Sharing is definitely caring in this case."
    "They laugh and return to their synchronized licking with renewed enthusiasm."
    "Their tongues trace patterns up and down my shaft, occasionally pausing to suck on the tip together."
    "They continue their dual oral worship for what feels like an eternity."
    "Their tongues work in perfect synchronization, exploring every inch."
    "Sometimes they focus on the tip together, other times one works the shaft while the other attends to my balls."
    gemmy "Mmm, so much bigger than Craig!"
    gemmy "So much better! You hear that, asshole?"
    gemmy "This is what a real man tastes like!"
    ersa "We could do this all night."
    ersa "Just worship this beautiful cock together."
    gemmy "He deserves it after how well he's treated us."
    gemmy "Never had our pleasure prioritized like this."
    "They increase their pace, their tongues dancing faster."
    "Gemmy focuses on the head while Ersa licks up and down the shaft."
    "Then they switch, seamlessly, like they've done this before."
    ersa "Yes! I love seeing you enjoy this!"
    ersa "This is what we needed! What we deserved!"
    gemmy "What we were denied for so long."
    ersa "Never again. Never settling for less again."
    "They continue their oral worship with increasing enthusiasm."
    "Their moans vibrate against my cock as they pleasure me."
    "By the end, my legs are shaking from the intensity of their combined attention."
    
    mc "I'm close... so close..."
    $ play_man_pleasure_sound()
    gemmy "Do it! Cover us both!"
    ersa "We want your cum!"
    
    scene scene_16_final
    with fade
    
    mc "Fuck!"
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    "I explode across both of their faces."
    "They both look up at me with satisfaction and lust."
    
    scene home_night
    $ all_naked = True
    show gemmy at gemmy_right_pos
    show ersa at ersa_left
    $ update_character_state("gemmy", CharState.AROUSED)
    $ update_character_state("ersa", CharState.AROUSED)
    with fade
    gemmy "Holy fuck. That was..."
    ersa "Incredible. Cathartic. Perfect."
    mc "You two were amazing."
    gemmy "We need to edit this and send it to Craig immediately."
    ersa "With a message. Something he can't ignore."
    menu:
        "How about: 'Your ex-wives wanted to thank you for setting them free'?":
            label test_choice_6qdfe:
            $ gemmy_love += 5
            $ ersa_love += 5
            mc "How about: 'Your ex-wives wanted to thank you for setting them free'?"
            mc "'Here's what they've been up to. Pay your child support or everyone else sees it too.'"
            gemmy "Perfect! Polite but devastating."
            ersa "And the threat ensures he'll comply."
            gemmy "He's too proud to let his drinking buddies see this."
            ersa "Or his customers. Imagine if we sent it to the butcher shop email?"
            gemmy "Craig always had delusions of grandeur... dreams of being bigger than he is..."
            menu:
                "What represents Craig's impossible dreams?":
                    label test_choice_15hbe:
                        gemmy "He used to dream about exploring space... escaping Earth..."
                        gemmy "Where do astronauts go to escape reality?"
                        jump outfit_44_puzzle
                        label outfit_44_puzzle_success:
                            gemmy "Too bad he can't escape his earthly responsibilities!"
                            gemmy "Time to bring him back down to reality!"
                        label outfit_44_puzzle_failure:
                            gemmy "His dreams are bigger than his character..."
                "Craig needs to face reality":
                    label test_choice_5hsij:
                    ersa "Absolutely. No more running from consequences."
            if butcher_blackmail_success:
                outline "When this video goes public, Craig will be exposed completely..."
                outline "What word describes his shameful state?"
                jump outfit_45_puzzle
                label outfit_45_puzzle_success:
                    outline "All his lies, all his selfishness, exposed for everyone to see!"
                label outfit_45_puzzle_failure:
                    outline "Craig's shame will be revealed in time..."
            mc "Let's keep that as plan B. Give him a chance to do the right thing first."
            gemmy "You're too nice. But fine."
        "Something simple: 'Pay up or this goes public.'":
            label test_choice_czm48:
            mc "Something simple: 'Pay up or this goes public.'"
            mc "Let the video speak for itself."
            ersa "Direct. I like it."
            gemmy "He'll know exactly what we want."
            gemmy "And what he stands to lose if he doesn't comply."
            ersa "His reputation is everything to him."
            ersa "This will destroy it if it gets out."
            mc "Then he better pay what he owes."
        "Let's not threaten him. Just send it with no message.":
            label test_choice_qt2l9:
            $ lose_sound()
            $ gemmy_love -= 5
            mc "Let's not threaten him. Just send it with no message."
            mc "Let him stew in it."
            gemmy "No! We need the leverage!"
            gemmy "This is about getting my child support!"
            ersa "And stopping him from spreading rumors."
            ersa "We need clear demands."
            mc "You're right. Sorry, I wasn't thinking."
            gemmy "Men. Even the good ones need direction sometimes."
    "We craft the perfect message and attach the edited video."
    "Both women kiss me goodbye, promising this won't be the last time."
    "As they leave together, arm in arm, I hear them making plans."
    gemmy "We should do this again sometime."
    ersa "Definitely. With or without the camera."
    gemmy "Who knew revenge could be so fun?"
    ersa "Or so satisfying."
    $ double_licking_scene = True
    $ butcher_blackmail_success = True
    jump episode_4_ending

label episode_4_ending:
    
    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    $ all_naked = False
    with Fade(0.5, 5.0, 0.5)
    
    "The next morning, I wake up to my phone buzzing."
    "Multiple messages, all variations of the same theme."
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    if double_licking_scene:
        bull_phone "HOLY SHIT! You actually did it!"
        bull_phone "Both ex-wives at once! The video is incredible!"
        bull_phone "Craig already responded. He's agreed to pay all back child support."
        bull_phone "AND he's promised to stop talking shit about you."
        mc "Really? That was fast."
        bull_phone "He sent a pathetic message begging you not to release it."
        bull_phone "Said his reputation would be ruined, his business would suffer."
        bull_phone "Offered to pay double what he owes if you delete it."
        mc "We're not deleting anything. That's our insurance."
        bull_phone "Smart man. Keep that leverage."
        bull_phone "You've come so far from the crying cuckold I first met."
        bull_phone "Nancy, Lauren, Emma, and now both of Craig's ex-wives..."
        bull_phone "You're building quite the reputation."
        mc "The best part? It's all true."
        mc "[girl_friend]'s lies are being exposed one conquest at a time."
        bull_phone "And we're not done yet. There are still people who believe her."
        bull_phone "But after this? Craig won't be one of them."
        bull_phone "He'll be too busy paying child support and keeping his mouth shut."
        
        $ update_character_state("mc", CharState.HAPPY)
        mc "What's next then?"
        bull_phone "Enjoy your victory for now. You've earned it."
        bull_phone "But stay ready. There are always more opportunities."
        bull_phone "More women who've been wronged, more assholes who deserve comeuppance."
        bull_phone "You're becoming the man I always knew you could be."
        mc "Thanks to you pushing me."
        bull_phone "I just showed you the path. You walked it yourself."
        bull_phone "Now, both Gemmy and Ersa texted saying they want to see you again."
        bull_phone "Separately this time. Seems you made quite an impression."
        mc "Life is good."
        bull_phone "And getting better every day."
        
    elif gemmy_love >= 30 or ersa_love >= 30:
        bull_phone "Well, you got one of them at least."
        bull_phone "The video worked - Craig's agreed to pay some of what he owes."
        bull_phone "Not the complete victory we wanted, but still progress."
        mc "One is better than none."
        bull_phone "True. And whichever one you got is singing your praises."
        bull_phone "Maybe you can still get the other one later."
        bull_phone "Complete the set, as it were."
        mc "Maybe. We'll see."
        bull_phone "That's the spirit. Always leave room for possibilities."
        
    else:
        $ update_character_state("bull", CharState.ANGRY)
        bull_phone "You fucked up both opportunities!"
        bull_phone "How do you manage to fail with two horny divorcees?"
        bull_phone "They were practically begging for it!"
        mc "I know. I got in my own head."
        bull_phone "Your head is your biggest enemy."
        bull_phone "Stop thinking so much and start acting."
        bull_phone "Craig's still talking shit, still not paying support."
        bull_phone "We accomplished nothing!"
        mc "I'll do better next time."
        bull_phone "You better. I'm running out of patience."
        bull_phone "And you're running out of chances to prove [girl_friend] wrong."
    
    hide bull
    with pixellate
    
    "I lie back in bed, reflecting on everything that's happened."
    "From Craig's ex-wives to my growing confidence..."
    "I'm not the same person I was when [girl_friend] destroyed me."
    "I'm becoming something more. Someone stronger."
    "And this is just the beginning."
    
    $ update_character_state("mc", CharState.HAPPY)
    mc "(Craig's been neutralized. [girl_friend]'s lies are crumbling.)"
    mc "(I've got beautiful women actually wanting me.)"
    mc "(For the first time in my life, I'm winning.)"
    mc "(And I'm not going to stop.)"
    
    # MC's reflection on his connections with the women
    if gemmy_love >= 30:
        outline "Gemmy really opened up to me about her hobbies..."
        outline "Her interests in anime and cosplay... things Craig never appreciated..."
        
        menu:
            "Think about Gemmy's otaku interests":
                label test_choice_e3rdv:
                outline "What art form inspires people to dress up as their favorite characters?"
                jump outfit_21_puzzle
                label outfit_21_puzzle_success:
                    outline "She mentioned having cosplay outfits... maybe she'd show me sometime..."
                label outfit_21_puzzle_failure:
                    outline "Gemmy's interests are more complex than I realized..."
            "Focus on our growing connection":
                label test_choice_zhr03:
                outline "Gemmy and I are building something real..."
    if gemmy_outcome == "best":
        outline "Gemmy completely trusted me with her true self..."
        outline "Her nerdy, otaku side that Craig mocked..."
        outline "What describes someone passionate about Japanese animation culture?"
        jump outfit_25_puzzle
        label outfit_25_puzzle_success:
            outline "She's proud of her interests, and I accept all of her..."
        label outfit_25_puzzle_failure:
            outline "Her interests are part of who she is..."
        # Additional Gemmy personality unlocks for best outcome
        outline "Gemmy mentioned she was into skating before she met Craig..."
        outline "She gave it up because he said it wasn't 'feminine enough'..."
        outline "What fun activity involves wheels and concrete streets?"
        jump outfit_56_puzzle
        label outfit_56_puzzle_success:
            outline "Maybe she'll take it up again now that she's free..."
        label outfit_56_puzzle_failure:
            outline "She'll rediscover her passions in time..."
        outline "She also talked about her rebellious phase in college..."
        outline "The music she loved, the style Craig made her abandon..."
        outline "What musical style represents breaking all the rules?"
        jump outfit_57_puzzle
        label outfit_57_puzzle_success:
            outline "Her rebel heart that he tried to crush..."
        label outfit_57_puzzle_failure:
            outline "Her rebellious spirit never truly left..."
    # Grant episode 4 completion achievement
    call grant_episode_achievement(4) from _call_grant_episode_achievement_1
    $ check_love_achievements()
    
    jump episode_5