# Episode 3 uses centralized points system from points_system.rpy
default gym_trap_success = False
default remembered_doctor = False
default doctor_flashback_intensity = 0

label episode_3:
    
    scene college_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    # MUSIC PLACEHOLDER: Upbeat, optimistic college theme - MC feeling confident about confronting Matthews
    play music "ES_All That I Want - Brendon Moeller.mp3" volume 0.2
    with Fade(0.5, 5.0, 0.5)
    
    "Walking through the college corridors, I notice something different today."

    "Some students who usually whisper and snicker when they see me are now looking away, uncertain."

    "Others nod slightly in acknowledgment, as if they're not quite sure what to make of me anymore."

    outline "The girls I've been with must be spreading the word that [girl_friend]'s stories were bullshit."

    outline "I'm not completely redeemed yet, but at least I'm not the campus pariah anymore."

    outline "Lauren must have told her friends about our dates, and if Nancy said anything positive..."

    outline "Still, most people probably think I'm the same loser [girl_friend] painted me as."

    outline "But it's time to change that narrative once and for all."
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    bull_phone "Feeling the change in the air, buddy?"
    mc "Yeah, it's strange but good strange. Like I'm not invisible anymore - people actually look at me instead of through me."
    bull_phone "That's the power of having allies, especially female allies who vouch for your... capabilities. But don't get cocky - most people still think you're a wimp and you've got work to do."
    $ update_character_state("mc", CharState.ANGRY)
    mc "I know, that's why I'm here - to ace Matthews' class and show everyone I'm back. That bastard has been humiliating me in front of everyone for months."
    bull_phone "And he probably fucked your ex-girlfriend too, just like all the other authority figures in your life."
    mc "Probably, but today's different - today I fight back."
    bull_phone "That's what I like to hear! Show him you're not the same broken boy he used to kick around."
    
    hide bull
    with pixellate
    
    scene classroom_light_on
    show matthews at matthews_convo
    $ update_character_state("matthews", CharState.NORMAL)
    with fade
    
    matthews "Well, well, well. Look who decided to grace us with his presence."

    matthews "Mr. [player_name], I hope you've been keeping up with the material during your... extended absence,"

    matthews "though I suppose grieving the loss of your dignity takes time."
    
    "The class goes quiet."
    "Some students look uncomfortable with Matthews' cruelty."
    "Others lean forward, expecting entertainment."
    
    $ update_character_state("mc", CharState.NORMAL)
    
    matthews "Tell me, can you explain the concept we discussed last week? Or were you too busy... crying at home?"
    matthews "I know it must be hard to focus on quantum mechanics when your personal life is in such... quantum uncertainty."
    
    "A few students snicker, but not as many as before."
    "Some girls roll their eyes at Matthews' behavior."
    
    menu:
        "Actually, I've been studying ahead. The concept you're referring to...":
            label test_choice_k9wyq:
            $ win_sound()
            $ emma_love += 5
            $ update_character_state("mc", CharState.NORMAL)
            mc "Actually, I've been studying ahead. The concept you're referring to is the Heisenberg uncertainty principle -"

            mc "it states that we cannot simultaneously know both the exact position and momentum of a particle,"

            mc "and the more precisely we determine one, the less precisely we can know the other."
            $ update_character_state("mc", CharState.HAPPY)
            mc "Kind of like how the more you try to humiliate me, the less respect you get from students who see through your bullshit."

            mc "Uncertainty works both ways, Professor - maybe you should be less certain about who you're dealing with."
            $ update_character_state("matthews", CharState.ANGRY)
            matthews "That's... correct, but watch your tone, Mr. [player_name]. Knowledge without respect is just arrogance."
            $ update_character_state("mc", CharState.HAPPY)
            mc "Funny, I was thinking the same thing about you."
            "The class murmurs in surprise."
            "A few girls whisper excitedly."
    matthews "You seem to think you command this classroom now..."
    
    menu:
        "What kind of leader commands through respect?":
            label test_choice_k7vft:
            if emma_love >= 5:
                outline "Matthews thinks he's some kind of commanding officer..."
                outline "What does a naval commander lead?"
                jump outfit_46_puzzle
                label outfit_46_puzzle_success:
                    outline "Too bad his ship is sinking with his poor teaching style!"
                label outfit_46_puzzle_failure:
                    outline "Matthews' authority complex is showing..."
        "Continue the lesson":
            label test_choice_g0h8i:
            "The class continues with tension in the air."
        "I've been busy with more important things than your boring lectures.":
            label test_choice_t51yr:
            $ lose_sound()
            $ update_character_state("mc", CharState.ANGRY)
            mc "I've been busy with more important things than your boring lectures."
            matthews "Oh? Like what - crying into your pillow, or perhaps writing angry letters to your ex-girlfriend's new boyfriend?"
            "More laughter. I feel my confidence wavering."
            $ update_character_state("mc", CharState.SAD)
            mc "No, I..."
            matthews "That's what I thought. Take your seat and try to keep up, though at this point I doubt you can catch up to where we are."
        "Why don't you ask your wife what I've been up to?":
            label test_choice_vrfqx:
            $ lose_sound()
            $ emma_love -= 5
            mc "Why don't you ask your wife what I've been up to?"
            matthews "Excuse me?"
            mc "You heard me. Maybe she can fill you in on what I've been studying."
            matthews "Get out of my classroom. NOW."
            mc "Gladly. This place reeks of desperation anyway."
            "I storm out, realizing too late that was stupid."
            "But at least I didn't back down."
            jump emma_approaches_after_class
            
    matthews "Now, as I was saying before the interruption..."
    matthews "Today we'll be discussing wave-particle duality. Though some of you might struggle with the concept of having dual natures."
    matthews "In physics, as in archaeology, we must dig deep to uncover hidden truths..."
    
    menu:
        "What do archaeologists uncover from the past?":
            label test_choice_1fqbv:
            if emma_love >= 5:
                outline "Matthews thinks he's so scholarly... digging into old knowledge..."
                outline "What do archaeologists find when they dig deep?"
                jump outfit_47_puzzle
                label outfit_47_puzzle_success:
                    outline "Too bad he can't dig himself out of his inappropriate behavior!"
                label outfit_47_puzzle_failure:
                    outline "Matthews' academic pretensions are showing..."
        "Focus on the physics lesson":
            label test_choice_ze6vw:
            "The lesson continues with wave-particle duality..."
    "The class continues, but Matthews keeps glancing at me nervously."
    "When he calls on students, he avoids me entirely."
    "His usual confident demeanor seems shaken."
    hide matthews
    show mc at mc_convo
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    bull_phone "Did you see that? He's rattled. He noticed something different about you."
    bull_phone "You're not the same pushover he could mock freely anymore."
    outline "Good. Let him wonder what changed."
    outline "I can see some students looking at me differently too."
    bull_phone "That's right! You just showed them you have balls. Now they're reassessing everything they thought they knew about you."
    bull_phone "Keep this energy. Don't let anyone walk over you anymore."
    hide bull
    with pixellate
    "The class ends, and students file out. I gather my things slowly, feeling more confident than I have in months."
    "A few students even nod at me as they pass - not in mockery, but in what seems like respect."
label emma_approaches_after_class:
    scene college_afternoon
    show emma at emma_convo
    $ update_character_state("emma", CharState.NORMAL)
    # MUSIC PLACEHOLDER: Tense, confrontational theme - Emma bullying MC in hallway
    play music "ES_Let's Go - Krithi.mp3" volume 0.1
    with fade
    $ update_character_state("emma", CharState.ANGRY)
    emma "Well, well. If it isn't the campus cuckold."
    emma "I heard some ridiculous rumors that you've been getting with girls lately."
    emma "But we both know that's impossible, right? I mean, look at you."
    emma "You're still the same pathetic loser who let [girl_friend] walk all over him."
    $ update_character_state("mc", CharState.NORMAL)
    emma "You have no balls, no spine, no nothing."
    emma "[girl_friend] told everyone how you used to beg her for the tiniest bit of affection."
    emma "How you'd cry when she went out with real men."
    emma "She said you even offered to watch while she fucked other guys, just to stay with her."
    emma "Is that true, [player_name]? Are you really that pathetic?"
    menu:
        "You're right, Emma. Want to go on a date and see for yourself?":
            label test_choice_evlqi:
            $ win_sound()
            $ emma_love += 5
            $ update_character_state("mc", CharState.HAPPY)
            mc "You're right, Emma. Want to go on a date and see for yourself? I mean, if you're so confident about what kind of man I am, prove it."
            $ update_character_state("emma", CharState.ANGRY)
            $ update_character_state("emma", CharState.ANGRY)
            emma "W-What?! Did you just... did you just ask me out?"
            mc "You heard me - tomorrow, 5 PM, unless you're scared to find out [girl_friend] was lying. What's the matter, the great Emma can't handle one little date with a 'loser'?"
            $ update_character_state("emma", CharState.NORMAL)
            emma "I... You... You can't just..."
            mc "What's wrong, the popular girl is speechless? Come on, it'll be fun - you can show everyone what a wimp I am, right?"
            emma "Fine! But only to prove to everyone what a pathetic loser you really are! I'll make sure the whole university knows just how much of a wimp you are!"
            mc "Looking forward to it. I promise it'll be... educational."
        "Fuck off, Emma. I don't have time for your bullshit.":
            label test_choice_l48vx:
            $ lose_sound()
            $ update_character_state("mc", CharState.ANGRY)
            mc "Fuck off, Emma. I don't have time for your bullshit - find someone else to boost your ego with."
            emma "Oh, touched a nerve? Going to cry like you did with [girl_friend], or are you going to run home and sob into your pillow about how mean I was?"
            $ update_character_state("mc", CharState.ANGRY)
            mc "I said fuck off!"
            $ update_character_state("emma", CharState.HAPPY)
            emma "Make me, loser. Oh wait, you can't. Because you're a spineless little-"
            $ update_character_state("mc", CharState.NORMAL)
            mc "You know what? Fine. Want to see what a loser I am? Go on a date with me."
            $ update_character_state("emma", CharState.NORMAL)
            emma "What?"
            mc "Tomorrow, 5 PM, unless you're too scared. I mean, you're so confident I'm pathetic, it should be easy to prove, right?"
            $ update_character_state("emma", CharState.ANGRY)
            emma "I'm not scared of you! Fine! I'll show everyone what a pathetic worm you are!"
        "Is that what Justin tells you to make you feel better about dating [girl_friend]'s sloppy seconds?":
            label test_choice_0poxu:
            $ lose_sound()
            $ emma_love -= 5
            mc "Is that what Justin tells you to make you feel better about dating [girl_friend]'s sloppy seconds?"
            mc "I mean, he was fucking her too, right? Does it bother you that your boyfriend's dick has been in my ex-girlfriend?"
            $ update_character_state("emma", CharState.ANGRY)
            emma "How DARE you!"
            "She slaps me hard across the face."
            $ update_character_state("mc", CharState.SAD)
            $ update_character_state("emma", CharState.ANGRY)
            emma "Don't you EVER talk about Justin like that!"
            emma "You're nothing compared to him! NOTHING!"
            emma "He's everything you'll never be - strong, confident, popular!"
            $ update_character_state("mc", CharState.NORMAL)
            mc "Then prove it. Date with me tomorrow."
            $ update_character_state("emma", CharState.ANGRY)
            emma "You're delusional if you think I'd waste my time with you!"
            mc "Scared?"
            emma "...Fine. But only to humiliate you in front of everyone!"
    $ update_character_state("emma", CharState.ANGRY)
    emma "Don't think this means anything, loser. I just want everyone to see what a joke you are."
    emma "Tomorrow at 5. Don't be late, or I'll tell everyone you were too scared to show up."
    emma "And trust me, by the time I'm done with you, you'll wish you'd never been born."
    hide emma
    with fade
    scene home_afternoon
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    $ update_character_state("mc", CharState.SAD)
    stop music fadeout 1.0
    mc "Did I really just ask Emma out on a date?"
    mc "Emma, the girl who's been one of my biggest bullies since [girl_friend] started spreading her lies."
    mc "What the hell was I thinking?"
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    bull_phone "You did, and it was beautiful! Did you see her face?"
    mc "She looked... confused. Almost happy for a second before covering it up."
    mc "Like she couldn't believe someone actually asked her out."
    bull_phone "That's because I think she actually likes you, deep down."
    mc "Emma? Like me? That's ridiculous."
    mc "She's been nothing but cruel to me since [girl_friend] turned everyone against me."
    bull_phone "Think about it. She's dating Justin, right? But she came to YOU to tease and bully."
    bull_phone "If she really thought you were nothing, she'd ignore you completely."
    bull_phone "Instead, she seeks you out. She pays attention to you. That's not hatred - that's interest."
    mc "I guess..."
    mc "But even if you're right, she's with Justin. The quarterback. Mr. Perfect."
    bull_phone "But here's the thing - her reputation and her boyfriend won't let her admit any feelings easily."
    bull_phone "You need intel. You need to know what makes her tick, what she really wants."
    bull_phone "How does she really feel about Justin? What are her insecurities? Her desires?"
    mc "What are you suggesting?"
    bull_phone "Follow her tomorrow. See how she acts with Justin. Learn her routine, her interests."
    bull_phone "Knowledge is power, my friend. And you'll need all the power you can get to crack this nut."
    mc "That's... kind of stalkerish."
    bull_phone "It's research. You want to impress her or not?"
    bull_phone "Besides, it's a public place. You're not breaking into her house."
    mc "...Fine. I'll do it."
    mc "But this better work. If she humiliates me in front of everyone..."
    bull_phone "Trust me. By the time I'm done helping you, she'll be the one begging for your attention."
    $ update_character_state("mc", CharState.HAPPY)
    hide bull
    with pixellate
    mc "Alright, tomorrow's the big day. I better get some sleep and prepare for this."
    mc "I can't believe I'm actually going to spy on Emma, but if it helps me understand her..."
    "I spend the rest of the evening going over what I know about Emma."
    "Her schedule, her relationship with Justin, her insecurities about her intelligence."
    "Eventually, exhaustion takes over and I fall asleep, wondering what tomorrow will bring."
    scene black
    with fade
    "..."
    "......"
    "........."
    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with Fade(0.5, 3.0, 0.5)
    play music "ES_Everyone Dance - Guustavv.mp3" volume 0.2
    "I wake up early, my alarm buzzing insistently."
    "Today's the day I follow Emma around campus to learn more about her."
    "Part of me feels like a stalker, but the Bull Phone insisted this was necessary."
    mc "Okay, let's do this. Time to see what Emma's really like when she thinks no one's watching."
    mc "If I'm going to have any chance with her, I need to understand what makes her tick."
    "I get dressed quickly and head out to campus, arriving earlier than usual."
label following_emma:
    scene college_morning
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    "I position myself where I can watch for Emma without being too obvious."
    "I feel like a creep doing this, but I need to understand her if I want to succeed."
    "Sure enough, she arrives with Justin, clinging to his arm and laughing loudly."
    "But even from a distance, something seems... forced about her laughter."
    show justin at justin_convo
    $ update_character_state("emma", CharState.HAPPY)
    $ update_character_state("justin", CharState.HAPPY)
    justin "Babe, I got practice. You good?"
    hide justin
    show emma at emma_convo
    play music "ES_Let's Go - Krithi.mp3" volume 0.2
    emma "Yeah, I'm going to hit the gym. Need to keep this body perfect for you."
    emma "Can't have my boyfriend dating anything less than perfection, right?"
    hide emma
    show justin at justin_convo
    justin "That's my girl. Just... don't overdo it, okay? I like you just how you are."
    justin "Besides, too much muscle on a girl is gross. You're perfect as my little trophy."
    hide justin
    show emma at emma_convo
    emma "You're so sweet!"
    emma "I love how you always know exactly what to say to make me feel special."
    "They kiss, and I feel a strange mix of disgust and... something else. Jealousy? No, that can't be right."
    "But I notice Emma's smile falter slightly when Justin calls her his 'little trophy.'"
    "Is that really how he sees her? Just an object to show off?"
    hide emma
    show justin at justin_convo
    justin "Alright, gotta run. Coach will kill me if I'm late again."
    justin "Try not to miss me too much while I'm gone, babe."
    hide justin
    show emma at emma_convo
    emma "I'll try to contain myself somehow."
    hide emma
    with fade
    "Justin heads to the football field while Emma goes toward the gym."
    "I follow at a safe distance, curious to see how she acts when she's alone."
    scene gym_morning
    show emma at emma_convo
    $ update_character_state("emma", CharState.NORMAL)
    with fade
    "Emma works out with intense focus, but I notice something interesting."
    "She keeps checking her phone, frowning each time."
    "No messages from Justin, I'm guessing."
    "Her workout is impressive though - she's clearly dedicated and strong."
    "Not just a pretty face like people assume."
    emma "*sigh* Come on, Emma. Push through it."
    emma "He said he'd text during his break..."
    emma "Maybe he's just busy. Yeah, that's it."
    "After an hour, she leaves, looking frustrated and disappointed."
    "Still no messages, apparently."
    scene gym_morning
    show emma at emma_convo
    $ update_character_state("emma", CharState.ANGRY)
    with fade
    "She goes back to the gym, sitting down in a quiet corner with her workout journal."
    "She pulls out her phone, scrolling through fitness apps and workout plans."
    "But after just fifteen minutes, she throws her phone down in frustration."
    "I can see her struggling to understand the complex fitness routines."
    emma "Ugh, this is impossible!"
    emma "Why can't this just make sense?"
    emma "Everyone thinks I'm just a dumb bimbo anyway..."
    emma "Maybe they're right."
    "She looks around to make sure no one heard her moment of vulnerability."
    "There's real pain in her voice - the pain of someone who's been underestimated her whole life."
    "She storms out, and I follow again."
    scene bathroom_afternoon
    show emma at emma_convo
    $ update_character_state("emma", CharState.NORMAL)
    with fade
    "Later, Emma meets up with Justin near the bathrooms."
    "They look around, then duck inside together."
    "I creep closer, my heart pounding."
    "I know I shouldn't be listening, but I need to understand their dynamic."
    hide emma
    show justin at justin_convo
    with fade
    justin "Come on, babe. You know I need this."
    justin "Practice got me all worked up, and seeing you in that tight gym outfit..."
    emma "Here? Really?"
    emma "Can't we go somewhere more... romantic? Your dorm maybe?"
    justin "What's wrong with here? You never complain usually."
    justin "Besides, my roommate's there. This is more private."
    emma "It's just... can't we go somewhere nicer?"
    emma "Maybe get dinner first? Talk a little?"
    justin "This is hot! The danger of getting caught!"
    justin "And we can talk later. Right now I need you."
    emma "If you say so..."
    emma "I guess you know what's best."
    "I hear... sounds. Obvious sounds."
    "Through the crack in the door, I can see more than I should."
    justin "Get on top."
    emma "Again? Why always facing away?"
    emma "Can't we... you know... face each other this time?"
    justin "You know why. I'm terrified of getting you pregnant."
    justin "My parents would kill me. Your ass is safer."
    justin "Besides, you love it like this. All girls do, they just won't admit it."
    emma "Right... safer..."
    emma "I just thought maybe sometimes we could be more... intimate?"
    justin "This is intimate. Stop overthinking it."
    scene black
    show scene_15
    with fade
    $ persistent.scene_15 = True
    stop music fadeout 1.0
    "Through the door crack, I can see them. Emma on top of Justin, facing away - riding him from behind."
    "She looks... resigned. Going through the motions."
    "This isn't passionate lovemaking - it's just Justin using her for his needs."
    emma "Ugh... not so rough..."
    emma "Maybe we could slow down a little?"
    justin "Stop complaining. You love it."
    justin "All the other girls I've been with loved it rough."
    emma "Other girls...?"
    justin "Before you, babe. Before you."
    emma "I... yeah... sure..."
    emma "I love it. This is perfect."
    "It's clear she doesn't. Her voice is flat, mechanical."
    "She's lying to keep him happy, sacrificing her own pleasure for his."
    "Justin doesn't even notice - he's too focused on himself."
    justin "Fuck yeah, take it all!"
    justin "God, you're so tight. Like a vice."
    emma "Mm-hmm... so good..."
    emma "(Is it over yet?)"
    justin "You close, babe? Cause I'm about to..."
    emma "Yes! So close!"
    emma "(If saying yes makes it end faster...)"
    "A few more rough thrusts and Justin finishes with a grunt."
    
    scene scene_15_final
    with fade
    
    justin "Damn, that was good!"
    emma "(Finally over...)"
    
    scene black
    with fade
    "Emma just stands there, clearly unsatisfied and uncomfortable."
    justin "We should do this more often. Maybe tomorrow?"
    emma "Sure... whatever you want."
    scene college_afternoon
    with fade
    show mc at mc_convo
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    bull_phone "Interesting. Very interesting."
    bull_phone "She wants romance, but he just wants a quick fuck."
    bull_phone "She struggles with studies but has to maintain her perfect image."
    bull_phone "And he's so scared of commitment he won't even fuck her pussy properly."
    bull_phone "Plus, did you hear that? 'Other girls'? He's probably still cheating on her."
    mc "(This is all useful, but I feel dirty listening to this.)"
    mc "(She deserves so much better than that selfish asshole.)"
    bull_phone "Just remember - she chose to date him. But is she happy?"
    bull_phone "From what we just saw, she's starving for real intimacy, real affection."
    bull_phone "Something you could provide if you play your cards right."
    hide bull
    with pixellate
    "I leave before they finish cleaning up, having heard enough."
    "Emma wants romance, genuine connection, someone who cares about her pleasure."
    "Justin gives her social status but nothing else."
    "I might actually have a chance here."
label gym_date:
    scene home_afternoon
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    play music "ES_All That I Want - Brendon Moeller.mp3" volume 0.2
    mc "Alright, it's almost time. I told her to meet me at the gym."
    mc "After seeing how she works out, I know she'll be comfortable there."
    mc "But I need to show her I'm not the weakling she thinks I am."
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    bull_phone "Good choice. She goes there often, so she'll be in her element."
    bull_phone "But remember - you need to impress her. Show her you're not the wimp she thinks you are."
    bull_phone "And after what we saw with Justin... show her what real attention looks like."
    mc "How do I do that?"
    bull_phone "Listen to her. Ask about her interests. Treat her like a person, not a trophy."
    bull_phone "And I have a special plan for later. Trust me on this one."
    mc "What kind of plan?"
    bull_phone "You'll see. Just be ready to be a hero when the moment comes."
    scene gym_morning
    show emma at emma_convo
    $ update_character_state("emma", CharState.NORMAL)
    with fade
    $ update_character_state("emma", CharState.ANGRY)
    play music "ES_Let's Go - Krithi.mp3" volume 0.2
    emma "The gym? Seriously?"
    emma "What, trying to show me how weak you are compared to Justin?"
    emma "This should be hilarious. I can't wait to see you struggle with the lightest weights."
    menu:
        "I thought you'd be comfortable here. You look great when you work out.":
            label test_choice_afyy3:
            $ win_sound()
            $ emma_love += 5
            $ update_character_state("mc", CharState.HAPPY)
            mc "I thought you'd be comfortable here. You look great when you work out."
            mc "I saw you here this morning - your form is perfect."
            $ update_character_state("emma", CharState.ANGRY)
            $ update_character_state("emma", CharState.NORMAL)
            emma "You... you've seen me work out?"
            emma "Were you... watching me?"
            mc "Hard not to notice. You have perfect form."
            mc "Most people just go through the motions, but you actually know what you're doing."
            $ update_character_state("emma", CharState.ANGRY)
            emma "I... That's... Don't think flattery will work on me!"
            emma "You're just saying that because you want something."
            mc "It's not flattery if it's true."
            mc "You're clearly dedicated. How long have you been training?"
        "Just wanted to show you I'm not the weakling you think I am.":
            label test_choice_0am7x:
            $ lose_sound()
            $ update_character_state("mc", CharState.NORMAL)
            mc "Just wanted to show you I'm not the weakling you think I am."
            mc "Figured if I'm going to be humiliated, might as well make it interesting."
            $ update_character_state("emma", CharState.HAPPY)
            emma "Ha! This should be hilarious."
            emma "Can you even lift the bar without weights?"
            emma "I bet you'll throw out your back trying to impress me."
            mc "You'll see."
            emma "Oh, I'm looking forward to this. It'll be great entertainment."
        "This is where you're most comfortable, right? Without Justin around?":
            label test_choice_0nwym:
            $ win_sound()
            $ emma_love += 5
            $ update_character_state("mc", CharState.NORMAL)
            mc "This is where you're most comfortable, right? Without Justin around?"
            mc "I noticed you seem more relaxed here. More like yourself."
            $ update_character_state("emma", CharState.ANGRY)
            emma "What's that supposed to mean?"
            mc "Just that you seem more focused here. More natural."
            mc "Not performing for anyone."
            mc "Like you can just be Emma, not 'Justin's girlfriend.'"
            $ update_character_state("emma", CharState.NORMAL)
            emma "I... I don't perform for anyone!"
            emma "I'm always myself!"
            mc "If you say so."
            mc "I just meant you seem more at peace when you're working out."
    $ update_character_state("emma", CharState.ANGRY)
    emma "Whatever. Let's get this over with."
    emma "Show me what you got, loser."
    emma "I want to see just how pathetic you really are."
    "We move through the gym, and I demonstrate various exercises."
    "I've been working out at home since the Bull phone started training me, and while I'm no bodybuilder, I'm not embarrassing myself either."
    "Emma watches with growing surprise as I handle the weights competently."
    $ update_character_state("emma", CharState.NORMAL)
    emma "Huh. You're... not completely pathetic."
    emma "I expected you to drop the weights on your foot or something."
    $ update_character_state("mc", CharState.HAPPY)
    mc "Thanks for the ringing endorsement."
    mc "Did you really think I was that weak?"
    emma "Honestly? Yeah. [girl_friend] said you couldn't even open a pickle jar."
    mc "[girl_friend] said a lot of things. How much of it do you think was actually true?"
    $ update_character_state("emma", CharState.SAD)
    emma "I... I don't know anymore."
    $ update_character_state("emma", CharState.ANGRY)
    emma "Don't get cocky though. Justin could bench press you."
    menu:
        "I'm not trying to compete with Justin. I'm just being myself.":
            label test_choice_388x9:
            $ win_sound()
            $ emma_love += 5
            $ update_character_state("mc", CharState.NORMAL)
            mc "I'm not trying to compete with Justin. I'm just being myself."
            mc "Is that so hard to understand?"
            mc "I'm not trying to be someone I'm not to impress anyone."
            $ update_character_state("emma", CharState.NORMAL)
            emma "..."
            emma "Most guys always try to act tougher around me. To impress me."
            emma "They flex and show off and make these ridiculous displays of masculinity."
            mc "Maybe that's because you make them feel like they have to."
            $ update_character_state("emma", CharState.ANGRY)
            emma "What's that supposed to mean?"
            mc "Nothing bad. Just that you're intimidating."
            mc "Beautiful, confident, popular. Guys probably feel like they need to prove themselves worthy."
            $ update_character_state("emma", CharState.NORMAL)
            emma "And you don't?"
            mc "I figure if you don't like me as I am, pretending to be someone else won't help."
            mc "Besides, authenticity is more attractive than fake bravado."
            emma "..."
            emma "That's... actually refreshing."
        "Justin this, Justin that. Do you ever think for yourself?":
            label test_choice_dqv2q:
            $ lose_sound()
            mc "Justin this, Justin that. Do you ever think for yourself?"
            mc "Every other sentence out of your mouth is about your boyfriend."
            $ update_character_state("emma", CharState.ANGRY)
            emma "Excuse me?!"
            emma "Of course I think for myself!"
            mc "I'm just saying-"
            emma "You don't get to talk about my boyfriend!"
            emma "He's amazing and perfect and everything you'll never be!"
            mc "Fine, sorry."
            mc "I just meant you're your own person. You don't need to compare everyone to him."
        "Good thing I'm not Justin then. I actually respect women.":
            label test_choice_t0kwa:
            $ lose_sound()
            $ emma_love -= 5
            mc "Good thing I'm not Justin then. I actually respect women."
            mc "I treat them like people, not trophies."
            emma "What's that supposed to mean?"
            mc "Oh, nothing. Just that some guys only want one thing."
            mc "They don't care about their girlfriend's thoughts or feelings."
            emma "Justin loves me!"
            emma "He cares about me deeply!"
            mc "Sure he does. That's why he only wants to fuck your ass in bathrooms."
            $ update_character_state("emma", CharState.ANGRY)
            emma "How... how do you...?"
            mc "Shit, I-"
            emma "You were SPYING on us?!"
            emma "You sick pervert! What is wrong with you?!"
    "We reach the heavy weights section."
    "Emma is about to say something when suddenly-"
    play sound "ES_Weightlifting, Barbell, Drop Weights, 100kg - Epidemic Sound.mp3"
    stop music fadeout 1.0
    $ update_character_state("emma", CharState.ANGRY)
    emma "Look out!"
    "A barbell with heavy weights starts falling from the rack above Emma!"
    "Time seems to slow down as I see the massive weight plummeting toward her."
    menu:
        "Dive and push Emma out of the way!":
            label test_choice_3mlbw:
            $ gym_trap_success = True
            $ win_sound()
            $ emma_love += 10
            "Without thinking, I lunge forward and shove Emma to safety."
            "The weights crash down where she was standing just a second ago."
            "The impact sends shockwaves through the gym floor."
            play sound "ES_Female, Gasp 02 - Epidemic Sound.mp3"
            $ update_character_state("emma", CharState.AROUSED)
            emma "Oh my god! You... you saved me!"
            emma "That could have... I could have been killed!"
            mc "Are you okay?"
            mc "Did you get hurt at all?"
            emma "I... yes... You actually..."
            emma "You didn't even hesitate. You just threw yourself in front of danger for me."
            "She's looking at me differently now. Her face is flushed, and not from the exercise."
            "There's something new in her eyes - respect? Gratitude? Something more?"
            emma "You're bleeding!"
            "I look down and see a cut on my arm from the falling weight."
            mc "It's nothing. As long as you're safe."
            mc "A small cut is nothing compared to what could have happened to you."
            emma "Don't be stupid! We need to clean that!"
            emma "You could get an infection or something."
            "She grabs my hand and drags me to the gym's first aid station."
            "Her hands are gentle as she cleans the wound, a stark contrast to her usual harsh demeanor."
            "I notice she's taking extra care, almost caressing my arm as she works."
            emma "[player_name]... I..."
            emma "Thank you."
            emma "Really. Thank you."
            mc "Hey, couldn't let anything happen to my date, could I?"
            $ update_character_state("emma", CharState.AROUSED)
            emma "Your date... right..."
            emma "I... I wasn't expecting..."
            "She's still holding my hand, her thumb unconsciously stroking my skin."
            "The usual mask of cruelty has completely fallen away."
        "Freeze in shock!":
            label test_choice_30zfo:
            $ lose_sound()
            $ emma_love -= 5
            "I stand frozen as the weights fall."
            "My mind goes blank, unable to process what's happening fast enough."
            "Emma manages to jump back just in time, but she trips and falls hard."
            "The weights crash down with a thunderous impact."
            $ update_character_state("emma", CharState.ANGRY)
            emma "What the hell?! You just stood there!"
            emma "I could have been seriously hurt!"
            mc "I... I'm sorry! It happened so fast!"
            mc "I wanted to help but I just... froze."
            emma "Some protector you are! I could have been killed!"
            emma "God, [girl_friend] was right. You really are useless!"
            emma "In a real crisis, you're completely worthless!"
            mc "Emma, I-"
            emma "Save it!"
            emma "I don't want to hear your excuses."
        "Try to catch the falling weights!":
            label test_choice_p3whp:
            $ lose_sound()
            $ emma_love -= 10
            "I try to catch the falling barbell like some kind of superhero."
            "As if I could somehow stop hundreds of pounds of metal with my bare hands."
            "Reality hits hard - literally."
            "The weights knock me down, and I scream in pain."
            mc "AHHH! My shoulder!"
            mc "Fuck, I think something's broken!"
            emma "Oh my god! Are you insane?!"
            emma "What were you thinking?!"
            "Gym staff rush over. This is humiliating."
            "Other gym members are staring and whispering."
            "After they help me up and confirm nothing's broken, Emma is shaking her head."
            emma "That was the stupidest thing I've ever seen."
            emma "Did you think you were in a movie or something?"
            emma "You could have been seriously injured!"
            mc "I was trying to protect you..."
            $ update_character_state("emma", CharState.ANGRY)
            emma "By getting yourself killed? Idiot."
            emma "That's not heroic, that's just stupid."
    # Date outcome based on points
    if emma_love <= 0:  # Too many mess ups
        jump game_over_emma
    elif emma_love >= 20 and gym_trap_success:
        jump gym_date_best
    elif emma_love >= 15:
        jump gym_date_good
    elif emma_love >= 5:
        jump gym_date_bad
    else:
        jump gym_date_worst

label gym_date_best:
    $ update_character_state("emma", CharState.AROUSED)
    emma "[player_name]... I can't believe you did that."
    emma "No one's ever... I mean, Justin would never..."
    emma "He would have worried about himself first. Maybe helped me after."
    mc "Hey, it's okay. You're safe. That's what matters."
    mc "I couldn't live with myself if something happened to you."
    emma "Is it weird that I'm... kind of turned on right now?"
    emma "Seeing you be so brave, so protective..."
    $ update_character_state("mc", CharState.AROUSED)
    mc "Emma..."
    emma "Shut up. Just... come here."
    emma "I need to... I want to thank you properly."
    
    "She pulls me into a secluded corner of the gym."
    "Her breathing is heavy, her eyes filled with desire I've never seen before."
    "This isn't the cruel, mocking Emma I know - this is someone else entirely."
    
    scene black
    show scene_11
    stop music fadeout 1.0
    with fade
    
    $ persistent.scene_11 = True
    
    "Before I know it, Emma's hands are on my chest, her lips on mine."
    "The kiss is desperate, hungry, like she's been starving and I'm her first meal."
    
    emma "Mmmph... God, when you pushed me out of the way..."
    emma "You looked so strong, so determined..."
    emma "So different from the broken boy I thought you were."
    mc "Emma, are you sure about this?"
    mc "I don't want you to do something you'll regret."
    emma "Shut up and let me thank you properly."
    emma "I know exactly what I want right now."
    
    "She presses her body against mine, her hands working at my gym shorts with urgent fingers."
    "Her eyes never leave mine, filled with a hunger I've never seen from her."
    
    emma "I want to make you feel good... Want to show you how grateful I am..."
    emma "No one's ever risked themselves for me like that."
    mc "Fuck, Emma... you don't have to..."
    emma "I want to. God, I want to so badly."
    
    "Her breasts are perfect - large, firm, and now wrapped around my cock."
    $ play_grab_sound()
    "The sensation is incredible, soft and warm and slippery."
    "This isn't just gratitude - this is raw desire."
    
    emma "Mmm... You're bigger than I expected..."
    emma "So much bigger than... than most guys."
    emma "Fuck, you feel so good between my tits..."
    $ play_woman_pleasure_sound()
    mc "Emma, Jesus Christ..."
    $ play_man_pleasure_sound()
    emma "You like that? You like how my tits feel around your cock?"
    emma "Tell me how good it feels..."
    mc "It feels incredible... Your tits are perfect..."
    
    "She works my cock between her breasts with growing enthusiasm."
    $ play_handjob_sound()
    "Her technique is amazing - clearly she knows what she's doing, but there's genuine passion here."
    
    emma "Way bigger than... never mind."
    emma "Mmm... I can't stop... you feel so fucking good..."
    mc "Than Justin?"
    mc "You can tell me. Is he smaller than me?"
    emma "I said never mind! Just... enjoy this."
    emma "But... maybe... just maybe you're more impressive than I thought."
    
    "She spits between her breasts, adding lubrication."
    $ play_mouth_sound("SALIVA")
    "The wet sounds of her tits sliding on my cock fill the small space."
    $ play_handjob_sound()
    "I can see her getting turned on just from pleasuring me."
    
    emma "Mmm, so slippery now... feels even better, doesn't it?"
    emma "I love how hard you are for me..."
    emma "Love how your cock throbs between my tits..."
    $ play_woman_pleasure_sound()
    mc "Emma... I'm going to..."
    mc "If you keep doing that..."
    $ play_man_pleasure_sound()
    emma "Mm-hmm! Do it! I want it!"
    emma "I want to see your cum... want to feel it on my skin..."
    mc "You sure? You don't have to..."
    emma "I WANT to! Cover me!"
    $ play_woman_pleasure_sound()
    
    "Her enthusiasm is intoxicating. She's not doing this out of obligation."
    "She genuinely wants to pleasure me, wants to make me feel good."
    "It's the complete opposite of what I saw with Justin."
    
    emma "Come on, baby... give me that cum..."
    emma "I want to see how good I make you feel..."
    $ play_woman_pleasure_sound()
    mc "Fuck, Emma... here it comes..."
    $ play_man_pleasure_sound()
    
    scene scene_11_final
    with fade

    mc "Fuuuck!"
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    emma "Mmm... So much..."
    emma "So warm... I can feel how much you enjoyed that."
    emma "Look at me... covered in your cum..."
    emma "It's kind of... sexy, isn't it?"
    $ play_woman_pleasure_sound()
    
    "I explode across her chest and face."
    "Thick ropes of cum paint her perfect breasts."
    "There's genuine pleasure in her eyes, like she enjoyed it as much as I did."
    
    scene gym_morning
    show emma at emma_convo
    $ update_character_state("emma", CharState.SAD)
    with fade
    
    $ update_character_state("emma", CharState.SAD)
    emma "We... we should go."
    emma "Someone might have seen us."
    emma "This never happened, understand?"
    $ update_character_state("mc", CharState.HAPPY)
    mc "If that's what you want."
    mc "But I don't regret it. You were incredible."
    $ update_character_state("emma", CharState.HAPPY)
    emma "I mean it! But..."
    emma "Maybe we could study together sometime? For that test?"
    emma "I mean, if you want to help me... academically."
    mc "I'd like that. I'd like that a lot."
    emma "Good. I'll... I'll text you."
    emma "Maybe we could even go to a nice party afterward... if things go well."
    
    menu:
        "I'd love to take you to a party":
            label test_choice_dlm8i:
            if emma_love >= 20 and gym_trap_success:
                emma "I know all the best cocktail parties on campus..."
                emma "Do you know any sophisticated drinks?"
                jump outfit_18_puzzle
                label outfit_18_puzzle_success:
                    emma "I have this elegant cocktail dress... perfect for sophisticated parties..."
                    emma "Maybe you'll get to see me in it soon..."
                label outfit_18_puzzle_failure:
                    emma "Well, we can work on your drink knowledge..."
        "Let's focus on studying for now":
            label test_choice_dxjzc:
            emma "Right, academics first..."
    $ update_character_state("emma", CharState.NORMAL)
    emma "And [player_name]? Thank you. For saving me."
    emma "No one's ever done anything like that for me before."
    "She practically runs out of the gym, but I can see her smiling as she goes."
    "Something fundamental just changed between us."
    jump post_gym_date

label gym_date_good:
    $ update_character_state("emma", CharState.HAPPY)
    emma "You really saved me back there."
    emma "I mean it. That was... that was really brave."
    $ update_character_state("mc", CharState.NORMAL)
    mc "Anyone would have done the same."
    mc "I just reacted instinctively."
    $ update_character_state("emma", CharState.SAD)
    emma "No... Justin wouldn't have. He would have been too worried about himself."
    emma "Too worried about his precious football career to risk injury."
    $ update_character_state("emma", CharState.NORMAL)
    emma "You're... different than I thought."
    mc "Is that a good thing?"
    $ update_character_state("emma", CharState.HAPPY)
    emma "Maybe."
    emma "Maybe I've been wrong about you."
    
    "She steps closer, her hand on my chest."
    "I can feel her heart racing, see the confusion in her eyes."
    
    $ update_character_state("emma", CharState.AROUSED)
    emma "You've been working out."
    emma "Your chest is... firmer than I expected."
    $ update_character_state("mc", CharState.NORMAL)
    mc "A little. Nothing compared to Justin though."
    $ update_character_state("emma", CharState.ANGRY)
    emma "Stop comparing yourself to him."
    $ update_character_state("emma", CharState.NORMAL)
    emma "You're... you're your own person."
    mc "It shows?"
    $ update_character_state("emma", CharState.HAPPY)
    emma "It shows."
    
    "Her hand lingers on my chest, tracing small circles."
    "The touch is electric, charged with unexpected intimacy."
    
    scene black
    show scene_11
    # MUSIC PLACEHOLDER: Stop music for Scene 11 (Good gym date outcome - Emma titjob)
    # stop music fadeout 1.0
    with fade
    
    "She presses her tits against me, her hands roaming my chest with growing boldness."
    "Her breathing is heavy, her eyes dark with desire."
    
    emma "You know... I could thank you properly..."
    emma "For saving me, I mean."
    emma "Would you... would you like that?"
    mc "Emma, you don't owe me anything."
    emma "I know. But I want to."
    emma "I want to make you feel good."
    
    "Her breasts are perfect - large, firm, and now wrapped around my cock."
    $ play_grab_sound()
    "The sensation is incredible, soft and warm and slippery."
    
    emma "Like this?"
    emma "Does this feel good?"
    mc "Fuck yes... so good..."
    $ play_man_pleasure_sound()
    emma "Mmm, you like my tits? They're natural, you know."
    emma "Not like some of the girls here with their fake ones."
    mc "They're perfect. You're perfect."
    emma "They're better than anything [girl_friend] had, right?"
    emma "I know you two... you know... back when you were together."
    mc "So much better... everything about you is better."
    emma "Good answer."
    emma "I like hearing that."
    
    "She works my cock between her breasts with growing skill and enthusiasm."
    "The sight of my dick disappearing between those perfect mounds is incredible."
    "Her technique improves as she finds her rhythm."
    
    emma "You're so hard... so big between my tits..."
    emma "I can feel you throbbing... does it feel that good?"
    mc "Amazing... you're amazing at this..."
    emma "I've never... I mean, Justin never wants me to..."
    emma "He just wants to get straight to the fucking."
    emma "But this is nice... intimate..."
    mc "Take your time. Enjoy it."
    emma "I am... I really am..."
    
    "She spits between her breasts, adding lubrication."
    "The wet sounds of her tits sliding on my cock fill the small space."
    
    emma "Mmm, so slippery now... feels even better, doesn't it?"
    emma "I love how you're looking at me..."
    emma "Like I'm the most beautiful thing you've ever seen..."
    mc "You are. Absolutely gorgeous."
    emma "Keep talking like that... it makes me feel..."
    mc "Feel what?"
    emma "Special. Desired. Not just like a trophy."
    
    mc "Emma, I'm close..."
    mc "Your tits feel too good..."
    $ play_man_pleasure_sound()
    emma "Do it. Cover me."
    emma "I want to see how much you want me."
    emma "I want to feel your cum on my skin."
    $ play_woman_pleasure_sound()
    
    scene scene_11_final
    with fade
    
    "I explode across her chest and face."
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    "Thick ropes of cum paint her perfect breasts."
    
    emma "Mmm... So much..."
    emma "So warm... I can feel how much you enjoyed that."
    $ play_woman_pleasure_sound()
    emma "Look at me... covered in your cum..."
    emma "It's kind of... sexy, isn't it?"
    
    scene gym_morning
    show emma at emma_convo
    $ update_character_state("emma", CharState.NORMAL)
    with fade
    
    emma "Not bad, [player_name]. Not bad at all."
    emma "Maybe those rumors about you aren't all lies."
    emma "Maybe there's more to you than meets the eye."
    mc "Want to find out more?"
    emma "Maybe. If you can help me with studying."
    emma "I'm failing Professor Chen's class."
    emma "And unlike what everyone thinks, I actually care about my grades."
    mc "I could help with that."
    mc "I'm actually pretty good at tutoring."
    emma "Then maybe we have a deal."
    emma "Academic help in exchange for... whatever this was."
    emma "You've seen a side of me no one else has... my real self..."
    
    menu:
        "I want to see all of your real self":
            label test_choice_srgpq:
            if emma_love >= 30 and gym_trap_success:
                emma "All of me? That's... that's very forward..."
                emma "What state would show you my truest, most honest self?"
                jump outfit_20_puzzle
                label outfit_20_puzzle_success:
                    emma "Maybe... maybe someday I'll trust you enough for that..."
                    emma "To be completely myself with you..."
                label outfit_20_puzzle_failure:
                    emma "I'm not ready to be that open yet..."
        "This arrangement works for me":
            label test_choice_ggzi6:
            emma "Good. Mutual benefit."
    mc "Sounds fair to me."
    jump post_gym_date

label gym_date_bad:
    emma "Well, that was... interesting."
    emma "I mean, you didn't completely embarrass yourself."
    mc "Interesting?"
    emma "You're not as pathetic as I thought. But you're still not impressive."
    emma "I mean, you saved me, I guess. Sort of."
    mc "Thanks, I guess?"
    emma "Look, this was... fine. But don't expect anything more."
    emma "I'm with Justin. This was just to prove a point."
    emma "To show everyone that even being nice to you doesn't change anything."
    mc "What point?"
    emma "That you're not worth my time."
    emma "That even when you try to be heroic, you're still just... you."
    emma "But... thanks for trying to save me, I guess."
    emma "Even if you were pretty useless at it."
    mc "So that's it?"
    emma "That's it. Don't read anything into this."
    emma "We're not friends. We're not anything."
    emma "Goodbye, [player_name]."
    
    jump post_gym_date

label gym_date_worst:
    $ update_character_state("emma", CharState.ANGRY)
    emma "This was a complete waste of time."
    emma "You're even more pathetic than [girl_friend] said."
    emma "Can't even protect a girl from some falling weights."
    emma "What kind of man just stands there like a statue?"
    mc "Emma, please-"
    emma "No. I'm done."
    emma "I'm going to tell everyone about this. How you just stood there."
    emma "How you froze when I needed help."
    emma "Or better yet..."
    
    "She pulls out her phone and calls someone."
    emma "Justin? Baby? You need to come to the gym."
    emma "Yeah, that loser [player_name] tried to hit on me."
    emma "And get this - when some weights almost fell on me, he just stood there like an idiot."
    emma "He's so pathetic! Come show him what a real man looks like."
    
    mc "Emma, don't-"
    emma "Too late, wimp."
    emma "Justin's going to love hearing about this."
    emma "How the great [player_name] couldn't even save a girl in danger."
    
    "I hear Justin's voice getting closer. Time to leave."
    "I run out of the gym, hearing Emma's cruel laughter behind me."
    "This was a disaster."
    
    jump post_gym_date

label post_gym_date:
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    if emma_love >= 15:  # good or best outcome
        bull_phone "Excellent work! Did you see how she melted when you saved her?"
        mc "Yeah, but the falling weights..."
        mc "That was you, wasn't it? You loosened them somehow."
        bull_phone "Were loosened by yours truly. You're welcome."
        mc "You could have killed her!"
        mc "What if I hadn't reacted fast enough?"
        bull_phone "Please. I calculated the trajectory perfectly. She was never in real danger."
        bull_phone "But SHE didn't know that. And now she sees you as her hero."
        bull_phone "The strong man who protected her when she was vulnerable."
        mc "That's... manipulative."
        mc "What if something had gone wrong?"
        bull_phone "That's smart planning. Nothing went wrong, did it?"
        bull_phone "And now she wants to study with you."
        bull_phone "And we both know studying isn't all she wants anymore."
        mc "I can't believe it actually worked."
        mc "She was so different when she thought I'd saved her life."
        bull_phone "Women love a protector. Someone who'll put their safety above his own."
        bull_phone "Justin would never do that for her, and she knows it."
    else:
        bull_phone "Well, that could have gone better."
        mc "You think?!"
        mc "She basically called me worthless to my face."
        bull_phone "Hey, you're the one who froze up."
        bull_phone "I gave you the perfect opportunity to be her hero."
        bull_phone "But it's not over. She still agreed to study with you, right?"
        mc "Barely."
        mc "And only to prove how pathetic I am."
        bull_phone "That's all we need. One more shot."
        bull_phone "Trust me, once you get her alone, things will change."
        
    mc "So what now?"
    bull_phone "Now you prepare for the real challenge."
    bull_phone "Study hard, but also work on yourself."
    bull_phone "Work on your confidence. Your body. Your game."
    bull_phone "When she comes to study, you need to be ready."
    bull_phone "Because this time, we're going all the way."
    mc "All the way?"
    bull_phone "You're going to fuck her, [player_name]."
    bull_phone "You're going to show her what real passion feels like."
    bull_phone "What it's like to be with a man who actually cares about her pleasure."
    mc "What if she says no?"
    bull_phone "After what happened today? Trust me, she won't."
    
    hide bull
    with pixellate
    
    "The adrenaline from today's events is still coursing through me."
    "I can't believe Emma actually... well, what she did in the gym."
    "And now she wants to study together. This could be my real chance."
    
    mc "I need to prepare for this study session. It's not just about academics anymore."
    mc "I have to be ready for anything. Emma is clearly more interested than she's letting on."
    
    "I spend the rest of the evening studying the material we'll be covering."
    "Physics, chemistry, whatever Emma is struggling with - I want to be genuinely helpful."
    "But I also can't stop thinking about the way she looked at me after I saved her."
    
    scene black
    with fade
    
    "..."
    "......"
    "........."
    
    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL) 
    with Fade(0.5, 3.0, 0.5)
    
    "I wake up feeling nervous but determined."
    "Today is the study date with Emma. After what happened at the gym, anything could happen."
    "I get ready carefully - I want to look good but not like I'm trying too hard."
    
    mc "Okay, [player_name]. Time to see if Emma really meant what she said about studying."
    mc "Something tells me this won't just be about textbooks."
    
    "My phone buzzes with a text from Emma confirming our meeting time and place."
    "An empty classroom after hours. Perfect for 'studying.'"
    
    "I grab my books and head to campus, my heart racing with anticipation."

label study_date:
    scene classroom_light_on
    show emma at emma_convo
    $ update_character_state("emma", CharState.NORMAL)
    # MUSIC PLACEHOLDER: Romantic, intimate study theme - MC and Emma growing closer
    # play music "your_music_file_here.mp3" volume 0.2
    with fade
    
    $ update_character_state("emma", CharState.SAD)
    emma "Can't believe I'm doing this."
    emma "If anyone sees us together..."
    emma "My reputation will be ruined."
    
    menu:
        "Then they'll see you getting help from someone who actually understands this stuff.":
            label test_choice_eecnw:
            $ win_sound()
            $ emma_love += 5
            $ update_character_state("mc", CharState.HAPPY)
            mc "Then they'll see you getting help from someone who actually understands this stuff."
            mc "Someone who won't judge you for struggling."
            $ update_character_state("emma", CharState.NORMAL)
            emma "You... you really think you can help?"
            emma "I mean, really help, not just pretend to be smart?"
            mc "I know I can. You're smart, Emma. You just need the right approach."
            mc "And someone who believes in you."
            $ update_character_state("emma", CharState.SAD)
            emma "No one's called me smart in... a long time."
            emma "Everyone just assumes I'm a dumb bimbo who gets by on looks."
            mc "That's because they're too busy looking at your body to notice your mind."
            mc "Their loss. You have so much more to offer than they realize."
            $ update_character_state("emma", CharState.HAPPY)
            emma "That's... actually kind of sweet."
            $ update_character_state("emma", CharState.NORMAL)
            emma "You really mean that?"
            mc "Every word."
        "Scared to be seen with me?":
            label test_choice_e6o90:
            $ lose_sound()
            $ update_character_state("mc", CharState.ANGRY)
            mc "Scared to be seen with me?"
            mc "Worried it'll hurt your precious image?"
            $ update_character_state("emma", CharState.ANGRY)
            emma "Obviously! My reputation-"
            emma "Do you know how hard I've worked to build my social status?"
            mc "Right. Your precious reputation."
            mc "Is that really all that matters to you?"
            $ update_character_state("emma", CharState.SAD)
            emma "It's all I have!"
            emma "Without my reputation, I'm nothing!"
            $ update_character_state("mc", CharState.NORMAL)
            mc "Is it though?"
            mc "Seems to me like you're more than just your image."
        "Then they'll wonder why you're here with me instead of your boyfriend.":
            label test_choice_5d6x4:
            $ win_sound()
            $ emma_love += 5
            mc "Then they'll wonder why you're here with me instead of your boyfriend."
            mc "Why you came to me for help instead of him."
            emma "Justin doesn't... he's not good with academics."
            emma "He's smart about football and... other things."
            mc "Too busy with practice?"
            emma "Too busy with everything except me."
            emma "Sometimes I feel like I'm just another piece of equipment to him."
            mc "His loss."
            mc "Any guy who doesn't appreciate your mind is an idiot."
            emma "..."
            emma "You really think I have a good mind?"
            mc "I think you're capable of amazing things if given the chance."
            
    "We sit down and open the textbooks."
    "I start explaining the concepts, and to my surprise, Emma actually pays attention."
    "She takes notes, asks questions, engages with the material."
    
    emma "Wait, so if X equals this, then Y has to be..."
    emma "Oh my god, I get it!"
    emma "The formula actually makes sense when you explain it like that!"
    mc "See? You're smarter than you think."
    mc "You just needed someone to explain it properly."
    emma "I... no one's ever taken the time to explain it properly."
    emma "Teachers just assume I'm another dumb bimbo."
    emma "They talk down to me or ignore me completely."
    emma "Like my questions aren't worth answering."
    
    menu:
        "You're not dumb, and you're definitely not just another anything.":
            label test_choice_f6eja:
            $ win_sound()
            $ emma_love += 5
            mc "You're not dumb, and you're definitely not just another anything."
            mc "You're Emma. Unique. Special."
            mc "One of a kind."
            $ update_character_state("emma", CharState.AROUSED)
            emma "[player_name]..."
            emma "No one's ever talked to me like that before."
            mc "And for what it's worth, I think you're brilliant."
            mc "You have insights that most people miss."
            emma "You... you really mean that?"
            emma "You're not just saying it to be nice?"
            $ update_character_state("mc", CharState.AROUSED)
            mc "Every word. I wouldn't lie to you."
            emma "I... I don't know what to say."
        "Well, you do play into the stereotype sometimes.":
            label test_choice_hjtpp:
            $ lose_sound()
            mc "Well, you do play into the stereotype sometimes."
            mc "I mean, you kind of encourage people to see you that way."
            $ update_character_state("emma", CharState.ANGRY)
            emma "Excuse me?"
            emma "What's that supposed to mean?"
            mc "I'm just saying-"
            emma "No, I get it. Even you think I'm just a dumb bimbo."
            emma "Just another pretty face with nothing upstairs."
            mc "That's not what I meant!"
            mc "I just meant that sometimes you don't show your intelligence."
            emma "Maybe because every time I try, people shoot me down!"
        "They're idiots if they can't see past the surface.":
            label test_choice_vyjth:
            $ win_sound()
            $ emma_love += 5
            mc "They're idiots if they can't see past the surface."
            mc "Though I admit, it's a very distracting surface."
            emma "*giggles* Smooth talker."
            emma "But thank you. That... that means more than you know."
            mc "Just honest. You deserve better than being underestimated."
            emma "Justin never talks to me like this."
            emma "He doesn't talk to me much at all, actually."
            mc "Like what?"
            emma "Like I'm a person. Not just a trophy."
            emma "Like my thoughts and opinions actually matter."
            mc "They do matter. To me, anyway."
            
    "We continue studying, but the tension is building."
    "Every time our hands accidentally touch, she jumps."
    "Every time I lean in to point something out, she holds her breath."
    "The air between us is electric."
    
    emma "[player_name]... at the gym..."
    mc "Yeah?"
    emma "When you saved me... I felt something."
    emma "You were so... dominant. In control of the situation."
    emma "I've never seen that side of you before."
    
    menu:
        "I know what I want and I take it":
            label test_choice_99vf2:
            if gym_trap_success and emma_love >= 20:
                emma "That confidence... that control..."
                emma "You know, I've always been drawn to power... real power, not fake popularity..."
                emma "There's something about a man who can take charge when it matters..."
                emma "I actually have this outfit that represents strength and control..."
                emma "It's made of tough black material... represents dominance and authority..."
                emma "What does that kind of powerful material symbolize?"
                jump outfit_16_puzzle
                label outfit_16_puzzle_success:
                    emma "Maybe... maybe you'd appreciate seeing me in that leather outfit..."
                    emma "When I want to show my stronger, more confident side..."
                label outfit_16_puzzle_failure:
                    emma "I thought someone with your new confidence might understand..."
        "I just did what felt right":
            label test_choice_pzves:
            emma "Well, what felt right was pretty amazing."
    emma "Something I haven't felt with Justin in... ever, actually."
    emma "Something I thought I'd never feel."
    mc "What kind of something?"
    emma "Protected. Cared for."
    emma "Like I actually mattered to someone."
    emma "Like I was worth risking yourself for."
    menu:
        "I felt it too, Emma.":
            label test_choice_30ome:
            $ win_sound()
            $ emma_love += 5
            $ update_character_state("emma", CharState.AROUSED)
            mc "I felt it too, Emma."
            mc "That connection between us."
            emma "You did?"
            emma "Really? It wasn't just me?"
            mc "How could I not? You're incredible."
            mc "Smart, beautiful, driven..."
            mc "Any man would be lucky to have your attention."
            emma "Stop, you're making me blush."
            emma "I don't... I'm not used to compliments like that."
            mc "Good. You look cute when you blush."
            mc "You should blush more often."
            emma "Justin never makes me blush anymore."
            emma "He used to, but now..."
            mc "Now?"
            emma "Now he just takes me for granted."
        "That was just adrenaline.":
            label test_choice_2vcx8:
            $ lose_sound()
            $ update_character_state("mc", CharState.SAD)
            mc "That was just adrenaline."
            mc "Life-or-death situations do that to people."
            emma "Oh... right. Of course."
            emma "How stupid of me to think it was something more."
            mc "Emma-"
            emma "No, you're right. Stupid of me."
            emma "Just adrenaline. Nothing more."
        "What about Justin?":
            label test_choice_infjn:
            $ lose_sound()
            $ emma_love -= 5
            mc "What about Justin?"
            mc "You have a boyfriend, Emma."
            $ update_character_state("emma", CharState.ANGRY)
            emma "Seriously? That's your response?"
            emma "I open up to you and that's what you say?"
            mc "I'm just saying, you have a boyfriend."
            emma "You think I don't know that?!"
            emma "God, you're just like everyone else!"
            emma "I thought you were different!"
    # Final outcome calculation
    if emma_love <= 0:  # Too many mess ups
        jump game_over_emma
    elif emma_love >= 35:
        jump study_date_best
    elif emma_love >= 25:
        jump study_date_good
    elif emma_love >= 15:
        jump study_date_bad
    else:
        jump study_date_worst

label study_date_best:
    $ update_character_state("emma", CharState.AROUSED)
    emma "I can't do this anymore."
    emma "I can't keep pretending."
    mc "Pretending what?"
    emma "Pretend. Pretend I don't want you."
    emma "Pretend Justin satisfies me."
    emma "Pretend I'm happy with how things are."
    emma "Pretend I don't think about you every night."
    
    "She climbs onto my lap, straddling me."
    "Her eyes are dark with desire, her breathing heavy."
    
    emma "I need you, [player_name]. Right here. Right now."
    emma "I can't wait anymore. I can't keep lying to myself."
    mc "Emma, are you sure about this?"
    mc "Once we cross this line, there's no going back."
    emma "I've never been more sure of anything in my life."
    emma "Please... make me feel like a real woman."
    emma "Not just a toy. Not just a trophy. A woman."
    emma "Show me what it's like to be with someone who actually wants me."
    
    scene black
    show scene_13
    # MUSIC PLACEHOLDER: Stop music for intimate scene
    # stop music fadeout 1.0
    with fade
    
    $ persistent.scene_13 = True
    
    "Our clothes come off in a frenzy of need and desire."
    "When I enter her, she gasps like she's never been touched before."
    "Her pussy is incredibly tight, gripping me like a vice."
    
    emma "Oh god! You're so... so deep!"
    emma "I can feel every inch of you inside me!"
    emma "Justin never... he never fucks my pussy!"
    emma "Always my ass, always from behind, always so quick!"
    mc "His loss. You feel incredible."
    mc "So tight, so wet... like you were made for me."
    emma "Harder! Please! Show me what I've been missing!"
    emma "Show me what real fucking feels like!"
    
    "I pound into her with all the passion she's been denied."
    "Her moans echo in the empty classroom, raw and primal."
    "This isn't just sex - it's reclaiming something that was stolen from her."
    
    emma "Yes! Yes! This is what I needed!"
    emma "A real man! Someone who wants ME!"
    emma "Someone who cares if I feel good!"
    mc "You're mine now, Emma. Say it."
    mc "Tell me who you belong to."
    emma "I'm yours! Only yours!"
    emma "Fuck Justin! Fuck everyone! I'm yours!"
    
    "Her pussy clenches around me as she cums, her whole body shaking."
    "The orgasm seems to last forever, wave after wave of pleasure."
    
    emma "Don't stop! Please don't stop!"
    emma "I'm cumming so hard! Harder than I ever have!"
    emma "You're making me cum like Justin never could!"
    mc "I'm going to fill you up, Emma."
    mc "Going to pump you full of my cum."
    emma "Yes! Do it! I don't care about the risk!"
    emma "I want your baby! Not his!"
    emma "I want everyone to know you're the one who satisfied me!"
    
    "I feel her pussy convulsing around me, milking my cock."
    "She's cumming again, even harder this time."
    
    emma "Breed me! Make me yours completely!"
    emma "I want to feel your cum in my womb!"
    mc "Take it all! Every drop!"
    emma "YES! Fill me up! Claim me!"
    
    scene scene_13_final
    with fade
    
    mc "Take it all!"
    emma "YESSSS! I can feel it! So hot inside me!"
    emma "So much cum... filling me up completely!"
    
    "I pump her full of cum, claiming her completely."
    "She collapses against me, crying tears of joy and relief."
    "We both haven't had enough of each other."
    "Her pussty dripping with my cum has only made her crave more."
    
    jump study_date_good

    scene classroom_light_on
    show emma at emma_convo
    $ update_character_state("emma", CharState.HAPPY)
    with fade
    
    $ update_character_state("emma", CharState.HAPPY)
    emma "I... I love you, [player_name]."
    emma "I think I have for a while now."
    emma "I was just too proud to admit it."
    emma "Too scared of what people would think."
    emma "But you make me feel things... passionate things I never felt with Justin."
    
    menu:
        "Tell me about these passionate feelings":
            label test_choice_6cb2u:
            if emma_love >= 25:
                emma "It's like... fire. Burning hot inside me."
                emma "What color represents that burning desire?"
                jump outfit_17_puzzle
                label outfit_17_puzzle_success:
                    emma "I have a stunning red dress... maybe you'd like to see me in it sometime..."
                label outfit_17_puzzle_failure:
                    emma "I thought you'd understand that burning feeling..."
        "I feel the same way":
            label test_choice_664em:
            emma "You do? Really?"
    $ update_character_state("mc", CharState.NORMAL)
    mc "What about Justin?"
    mc "What about your reputation?"
    $ update_character_state("emma", CharState.ANGRY)
    emma "Fuck Justin. I'm breaking up with him."
    emma "Tonight. Right now, actually."
    $ update_character_state("emma", CharState.HAPPY)
    emma "I want you. Only you."
    # Check for revenge path achievement
    $ grant_achievement("REVENGE_PATH")
    emma "And I don't care what anyone thinks anymore."
    emma "And I'm going to tell everyone."
    emma "How you saved me. How you helped me. How you're the best man I've ever been with."
    emma "How you actually care about my pleasure, my thoughts, my feelings."
    mc "Emma..."
    $ update_character_state("emma", CharState.SAD)
    emma "I'm sorry for all the bullying. For believing [girl_friend]'s lies."
    emma "For being such a bitch to you when you didn't deserve it."
    $ update_character_state("emma", CharState.HAPPY)
    emma "Let me make it up to you. Let me fix your reputation."
    emma "I have influence. I'll use it for you."
    emma "Everyone will know that [girl_friend] was lying about everything."
    $ update_character_state("mc", CharState.HAPPY)
    mc "I'd like that. I'd like that a lot."
    $ update_character_state("emma", CharState.HAPPY)
    emma "Good. Because you're stuck with me now."
    emma "I'm never letting you go. Never."

label study_date_good:
    $ update_character_state("emma", CharState.AROUSED)
    $ update_character_state("mc", CharState.AROUSED)
    
    scene black
    show scene_14
    # MUSIC PLACEHOLDER: Stop music for intimate scene
    # stop music fadeout 1.0
    with fade
    
    $ persistent.scene_14 = True
    
    "She pushes me back and straddles me on the desk."
    "Papers scatter as we fuck right there in the classroom."
    "Her movements are desperate, hungry."
    
    emma "Oh fuck! Your cock is amazing!"
    emma "So much bigger than... than..."
    emma "So much better!"
    mc "Say it, Emma. Say I'm better than him."
    emma "Better than Justin's!"
    emma "He never makes me feel like this!"
    emma "Never makes me this wet!"
    
    "I grab her hips and thrust up into her."
    "She rides me like her life depends on it."
    "Like she's trying to fuck away years of dissatisfaction."
    
    emma "I'm cumming! Oh god, I'm cumming!"
    emma "You're making me cum so hard!"
    emma "Justin never... he never cares if I cum!"
    
    mc "I'm going to fill you, Emma!"
    emma "Yes! Fill me! I want your cum!"
    
    scene scene_14_final
    with fade
    
    mc "Take it all!"
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    emma "YESSSS! So much! Filling me completely!"
    $ play_woman_pleasure_sound()
    
    "I haven't had enough of her yet."
    "I want to show her how it's different with me."
    
    mc "Turn around. On your back."
    emma "W-what?"
    emma "Like... like Justin does?"
    mc "You heard me. But this will be different."
    mc "I promise."
    
    scene scene_12_initial
    with fade
    
    $ persistent.scene_12 = True
    
    "She obeys, presenting her ass to me."
    "But I take my time, preparing her gently."
    
    emma "Be gentle... Justin is always so rough..."
    emma "He just... he just shoves it in."
    mc "I'm not Justin."
    mc "I actually care about how you feel."

    scene scene_12
    
    "I enter her ass slowly, carefully."
    "Taking time to let her adjust."
    "She moans in pleasure instead of pain."
    
    emma "Oh... oh that's... that's actually good..."
    emma "You're so much more careful..."
    emma "So much more considerate..."
    mc "Because I actually care about you feeling good."
    mc "Your pleasure matters to me."
    emma "No one's ever... oh fuck..."
    emma "No one's ever cared about my pleasure before..."
    
    "I fuck her ass with long, slow strokes."
    "Building pleasure instead of just taking it."
    
    emma "This is... this is incredible..."
    emma "I never knew it could feel good..."
    emma "You're so gentle but so deep..."
    mc "You deserve to feel good, Emma."
    mc "You deserve someone who cares."
    emma "Don't stop... please don't stop..."
    emma "I'm going to cum again..."
    
    scene scene_12_final
    with fade
    
    "I fill her ass with cum as she shudders through another orgasm."
    "She collapses forward, completely spent."
    
    scene classroom_light_on
    show emma at emma_convo
    $ update_character_state("emma", CharState.AROUSED)
    with fade
    
    emma "That was... incredible."
    emma "I've never felt so... cared for during sex."
    emma "Like you actually wanted me to feel good too."
    mc "You deserve to be cared for."
    mc "You deserve so much better than what you're getting."
    emma "I... I think I'm falling for you."
    emma "But I can't leave Justin. Not yet."
    emma "My reputation... my social status..."
    emma "I wish I could see into the future... know how this all ends..."
    
    menu:
        "The future will work itself out":
            label test_choice_vw710:
            if emma_love >= 15:
                emma "I've actually been learning tarot lately... trying to predict things..."
                emma "What do fortune tellers try to see?"
                jump outfit_19_puzzle
                label outfit_19_puzzle_success:
                    emma "I have this mystical fortune teller outfit... maybe it brings good luck..."
                    emma "Maybe the cards will tell us what's meant to be..."
                label outfit_19_puzzle_failure:
                    emma "I guess the future is uncertain for both of us..."
        "We'll make our own future":
            label test_choice_32qms:
            emma "You're right... we control our destiny."
    mc "I understand."
    mc "When you're ready, I'll be here."
    emma "But I want to see you again. In secret."
    emma "And I'll stop the bullying. I'll tell people [girl_friend] was lying."
    emma "It's the least I can do."
    emma "After what you've shown me... what you've given me..."
    jump emma_aftermath

label study_date_bad:
    emma "This was a mistake."
    emma "I shouldn't have come here."
    mc "Emma-"
    emma "No. I have a boyfriend. I shouldn't be here."
    emma "Thanks for the help with studying, but that's all this was."
    emma "Academic assistance. Nothing more."
    mc "You felt something. I know you did."
    mc "When I saved you, when we were studying together..."
    emma "It doesn't matter what I felt!"
    emma "Feelings don't change facts!"
    emma "I'm with Justin. Popular girls date football players."
    emma "Not... whatever you are."
    emma "Not losers who everyone laughs at."
    mc "So that's it?"
    emma "That's it."
    emma "Don't talk to me at university. Don't approach me."
    emma "This never happened."
    emma "And if you tell anyone about this, I'll deny everything."
    
    "She gathers her things and leaves."
    "But I notice her hands shaking as she packs up."
    "She's not as sure as she pretends to be."
    
    jump emma_aftermath

label study_date_worst:
    $ update_character_state("emma", CharState.ANGRY)
    emma "You know what? Fuck this."
    emma "I tried to give you a chance, but you're hopeless."
    emma "Absolutely hopeless."
    emma "No wonder [girl_friend] cheated on you."
    emma "No wonder everyone thinks you're pathetic."
    mc "Emma, wait-"
    emma "No! I'm done waiting!"
    emma "Done pretending you might be worth my time!"
    
    "She pulls out her phone and starts recording."
    emma "Hey everyone! I'm here with the famous [player_name]!"
    emma "He actually thought he had a chance with me!"
    emma "Look at him! Pathetic!"
    emma "Sitting there like a lost puppy!"
    
    mc "Stop it!"
    emma "Or what? You'll cry?"
    emma "Actually, yes! Cry for the camera!"
    emma "Show everyone what a little bitch you are!"
    emma "Show them how [girl_friend] was right about everything!"
    
    "She shoves me, and I stumble backward."
    emma "That's right! Can't even stand up to a girl!"
    emma "Justin is going to love this video!"
    emma "Everyone is going to see what a complete loser you are!"
    emma "This is going viral, baby!"
    
    "She storms out, laughing cruelly."
    "I know by tomorrow, that video will be everywhere."
    "My reputation will be destroyed completely."
    
    jump emma_aftermath

label emma_aftermath:
    scene college_afternoon
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    "As I leave the classroom, I see something that makes my blood boil."
    "My mood, whatever it was, instantly turns to rage."
    $ update_character_state("mc", CharState.ANGRY)
    
    show nancy at nancy_convo
    $ update_character_state("nancy", CharState.HAPPY)
    $ update_character_state("matthews", CharState.HAPPY)
    
    "Nancy is hugging Matthews, giggling at something he said."
    "They're walking together, intimately close."
    "Her hand is on his chest, his arm around her waist."
    matthews "Nancy, my dear, you have such refined taste... such proper manners..."
    matthews "Not like these crude modern students..."
    menu:
        "What era does Matthews think he's from?":
            label test_choice_gcim4:
            if emma_love >= 35:
                outline "Matthews acts like he's from another time period..."
                outline "What defines refined manners from the 1800s?"
                jump outfit_49_puzzle
                label outfit_49_puzzle_success:
                    outline "Matthews thinks his outdated 'chivalry' justifies his predatory behavior!"
                    outline "But his Victorian facade is just manipulation!"
                    outline "He probably thinks he's some kind of scholar too..."
                    outline "What do people uncover when they dig into the past?"
                    jump outfit_59_puzzle
                    label outfit_59_puzzle_success:
                        outline "Too bad he can't dig himself out of his inappropriate behavior!"
                    label outfit_59_puzzle_failure:
                    outline "Matthews' old-fashioned act is just a cover..."
                label outfit_49_puzzle_failure:
                    outline "Matthews' old-fashioned act is just a cover..."
        "Focus on the inappropriate behavior":
            label test_choice_bs1et:
            outline "This is clearly inappropriate teacher-student conduct..."
    hide nancy
    show matthews at matthews_convo
    matthews "Oh look, if it isn't our star student."
    matthews "How's the studying going, [player_name]?"
    matthews "Managing to keep up with the... workload?"
    "The way he emphasizes 'workload' while looking at Nancy makes it clear."
    "He's fucking her. Another one of my connections, stolen by these predators."
    "First [girl_friend] with half the faculty, now Nancy with Matthews."
    hide matthews
    show nancy at nancy_convo
    nancy "Hi [player_name]! Professor Matthews has been so helpful!"
    nancy "He's been giving me... private lessons."
    nancy "Very... intensive private lessons."
    hide nancy
    show matthews at matthews_convo
    matthews "Yes, Nancy is proving to be very... eager to learn."
    matthews "Very receptive to my teaching methods."
    matthews "Unlike some students who disappear for weeks."
    matthews "Nancy appreciates a man who can... guide her properly."
    menu:
        "Say nothing and walk away":
            label test_choice_htkkl:
            "I clench my fists but stay silent."
            "My jaw tightens but I refuse to give them the satisfaction."
            "I turn and walk away, hearing their laughter behind me."
            "Matthews' smug chuckle and Nancy's nervous giggle."
        "Hope you're being safe, Nancy.":
            label test_choice_lttj4:
            mc "Hope you're being safe, Nancy."
            mc "Older men can be... unpredictable."
            hide matthews
            show nancy at nancy_convo
            nancy "What's that supposed to mean?"
            nancy "Professor Matthews is wonderful!"
            mc "Nothing. Just... be careful who you trust."
            mc "Some people have hidden motives."
            hide nancy
            show matthews at matthews_convo
            matthews "Is that a threat, Mr. [player_name]?"
            mc "Just friendly advice."
            mc "From someone who's learned the hard way."
        "(To Matthews) Does your wife know about your 'private lessons'?":
            label test_choice_7vfqe:
            mc "Does your wife know about your 'private lessons'?"
            mc "I'm sure she'd be very interested in your teaching methods."
            $ update_character_state("matthews", CharState.ANGRY)
            matthews "Watch your tongue, boy."
            matthews "You're on thin ice already."
            mc "Just curious about your teaching methods."
            mc "They seem very... hands-on."
            hide matthews
            show nancy at nancy_convo
            nancy "[player_name]! Don't be rude!"
            nancy "Professor Matthews is just helping me!"
            hide nancy
            show matthews at matthews_convo
            matthews "Some people can't handle seeing others' success."
            matthews "Jealousy is an ugly thing, Mr. [player_name]."
    outline "Matthews thinks he's untouchable... but predators eventually get exposed..."
    outline "What has this teacher become through his inappropriate behavior?"
    jump outfit_50_puzzle
    label outfit_50_puzzle_success:
        outline "When his misconduct is revealed, he'll be stripped of everything!"
        outline "Academic dignity, respect, credibility... all gone!"
    label outfit_50_puzzle_failure:
        outline "Matthews will face consequences for his actions..."
    "They walk away together, Nancy hanging on his every word."
    "Just like she used to hang on mine."
    "Another girl, stolen by another authority figure."
    hide matthews
    show mc at mc_convo
    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate
    bull_phone "That fucking bastard."
    bull_phone "Another predator taking advantage of vulnerable girls."
    mc "First [girl_friend] with half the college, now Nancy..."
    mc "Is there any girl these bastards won't steal from me?"
    bull_phone "Don't let it get to you. He's a predator who goes after vulnerable girls."
    bull_phone "But you're building something better. Real connections."
    bull_phone "Connections based on genuine attraction, not power dynamics."
    mc "Am I? Emma still might choose Justin. Lauren is sweet but..."
    mc "And now Nancy's gone too."
    bull_phone "You're making progress. But you need easier targets too."
    bull_phone "Remember the butcher's ex-wife? Gemmy?"
    mc "The one who kissed me in front of Craig?"
    bull_phone "She's divorced, hungry for affection, and already showed interest."
    bull_phone "Sometimes you need easy wins to build confidence."
    bull_phone "Start with the eager ones. Build your reputation."
    bull_phone "Then go after the taken ones when you're stronger."
    mc "You're right. I need to be strategic."
    mc "Can't just focus on the hard targets."
    bull_phone "Exactly. Gemmy is probably sitting at home right now, lonely."
    bull_phone "Thinking about that kiss, wondering if you'll call."
    bull_phone "Easy pussy to build your confidence."
    bull_phone "Then you come back for the bigger prizes."
    mc "Makes sense. Start small, work my way up."
    bull_phone "Now you're thinking like a real player."
    bull_phone "But wait, something just occurred to me."
    bull_phone "You're looking more confident, more powerful."
    bull_phone "Reminds me of your glory days before [girl_friend]."
    mc "What glory days? I was always a loser."
    bull_phone "Oh really? What about Dr. Morrison?"
    bull_phone "The hot brunette doctor at your old school?"
    bull_phone "The one who gave you very... thorough examinations?"
    mc "How do you know about that?"
    bull_phone "I know everything about you, remember?"
    bull_phone "She was quite the conquest. A mature woman in her thirties."
    bull_phone "Stuck in a loveless marriage, frustrated, until you came along."
    mc "That was different. That was before [girl_friend] destroyed my confidence."
    bull_phone "Exactly. And now you're getting it back."
    bull_phone "Remember what you're capable of when you're confident."
    bull_phone "Remember how good it felt to have that power."
    mc "I... I haven't thought about Dr. Morrison in a long time."
    bull_phone "Well, think about her now. Remember what you did."
    bull_phone "Use those memories to fuel your comeback."
    jump doctor_flashback_scene

label doctor_flashback_scene:
    
    scene black
    $ update_character_state("mc", CharState.NORMAL)
    play music "ES_Moonlight Mystery - Alexandra Woodward.mp3" volume 0.1
    with fade
    
    "The memories come flooding back..."
    "Dr. Morrison. God, how could I have forgotten about her?"
    
    scene medical_office
    with fade
    
    "It was two years ago, at my old school, before I met [girl_friend]."
    "Before everything went to hell."
    
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    
    "I was different then. Confident. A bit cocky even."
    "I'd gone to the medical office for a sports physical."
    "Dr. Morrison was the school physician - early thirties, gorgeous brunette."
    "Married to some investment banker who was never home."
    
    "I remember how she looked at me that first time..."
    "Professional on the surface, but her eyes betrayed her interest."
    "She was lonely, frustrated, stuck in a routine."
    "And I was young, fit, and bold enough to notice."
    
    menu:
        "Remember how it started...":
            label test_choice_7r5x5:
            $ doctor_flashback_intensity += 2
            
            "It started innocently enough."
            "She'd ask me to remove my shirt for the examination."
            "Her hands would linger a bit too long on my chest."
            "She'd stand closer than necessary."
            
            mc "(remembering) 'You seem tense, Dr. Morrison.'"
            mc "(remembering) 'When's the last time someone took care of you?'"
            
            "She'd tried to maintain professionalism at first."
            "But I could see her resolve weakening with each visit."
            "I started scheduling appointments for minor issues."
            "Just excuses to see her, to push things further."
            
        "Try to forget those memories...":
            label test_choice_be464:
            $ lose_sound()
            
            "No, I shouldn't think about this."
            "That was a different person, a different life."
            "Before [girl_friend], before the humiliation."
            
            "But the memories won't leave..."
            
        "Remember the first time you seduced her...":
            label test_choice_u9rmm:
            $ doctor_flashback_intensity += 3
            
            "I remember the exact moment her professional walls crumbled."
            "It was my fourth 'appointment' in two weeks."
            
            mc "(remembering) 'Your husband's a fool, Dr. Morrison.'"
            mc "(remembering) 'Any man who neglects a woman like you...'"
            mc "(remembering) 'He doesn't deserve you.'"
            
            "She'd broken down crying."
            "Told me about the loneliness, the neglect."
            "How her husband hadn't touched her in months."
            "How she felt invisible, unwanted."
    
    "The flashback continues, more vivid now..."
    
    if doctor_flashback_intensity >= 2:
        "I remember the first time we crossed the line."
        "It was after hours. She'd asked me to come back for 'additional tests.'"
        "We both knew what that meant."
        
        mc "(remembering) 'Lock the door, Dr. Morrison.'"
        mc "(remembering) 'We wouldn't want anyone walking in.'"
        
        "She did it without hesitation."
        "Her hands trembling with anticipation."
        
        "I remember pushing her against the examination table."
        "How she gasped when I kissed her neck."
        "How desperately she grabbed at me."
        "Like she was drowning and I was air."
        
        # Detailed medical examination scene (flashback)
        scene medical_office
        with fade
        
        "I remember that first detailed 'examination'..."
        "Dr. Morrison in her professional coat, trying to maintain composure."
        
        mc "(remembering) 'Dr. Morrison, this examination seems very... thorough.'"
        
        "She was wearing her medical coat, but I could see she wasn't wearing much underneath."
        "Her breathing was already heavy when I entered her office."
        
        mc "(remembering) 'Please, have a seat on the examination table, [player_name].'"
        mc "(remembering) 'I need to check your... stamina levels.'"
        
        "She approached with her stethoscope, leaning in unnecessarily close."
        
        mc "(remembering) 'Elevated heart rate. Are you nervous?'"
        mc "(remembering) 'This is highly unprofessional, Doctor.'"
        mc "(remembering) 'Perhaps. But necessary.'"
        
        "I remember how she asked me to remove my clothes 'for the examination.'"
        "How her hands trembled as she touched me."
        
        scene black
        show scene_19
        with fade
        
        $ persistent.scene_19 = True
        
        "I remember how desperate she was, how she needed me right there against the wall."
        $ play_grab_sound()
        "Her hands grabbed at me urgently, pulling me closer."
        "She was so frustrated, so hungry for real passion."
        
        mc "(remembering) 'I can't wait for the examination table...'"
        mc "(remembering) 'I need you now. Right here.'"
        
        "She lifted her leg up in the air, wrapping it around my waist with athletic grace."
        "The position was incredibly sexy - standing, her leg high, completely open to me."
        $ play_penetration_sound()
        
        mc "(remembering) 'God, you're so flexible... so beautiful like this.'"
        mc "(remembering) 'Hold that leg up high for me.'"
        
        "I entered her in that standing position, her leg stretched up in the air."
        "The angle was perfect, allowing me to go incredibly deep."
        $ play_vagina_insertion_sound()
        
        mc "(remembering) 'Oh fuck! You're so deep when I'm like this!'"
        $ play_woman_pleasure_sound()
        
        "The standing position with her leg up gave me complete control."
        
        mc "(remembering) 'My husband could never hold me up like this...'"
        mc "(remembering) 'Never fuck me standing... never make me feel so exposed and wanted...'"
        
        "I held her firmly against the wall, her leg high in the air, fucking her with deep strokes."
        
        mc "(remembering) 'You're so strong... keeping me balanced...'"
        mc "(remembering) 'This position makes me feel so vulnerable... so completely yours...'"
        
        "Her pussy gripped me perfectly in that elevated position - the angle was incredible."
        "Every thrust hit deeper than her husband ever could."
        $ play_penetration_sound()
        
        mc "(remembering) 'I'm going to cum! This angle is too perfect!'"
        $ play_woman_pleasure_sound()
        mc "(remembering) 'Fill me up! Right here against the wall with my leg up!'"
        
        scene scene_19_final
        with fade
        
        "I filled her with cum as she convulsed, her leg trembling in the air."
        $ play_cum_sound()
        $ play_man_pleasure_sound()
        "Her leg finally gave out, and she slumped against me, breathing hard."
        $ play_woman_breathing_sound()
        
        scene medical_office
        with fade
        
        "Afterward, she was amazed by the intensity."
        
        mc "(remembering) 'That position... I've never felt so exposed, so taken.'"
        mc "(remembering) 'You made me feel like a goddess.'"
        mc "(remembering) 'My husband could never pleasure me like that...'"
        
        "We fucked right there on that table so many times."
        "Where she examined patients every day."
        "She kept saying her husband's name, but not in guilt."
        "She was comparing us, and I was winning."
        
        mc "(remembering) 'This is what you've been missing.'"
        mc "(remembering) 'This is what you deserve.'"
        
        "She came three times that first night."
        "Said it was more than her husband had given her in years."
        
    else:
        "The memories are hazy, fragmented."
        "But I remember the power I felt."
        "Having this older, sophisticated woman desperate for me."
        "Begging for my attention, my touch."
    
    "The affair lasted three months."
    "Three months of secret meetings, stolen moments."
    "She'd text me late at night when her husband was asleep."
    "Send me pictures from her bathroom, her bedroom."
    "Beg me to come over when he was on business trips."
    
    menu:
        "Remember the riskiest encounter...":
            label test_choice_9xgev:
            $ doctor_flashback_intensity += 2
            
            "The riskiest time was during a school board meeting."
            "Her husband was there, in the auditorium."
            "She texted me, desperate, needing release."
            
            mc "(remembering) 'Meet me in your office. Now.'"
            
            "We fucked with her husband just two floors below."
            "She had to bite her lab coat to muffle her screams."
            "The danger, the risk, it made everything more intense."
            
            "Afterward, she went back to the meeting."
            "Sat next to her husband with my cum still inside her."
            "Smiled and nodded at his boring stories."
            "While texting me under the table about round two."
            
            mc "(remembering) 'You're mine, Dr. Morrison.'"
            mc "(remembering) 'Your body knows it, even if he doesn't.'"
            
        "Remember how it ended...":
            label test_choice_e4utf:
            $ lose_sound()
            
            "It ended when I met [girl_friend]."
            "[girl_friend] was everything Dr. Morrison wasn't."
            "Young, vibrant, supposedly innocent."
            "I was an idiot. I threw away guaranteed pussy for a fantasy."
            
            "Dr. Morrison begged me not to end it."
            "Said she'd leave her husband, start fresh with me."
            "But I was young and stupid."
            "I wanted the college girlfriend experience."
            
            "Last I heard, she'd moved away."
            "Divorced her husband, started over somewhere else."
            "Sometimes I wonder if she thinks about me."
            
        "Remember her special techniques...":
            label test_choice_iq5c2:
            $ doctor_flashback_intensity += 1
            
            "Dr. Morrison had techniques I'd never experienced."
            "Things she'd learned from medical texts, anatomy studies."
            "She knew exactly where to touch, how to touch."
            
            "She could make me cum without even touching my cock."
            "Just pressure points, nerve stimulation."
            "Medical knowledge applied to pleasure."
            
            mc "(remembering) 'Where did you learn that?'"
            mc "(remembering) 'Medical school had some interesting electives.'"
            
            "She taught me things too."
            "How to find the g-spot, properly stimulate the clit."
            "Anatomically precise pleasure."
            "Skills I've used on every girl since."
    
    scene black
    with fade
    
    "The memories fade, but the feelings remain."
    "The confidence. The power. The control."
    "I had it once. I can have it again."
    
    if doctor_flashback_intensity >= 3:
        "Dr. Morrison taught me so much."
        "Not just about sex, but about women."
        "How desperate they can be for attention."
        "How easy they are to seduce when neglected."
        "How much they'll risk for good dick."
        
        mc "I was a fucking god back then."
        mc "Before [girl_friend]. Before the humiliation."
        mc "But I'm getting it back."
        
        $ remembered_doctor = True
        
    else:
        "The memories are painful."
        "A reminder of what I used to be."
        "What I lost when I chose [girl_friend]."
        
        mc "I need to forget the past."
        mc "Focus on the future."
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    if doctor_flashback_intensity >= 3:
        bull_phone "Excellent! You remember who you really are!"
        bull_phone "That confident young stud who had a married doctor begging for his cock."
        bull_phone "That's the real you, not the broken boy [girl_friend] created."
        bull_phone "Use those memories. Channel that confidence."
        mc "You're right. I did it before, I can do it again."
        mc "Dr. Morrison was just the beginning."
        bull_phone "Exactly! And now you have the experience."
        bull_phone "You know what works. You know how to seduce."
        bull_phone "Time to put those skills back to use."
    else:
        bull_phone "You're still holding back."
        bull_phone "Afraid to remember who you really were."
        bull_phone "But that's okay. It'll come back."
        mc "It's just... painful to remember."
        mc "How far I've fallen."
        bull_phone "Then use that pain as motivation."
        bull_phone "To climb back up. To reclaim your throne."
    
    bull_phone "Now, about Gemmy..."
    bull_phone "She's exactly the type you used to excel with."
    bull_phone "Neglected, desperate, hungry for attention."
    bull_phone "Just like Dr. Morrison was."
    bull_phone "Time to show her what she's been missing."
    
    mc "You're right. Same type, same approach."
    mc "Make her feel desired, wanted, special."
    mc "Everything her ex-husband didn't do."
    
    bull_phone "Now you're thinking like the old you."
    bull_phone "The you that had older women begging."
    bull_phone "Time to make your move on easier targets."
    bull_phone "Build your confidence, then circle back for the harder conquests."
    
    # Advanced Doctor Morrison scene for high intensity flashback players
    if doctor_flashback_intensity >= 3 and remembered_doctor == True:
        
        "As the Bull Phone's words sink in, a sudden realization hits me."
        "Dr. Morrison. She moved away after I left her, but..."
        "What if she transferred to this university's medical center?"
        
        show bull at bull_convo
        $ update_character_state("bull", CharState.HAPPY)
        with pixellate
        
        bull_phone "I can see those gears turning, stud."
        bull_phone "You're thinking about your doctor, aren't you?"
        
        mc "She could be here. At the university medical center."
        mc "It's been two years, but..."
        
        bull_phone "Only one way to find out."
        bull_phone "And if she is... well, you know exactly how to handle lonely, neglected women."
        
        menu:
            "Go to the university medical center":
                label test_choice_22nbb:
                mc "You know what? I need to find out."
                mc "If she's here, if she remembers me..."
                mc "It could be exactly what I need to get my confidence back."
                
                bull_phone "That's the spirit!"
                bull_phone "Go claim what was always yours."
                
                jump doctor_morrison_reunion
                
            "Focus on new targets instead":
                label test_choice_t3js5:
                $ lose_sound()
                mc "No, that's the past. I should focus on new conquests."
                mc "Gemmy, Emma... girls who don't know the old me."
                
                bull_phone "Your choice. But opportunity knocks rarely."
                bull_phone "Don't say I didn't warn you if you regret it later."
                
                # Grant episode 3 completion achievement
                # call grant_episode_achievement(3)
                # $ check_love_achievements()
                
                jump episode_4
    else:
        # Grant episode 3 completion achievement
        # call grant_episode_achievement(3)
        # $ check_love_achievements()
        
        jump episode_4

label doctor_morrison_reunion:
    
    scene black
    with fade
    
    "The memories intensify, becoming more vivid."
    "I remember one encounter in particular..."
    "The one that showed me just how completely she belonged to me."
    
    scene medical_office
    with fade
    
    "I remember walking into her office after hours."
    "She was waiting for me, pretending to do paperwork."
    "But I could see the anticipation in her eyes."
    "The way her breathing quickened when I entered."
    
    mc "(remembering) 'Working late again, Dr. Morrison?'"
    
    "She looked up at me with those desperate eyes."
    "The same look every neglected woman gives me."
    "The look that says they need what only I can provide."
    
    mc "(remembering) 'You know why you stay late.'"
    mc "(remembering) 'You know what you really want.'"
    
    "I remember how she didn't even try to deny it anymore."
    "How she stood up from her desk, already reaching for me."
    "How completely she had surrendered to her needs."
    
    mc "(remembering) 'Please... I need you so badly.'"
    mc "(remembering) 'My husband... he doesn't touch me anymore.'"
    
    "The memory is so vivid I can almost feel her desperation."
    "The way she clung to me like I was her salvation."
    "Like I was the only thing keeping her alive."
    
    mc "(remembering) 'Then let me take care of you, Sarah.'"
    mc "(remembering) 'Let me give you what he can't.'"
    
    "I remember guiding her back to the examination table."
    "Our usual spot. Our sacred place."
    "Where she stopped being a doctor and became just a woman."
    "My woman."
    
    mc "(remembering) 'This is where you belong.'"
    mc "(remembering) 'Not with him. Here. With me.'"
    
    "She never argued. Never resisted."
    "Just melted into my arms like she always did."
    "Completely surrendering to what we both knew was inevitable."
    
    scene black
    show scene_23_initial
    stop music fadeout 1.0
    with fade
    
    outline "I remember lifting her onto the examination table."
    outline "How she spread her legs willingly, draping them over my shoulders."
    outline "The familiar position that drove us both wild."
    outline "Her complete surrender to our forbidden desire."
    
    mc "(remembering) 'Oh god... [player_name]...'"
    $ play_woman_pleasure_sound()
    
    mc "(remembering) 'I know you need this, Sarah.'"
    mc "(remembering) 'Your body is mine, even if he doesn't understand that.'"
    $ play_man_pleasure_sound()
    
    mc "(remembering) 'Yes... yes, I'm yours...'"
    $ play_woman_pleasure_sound()
    
    scene black
    show scene_23
    with fade
    
    outline "I remember entering her slowly, savoring every moment."
    outline "How her legs trembled on my shoulders as I filled her completely."
    outline "The way the examination table creaked with our passionate rhythm."
    outline "The desperation in her moans as she clung to me."
    
    mc "(remembering) 'This is where you belong, Sarah.'"
    mc "(remembering) 'Not in some cold marriage bed. Here, with me.'"
    $ play_man_pleasure_sound()
    $ play_penetration_sound()
    
    mc "(remembering) 'I know... God, I know...'"
    mc "(remembering) 'I've never felt this alive with anyone else...'"
    $ play_woman_pleasure_sound()
    
    outline "I remember increasing the pace, her legs gripping my shoulders."
    outline "How she arched beneath me, pushing herself against me."
    outline "Desperately seeking more contact, more pleasure."
    outline "More of what only I could give her."
    
    mc "(remembering) 'No other man has ever touched me like this.'"
    mc "(remembering) 'Only you know how to make me feel this way.'"
    $ play_man_pleasure_sound()
    $ play_penetration_sound()
    
    mc "(remembering) 'Because you're mine, Sarah.'"
    mc "(remembering) 'Your body knows it, even when your mind fights it.'"
    $ play_woman_pleasure_sound()
    
    outline "I remember how the confession drove me wild."
    outline "Gripping her hips, pulling her against me with each thrust."
    outline "The table shaking as our passion reached its peak."
    outline "Her desperate cries echoing through the empty office."
    
    mc "(remembering) 'I'm so close... please don't stop...'"
    mc "(remembering) 'I need this... I need you...'"
    $ play_woman_pleasure_sound()
    
    mc "(remembering) 'Come for me, Sarah.'"
    mc "(remembering) 'Show me you're completely mine.'"
    $ play_man_pleasure_sound()
    
    mc "(remembering) 'YES! Oh god, YES! I'm yours!'"
    $ play_woman_pleasure_sound()
    
    outline "I remember how she climaxed with earth-shattering intensity."
    outline "Her legs gripping my shoulders as waves of pleasure consumed her."
    outline "How her complete surrender pushed me over the edge."
    outline "The moment I truly claimed her as mine."
    
    mc "(remembering) 'Sarah! You're perfect!'"
    $ play_man_pleasure_sound()
    
    scene scene_23_final
    with fade
    
    outline "I remember reaching my climax while she trembled beneath me."
    outline "Filling her completely as her legs remained wrapped around my shoulders."
    outline "Her soft cries of satisfaction mixing with my groans of dominance."
    outline "The perfect moment of complete possession."
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    
    mc "(remembering) 'Mmm... you're incredible...'"
    $ play_woman_pleasure_sound()
    $ play_woman_breathing_sound()
    
    scene black
    with fade
    
    "The memory fades, but the feelings remain vivid."
    "The power I had over her. The complete control."
    "How she would beg me to stay after our encounters."
    "The way she looked at me like I was her entire world."
    
    "I remember how we would separate afterward."
    "Both breathless and satisfied."
    "Her sitting on that examination table, glowing with satisfaction."
    "The look of a woman who had been truly fulfilled."
    
    mc "(remembering) 'I can't believe we just did that...'"
    mc "(remembering) 'In my office... what if someone had walked in?'"
    
    "But I knew she loved the risk. The danger."
    "It made everything more intense."
    "More addictive."
    
    mc "(remembering) 'We needed it. You needed it.'"
    mc "(remembering) 'Your husband doesn't make you feel this way.'"
    
    "I remember how she would always bring up her husband afterward."
    "The guilt and the desire warring in her eyes."
    "But the desire always won."
    
    mc "(remembering) 'He'll be expecting me home...'"
    mc "(remembering) 'But I don't want you to leave...'"
    
    "She never wanted me to leave."
    "Would beg me to stay, to hold her."
    "To make her feel desired just a little longer."
    
    mc "(remembering) 'Then don't let me go.'"
    mc "(remembering) 'Choose what makes you happy for once.'"
    
    "But she was always trapped between duty and desire."
    "Professional reputation versus personal satisfaction."
    "The same struggle every woman faces."
    "Until they choose me."
    
    "I remember her laugh. So genuine, so free."
    "The sound of a woman who had found what she was missing."
    "What her husband could never give her."
    
    mc "(remembering) 'You haven't changed at all...'"
    mc "(remembering) 'Still the same confident man who owns my body...'"
    
    "And I remember my response."
    "The truth we both knew but rarely spoke."
    
    mc "(remembering) 'And you're still the lonely doctor who belongs to me.'"
    
    "The memory ends with her promise."
    "To meet again. To continue what we had."
    "The addiction that neither of us could break."
    
    "That confidence. That power."
    "I had it once."
    "And I can have it again."
    
    $ persistent.scene_23 = True
    
    # Additional intense memory if high flashback intensity
    if doctor_flashback_intensity >= 3:
        
        "But wait... there's another memory."
        "One even more intense. More dominant."
        "The time I truly showed her who was in control."
        
        jump doctor_dominant_memory
    else:
        # Grant episode 3 completion achievement
        # call grant_episode_achievement(3)
        # $ check_love_achievements()
        
        jump episode_4

label doctor_dominant_memory:
    
    scene black
    with fade
    
    "Another memory surfaces. More vivid. More powerful."
    "The night I took complete control."
    "When she stopped being Dr. Morrison and became just Sarah."
    "My Sarah."
    
    scene medical_office
    with fade
    
    "I remember walking into her office that night."
    "She was working late again, but this time was different."
    "This time I didn't ask permission."
    "I simply took what was already mine."
    
    mc "(remembering) 'Turn around, Sarah.'"
    
    "She looked up from her paperwork, surprised by my commanding tone."
    "But she didn't question it. She never questioned me."
    "Just slowly stood and turned around, facing away from me."
    "Submitting to my authority like she always did."
    
    mc "(remembering) 'Place your hands on the desk.'"
    mc "(remembering) 'Don't turn around until I tell you.'"
    
    "I remember how she trembled with anticipation."
    "How her breathing became shallow and rapid."
    "She wanted this. Needed this level of control from me."
    "Needed to surrender completely."
    
    mc "(remembering) 'Please... I've been thinking about you all day...'"
    mc "(remembering) 'I couldn't concentrate on anything else...'"
    
    "Her confession only fueled my dominance."
    "She was completely addicted to what I gave her."
    "What her husband could never provide."
    "True masculine control."
    
    mc "(remembering) 'Good. That's exactly how it should be.'"
    mc "(remembering) 'You belong to me, not to him.'"
    
    scene black
    show scene_24_initial
    stop music fadeout 1.0
    with fade
    
    outline "I remember positioning her bent over the desk."
    outline "Her professional attire disheveled, vulnerable."
    outline "The way she gripped the edge of the desk, waiting."
    outline "Completely at my mercy, exactly where she belonged."
    
    mc "(remembering) 'Oh god... yes... take me...'"
    $ play_woman_pleasure_sound()
    
    mc "(remembering) 'You're mine, Sarah. Say it.'"
    mc "(remembering) 'Tell me who you belong to.'"
    $ play_man_pleasure_sound()
    
    mc "(remembering) 'I'm yours... only yours...'"
    $ play_woman_pleasure_sound()
    
    scene black
    show scene_24
    with fade
    
    outline "I remember taking her from behind, asserting complete dominance."
    outline "Her desperate moans as I set the rhythm, the pace."
    outline "How she could only grip the desk and surrender to my will."
    outline "The perfect position of absolute control."
    
    mc "(remembering) 'This is how it should always be.'"
    mc "(remembering) 'You bent over for me, submitting completely.'"
    $ play_man_pleasure_sound()
    $ play_penetration_sound()
    
    mc "(remembering) 'Yes... yes... I need this so badly...'"
    mc "(remembering) 'No one has ever made me feel this way...'"
    $ play_woman_pleasure_sound()
    
    outline "I remember gripping her hips, pulling her back against me."
    outline "The sound of our bodies colliding with each powerful thrust."
    outline "How she could only take what I gave her."
    outline "Completely powerless, completely mine."
    
    mc "(remembering) 'Harder... please... don't hold back...'"
    mc "(remembering) 'I want to feel your strength...'"
    $ play_woman_pleasure_sound()
    
    mc "(remembering) 'You want me to use you completely?'"
    mc "(remembering) 'To show you what real dominance feels like?'"
    $ play_man_pleasure_sound()
    $ play_penetration_sound()
    
    mc "(remembering) 'Yes! Use me! I'm yours to use!'"
    $ play_woman_pleasure_sound()
    
    outline "I remember increasing the intensity, showing no mercy."
    outline "Her desperate cries echoing through the empty office."
    outline "The desk shaking with the force of my thrusts."
    outline "Pure, primal dominance over her willing body."
    
    mc "(remembering) 'I'm going to... I can't hold back...'"
    mc "(remembering) 'You're making me lose control...'"
    $ play_woman_pleasure_sound()
    
    mc "(remembering) 'Then lose control. Give me everything.'"
    mc "(remembering) 'Show me how much you need this.'"
    $ play_man_pleasure_sound()
    
    mc "(remembering) 'I'M CUMMING! OH GOD, I'M CUMMING!'"
    $ play_woman_pleasure_sound()
    
    outline "I remember her climax, violent and earth-shattering."
    outline "How her entire body convulsed as waves of pleasure consumed her."
    outline "The moment she truly surrendered her soul to me."
    outline "Complete and total possession."
    
    mc "(remembering) 'Sarah! Take everything!'"
    $ play_man_pleasure_sound()
    
    scene scene_24_final
    with fade
    
    outline "I remember reaching my peak while she was still trembling."
    outline "Claiming her completely, marking her as mine."
    outline "Her soft whimpers of satisfaction as I filled her."
    outline "The perfect moment of absolute domination."
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    
    mc "(remembering) 'Mmm... you're perfect like this...'"
    $ play_woman_pleasure_sound()
    $ play_woman_breathing_sound()
    
    scene black
    with fade
    
    "The memory fades, but the power remains."
    "That night changed everything between us."
    "After that, she was completely mine."
    "Body, mind, and soul."
    
    "I remember how she collapsed onto the desk afterward."
    "Completely spent, completely satisfied."
    "Looking back at me with pure adoration."
    "The look of a woman who had found her master."
    
    mc "(remembering) 'I've never... that was incredible...'"
    mc "(remembering) 'You make me feel things I didn't know were possible...'"
    
    "She would always say that after our most intense encounters."
    "How I awakened something in her."
    "Something her husband could never touch."
    "Something that belonged only to me."
    
    mc "(remembering) 'Because you're mine, Sarah.'"
    mc "(remembering) 'And I know exactly what you need.'"
    
    "That confidence. That absolute certainty."
    "Knowing I could dominate any woman completely."
    "Make them beg for more, even as I used them."
    "Especially the married ones."
    
    "They were always the most desperate."
    "The most grateful."
    "The most addicted to what I provided."
    "Pure, masculine dominance."
    
    $ persistent.scene_24 = True
    
    # Grant episode 3 completion achievement
    # call grant_episode_achievement(3)
    # $ check_love_achievements()
    
    jump episode_4

label game_over_emma:
    scene black
    # MUSIC PLACEHOLDER: Stop music for game over scene - dramatic failure
    # stop music fadeout 1.0
    with fade
    
    "Emma spreads the word about how pathetic I am."
    "The video of me failing at the gym goes viral on campus."
    "Even the girls who defended me start to doubt their support."
    "[girl_friend]'s lies seem like truths now, validated by Emma's testimony."
    "My reputation is destroyed beyond repair."
    
    bull_phone "You've fucked up too many times."
    bull_phone "I can't help someone who won't help himself."
    bull_phone "You had every opportunity and you blew them all."
    bull_phone "Goodbye, loser."
    
    "The phone goes silent forever."
    "My reputation is destroyed beyond repair."
    "I drop out of college and never recover."
    "I spend the rest of my life as the laughingstock Emma made me."
    
    return