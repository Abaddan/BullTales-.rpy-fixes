# Bull Phone Origin Story Implementation
# This prologue shows the MC finding the Bull Phone on his first day moving in with [girl_friend]
# The phone has mysterious supernatural powers and can possess the MC's body
# Note: In the prequel "CuckTales", there's a different origin where MC finds it later
# and thinks it belongs to "the Butcher" - this version establishes it as found day one

# Import centralized points system
default nancy_key_question_passed = False
default found_bull_phone = False  # Track if origin scene was shown
default nancy_outcome_prologue = "neutral"

image phone_holding = At("images/non_sex_scenes/holding_phone.png", background_zoom)
image phone_throwing = At("images/non_sex_scenes/phone_throwing.png", background_zoom)
image call_lauren = At("images/non_sex_scenes/call_lauren.png", background_zoom)
# Bull Phone discovery image - generated using AI (Gemini)
image phone_on_ground = At("images/non_sex_scenes/phone_on_ground.png", background_zoom)

label prologue:
    # Bull Phone Origin Scene - First Day in Town
    scene home_morning
    play music "ES_Summer '15 - Maybe.mp3" volume 0.2
    with Fade(0.5, 2.0, 0.5)
    
    outline "Two months ago..."
    outline "The day [girl_friend] and I first arrived at our new place. Everything seemed so perfect then."
    
    show jane at jane_convo
    $ update_character_state("jane", CharState.HAPPY)
    with dissolve
    
    jane "Finally! Our own place, [player_name]! Can you believe it?"
    jane "No more dorms, no more roommates... just us."
    
    mc "Yeah, it's amazing. A fresh start in a new town."
    jane "I'll start unpacking the kitchen stuff. Why don't you check if we got any mail or packages?"
    mc "Sure, I'll take a look around outside."
    
    hide jane
    with dissolve
    
    # MC goes outside
    # MC goes outside (using home_morning as placeholder for exterior scene)
    scene home_front_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    outline "I walked around the front of the house, checking the mailbox and looking for any deliveries."
    outline "That's when I saw it - a phone lying on the ground near the sidewalk, partially hidden in the grass."
    
    mc "Huh? Someone dropped their phone?"
    
    menu:
        "Pick up the phone":
            label test_choice_n1xzn:
            $ found_bull_phone = True
            with dissolve
            
            outline "I picked up the small flip phone, turning it over in my hand. It was an unusual device - the case had a strange bull-like design etched into it, with tiny horns that seemed to shimmer in the sunlight."
            outline "Despite looking expensive, it was just lying there abandoned, with no one around who might have dropped it."
            
            mc "Weird... This looks pretty new. A flip phone in this day and age? And why would someone just leave it here?"
            
            play sound "ES_Effect, Strange Ring 04 - Epidemic Sound.mp3"
            
            outline "As I examined the phone in my palm, I felt a strange tingling sensation, like static electricity but... different."
            outline "The small screen flickered to life despite the phone being closed and appearing to be powered off."
            
            show mc at mc_convo
            hide phone_on_ground
            with pixellate
            
            mc "What the..."
            
            # First contact with Bull Phone
            $ update_character_state("bull", CharState.NORMAL)
            show bull at bull_convo
            with pixellate
            
            bull_phone "..."
            mc "Did... did this phone just turn on by itself?"
            bull_phone "..."
            outline "The screen displayed strange symbols I couldn't read, pulsing with an eerie red glow."
            mc "Must be some weird screensaver or something. I should try to find the owner."
            
            hide bull
            with pixellate
            
            outline "I pocketed the phone, planning to ask around the neighborhood later."
            outline "Little did I know what I had just picked up..."
    
    # Transition back inside
    scene home_morning
    show jane at jane_convo
    $ update_character_state("jane", CharState.HAPPY)
    with fade
    
    jane "Find anything interesting out there?"
    mc "Just someone's lost phone. I'll try to find the owner later."
    jane "That's sweet of you. Always trying to help people."
    jane "Come on, let's finish unpacking. I want to make this place feel like home."
    
    mc "Yeah... home."
    
    outline "If only I had known then what that phone really was..."
    outline "Or what would happen to [girl_friend] and me in just two short months..."
    
    # Fade to present time
    scene black
    with Fade(1.0, 2.0, 0.0)
    
    centered "{size=+10}Two Months Later{/size}"
    
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.SAD)
    play music "ES_Black Venom - Ruiqi Zhao.mp3" volume 0.3
    with Fade(0.5, 5.0, 0.5)

    mc "Haha, look at you, so cute in these clothes." # [cite: 1]
    outline "After admiring my cute (ex)girlfriend posing for the camera for a moment, I swiped my fingers to the side and the next photo." # [cite: 1]
    mc "Aah, I remember this day. We had so much fun back then." # [cite: 1]
    outline "I swiped again, and-" # [cite: 1]

    $ update_character_state("mc", CharState.ANGRY)

    mc "AHHHH-?!" # [cite: 1]
    outline "And there it was, something I didn’t want to see: [girl_friend] and her new boyfriend, the very same guy she cheated on me with, Justin." # [cite: 1]
    mc "AAW, fuck no!" # [cite: 1]

    menu:
        "Throw your phone":
            label test_choice_zeej7:
            hide mc
            show phone_throwing
            with dissolve
            play effects "ES_Phone, Drop On Floor 03 - Epidemic Sound.mp3"

            pause 2.0

            outline "Bawling out, I hurled my phone away, gritting my teeth as if that the immense pressure I put on my jaws were enough to keep my heart pieces glued together." # [cite: 1]

    hide phone_throwing
    show mc at mc_convo
    with fade

    mc "Why, [girl_friend]? Why, dammit…?!" # [cite: 1]

    menu:
        "Why'd you leave":
            label test_choice_wr8ni:
            play effects "ES_Effect, Strange Ring 04 - Epidemic Sound.mp3"
            outline "I wasn’t sure I wanted to know the answer for that question."

    play sound "ring.mp3"
    "Ring!"

    $ update_character_state("mc", CharState.HAPPY)

    mc "[girl_friend]?!" # [cite: 1]

    menu:
        "Get your phone":
            label test_choice_q0ucv:
            play effects "ES_Grass, Male, Leather Sole, Running, Stops - Epidemic Sound.mp3"
            outline "I hurried to the phone, holding onto my last threat of hope." # [cite: 1]

    $ update_character_state("mc", CharState.ANGRY)
    $ update_character_state("bull", CharState.HAPPY)
    show bull at bull_convo
    with pixellate

    # Bull Phone interaction starts
    # Maybe show a phone overlay or use the character
    # show screen bull_phone_indicator # Example screen
    bull_phone "Hey, feeling sorry enough for yourself already?" # [cite: 1]
    mc "This guy…" # [cite: 1]

    menu:
        "Turn off phone":
            label test_choice_vsve9:
            outline "I turned my phone off, and head back to bed." # [cite: 1]

    bull_phone "Will you really try to ignore me? Seriously? After all we went through?" # [cite: 1]
    outline "He speaks as if we went through anything good!" # [cite: 1]
    bull_phone "You can’t really blame ME for everything you went through, not when your response to getting dumped is to rot in bed for months on end." # [cite: 1]
    outline "I covered my ears with my hands, trying to block out the voice." # [cite: 1]
    bull_phone "Come on, I know you can hear me. We went through this before, haven’t we?" # [cite: 1]
    bull_phone "From the moment you first picked me up from the ground outside, we are bound together, [player_name]." # [cite: 1]
    mc "Shut up…" # [cite: 1]
    bull_phone "I’ve seen every blunder and fuck up you committed with that girly of yours, and I have to say, I laughed my ass off!" # [cite: 1]
    mc "Shu up…!" # [cite: 1]
    bull_phone "You truly put quite a show for me during this! Hahaha" # [cite: 1]
    outline "Finally, I jumped out of bed and picked the damn phone again – demon, ghost, or whatever that cursed thing was." # [cite: 1]
    mc "Just what do you want?! I don’t have a girlfriend anymore, so why won’t you just go away!?" # [cite: 1]
    bull_phone "If you only were this brave with people than me…" # [cite: 1]

    $ update_character_state("mc", CharState.SAD)

    outline "He knew exactly how to hurt me, even without arms." # [cite: 1]
    outline "He knew that I'd never be able to scream like that with Justin, not when even my own phone made me tremble in fear."
    bull_phone "But if you want to know so bad what I want, I'll tell you... or at least, what I can tell you." # [cite: 1]
    bull_phone "I'm no divine punishment, no ordinary AI, no simple ghost haunting technology." # [cite: 1]
    bull_phone "What am I? That's not for you to know. Not yet. Maybe never." # [cite: 1]
    bull_phone "But I'll tell you this - I wasn't randomly lying on that sidewalk. I chose to be found. I chose YOU." # [cite: 1]
    mc "W-What…? Why me?" # [cite: 1]
    bull_phone "Every mistake you've made is entirely your own fault. I've been just a spectator of your fall... until now." # [cite: 1]
    bull_phone "My real purpose, my real job, starts now that you've hit rock bottom." # [cite: 1]
    bull_phone "Look, your defeats, everything that happened from the day we met until you lost your girlfriend, all of that was very entertaining- I mean, unfortunate indeed." # [cite: 1]
    bull_phone "But I'm not here to play psychologist and talk about the traumas that led you here." # [cite: 1]
    bull_phone "No, I'm here to pull you out of this hole… and plunge you into another, softer one, hehehe." # [cite: 1]
    
    # OUTFIT PUZZLE TUTORIAL SECTION
    bull_phone "But before we begin your transformation, you need to understand how this works."
    bull_phone "Throughout your journey, you'll encounter moments where understanding someone deeply will unlock special rewards."
    bull_phone "I call them 'outfit puzzles' - riddles that test your insight into people's true nature."
    
    mc "Outfit puzzles? What are you talking about?"
    
    bull_phone "Think of it this way - when you truly understand what drives someone, what they desire, what they represent..."
    bull_phone "You unlock their hidden potential. Literally."
    bull_phone "Answer correctly, and you'll see them in new ways. New outfits that reflect who they really are inside."
    
    mc "That sounds... bizarre."
    
    bull_phone "Let me give you a simple example to show you how this works."
    bull_phone "Picture yourself - what do you feel like right now, hiding in this dark room?"
    
    outline "The Bull Phone wants to teach me about these 'outfit puzzles' with a practice example."
    outline "What represents someone who hides from the world?"
    
    $ play_puzzle_sound()
    # Practice puzzle - tutorial example
    menu:
        "A king on his throne":
            label test_choice_910dh:
            bull_phone "Hardly. Kings don't hide in bedrooms feeling sorry for themselves."
            bull_phone "Try to think about what you're actually doing right now."
        
        "A shadow in darkness":
            label test_choice_jy7tb:
            bull_phone "Exactly! You understand the concept!"
            bull_phone "When you see the truth of what someone represents, you unlock that insight."
            $ puzzle_unlock_outfit("mc", "ninja", _("🥷 MC Ninja outfit unlocked! (Tutorial)"))
            bull_phone "See? You've unlocked the ninja outfit - perfect for someone who hides in shadows."
        
        "A bright light":
            label test_choice_z3c6z:
            bull_phone "Not even close. You're doing the opposite of shining bright."
            bull_phone "Think about your current state - hiding, avoiding the world."
    
    bull_phone "The key is understanding the deeper meaning, not just the surface."
    bull_phone "When you meet people, listen carefully. Their words, their desires, their fears - they all contain clues."
    bull_phone "Sometimes the puzzle will be about what they want to be. Sometimes about what they fear."
    bull_phone "Sometimes about what they truly are underneath it all."
    
    mc "And if I get it wrong?"
    
    bull_phone "Nothing terrible happens. You just don't unlock that particular insight."
    bull_phone "But get it right, and you'll see sides of people others never do."
    bull_phone "Trust me, these unlocked outfits will become very... interesting... as we progress."
    
    outline "I'm starting to understand. This phone doesn't just give advice."
    outline "It somehow reveals hidden aspects of people when I truly understand them."
    outline "But how is that even possible?"
    
    mc "How can a phone actually change what people wear? This is impossible."
    
    bull_phone "Kid, I can possess your body and you're worried about outfit changes?"
    bull_phone "Let's just say I have influence over more than just your actions."
    bull_phone "The outfits represent understanding. The deeper you understand someone, the more you see their true potential."
    bull_phone "And in this game we're playing, seeing someone's true potential has... benefits."
    
    mc "What kind of benefits?"
    
    bull_phone "Let's just say that when you truly understand a woman's desires..."
    bull_phone "She becomes much more receptive to yours. Hehehe."
    bull_phone "But enough theory. Time for practice. You need food, and I guarantee you'll encounter someone interesting."
    
    mc "My bed is soft enough. Just leave me alone." # [cite: 1]
    outline "I threw myself back on my bed, just wanting to fall asleep and dream of [girl_friend]." # [cite: 1]
    bull_phone "After all this time locked in here, you MUST want to take some fresh air, right?" # [cite: 1]
    mc "I’m perfectly fine in he-" # [cite: 1]

    play sound "stomach_growl.mp3"
    $ update_character_state("mc", CharState.AROUSED)
    "Grrrooowlll~~!" # [cite: 1]

    bull_phone "Even though your food stock ended yesterday? Hehehe." # [cite: 1]
    outline "It was hard to swallow that I had to admit defeat to a disembodied voice." # [cite: 1]
    outline "Nevertheless, he was indeed right, it had been two days since I last ate," # [cite: 1]
    outline "and though it was true that I didn’t want to leave my bedroom, it wasn’t like I wanted to *literally* rot in there."
    mc "Sigh." # [cite: 1]
    mc "At least don’t talk to me in public, then… please." # [cite: 1]
    bull_phone "…" # [cite: 1]

    hide bull
    with dissolve

    mc "Quiet as long as I do what you want, hu?" # [cite: 1]

    menu:
        "Listen to music":
            label test_choice_lte24:
            hide mc
            show phone_holding
            with dissolve

            $ notify(_("Click the door to navigate to the convenience store."))

            outline "Since the bull was no longer bothering me, I picked up my phone, put on some earbuds to listen to music while on my way, and headed to the nearest convenience store." # [cite: 1]

    jump home


# ----------------------------------------------------


label convenience_store_encounter:

    stop music
    scene mall_interior_night
    show mc at mc_convo
    show screen empty_interactions
    with Fade(0.5, 5.0, 0.5)

    $ update_character_state("mc", CharState.SAD)

    mc "I don’t have much money, so I’ll buy just the necessary, and the cheapest options so that I can stay inside for as long as possible." # [cite: 1]
    mc "Ramen, soda, and… that’s it, I guess. I’ll just find the cheapest options. Oh look there's a dollar store." # [cite: 1]
    "I was about to head to the dollar store when I bumpped into someone." # [cite: 1]
    mc "Ah! S-Sorry." # [cite: 1]

    hide mc
    show nancy at nancy_convo
    with fade
    play music "ES_Pillow (Instrumental Version) - SCENE.mp3" volume 0.1

    nancy "It’s alright- wait, [player_name]?" # [cite: 1]
    mc "Nancy?" # [cite: 1]
    nancy "I haven’t… seen you in a long time." # [cite: 1]
    mc "Yeah, I- Uhm…" # [cite: 1]
    outline "I felt my knees weakening, my palms sweating, and my core freezing up." # [cite: 1]
    outline "I had accidentally stumbled upon an old friend of mine, someone who knew about my girlfriend cheating on me with an asshole and leaving me to become his second girlfriend, nevertheless." # [cite: 1]
    outline "Nancy looked at me with equal measure of pity and disgust, and that only made me act even more pitifully and disgustingly." # [cite: 1]

    $ update_character_state("bull", CharState.ANGRY)
    show bull at bull_convo
    with pixellate

    bull_phone "Shit, [player_name], why can’t you be honest with yourself at least one? You’re none of that, right?" # [cite: 1]
    outline "Out of every time that damn phone could have chosen to speak to me, he picked the worst one – at least I was the only one hearing to him, through my earbuds." # [cite: 1]
    bull_phone "What you feel is something entirely different. You’re frustrated… you’re ANGRY." # [cite: 1]
    mc "Eh?" # [cite: 1]
    nancy "[player_name]? Are you alright?" # [cite: 1]
    bull_phone "Listen to me, if you want to come out on top of this; you can’t just stand there, mouth gaping, staring at her." # [cite: 1]
    bull_phone "Show her that you’re better than she thinks, give her a proper answer, and improve her view of you! Not a bad answer, not a neutral answer, but a good one!" # [cite: 1]

    menu:
        "I’m fine, thank you. What about you?":
            label test_choice_0yy80:
            $ nancy_love += 6
            $ update_character_state("nancy", CharState.HAPPY)
            mc "I'm fine, thank you. What about you?"
            nancy "It’s good to hear that." # [cite: 1]
            nancy "I’m also fine, thank you for asking." # [cite: 1]
            bull_phone "Good, good, you showed that you’re at least minimally functional." # [cite: 1]
            bull_phone "But that’s still far from the result we’re looking for." # [cite: 1]
            jump nancy_conversation_continue

        "I’m terrible, can’t stop thinking about [girl_friend]…":
            label test_choice_uw8ve:
            $ update_character_state("nancy", CharState.SAD)
            $ lose_sound()
            mc "I'm terrible, can't stop thinking about [girl_friend]..."
            nancy "Oh. I should have imagined. I’m sorry for asking." # [cite: 1]
            nancy "After everything that happened involving your girlfriend… of course you’d feel like that." # [cite: 1]
            bull_phone "Holly hell, [player_name], you messed this up." # [cite: 1]
            bull_phone "But that’s fine, you’ll still have more chances to make up for this mistake." # [cite: 1]
            jump nancy_conversation_continue

        "So-so.":
            label test_choice_93kap:
            $ update_character_state("nancy", CharState.SAD)
            $ lose_sound()
            mc "So-so."
            nancy "I see. I guess I can say I feel the same, then." # [cite: 1]
            bull_phone "You’ll have to be more interesting than that, if you want to get anyone’s respect back – or more." # [cite: 1]
            bull_phone "Whatever, you’ll still have more chances to improve her view of you." # [cite: 1]
            jump nancy_conversation_continue


# ----------------------------------------------------


label nancy_conversation_continue:

    scene mall_interior_night
    $ update_character_state("bull", CharState.ANGRY)
    $ update_character_state("nancy", CharState.NORMAL)
    show nancy at nancy_convo
    show bull at bull_convo
    with fade

    bull_phone "To get even more on her good side, pay attention to what she has to say, then give her an answer that fits her interests and personality." # [cite: 1] # This advice appears regardless of previous choice in the original script

    hide bull
    with pixellate

    mc "F-Feeling like you need a sugary pick me up? Haha…" # [cite: 1] # Assuming [player_name] says this to continue
    nancy "Yes, there’s a test coming up next week, and I’d like to be well prepared for it." # [34]
    nancy "And, you know? The brain uses up to 20 percent of the body’s energy, and it’s mostly powered by sugar." # [34]
    nancy "Treats like this are a pretty good fuel for studying, and…" # [34]
    nancy "Well, I admit that they are a very pleasing reward for myself, too." # [34]

    menu:
        "I hate candy.":
            label test_choice_zx7aq:
            mc "I hate candy."
            $ update_character_state("nancy", CharState.ANGRY)
            $ lose_sound()
            nancy "Then just don’t buy it?" # [cite: 1]
            nancy "I like it, however." # [cite: 1]
            nancy "And I will buy some, independently of what you think." # [cite: 1]
            mc "But drinking cola helps me with digestion, and since I’m constipated-" # [cite: 1]
            nancy "I don’t need to, and I definitely don’t want to hear details about that!" # [cite: 1]
            jump nancy_conversation_studies

        "But drinking cola helps me with digestion, and since I’m constipated-":
            label test_choice_ebrol:
            $ update_character_state("nancy", CharState.ANGRY)
            $ lose_sound()
            nancy "I don’t need to, and I definitely don’t want to hear details about that!" # [8]
            jump nancy_conversation_studies

        "Pavloving yourself, is it?":
            label test_choice_bxnzw:
            $ nancy_love += 6
            mc "Pavloving yourself, is it?"
            $ update_character_state("nancy", CharState.HAPPY)
            nancy "Hahaha! Yes, you can say so, I guess." # [cite: 1]
            nancy "I know it sounds silly, but it actually works, you know?" # [cite: 1]
            mc "Yeah, it makes sense." # [cite: 1]
            mc "I’ll try it out any of these days." # [cite: 1]
            jump nancy_conversation_studies

        "Yep, that sounds right.":
            label test_choice_61x93:
            $ lose_sound()
            mc "Yep, that sounds right."
            $ update_character_state("nancy", CharState.NORMAL)
            nancy "Yes." # [cite: 1]
            mc "Yeah…" # [cite: 1]
            nancy "So…" # [cite: 1]
            jump nancy_conversation_studies


# ----------------------------------------------------


label nancy_conversation_studies:

    scene mall_interior_night
    $ update_character_state("nancy", CharState.NORMAL)
    show nancy at nancy_convo

    mc "Still, studying hard a week prior to your test? You must be at the top of your class, right?" # [cite: 1]
    nancy "My grades aren’t half bad, indeed." # [cite: 1]

    $ update_character_state("bull", CharState.ANGRY)
    show bull at bull_convo
    with pixellate

    bull_phone "See? She, like any other woman, will react to your answers and her opinion of you will grow or diminish based on them." # [cite: 1]
    bull_phone "Coincidental meetings, first dates, and casual talks are mostly light weighted, but sometimes, especially after you meet the person a second time or more…" # [cite: 1]

    nancy "Speaking of which, what about your studies?" # [cite: 1]
    nancy "I haven’t seen you in the campus for some time already." # [cite: 1]
    nancy "You haven’t dropped your studies, right? You know how this is important in today’s world." # [cite: 1]
    bull_phone "More like, important to her!" # [cite: 1]
    mc "That…" # [cite: 1]
    bull_phone "Now, listen closely, this is what I was talking about: it’s a key question!" # [cite: 1]
    bull_phone "Answer it wrong, and this conversation ends here. So, be sure to think this through!" # [cite: 1]

    menu:
        "I’ve been studying at home.":
            label test_choice_uyzf7:
            $ nancy_love += 6
            $ nancy_key_question_passed = True
            $ update_character_state("nancy", CharState.HAPPY)
            mc "I’ve been studying at home."
            nancy "At home?" # [cite: 1]
            mc "Yeah, I had to read a few books, and then write an assignment, and I did it all online, so it’s not really surprising you haven’t seen me around." # [cite: 1]
            nancy "Ah, I know what you mean. Indeed, I understand that doing such things with the help of the internet and in the comfort of your bedroom is much easier." # [cite: 1]
            nancy "I’m the weird one here, for preferring old books and pen and paper, haha." # [cite: 1]
            mc "Not at all, I totally get the appeal of ink and paper, I was just on a tight schedule to finish all of my assignments." # [cite: 1]
            bull_phone "Great, you overcame this challenge. But don’t rest just yet, this conversation isn’t over yet!" # [cite: 1]
            jump nancy_conversation_questions

        "I’ve been just lazing around.":
            label test_choice_w3722:
            $ lose_sound()
            mc "I've been just lazing around."
            $ update_character_state("nancy", CharState.ANGRY)
            nancy "[player_name], that’s incredibly irresponsible. You’re no longer a child you know? Your future is at stake here." # [cite: 1]
            nancy "…Maybe it’s because of that attitude that [girl_friend] left you." # [cite: 1]
            mc "What…?!" # [cite: 1]
            nancy "If you make no efforts to build a future for yourself, how could your girlfriend rely on you? How could your friends?" # [cite: 1]
            mc "That…" # [cite: 1]
            nancy "Excuse me, [player_name]. I have places to be now. Some of us take our lives seriously, after all." # [cite: 1]
            bull_phone "You seriously messed up now, you got a key question wrong..." # [cite: 1]
            bull_phone "I won’t tell you this is the end of the world, as you’d have to fumble a couple more times for me to give up on you…" # [cite: 1]
            bull_phone "But I’ll let you know that, had things gone differently, you could have gotten something good out of this interaction." # [cite: 1]
            # Set outcome directly based on failing key question
            # No love points for failing key question
            hide nancy with dissolve
            jump nancy_conversation_end # Skip to end calculation


# ----------------------------------------------------


label nancy_conversation_questions:

    scene mall_interior_night
    $ update_character_state("bull", CharState.ANGRY)
    $ update_character_state("nancy", CharState.NORMAL)
    show nancy at nancy_convo
    show bull at bull_convo

    nancy "Studying online has its own drawbacks, though, right?" # [cite: 1]
    nancy "I mean, if you end up with a question, it’s not like you can just ask your teacher about it right away." # [cite: 1]

    menu:
        "I just look it up on a search engine.":
            label test_choice_10gnc:
            $ nancy_love += 6
            mc "I just look it up on a search engine."
            nancy "Oh, yes, I suppose you could do that." # [cite: 1]
            nancy "I’m not very familiar with such technologies." # [cite: 1]
            mc "But aren’t you a ner- I mean, a studious girl? I thought you’d know a lot about tech." # [cite: 1]
            nancy "I’m more of a humanities student than a tech and math one." # [cite: 1]
            nancy "I could tell you all about ethics and art, but not so much about, how was it again? Search motors?" # [cite: 1]
            mc "Engines. But I get it now. Pretty cool." # [cite: 1]
            jump nancy_conversation_resting

        "I just leave the hard questions blank.":
            label test_choice_b2tth:
            $ lose_sound()
            mc "I just leave the hard questions blank."
            nancy "What?" # [cite: 1]
            nancy "If you don’t really try to understand the harder topics, you can’t really say you’re studying, right?" # [cite: 1]
            mc "Nah, of course I’m studying: I answer the questions that I already know the answer, and the ones I don’t, I skip." # [cite: 1]
            nancy "Yes, this means you aren’t learning anything new, therefore not studying." # [cite: 1]
            mc "You know what? Let’s change topics." # [cite: 1]
            jump nancy_conversation_resting


# ----------------------------------------------------


label nancy_conversation_resting:

    scene mall_interior_night
    $ update_character_state("bull", CharState.ANGRY)
    $ update_character_state("nancy", CharState.NORMAL)
    show nancy at nancy_convo
    show bull at bull_convo
    with fade

    mc "What about resting, though? You haven’t just been studying non-stop, have you?" # [cite: 1]
    nancy "I-I admit that may be a flaw of mine, making time to rest and alleviate built up stress." # [cite: 1]
    nancy "What about you, though?" # [cite: 1]
    bull_phone "This is your chance, [player_name]!" # [cite: 1]
    bull_phone "The conversation is going to interesting places. So, surprise her, show her your dominant side, and you mind get something good from her." # [cite: 1]
    bull_phone "Just don’t be an idiot about it." # [cite: 1]

    menu:
        "I jerk off.":
            label test_choice_zh62i:
            $ nancy_love += 6
            $ update_character_state("nancy", CharState.AROUSED)
            $ update_character_state("bull", CharState.HAPPY)
            mc "I jerk off."
            nancy "W-What?" # [cite: 1]
            mc "Well, you know. Alone in my bedroom, when I get too stressed out from studying, I just whip my cock out and jerk off." # [cite: 1]
            nancy "I-I-I see." # [cite: 1]
            mc "Come on, you’re all about being an adult and having responsibilities and knowledge, so you must know that this is a valid calming method, right?" # [cite: 1]
            mc "Or, what, will you tell me you don’t play with yourself ever?" # [cite: 1]
            nancy "That- Well- I…" # [cite: 1]
            nancy "…I do, you’re right." # [cite: 1]
            bull_phone "Nice one." # [cite: 1]
            jump nancy_conversation_sleep

        "I spy on girls through my window.":
            label test_choice_euqnf:
            $ lose_sound()
            $ update_character_state("nancy", CharState.AROUSED)
            mc "I spy on girls through my window."
            nancy "That’s… quite an ‘unique’ hobby, to say the least…" # [cite: 1]
            mc "Some of them are hot." # [cite: 1]
            nancy "Good for them… is what I’d say, if they were not getting spied on." # [cite: 1]
            bull_phone "Fucking hell, you’re going to give me a lot of work to fix you, won’t you, [player_name]?" # [cite: 1]
            jump nancy_conversation_sleep


# ----------------------------------------------------


label nancy_conversation_sleep:

    scene mall_interior_night
    $ update_character_state("bull", CharState.ANGRY)
    $ update_character_state("nancy", CharState.NORMAL)
    show nancy at nancy_convo
    show bull at bull_convo

    nancy "But, you’re right, studying isn’t everything, we have to take care of our health." # [cite: 1]
    mc "Mental and physical health. Have you been sleeping well?" # [cite: 1]
    nancy "I have, yes." # [cite: 1]
    mc "Really? I mean buying coke at night to fuel your studies and all…" # [cite: 1]
    nancy "Alright, you got me, haha. I’ve been prioritizing finishing the book I have to read over a proper eight hours of sleep." # [cite: 1]
    mc "That’s not good, you know?" # [cite: 1]
    nancy "I know, but I just can't relax and fall asleep knowing that I haven't finished at least sixty pages in a day…" # [cite: 1]
    nancy "Sometimes I dream about summer... beaches and warm weather..."
    
    menu:
        "What's your favorite season?":
            label test_choice_zy96l:
            if nancy_love >= 10:
                nancy "I love the warmth... what season is perfect for swimming and sun?"
                outline "Wait... this feels familiar. The Bull Phone mentioned something about understanding people's true desires."
                outline "Nancy's talking about warmth and swimming... maybe this is one of those 'outfit puzzles' it mentioned?"
                jump outfit_9_puzzle
                label outfit_9_puzzle_success:
                    nancy "I have this cute bikini I've been saving for the right beach trip..."
                label outfit_9_puzzle_failure:
                    nancy "I was hoping you'd understand my love for warm weather..."
        "Tell me more about your studies":
            label test_choice_8msi2:
            nancy "Well, I'm focusing on humanities..."
    hide nancy
    hide bull
    $ update_character_state("mc", CharState.HAPPY)
    show mc at mc_convo
    with fade
    bull_phone "You’ve done your best." # [cite: 1]
    bull_phone "Now, there’s only one more thing that I can teach you about interacting with girls, [player_name]…" # [cite: 1]
    play sound "ES_Human, Heartbeat - Epidemic Sound.mp3" # Assumed sound effect
    "Ba-dum! Ba-dum! Ba-dum! Ba-dum! Ba-dum! Ba-dum!  Ba-dum! Ba-dum!  Ba-dum! Ba-dum!  Ba-dum! Ba-dum!"
    hide mc
    $ update_character_state("mc", CharState.AROUSED)
    show mc at mc_convo, bull_glow_effect
    stop music fadeout 0.5
    play sound "Male, Evil, Gravel Laugh, Male Laughs 02.mp3"
    play music "ES_Moonlight Mystery - Alexandra Woodward.mp3"
    with dissolve
    outline "(What the hell is happening?!)" # [cite: 1]
    outline "(Wh-What is this?! What is happening? I feel… numb.)" # [cite: 1]
    $ update_character_state("mc", CharState.ANGRY)
    mc "That won't do, Nancy. In the long run, such schedule will hurt your academic performance too, you know?" # [cite: 1]
    outline "(What?! I'm not the one saying these words!)" # [cite: 1]
    bull_phone "That's right, I possessed your body!" # [cite: 1]
    bull_phone "But don't get used to it. My power has... specific conditions. Specific purposes." # [cite: 1]
    bull_phone "I can only take control when it serves my agenda - helping you with women, pushing you toward certain outcomes." # [cite: 1]
    bull_phone "Don't expect me to possess you for mundane tasks like cleaning your room or doing homework. That's not what I'm here for." # [cite: 1]
    bull_phone "And based on your actions so far, I'll get you the best result I can with Nancy." # [cite: 1]
    bull_phone "Give enough good answers to the girls you interact with, and they'll give you something good back." # [cite: 1]
    bull_phone "Fail at that, and they'll walk away. Fail REPEATEDLY at that, and I'll walk away too, and that will be the end of this for you!" # [cite: 1]
    bull_phone "But give ALL the right answers, and you get something specially interesting… though that is also valid the other way around." # [cite: 1]
    bull_phone "If you give all the wrong answers, something especially bad might happen." # [cite: 1]
    bull_phone "Now, let me get you what you deserve! The fruit of your labor!" # [cite: 1]
    # Determine outcome based on nancy_love (centralized system)
    if nancy_key_question_passed:
        if nancy_love >= 20:  # 4+ correct choices
            jump nancy_outcome_prologue_best
        elif nancy_love >= 15:  # 3 correct choices
            jump nancy_outcome_prologue_good
        elif nancy_love >= 10:  # 2 correct choices
            jump nancy_outcome_prologue_neutral
        else: # 0 or 1 right choice
            jump nancy_outcome_prologue_worst_from_choices
    else:
        # If key question failed, it's already worst outcome handled earlier
        pass # Should already be at nancy_conversation_end
        jump nancy_conversation_sleep


# ----------------------------------------------------


label nancy_outcome_prologue_best:

    scene mall_interior_night
    $ update_character_state("nancy", CharState.AROUSED)
    show nancy at nancy_convo
    with fade

    # Best outcome: 4 right answers
    nancy "I know that… But it’s beyond of my control. I just fail to relax." # [cite: 1]
    nancy "When I lay my head on the pillow, all I can think of is how I’m still unprepared for the incoming test, and how I should be trying harder." # [cite: 1]
    mc "You’re trying hard enough already, Nancy… And you deserve a reward for that." # [cite: 1]
    nancy "A reward?" # [cite: 1]
    mc "That’s right, something to ease your nerves, to soothe you into a good night of sleep, and to motivate you to study harder the next day, not by fear, but by determination." # [cite: 1]
    mc "Something that will make you feel like everything was worth it, and that you’re in good hands, safe." # [cite: 1]
    nancy "But what could that…" # [cite: 1]
    mc "I could help you with that. As your friend, you know?" # [cite: 1]
    nancy "And- And what would that entail…?" # [cite: 1]
    mc "Something good, I promise." # [cite: 1]
    mc "Actually, maybe it would be for the best to do that right now, instead of staying yet another night awake and studying, fueled by coke, degrading your health." # [cite: 1]
    mc "What do you say? Want to come with me to the back of the store real quick?" # [cite: 1]
    # Show Nancy blushing/nervous
    nancy "…F-Fine." # [cite: 1]

    scene black
    show scene_0_initial
    stop music fadeout 1.0
    play music "ES_Pillow (Instrumental Version) - SCENE.mp3" volume 0.1
    with fade

    outline "I almost couldn’t believe my eyes- no, I almost couldn’t believe anything that happened that night." # [cite: 1]
    outline "My mouth said things that I would never be brave enough to say, and then I was looking at Nancy while she leaned against me, face blushing and respiration accelerated." # [cite: 1]
    outline "W-What was about to happen?! What did that dang phone had in mind?!" # [cite: 1]
    mc "Here we are. Just leave everything to me, and I’ll make sure that you’ll have a good night of sleep." # [cite: 1]

    hide scene_0_initial
    show scene_0
    outline "Suddenly, the hand that I could not control lunged at Nancy's breasts." # [cite: 1]
    $ play_grab_sound()
    nancy "Gyahn!" # [cite: 1]
    $ play_woman_pleasure_sound()
    play sound "ES_Human, Heartbeat - Epidemic Sound.mp3" # Assumed sound effect
    outline "My heartbeat was fast, but it couldn’t even be compared to that of Nancy; it was as if she was in the middle of a marathon." # [cite: 1]
    outline "And soon, the rest of her body started to answer her excitement too." # [cite: 1]
    mc "You’re so soft, and fill up my palms just perfectly…" # [cite: 1]
    mc "It’s such a waste that you’re constantly locked inside that damn library, keeping this away from me." # [cite: 1]
    # Show Nancy reacting more
    nancy "Ughn… Aghn…" # [cite: 1]
    $ play_woman_breathing_sound()
    outline "Her nipples quickly hardened, the redness in her face deepened, and soon sweat sprouted from her every pore." # [cite: 1]
    outline "Her breathing was irregular and deep, her thorax inflating and deflating in my hands, as if helping me massage her." # [cite: 1]
    nancy "S-Studying is- Ughn! N-Nice too…" # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "Better than this?" # [cite: 1]
    outline "I squeezed and spined her tits around, her heat and mushiness evident even through her clothes." # [cite: 1]
    $ play_grab_sound()
    nancy "Gyahn…!" # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "Maybe I should start visiting you in that library too? Give you the best of both worlds." # [cite: 1]
    mc "While you read your books at the back of the library, I could stand behind you and feel you all up…" # [cite: 1]
    nancy "*Panting, panting…!" # [cite: 1]
    $ play_woman_breathing_sound()
    mc "Maybe even go a step further, and and have some sking to skin bonding?" # [cite: 1]
    "My hands swiftly exposed her bra, and then the dew-like dropplets of sweat running between her mounds looked so sweet, I wanted to drink them straight from their source." # [cite: 1] # Requires appropriate CG or layered sprite
    $ play_grab_sound()
    nancy "Nghn…! B-But we'd be found in the library." # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "Not if you stayed quiet… Not if I quieted you down with my mouth." # [cite: 1]
    nancy "Aghn!" # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "Your tits are so beautiful, they deserve more attention than what they're getting, Nancy." # [cite: 1]
    nancy "Ughn! Aagh! Agghn!" # [cite: 1]
    $ play_woman_pleasure_sound()
    outline "She seemed to be quickly approaching a peak of ecstasy, her tired mind and body utterly unprepared for even that quick feel-up." # [cite: 1]
    mc "And while my hands are delighted to meet your tits, I have other parts that are just dying to meet them too, jealous." # [cite: 1]
    nancy "G-Gyaaahnn!!" # [cite: 1]
    $ play_woman_pleasure_sound()
    outline "Finaly, Nancy threw her head back, leaning as much as she could against the wall, standing on the tip of her toes, and had every hair of her body standing on its end." # [cite: 1]
    nancy "*Panting… Panting…" # [cite: 1]
    $ play_woman_breathing_sound()
    outline "The next moment, she hid her bra and breasts once more, and struggled to maintain a façade of naturality." # [cite: 1] # Needs sprite update

    scene mall_interior_night
    $ update_character_state("nancy", CharState.AROUSED)
    $ persistent.scene_0 = True
    show nancy at nancy_convo
    stop music fadeout 1.0
    with fade

    nancy "T-This is enough." # [cite: 1]
    mc "Whatever you say." # [cite: 1]
    outline "As much as my cock was throbbing and longing, it wasn’t the right time to be insistent, and I could tell that even without the phone nagging at me." # [cite: 1]
    mc "You think you’ll be able to sleep well this night, then?" # [cite: 1]
    nancy "…Yes. I think… this will be the best night of sleep I’ll have in weeks." # [cite: 1]
    nancy "You’re totally different from the rumors that [girl_friend] and Justin and have been spreading." # [cite: 1]
    nancy "So, uhm… Thank you, [player_name]." # [cite: 1]
    nancy "And goodbye!" # [cite: 1]

    hide nancy
    $ update_character_state("mc", CharState.AROUSED)
    $ update_character_state("bull", CharState.HAPPY)
    show mc at mc_convo
    show bull at bull_convo
    with fade

    mc "She ran away… did we scare her?" # [cite: 1] # [player_name] back in control
    bull_phone "Not at all, you naïve youngster! She is dashing to her bedroom so she can masturbate thinking about this moment, of course!" # [cite: 1]
    mc "M-Masturbate?!" # [cite: 1]
    bull_phone "That’s right, you’ve done a perfect job here today, and got her all wet." # [cite: 1]
    bull_phone "If you repeat this a couple more times, you may very well be the one getting in and out of her pussy, instead of her own fingers, hehehe." # [cite: 1]
    bull_phone "Now, take control over this body of yours again, I’ll show up only when there are girls involved." # [cite: 1]

    jump nancy_conversation_end


# ----------------------------------------------------


label nancy_outcome_prologue_good:

    scene mall_interior_night
    $ update_character_state("nancy", CharState.AROUSED)
    show nancy at nancy_convo
    with fade

    mc "Well, you’re a smart and competent girl, I know you’ll be able to take care of yourself." # [cite: 1]
    mc "Just don’t work too hard, okay?" # [cite: 1]
    nancy "Oh, [player_name], thank you." # [cite: 1]
    nancy "And… well, sorry if I sounded cold earlier. It’s just…" # [cite: 1]
    nancy "There are so really distasteful rumors about you going around campus and beyond right now, and…" # [cite: 1]
    mc "I know, Nancy, it’s alright." # [cite: 1] # Still possessed? Script implies [player_name] takes over for hug. Let's assume Bull Phone relinquishes control here.
    mc "That’s [girl_friend]’s fault, when I discovered her cheating, I broke up with her, and she decided to get ‘revenge’ by saying all sorts of bullshit about me to everyone willing to listen." # [cite: 1]
    nancy "Still, I should have taken those rumors with a grain of salt." # [cite: 1]
    nancy "Sometimes I feel like I have this dark side... judging people too quickly..." # [cite: 1]
    nancy "What represents the shadows in our hearts?"
    
    menu:
        "We all have darkness inside":
            label test_choice_6ah7e:
            if nancy_love >= 10:
                outline "Another outfit puzzle opportunity. Nancy's talking about her shadow side... her darkness."
                outline "I'm starting to understand how this works. Listen to what people reveal about themselves."
                jump outfit_8_puzzle
                label outfit_8_puzzle_success:
                    nancy "I actually have this black outfit... represents my shadow side..."
                    nancy "Maybe embracing the darkness isn't always bad..."
                label outfit_8_puzzle_failure:
                    nancy "I suppose we all struggle with our shadows..."
        "You're not dark, you're just careful":
            label test_choice_06fm3:
            nancy "Maybe you're right..."
    nancy "So, uhm… sorry, I'm not really good with this sort of thing." # [cite: 1]
    nancy "How about an 'I'm sorry hug'?" # [cite: 1]
    mc "Hahaha, yeah, I’ll gladly accept an I’m sorry hug. Come here." # [cite: 1]
    # Hug sequence - might need specific sprites or narration
    # show mc happy at left
    # show nancy slightly_blushing at right
    outline "Nancy and I closed our arms around one another, and that was the first time in months I felt any human heat and love…" # [cite: 1]
    outline "Not unsurprisingly, precisely because of that, I popped up a bonner almost immediately." # [cite: 1]
    nancy "Gah-?!" # [cite: 1]
    outline "And Nancy seemed to have noticed it too." # [cite: 1]
    outline "I despaired and wanted to pull away from her at that very moment, but the damn bull phone didn’t let me." # [cite: 1] # Phone still has some influence? Or [player_name] uses it as excuse? Assuming [player_name] pushes through.
    mc "I am also thankful, Nancy." # [cite: 1]
    mc "After everything that happened, it’s been hard to go outside without being judged, so, I appreciate this." # [cite: 1]
    outline "My cock twitched, skidding across Nancy’s bely and crumpling her top." # [cite: 1]
    outline "My veins throbbed hard, and had I been wearing any thinner pants, a wet mark would crown my erection already." # [cite: 1]
    nancy "I-I can tell that you… appreciate it." # [cite: 1]
    outline "Strangely enough, Nancy didn’t pull away immediately, but curled her fingers up, grabbing my shirt with trembling hands." # [cite: 1]
    nancy "I… I also appreciate it. I think I needed this as much as you, after all." # [cite: 1]
    outline "Finally, we came apart, and when I took a look at her face, she was red as a tomato." # [cite: 1]
    nancy "B-But I really need to go now." # [cite: 1]
    mc "I understand. Good bye, and good night Nancy." # [cite: 1]
    bull_phone "Hey, not bad, [player_name]. You managed to get on her good side, after all." # [cite: 1]
    bull_phone "Keep going like this, and we’ll get in her panties in no time, hehehe." # [cite: 1]
    mc "P-Panties?!" # [cite: 1]
    bull_phone "That’s the objective. Now, take control over this body of yours again, I have no interest of taking care of your mundane tasks." # [cite: 1]
    jump nancy_conversation_end


# ----------------------------------------------------


label nancy_outcome_prologue_neutral:

    scene mall_interior_night
    $ update_character_state("nancy", CharState.HAPPY)
    show nancy at nancy_convo
    with fade

    nancy "Well, it was good to see you, [player_name]." # [cite: 1]
    nancy "But I have to head back to my bedroom and finish reading through a certain chapter." # [cite: 1]
    nancy "Now, if you excuse me." # [cite: 1]
    mc "Of course, goodbye." # [cite: 1] # Still possessed for the goodbye? Assume yes.

    hide nancy
    $ update_character_state("mc", CharState.SAD)
    show mc at mc_convo
    with fade

    mc "This…wasn’t what I expected." # [cite: 1] # [player_name] back in control

    $ update_character_state("bull", CharState.ANGRY)
    show bull at bull_convo
    with pixellate

    bull_phone "Don’t blame me, you were the one who failed to impress her today." # [cite: 1]
    bull_phone "Be this boring three times, and I’ll seriously give up on you." # [cite: 1]
    bull_phone "Now, take care of your body again, I won’t deal with your shopping list." # [cite: 1]
    jump nancy_conversation_end


# ----------------------------------------------------


label nancy_outcome_prologue_worst_from_choices:

    scene convenience_store_night
    $ update_character_state("nancy", CharState.ANGRY)
    show nancy at nancy_convo
    with fade

    nancy "You know what, [player_name]? You just made me realize something." # [cite: 1]
    mc "What is it?" # [cite: 1] # Still possessed? Assume yes.
    nancy "I need to relax a bit from all this studying. And I just know how." # [cite: 1]
    mc "Of really, and how?" # [cite: 1]
    nancy "By following the example of [girl_friend], of course." # [cite: 1]
    mc "E-Eh…?" # [cite: 1]
    nancy "Honestly, I don’t even know how she managed to be your girlfriend for so long, you’re utterly hopeless." # [cite: 1]
    nancy "But after talking to you, just in these short few minutes, I have realized that ANY other man would be more pleasing to be with than you." # [cite: 1]
    nancy "And that’s exactly what I’ll look for: any other man." # [cite: 1]
    nancy "And you’ll help me with that." # [cite: 1]
    bull_phone "Hell no, you take care of things from here on. You messed this up seriously, [player_name], you haven’t said more than just one thing that she liked!" # [cite: 1]
    mc "W-What do you want me to do?" # [cite: 1] # [player_name] back in control
    nancy "Come with me." # [cite: 1]
    outline "Nancy took me to the cashier, and picked a package of condoms." # [cite: 1]
    nancy "Buy these for me." # [cite: 1]
    mc "You’ll need… all of this?" # [cite: 1]
    nancy "Don’t get your hopes up, I won’t use a single one with you." # [cite: 1]
    nancy "I doubt that they would even fit your tiny cock." # [cite: 1]
    nancy "But you better bet that every other guy neighbor of yours is gonna have a really good time." # [cite: 1]
    nancy "Now, don’t waste my time any further, and buy them for me. I won’t repeat myself a third time." # [cite: 1]
    mc "Alright, alright! H-Here’s the money." # [cite: 1]
    outline "I paid for the condoms, and I couldn’t even face the cashier, who threw me a look so filled with pity, even a dying abandoned puppy wouldn’t be stared like that." # [cite: 1]
    nancy "God, you’re pathetic. Just having met you today has fucking ruined my night." # [cite: 1]
    hide nancy with dissolve
    outline "At last, I was left alone." # [cite: 1]
    bull_phone "This was the worst result you could have gotten from this. Repeat this bullshit again two more times, and I’ll seriously give up on you, dude." # [cite: 1]
    jump nancy_conversation_end


# ----------------------------------------------------


label nancy_conversation_end:

    outline "After that, I bought my food, and returned to my bedroom." # [cite: 1]
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with Fade(0.5, 5.0, 0.5)

    mc "*Sigh!" # [cite: 1]
    outline "I threw myself in bed. It had been so long, I had forgotten how tiresome interacting with other people could be." # [cite: 1]

    $ update_character_state("bull", CharState.NORMAL)
    show bull at bull_convo
    with pixellate

    bull_phone "It’s only tiresome, because you’re a bit… no, a lot… no, EXTREMELY rusty in this, but you’ll get used to it. And you’ll like it." # [cite: 1]
    bull_phone "Put in practice everything that I taught you today, and your rewards shall be great, hehehe." # [cite: 1]
    bull_phone "Approach girls, give them the right answers based on their personalities, don’t mess up three dates, and soon you won’t ever need to masturbate again!" # [cite: 1]
    mc "Masturbate…?" # [cite: 1]

    $ update_character_state("mc", CharState.AROUSED)

    # Nancy outfit unlock during the good ending scene
    if nancy_love >= 20:
        menu:
            "Think about Nancy's devotion":
                label test_choice_z9w4m:
                outline "Nancy's devotion to me is incredible..."
                outline "She wants to serve, to be completely devoted..."
                outline "What am I showing when I care for others without expecting anything back?"
                jump outfit_6_puzzle
                label outfit_6_puzzle_success:
                    outline "Complete, devoted service... she'd make an amazing partner."
                label outfit_6_puzzle_failure:
                    outline "Maybe I don't fully understand her devotion yet..."
    elif nancy_love >= 15:
        menu:
            "Think about how Nancy sees me":
                label test_choice_v8k2p:
                outline "The way Nancy looks at me... like I'm something precious..."
                outline "Like I deserve royal treatment..."
                outline "What represents luxury and being treated like nobility?"
                jump outfit_7_puzzle
                label outfit_7_puzzle_success:
                    outline "She deserves to be treated like a princess in return."
                label outfit_7_puzzle_failure:
                    outline "Maybe I misunderstood what she was looking for..."
    scene black
    with fade
    # Masturbation sequence based on Nancy outcome
    if nancy_love >= 20:  # best outcome
        outline "I had to admit it, after groping Nancy’s tits and hearing her moans, I ended up really hard, so much so that my cock was still painfully erect." # [cite: 1]
        outline "I probably wouldn’t be able to think straight about anything until I dealt with that." # [cite: 1]
        menu:
            "Masturbate":
                label test_choice_9etsv:
                outline "And so, I allowed my hands to slid down my pants…" # [cite: 1]
        jump masturbation_sequence
    elif nancy_love >= 15:  # good outcome
        outline "The memory of Nancy’s body against mine, her sweet smell, her soft tits, it was all still way too vivid in my mind." # [cite: 1]
        outline "It was all still too vivid for my cock: I throbbed and begged for release." # [cite: 1]
        menu:
            "Masturbate":
                label test_choice_aiv4w:
                outline "And so, I allowed my hands to slid down my pants…" # [cite: 1]
        outline "And I heard it, sliding my hands down my pants…" # [cite: 1]
        jump masturbation_sequence
    elif nancy_love >= 10:  # neutral outcome
        outline "I had to admit it, I had greater expectations for how tings would end up with Nancy." # [cite: 1]
        outline "But everything went just as the Bull Phone promised me they would, every mistake and right thing." # [cite: 1]
        outline "If I just heard him, I’d get to really good things." # [cite: 1]
        outline "And when I thought about really good things, I popped a boner." # [cite: 1]
        menu:
            "Masturbate":
                label test_choice_gwtpd:
                outline "And so, I allowed my hands to slid down my pants…" # [cite: 1]
        outline "I reached for my quickly hardening cock." # [cite: 1]
        jump masturbation_sequence
        jump nancy_conversation_end
    else:  # worst outcome
        outline "Things had gone terribly wrong, and I just wanted a way to distract myself from that, so the phone’s suggestion didn’t seem so bad, then." # [cite: 1]
        menu:
            "Masturbate":
                label test_choice_doou2:
                outline "And so, I allowed my hands to slid down my pants…" # [cite: 1]
        outline "I whipped my cock out , and wrapped my fingers around it." # [cite: 1]
        jump masturbation_sequence


# ----------------------------------------------------


label masturbation_sequence:

    scene home_night
    show mc at mc_convo
    stop music fadeout 1.0
    $ update_character_state("mc", CharState.SAD)
    with fade

    outline "(Let me think about something good, something that will help me to finish this off…)" # [cite: 1]
    outline "(Nancy is beautiful, but I haven’t seen nearly enough of her to jerk off about the situation.)" # [cite: 1]
    outline "(No, instead, the first one I think of when I imagine a naked hot woman to have fun with is…)" # [cite: 1]
    mc "[girl_friend]." # [cite: 1]

    # Flashback/Fantasy sequence - Use CGs or different scene/sprites
    scene black
    show scene_1_initial
    with fade

    outline "When I closed my eyes, I saw my ex-girlfriend's huge naked ass." # [cite: 1]
    outline "As much as she has hurt me, I'd be lying if I said that she hasn't made me feel just as good too." # [cite: 1]
    outline "And that memory in particular was one of my favorites." # [cite: 1]
    $ play_handjob_sound()  # MC starts masturbating
    jane "Hmmm…" # [cite: 1]
    $ play_woman_pleasure_sound()
    outline "She positioned my dick right against her wet slit, and I felt her juices washing over me, dripping onto my cock and spreading over its glans and shaft." # [cite: 1]
    $ play_vagina_insertion_sound()
    jane "Can you see it, [player_name]? I'm just so wet…" # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "I can see it. And now I want to FEEL it." # [cite: 1]
    $ play_man_pleasure_sound()
    jane "~Oh my. You're so eager… I like that." # [cite: 1]
    outline "Slowly, [girl_friend] lowered her waist down, taking me inside of her inch by inch." # [cite: 1]
    $ play_penetration_sound()
    $ play_handjob_sound()  # MC continues masturbating
    jane "Hyumm…!" # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "Augh, damn!" # [cite: 1]
    $ play_man_pleasure_sound()

    scene black
    show scene_1

    outline "Her pussy gripped onto my cock with a NASCAR tire grip, the wet friction alone pushing all my buttons." # [cite: 1]
    $ play_penetration_sound()
    $ play_handjob_sound()  # MC continues masturbating
    outline "By the time I was fully inside of her, and she had her tight asshole pointed straight at me face, my cock was throbbing so hard, stealing so much of my blood, that I felt as if I could faint." # [cite: 1]
    jane "You've been a good boy recently, and good boys deserve a treat, right?" # [cite: 1]
    $ play_woman_pleasure_sound()
    outline "Her breathing was deep and shaky, but I was even worse. There was no doubt about who was in control there." # [cite: 1]
    outline "And she knew it. And she showed it." # [cite: 1]
    mc "Gaahn…!" # [cite: 1]
    $ play_man_pleasure_sound()
    outline "[girl_friend] finally started to get serious, and her hips started moving up and down with loud squelching sounds." # [cite: 1] # Add sound effects
    $ play_vagina_insertion_sound()
    $ play_woman_pleasure_sound()
    jane "Hmm, hm, aaughn…" # [cite: 1]
    $ play_woman_pleasure_sound()
    outline "It was as if her pussy had a gravitational pull of its own, and whenever she pulled her hips up, a vacuum seemed to pull more pre-cum out of my tip, making it into a fountain of natural lubricant." # [cite: 1]
    $ play_vagina_insertion_sound()
    $ play_handjob_sound()  # MC still masturbating
    jane "Mmmmm, do you hear these sounds?" # [cite: 1]
    "*Squelch, squish, splash!" # [cite: 1]
    $ play_vagina_insertion_sound()
    outline "I wasn't so much as clapping her ass, as she was drowning my cock with her pussy." # [cite: 1]
    jane "You seem to be even wetter than I am." # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "You're just so fucking hot, [girl_friend]!" # [cite: 1]
    $ play_man_pleasure_sound()
    outline "At my compliment, she picked up speed, bringing her hole down on me, jerking me off with her vaginal walls even faster, louder, sloppier." # [cite: 1]
    $ play_penetration_sound()

    scene black
    show scene_2
    with fade

    $ play_woman_pleasure_sound()
    jane "D-Do you think so? Gahn!" # [cite: 1]
    $ play_woman_breathing_sound()
    outline "She didn't seem completely unaffected by all of that either: her breathing turned faster, more irregular, and the heartbeat I felt through my glans grew faster." # [cite: 1]
    jane "Compliment me more, then." # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "Gahn-! Your ass is just so fucking huge!" # [cite: 1]
    $ play_man_pleasure_sound()
    jane "More! More!" # [cite: 1]
    mc "And your pussy is so tight! Aaghn! You're gonna milk me dry!" # [cite: 1]
    $ play_man_pleasure_sound()
    $ play_handjob_sound()  # MC getting close to climax
    jane "Yes, completely dry! I'll milk you until you're nothing but the husk of a man, [player_name]!" # [cite: 1]
    $ play_woman_pleasure_sound()
    outline "Seemingly satisfied with herself, [girl_friend] bounced on my cock at light speed , splashing both of our juices everywhere with each jump." # [cite: 1]
    $ play_penetration_sound()
    outline "And with each new impact of her ass against my hips, whenever she devoured my cock with her massaging pussy, I got closer to the finish line, and just just by a step or two, but by miles." # [cite: 1]
    outline "That was just how sexy she was, how ecstatic her pussy was, how mindblowing her technique was." # [cite: 1]
    mc "I-I'm gonna-" # [cite: 1]
    $ play_man_pleasure_sound()
    jane "Cum, [player_name]! Shoot your shot! For me! Just for me! Show me just how good you think I am!" # [cite: 1]
    $ play_woman_pleasure_sound()
    outline "As much as I wanted to see [girl_friend] cumming first, as much as I wanted to be the one to make her feel good, she seemed satisfied enough in her position." # [cite: 1]
    outline "So, I didn't hold back, but stretched my legs, curled up my toes, and…" # [cite: 1]
    $ play_handjob_sound()  # Final masturbation strokes

    scene scene_1_final
    with fade

    mc "Guhnn…! Aaagghh!" # [cite: 1] # Climax effect/sound
    $ play_cum_sound()
    $ play_man_pleasure_sound()

    stop sound # Stop the looping squelch sound
    outline "I released my sperms, so desperate to find their way to her egg." # [cite: 1]
    jane "Hmmm…!" # [cite: 1]
    $ play_woman_pleasure_sound()
    mc "*Panting… Panting…" # [cite: 1]
    $ play_man_breathing_sound()
    jane "You came so much… Good boy. You make me proud." # [cite: 1]

    outline "Soon after I came in that memory, I came in real life, as I was masturbating along my recollection of that event." # [cite: 1]
    outline "And so, once that I was finally destressed and mindful, I cleaned myself and sat up on my bed, thinking deeply about… everything." # [cite: 1]
    $ play_man_breathing_sound()
    
    $ persistent.scene_1 = True
    $ persistent.scene_2 = True


    play music "ES_Annoying - Ludvig Moulin.mp3" volume 0.3
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.SAD)
    with fade

    mc "She always took control of everything, and I didn’t pay that any mind. I always thought that she just had more fun this way." # [cite: 1]
    mc "I just wanted to make her happy." # [cite: 1]

    show bull at bull_convo
    $ update_character_state("bull", CharState.NORMAL)
    with pixellate

    bull_phone "You can never be good enough to make a bitch happy, [player_name], that was your mistake." # [cite: 1]
    bull_phone "Bitches can’t be treated like ladies, but as the dogs in heat they are." # [cite: 1]
    mc "…You said that, if I give you my ears, you’ll help me, right?" # [cite: 1]
    mc "Make me get out of this place." # [cite: 1]
    bull_phone "Seems like someone has finally stopped to dig their own hole, and look up, hehehe." # [cite: 1]
    bull_phone "That’s right, [player_name], hear me out, and I’ll help you get back the life you gave up for the sake of your bitch ex." # [cite: 1]
    mc "Alright. I’ll hear you out. I want to get back at… everyone." # [cite: 1]
    mc "Every single bastard who has fucked my ex, every girl that has been looking own on me because of the rumors she spread, and mostly, I want to make [girl_friend] regret." # [cite: 1]
    bull_phone "Yeah, that’s what I wanted to hear, that’s the expression that you should be wearing right now, not that self-pitying shitface." # [cite: 1]
    bull_phone "But if you want to take the first step to completing your vengeance, you must start slow, with something easy so that you can get the hand of things." # [cite: 1]
    bull_phone "Therefore, we should start this with something easy." # [cite: 1]
    bull_phone "So, who is the girl that you think would give in to your advances the easiest?" # [cite: 1]

    play effects "ES_Effect, Strange Ring 04 - Epidemic Sound.mp3"

    mc "Well… There was this girl who used to be interested in me, before I started dating [girl_friend]." # [cite: 1]

    scene university_front_night
    show lauren at lauren_convo
    with fade

    mc "She used to be quite pretty, and seemed nice enough, but I ended up choosing [girl_friend] instead… unfortunately." # [cite: 1]
    mc "Her name was Lauren. I don't know what she thinks of me nowadays, though, especially after all these rumors started going around." # [cite: 1]
    bull_phone "Lauren, huh? Let me see..." # [cite: 1]
    outline "The phone's screen flickered with those same strange symbols I saw when I first picked it up." # [cite: 1]
    bull_phone "Ah yes, Lauren Mitchell. Age 20. Studies literature. Lives alone in apartment 4B on Rosewood Avenue." # [cite: 1]
    mc "How do you know all that?! I never saved her information!" # [cite: 1]
    bull_phone "I have my ways. Let's just say my 'database' isn't limited to what's stored on this device." # [cite: 1]
    bull_phone "I know things. I see connections. I access... let's call it the underlying fabric of information." # [cite: 1]
    mc "That's impossible. You're just a phone-" # [cite: 1]
    bull_phone "Am I? Am I really 'just' anything? Here, I'm calling her now..." # [cite: 1]

    play sound "ES_Telephone Ringback Tone - Epidemic Sound.mp3"

    mc "Wait, what?!" # [cite: 1]


    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.AROUSED)
    show bull at bull_convo
    with fade

    bull_phone "You want to follow through with my plan, right? So, I’m inviting her out on a date with you." # [cite: 1]
    mc "B-But I don’t even know what to say!" # [cite: 1]
    bull_phone "Then, you better start thinking about that, because... she just picked up my call!" # [cite: 1]
    menu:
        "Grab the phone":
            label test_choice_szgq8:
            mc "Eh-?!" # [cite: 1]



    mc "…Lauren? Hello?" # [cite: 1]
    lauren "(on phone) …Hello." # [cite: 1]
    mc "Uhm…" # [cite: 1]
    mc "(Shit, what do I say? ‘It’s been a long time, let’s fuck’? Now way!)" # [cite: 1]
    mc "(No, remember what the damn phone said. Let’s start this slow, slow.)" # [cite: 1]
    mc "So, how you’ve been?" # [cite: 1]
    lauren "(on phone) …Good." # [cite: 1]
    mc "That’s good, haha. Yeah, being good is good…" # [cite: 1]
    mc "Uhm, you know, I…" # [cite: 1]
    mc "*Sigh." # [cite: 1]
    mc "I don’t know. I was just thinking about the past. And I felt nostalgic." # [cite: 1]
    mc "I think you really do only realize how important the things you had in your life were after you lose them." # [cite: 1]
    lauren "(on phone) …" # [cite: 1]
    mc "…I miss you, Lauren. And I was thinking, maybe we could meet up any of these days? Be friends again?" # [cite: 1]
    lauren "(on phone) …" # [cite: 1]
    mc "(Did I mess this up? Do I really have no hope of ever getting out of this depressive episode?)" # [cite: 1]
    lauren "(on phone) Meet me at the park tomorrow. 09:00 AM." # [cite: 1]
    mc "Y-Yes! I’ll be there!" # [cite: 1]

    menu:
        "Hang up the phone":
            label test_choice_05wqx:
            play sound "ES_Mobile Phone, Hang Up Beeps - Epidemic Sound.mp3"

    "Beep, beep, beep…" # [cite: 1]

    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.AROUSED)
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with fade

    bull_phone "Monotone all throughout, then turning off her phone as soon as she agreed on going out on a date with you…" # [cite: 1]
    bull_phone "Are you sure that this girl used to like you not long ago? She might be actually planning on murdering you." # [cite: 1]
    mc "She… is a unique character, for sure. But she even confessed to me once, so I’m sure she harbored feelings for me." # [cite: 1]
    mc "Though, that’s probably not the case anymore, she might still see me as someone who she is capable of hitting off." # [cite: 1]
    mc "Or so I hope, I’d hate to die before getting my revenge on anyone." # [cite: 1]
    bull_phone "Yeah, speaking of that, don’t you think you have some things to do now?" # [cite: 1]
    bull_phone "You have a date tomorrow, dude! Shave that beard, iron your best clothes!" # [cite: 1]
    bull_phone "And for goodness sake, take a bath! I swear, you spent so much time in here, I wouldn’t be surprised if there were mushrooms growing out of your hair." # [cite: 1]
    mc "There aren’t mushrooms anywhere in my body." # [cite: 1]
    outline "Though extremely exaggerated, there was truth to the phone’s words, and so I started to get myself and my clothes in shape." # [cite: 1]
    outline "I’d have a long day tomorrow." # [cite: 1]
    outline "By the time I was done with everything, I practically fainted on my bed." # [cite: 1]

    stop music fadeout 1.0
    scene black with fade

    # Next morning
    # play sound "alarm_clock.ogg" # Assumed sound effect
    bull_phone "Wake up, soldier, you’re late!" # [cite: 1]

    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.SAD)
    show bull at bull_convo
    with fade

    mc "Wagh?!" # [cite: 1]
    mc "W-What hour is it?!" # [cite: 1]
    bull_phone "06 AM." # [cite: 1]
    mc "Then, I’m no late at all!" # [cite: 1]
    bull_phone "But you’ll be, with that mentality." # [cite: 1]
    mc "(Is this phone really helping me? Maybe I should throw it in a fire, or get it exorcised by a priest.)" # [cite: 1]
    mc "But I'm already awake now, anyway. I guess I'll have some breakfast and start to get ready." # [cite: 1]
    outline "After a humble breakfast and dressing up, even putting on some cologne, something that I didn't do in months, I was finally ready to go." # [cite: 1]

    $ notify(_("You have a date with Lauren at the park. Don't be late!"))
    
    # Grant prologue completion achievement
    $ achievement.grant("FIRST_STEPS")
    $ achievement.sync()

    $ check_love_achievements()

    jump home