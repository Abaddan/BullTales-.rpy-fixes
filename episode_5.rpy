# Episode 5: The Climax
# Episode 5 uses centralized points system from points_system.rpy
default jane_jealousy_level = 0
default submissive_choices = 0
default witnessed_betrayal = False
default justin_humiliated = False
default power_consolidated = False

label episode_5:
    
    # Calculate previous conquests using centralized love system
    python:
        previous_conquests = get_total_conquests()
    
    scene home_morning
    show mc at mc_convo
    $ update_character_state("mc", CharState.HAPPY)
    play music "ES_Moonlight Mystery - Alexandra Woodward.mp3" volume 0.2
    with Fade(0.5, 5.0, 0.5)
    
    "A week has passed since my triumph with Craig's ex-wives."
    "Gemmy's child support payments started coming in immediately after Craig received our video."
    "Ersa texted this morning that Craig won't even look her in the eye when he passes her on the street."
    "The satisfaction of that complete victory still feels incredible."
    
    outline "But as I'm savoring my success, something feels different today."
    outline "There's electricity in the air, like a storm approaching."
    outline "And I have a feeling I know exactly what kind of storm it is."
    
    $ update_character_state("mc", CharState.NORMAL)
    mc "(Things have been going almost too well lately.)"
    mc "(Nancy's been texting me daily, Lauren and I have plans this weekend.)"
    mc "(Emma even broke up with Justin officially yesterday.)"
    mc "(But something tells me the real test is coming.)"
    
    play sound "ES_Notification, Message, Text 04 - Epidemic Sound.mp3"
    
    "My phone buzzes with an unknown number."
    "When I read the message, my blood runs cold."
    
    $ update_character_state("mc", CharState.ANGRY)
    
    mc "No... it can't be..."
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    bull_phone "Speaking of storms, remember when I said we weren't done yet?"
    bull_phone "Well, the final boss has arrived!"
    bull_phone "Your dear ex-girlfriend [girl_friend] has returned to town!"
    
    if double_licking_scene == True:
        bull_phone "Perfect timing too - right after our masterpiece with Craig's ex-wives."
        bull_phone "That video broke Craig completely. He's been paying everything he owes."
        bull_phone "Now we get to deal with the source of all your problems."
    elif butcher_blackmail_success == True:
        bull_phone "Right after we neutralized Craig with his ex-wife."
        bull_phone "You're building quite the reputation as a women-stealer."
        bull_phone "And now the biggest test arrives."
    else:
        bull_phone "And your timing with women is finally getting good enough to handle her."
    
    bull_phone "[girl_friend]'s single again. Justin couldn't keep his dick in his pants."
    bull_phone "Cheated on her with multiple women - including some you know."
    bull_phone "The same women he was fucking while she was cheating on you with him."
    
    mc "That's... ironically perfect."
    mc "She left me for a cheater, only to get cheated on herself."
    
    bull_phone "The universe has a sense of humor, doesn't it?"
    bull_phone "But here's the interesting part - she wants to 'talk' about what happened."
    bull_phone "Says she has something important to tell you."
    
    "I read [girl_friend]'s message again:"
    outline "'[player_name], I know I have no right to ask, but I need to see you."
    outline "I'm back in town, staying with my sister."
    outline "There are things you need to know about what really happened with Justin."
    outline "Things that might change how you see everything."
    outline "Please. Just one conversation.'"
    
    mc "She has some nerve asking to see me after everything."
    mc "After destroying my reputation, spreading those lies..."
    
    bull_phone "But aren't you curious? Don't you want to show her what she threw away?"
    bull_phone "Look at you now - Nancy adores you, Lauren's devoted, Emma's conflicted but interested."
    bull_phone "You've conquered Craig's ex-wives, exposed him for the deadbeat he is."
    bull_phone "You're not the same broken boy she left behind."
    
    mc "You're right. I'm not."
    mc "The question is, what do I do about this?"
    
    bull_phone "That's up to you. But remember - this is your chance for closure."
    bull_phone "Or revenge. Or both."
    bull_phone "The final act of your transformation begins now."
    
    menu:
        "You come over. We need to settle this once and for all.":
            label test_choice_gnddh:
            # Strong confrontation
            $ jane_love -= 5
            $ justin_hate += 10
            
            $ update_character_state("mc", CharState.ANGRY)
            mc "You come over. We need to settle this once and for all."
            mc "She wants to talk? Fine. But it'll be on my terms this time."
            
            $ update_character_state("bull", CharState.HAPPY)
            bull_phone "Yes! That's the energy I want to see!"
            bull_phone "Show her what she lost. Make her understand the mistake she made."
            bull_phone "And if the opportunity presents itself... well, you know what to do."
            
            mc "I know exactly what to do."
            mc "Time to face the past and bury it properly."
            
            jump jane_immediate_meeting
            
        "We need to talk, but on my terms. She comes to me.":
            label test_choice_jzsvm:
            # Moderate confrontation
            $ win_sound()
            $ jane_love += 3
            $ jane_humiliation_level += 2
            
            $ update_character_state("mc", CharState.NORMAL)
            mc "We need to talk, but on my terms. She comes to me."
            mc "I'm not running to her like some eager puppy anymore."
            mc "If she wants to talk, she can make the effort."
            
            bull_phone "Good. Make her work for it."
            bull_phone "Show her you're not desperate for her attention anymore."
            
            "I text [girl_friend] back:"
            mc "'If you want to talk, come to my place tonight at 8. Take it or leave it.'"
            
            "Her response is almost immediate:"
            outline "'Okay. I'll be there. Thank you for giving me a chance.'"
            
            bull_phone "She agreed quickly. She must be desperate."
            bull_phone "This gives you time to prepare. Maybe invite one of your girls over first?"
            bull_phone "Let [girl_friend] see you've moved on?"
            
            jump jane_prepare_meeting
            
        "I have nothing to say to you. Stay away from me.":
            label test_choice_ibaz7:
            $ lose_sound()
            # Mild confrontation
            $ submissive_choices += 1
            
            $ update_character_state("mc", CharState.SAD)
            mc "I have nothing to say to you. Stay away from me."
            mc "I can't... I can't go through that again."
            
            $ update_character_state("bull", CharState.ANGRY)
            bull_phone "Are you serious? After everything we've built?"
            bull_phone "You're going to run away from the ultimate confrontation?"
            
            mc "It's not running. It's protecting myself."
            mc "I've moved on. I don't need to see her."
            
            bull_phone "You're lying to yourself. You need closure."
            bull_phone "And whether you like it or not, she's not going to stay away."
            bull_phone "[girl_friend] always gets what she wants, remember?"
            
            jump jane_avoidance_path
            
        "Only if you admit what you did wrong first.":
            label test_choice_if350:
            # Moderate confrontation
            $ win_sound()
            $ jane_love += 5
            $ jane_humiliation_level += 5
            
            $ update_character_state("mc", CharState.NORMAL)
            mc "Only if you admit what you did wrong first."
            mc "I want a written admission of your lies, your cheating, everything."
            mc "Then maybe we can talk."
            
            "I send the message and wait."
            "It takes her longer to respond this time."
            
            outline "'I... I know I hurt you. Yes, I was wrong about many things. I spread lies because I was angry and confused. I'll admit everything if that's what it takes. Please, just let me explain.'"
            
            bull_phone "Interesting. She's actually admitting fault."
            bull_phone "This could be useful. A written confession from her..."
            bull_phone "You could clear your name completely."
            
            mc "It's a start. But I want more than just words."
            mc "I want her to understand what she put me through."
            
            jump jane_conditional_meeting

label jane_immediate_meeting:
    
    scene home_night
    $ update_character_state("jane", CharState.SAD)
    show jane at jane_convo
    stop music
    with fade
    
    "She opens the door, and I'm struck by how different she looks."
    "The confident, cruel woman who destroyed me seems smaller somehow."
    "Her eyes are red from crying, her usually perfect appearance disheveled."
    
    jane "[player_name]... you actually came."
    jane "I wasn't sure you would after... everything."
    
    $ update_character_state("mc", CharState.ANGRY)
    mc "I'm here. Talk."
    mc "You have five minutes to say whatever you need to say."
    
    $ update_character_state("jane", CharState.SAD)
    jane "Five minutes? [player_name], please, I need more time than that."
    jane "There's so much you don't know. So much I need to tell you."
    
    menu:
        "You had months to talk. Why should I listen now?":
            label test_choice_76dpg:
            $ jane_love -= 3
            $ justin_hate += 5
            
            mc "You had months to talk. Why should I listen now?"
            mc "When you were spreading lies about me, destroying my reputation?"
            mc "When you were fucking Justin and laughing about it?"
            
            $ update_character_state("jane", CharState.SAD)
            jane "I know! I know I was horrible!"
            jane "But I was angry and hurt and confused!"
            jane "Justin told me things... showed me things..."
            
            mc "What things?"
            mc "What possible excuse could you have?"
            
            jane "He had photos. Messages. Made it look like you were cheating."
            jane "Fake conversations with other girls. I was an idiot to believe him."
            jane "But he was so convincing, so charming..."
            
            mc "So you fucked him to get back at me for something I didn't even do?"
            mc "Do you have any idea what you put me through?"
            
        "Fine. Talk. But I'm not promising anything.":
            label test_choice_ex861:
            $ win_sound()
            $ jane_love += 3
            
            $ update_character_state("mc", CharState.NORMAL)
            mc "Fine. Talk. But I'm not promising anything."
            mc "I'll listen, but that doesn't mean I'll forgive."
            
            jane "That's fair. More than fair, actually."
            jane "Can we sit down? This might take a while."
            
            "We move to the living room."
            "The tension between us is palpable."
            "Part anger, part hurt, and something else... residual attraction?"
            
            jane "First, I need you to know that Justin played us both."
            jane "He wanted me because I was yours. It was a game to him."
            jane "Conquering another man's girlfriend, proving his dominance."
            
            mc "And you fell for it."
            
            jane "I did. I was stupid and vain and I fell for it completely."
            jane "But that's not the worst part..."
            
        "You chose Justin. Now live with that choice.":
            label test_choice_uldlb:
            $ jane_love -= 8
            $ justin_hate += 15
            
            mc "You chose Justin. Now live with that choice."
            mc "Or can't you? Is that why you're here?"
            mc "Because he dumped you like the trash you are?"
            
            $ update_character_state("jane", CharState.ANGRY)
            jane "How dare you-"
            jane "No. No, you're right. I deserve that."
            jane "I am trash. I threw away something real for an illusion."
            
            $ update_character_state("jane", CharState.SAD)
            jane "Justin didn't dump me. I left him."
            jane "After I found out he was fucking my best friend. And my roommate."
            jane "And at least three other girls from campus."
            jane "All while telling me I was the only one."

    jane "But here's what you really need to know."
    jane "Justin bragged about it. About all of it."
    jane "How he 'stole' me from you. How he made you a laughingstock."
    jane "He showed me videos... of you crying in your room."
    
    $ update_character_state("mc", CharState.ANGRY)
    mc "Videos? How did he-"
    
    jane "Your roommate. He paid him to record you at your lowest."
    jane "Justin wanted trophies. Evidence of his conquests."
    jane "He has videos of me too. Of us... together."
    jane "He threatens to release them if I don't do what he wants."
    
    menu:
        "So you came to me for help? After everything?":
            label test_choice_hm78n:
            $ jane_love -= 5
            $ justin_hate += 10
            
            mc "So you came to me for help? After everything?"
            mc "You destroy my life, and now that yours is falling apart, you run to me?"
            mc "The irony is incredible."
            
            $ update_character_state("jane", CharState.SAD)
            jane "I'm not asking for help. I'm trying to warn you."
            jane "Justin's planning something. He knows about your recent... activities."
            jane "Nancy, Lauren, Emma... he knows about all of them."
            
            mc "How does he know about Emma?"
            mc "She's his girlfriend... or was."
            
            jane "She told him. Everything."
            jane "She's still with him, [player_name]. It was all a game."
            jane "She was supposed to humiliate you, but apparently you turned the tables."
            jane "Now Justin wants revenge."
            
        "What does he have on you exactly?":
            label test_choice_ssw2u:
            $ win_sound()
            $ jane_love += 3
            $ jane_humiliation_level += 5
            
            mc "What does he have on you exactly?"
            mc "These videos... how bad are they?"
            
            $ update_character_state("jane", CharState.AROUSED)
            jane "They're... explicit. Very explicit."
            jane "Things I did to please him. Things I'm ashamed of."
            jane "If they got out, my career would be over before it started."
            
            mc "And you think I care because...?"
            
            jane "Because despite everything, I know you're not cruel."
            jane "You're not like Justin. You never were."
            jane "That's why losing you was the biggest mistake of my life."
            
            $ jane_jealousy_level += 1
            $ jane_humiliation_level += 2
            
        "Look at what you threw away. *Show her photos with other girls*":
            label test_choice_a45tw:
            $ jane_love -= 10
            $ justin_hate += 20
            $ jane_jealousy_level += 3
            $ jane_humiliation_level += 2
            
            mc "Look at what you threw away."
            
            "I pull out my phone and show her photos."
            "Me with Nancy at the library. Lauren on our dates."
            "Emma in compromising positions. Gemmy and Ersa together."
            
            mc "This is my life now. These women actually appreciate me."
            mc "They don't lie about me or betray me."
            mc "They see value in what you discarded."
            
            $ update_character_state("jane", CharState.ANGRY)
            jane "You're... you're with all of them?"
            jane "How is that possible? You could barely talk to women when we were together!"
            
            mc "That's because you destroyed my confidence."
            mc "You made me feel worthless, inadequate."
            mc "Turns out, I just needed better women in my life."
            
            $ update_character_state("jane", CharState.AROUSED)
            jane "I... they're all beautiful."
            jane "Especially that pretty one... is that Emma? Justin's Emma?"
            
            mc "She's not Justin's anymore. Not after she experienced what real passion feels like."
            mc "Something you threw away for quick bathroom fucks with a cheater."

    $ update_character_state("jane", CharState.AROUSED)
    jane "You've changed so much."
    jane "You're confident, strong... sexy."
    jane "The way you're looking at me right now..."
    
    "She moves closer, her hand reaching for mine."
    "I can smell her perfume - the same one she always wore."
    "It brings back memories, both good and painful."
    
    jane "I was such a fool, [player_name]."
    jane "I had everything with you, and I threw it away for nothing."
    jane "Justin never loved me. He just wanted to win."
    jane "But you... you actually cared about me."
    
    menu:
        "I did care. Past tense. That person is gone now.":
            label test_choice_w60z1:
            $ jane_love -= 8
            $ justin_hate += 10
            
            $ update_character_state("mc", CharState.ANGRY)
            mc "I did care. Past tense. That person is gone now."
            mc "You killed him when you chose Justin."
            mc "The man standing here doesn't give a fuck about you."
            
            $ update_character_state("jane", CharState.SAD)
            jane "Don't say that. Please."
            jane "I can see it in your eyes. There's still something there."
            jane "We had three years together. That doesn't just disappear."
            
            mc "Watch it disappear."
            mc "You mean nothing to me now except a reminder of my worst mistakes."
            mc "Trusting you. Loving you. Believing in us."
            
            jane "Then why are you here?"
            jane "If I mean nothing, why did you come?"
            
            mc "Closure. And maybe revenge."
            mc "I want you to see what you lost. Feel what I felt."
            
        "We both made mistakes. But yours were unforgivable.":
            label test_choice_fe52u:
            $ win_sound()
            $ jane_love += 5
            # Mild confrontation
            
            mc "We both made mistakes. But yours were unforgivable."
            mc "I may have been passive, weak, too accommodating."
            mc "But I never betrayed you. Never humiliated you publicly."
            
            jane "You're right. God, you're so right."
            jane "I took your kindness for weakness."
            jane "Your love for granted."
            jane "And I'm paying for it now."
            
            mc "How are you paying for it?"
            mc "You seem fine to me."
            
            $ update_character_state("jane", CharState.SAD)
            jane "I'm not fine. I haven't been fine since I realized what I lost."
            jane "Every night, I think about you. About us."
            jane "About how different things could have been."
            
        "There's still something between us. I feel it too.":
            label test_choice_4n9jk:
            $ lose_sound()
            $ submissive_choices += 1
            $ jane_love += 3
            
            $ update_character_state("mc", CharState.SAD)
            mc "There's still something between us. I feel it too."
            mc "As much as I hate what you did, I can't deny that."
            
            $ update_character_state("jane", CharState.HAPPY)
            jane "Really? You still feel it?"
            jane "Oh, [player_name], I knew you couldn't forget what we had!"
            
            "She throws her arms around me."
            "For a moment, I'm transported back to better times."
            "Before the betrayal, the lies, the pain."
            
            jane "We could try again. Start over."
            jane "I'll make it up to you, I promise."
            jane "I'll tell everyone the truth about what happened."
            
            mc "It's not that simple, [girl_friend]."
            mc "You can't just erase what happened."

    hide jane
    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate
    
    bull_phone "What are you doing? Don't let her manipulate you!"
    bull_phone "She's playing the victim now, but she's the one who destroyed you!"
    bull_phone "Remember the plan. Make her pay for what she did."
    bull_phone "Or at least get something out of this meeting."
    
    hide bull
    show jane at jane_convo
    $ update_character_state("jane", CharState.AROUSED)
    with pixellate
    
    jane "You're thinking about him, aren't you? The voice?"
    jane "Justin told me about that too. Your phone friend."
    jane "He said you were going crazy, talking to yourself."
    
    mc "Justin doesn't know anything about me."
    mc "And neither do you anymore."
    
    jane "Then let me learn. Let me know the new you."
    jane "The confident, strong man you've become."
    jane "Show me what I missed out on."
    
    "Her hand slides down my chest."
    "Her intentions are becoming crystal clear."
    "She wants me. Whether from genuine desire or manipulation, I can't tell."
    
    $ update_character_state("jane", CharState.AROUSED)
    jane "I've thought about you every night since I left."
    jane "About how you used to touch me. How you made me feel."
    jane "Justin was rougher, more aggressive, but never satisfying."
    jane "He only cared about his own pleasure."
    
    menu:
        "Then you got exactly what you deserved.":
            label test_choice_c7lcf:
            $ jane_love -= 15
            $ justin_hate += 15
            
            mc "Then you got exactly what you deserved."
            mc "A selfish lover for a selfish woman."
            mc "You threw away someone who cared about your pleasure for that?"
            
            $ update_character_state("jane", CharState.ANGRY)
            jane "You're being cruel."
            
            mc "I learned from the best."
            mc "You taught me that caring about someone's feelings is weakness."
            mc "So I stopped caring. About you, specifically."
            
            $ update_character_state("jane", CharState.AROUSED)
            jane "This new attitude... it's actually kind of hot."
            jane "You never talked to me like this before."
            jane "You were always so eager to please, so accommodating."
            
            mc "And look where that got me."
            mc "Cheated on, humiliated, destroyed."
            mc "Never again."
            
            jane "Prove it."
            jane "Show me this new you. Show me what I missed out on."
            jane "Make me regret everything."
            
            if jane_love <= -20 and justin_hate >= 30 and previous_conquests >= 2:
                jump scene_18_angry_jane
            
        "You made your choice. Now live with the consequences.":
            label test_choice_28mw9:
            $ win_sound()
            $ jane_love += 5
            # Moderate confrontation
            
            mc "You made your choice. Now live with the consequences."
            mc "I'm not here to make you feel better about your mistakes."
            
            jane "I'm not asking you to."
            jane "I'm asking for a chance to make things right."
            jane "Or at least... to have one last moment together."
            jane "For closure, if nothing else."
            
            mc "Closure? Is that what you call this?"
            mc "Your hand on my chest, your body pressed against mine?"
            
            jane "Can you blame me for wanting you?"
            jane "Look at you now. You're everything I wanted you to become."
            jane "Strong, confident, desirable..."
            
            mc "I became this despite you, not because of you."
            mc "Your betrayal forced me to change or die."
            
            jane "Then let me see the full transformation."
            jane "Show me the man you've become."
            
            if jane_love >= 15:  # Balanced path
                jump scene_20_side_jane
                
        "Maybe we both need closure. Real closure.":
            label test_choice_hij2c:
            $ lose_sound()
            $ jane_love += 8
            $ submissive_choices += 1
            
            mc "Maybe we both need closure. Real closure."
            mc "Not just words, but... something final."
            
            $ update_character_state("jane", CharState.HAPPY)
            jane "Yes. That's exactly what I need."
            jane "One last time. To say goodbye properly."
            jane "To what we had, what we lost..."
            
            "She kisses me suddenly."
            "It's desperate, hungry, filled with regret and longing."
            "For a moment, I kiss her back, lost in familiar sensations."
            
            jane "Please, [player_name]. I need this."
            jane "I need to feel you again. To remember what real intimacy was like."
            jane "Before I ruined everything."
            
            if submissive_choices >= 3:
                $ witnessed_betrayal = True
                jump scene_21_betrayal

    "Suddenly, there's a knock at the door."
    "[girl_friend] freezes, her face going pale."
    
    jane "Oh no. No, no, no..."
    jane "He wasn't supposed to be here today!"
    
    mc "Who? Who's here?"
    
    "The door opens before she can answer."
    "Justin walks in like he owns the place."
    "His eyes immediately lock onto mine."
    
    jump justin_confrontation

label jane_prepare_meeting:
    
    scene home_afternoon
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    "I have a few hours before [girl_friend] arrives."
    "Time to prepare. Time to decide how I want this to go."
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    bull_phone "Smart move making her come to you."
    bull_phone "This is your territory. Your terms."
    bull_phone "Now, who should we invite over to make [girl_friend] jealous?"
    
    menu:
        "Nancy. She's been loyal from the start." if nancy_love >= 20:
            $ jane_jealousy_level += 2
            $ jane_humiliation_level += 2
            
            mc "Nancy. She's been loyal from the start."
            mc "And she's exactly the kind of girl [girl_friend] would never expect me to get."
            
            bull_phone "Perfect choice. Nancy's devotion will drive [girl_friend] crazy."
            bull_phone "Plus, Nancy mentioned something about a medical fantasy..."
            
            "I text Nancy:"
            mc "'Hey, want to come over? I have a situation and could use your support.'"
            
            "Her response is immediate:"
            outline "'Of course! Is everything okay? I'll be right there.'"
            
            mc "She's so different from [girl_friend]."
            mc "Actually cares about my wellbeing."
            
            jump nancy_support_scene
            
        "Lauren. Show [girl_friend] I can maintain real relationships.":
            label test_choice_fbhra:
            $ jane_jealousy_level += 2
            $ jane_humiliation_level += 2
            
            mc "Lauren. Show [girl_friend] I can maintain real relationships."
            mc "Not just hookups, but something meaningful."
            
            bull_phone "Interesting. The emotional angle."
            bull_phone "Show [girl_friend] what she gave up - not just sex, but connection."
            
            "I call Lauren, and she answers on the second ring."
            
            mc "Hey, Lauren. I need to tell you something."
            mc "[girl_friend]'s coming over tonight. She wants to talk."
            
            outline "There's a pause before Lauren responds."
            outline "'Are you okay? Do you need me there?'"
            
            mc "I'd like that. For support."
            
            jump lauren_support_scene
            
        "No one. I'll handle [girl_friend] alone.":
            label test_choice_sizel:
            
            mc "No one. I'll handle [girl_friend] alone."
            mc "This is between me and her."
            
            $ update_character_state("bull", CharState.ANGRY)
            bull_phone "Mistake. You're giving up psychological advantage."
            bull_phone "But fine. Your funeral."
            
            mc "It's not about games anymore."
            mc "It's about closure."
            
            jump jane_alone_meeting

label nancy_support_scene:
    
    "Nancy arrives within an hour, looking concerned."
    
    hide mc
    show nancy at nancy_convo
    $ update_character_state("nancy", CharState.NORMAL)
    with fade
    
    nancy "What's wrong? You sounded worried in your text."
    
    mc "My ex [girl_friend] is coming over. She wants to talk."
    mc "I wanted you here because... well..."
    
    $ update_character_state("nancy", CharState.HAPPY)
    nancy "You want her to see you've moved on?"
    nancy "That you have someone better now?"
    
    mc "Is that petty?"
    
    nancy "After what she did to you? Not at all."
    nancy "I'll be the best supportive girlfriend you could ask for."
    nancy "She'll eat her heart out."
    
    "Nancy kisses me deeply."
    "Her hands roam my body with familiar confidence."
    
    $ update_character_state("nancy", CharState.AROUSED)
    nancy "Actually... I have an idea."
    nancy "After you deal with [girl_friend], maybe we could spend some time together?"
    nancy "Just you and me, to celebrate your closure?"
    
    mc "That sounds... perfect actually."
    mc "Something to look forward to after this mess."
    
    nancy "Exactly. Now, let's make your ex regret everything."
    nancy "When she gets here, I'll be all over you."
    nancy "She needs to see what she lost."
    
    "We spend the next hour preparing."
    "Nancy helps me choose clothes that show off my improved physique."
    "She styles my hair, making sure I look my absolute best."
    
    nancy "There. You look incredible."
    nancy "[girl_friend]'s going to die when she sees you."
    nancy "Especially with me on your arm."
    
    "The doorbell rings."
    "Showtime."
    
    jump jane_meeting_with_nancy

label lauren_support_scene:
    
    "Lauren arrives looking beautiful but nervous."
    
    show lauren at lauren_convo
    hide mc
    stop music
    $ update_character_state("lauren", CharState.NORMAL)
    with fade
    
    lauren "So... [girl_friend]'s coming here?"
    lauren "The ex who destroyed your reputation?"
    
    mc "Yeah. She says she needs to talk."
    mc "Claims she has information about Justin."
    
    $ update_character_state("lauren", CharState.ANGRY)
    lauren "Justin. That bastard."
    lauren "He's been spreading new rumors about you, you know."
    lauren "About us. About our dates."
    lauren "Saying horrible things."
    
    mc "Like what?"
    
    lauren "That you're... compensating. That you're desperate."
    lauren "That any girl who dates you is settling."
    lauren "It made me so angry I almost confronted him myself."
    
    mc "Lauren..."
    
    $ update_character_state("lauren", CharState.HAPPY)
    lauren "But then I realized something."
    lauren "He's jealous. He's threatened by you."
    lauren "Because you're becoming something he never expected."
    
    "She takes my hand."
    
    lauren "You're kind, genuine, caring..."
    lauren "Everything Justin pretends to be but isn't."
    lauren "And [girl_friend] threw that away."
    
    mc "You really think that?"
    
    lauren "I know that."
    lauren "And when [girl_friend] sees us together, she'll know it too."
    lauren "She'll see what real affection looks like."
    
    "The doorbell rings."
    
    lauren "Ready for this?"
    
    mc "With you here? Yeah, I'm ready."
    
    jump jane_meeting_with_lauren

label jane_alone_meeting:
    
    "I spend the time until 8 PM preparing myself mentally."
    "Going over what I want to say, how I want this to go."
    "The doorbell rings exactly at 8."
    
    "I open the door to find [girl_friend] standing there."
    "She looks different - vulnerable, smaller somehow."
    
    hide mc
    show jane at jane_convo
    $ update_character_state("jane", CharState.SAD)
    with fade
    
    jane "Hi. Thank you for agreeing to see me."
    jane "Can I come in?"
    
    mc "Yeah. Come in."
    
    "She enters, looking around my apartment."
    "Taking in the changes since she was last here."
    
    jane "You've redecorated."
    jane "It looks good. More... mature."
    
    mc "I've changed a lot of things."
    mc "Not just the furniture."
    
    $ update_character_state("jane", CharState.NORMAL)
    jane "I can see that."
    jane "You look different. Good different."
    jane "Confident."
    
    "We sit on opposite ends of the couch."
    "The distance between us feels both too much and not enough."
    
    jane "I know you probably hate me."
    jane "And you have every right to."
    jane "But I need you to know the truth about what happened."
    
    jump jane_truth_revelation

label jane_meeting_with_nancy:
    
    "I open the door with Nancy draped on my arm."
    "[girl_friend]'s face immediately changes when she sees her."
    
    $ jane_humiliation_level += 2
    $ jane_jealousy_level += 5
    
    show jane at jane_left
    show nancy at nancy_right
    $ update_character_state("jane", CharState.ANGRY)
    $ update_character_state("nancy", CharState.HAPPY)
    with fade
    
    jane "Oh. You have... company."
    jane "I thought we were meeting alone."
    
    nancy "Hi [girl_friend]! I'm Nancy, [player_name]'s girlfriend."
    nancy "He told me all about you. The ex who cheated, right?"
    
    $ update_character_state("jane", CharState.ANGRY)
    jane "I... yes. That's me."
    jane "Though it's more complicated than that."
    
    nancy "Is it though?"
    nancy "You cheated with Justin, spread lies about [player_name], tried to destroy him."
    nancy "Seems pretty simple to me."
    
    mc "Nancy, it's okay. Let her in."
    mc "She came here to talk."
    
    "We move to the living room."
    "Nancy stays practically attached to me."
    "Her hand on my thigh, her body pressed against mine."
    
    $ jane_jealousy_level += 2
    
    jane "So... you two are together now?"
    
    nancy "Very together. He's amazing."
    nancy "Caring, passionate, incredible in bed..."
    nancy "Everything a girl could want."
    
    $ update_character_state("jane", CharState.SAD)
    jane "I... I know. I remember."
    
    nancy "Do you though?"
    nancy "Because from what I heard, you threw it all away for bathroom quickies with a cheater."
    
    jump jane_truth_revelation

label jane_meeting_with_lauren:
    
    "I open the door with Lauren beside me."
    "[girl_friend]'s eyes widen when she sees her."
    
    $ jane_humiliation_level += 2
    $ jane_jealousy_level += 5
    
    show jane at jane_left
    show lauren at lauren_right
    $ update_character_state("jane", CharState.NORMAL)
    $ update_character_state("lauren", CharState.NORMAL)
    with fade
    
    jane "Lauren? You're with Lauren now?"
    jane "But she's so... different from me."
    
    lauren "Yes, I am different."
    lauren "I actually appreciate him. Value him."
    lauren "Don't cheat on him with meathead football players."
    
    $ update_character_state("jane", CharState.SAD)
    jane "That's... fair."
    
    "We move inside, the tension thick."
    "Lauren holds my hand protectively."
    
    jane "How long have you two been together?"
    
    lauren "Long enough to know he's wonderful."
    lauren "Long enough to see past the lies you spread."
    lauren "Long enough to fall for him completely."
    
    $ jane_jealousy_level += 1
    
    mc "[girl_friend] came to talk about Justin."
    mc "Claims there's more to the story."
    
    lauren "There always is with cheaters."
    lauren "They always have excuses, justifications."
    lauren "But betrayal is betrayal."
    
    jump jane_truth_revelation

label jane_avoidance_path:
    
    scene university_afternoon
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    "I tried to avoid [girl_friend], focusing on my classes instead."
    "But of course, the universe has other plans."
    
    "I'm walking through campus when I hear her voice."
    
    jane "[player_name]! Wait!"
    
    "I turn to see [girl_friend] running toward me."
    "But she's not alone. Justin is with her."
    
    show jane at jane_left
    show justin at justin_right
    $ update_character_state("jane", CharState.NORMAL)
    $ update_character_state("justin", CharState.HAPPY)
    with fade
    
    justin "Well, well. If it isn't the campus legend himself."
    justin "The man who thinks he's some kind of player now."
    
    mc "Justin. Still following [girl_friend] around like a dog?"
    mc "Even after she dumped you?"
    
    $ update_character_state("justin", CharState.ANGRY)
    justin "She didn't dump me. We're working things out."
    justin "Right, babe?"
    
    $ update_character_state("jane", CharState.SAD)
    jane "Justin, please. I told you I needed to talk to him alone."
    
    justin "And I told you that's not happening."
    justin "This loser doesn't deserve your time."
    
    "A crowd is starting to gather."
    "Students sensing drama, pulling out their phones."
    
    menu:
        "She seems to disagree. Or she wouldn't be here.":
            label test_choice_ia68g:
            # Moderate confrontation
            $ justin_hate += 5
            
            mc "She seems to disagree. Or she wouldn't be here."
            mc "What's wrong, Justin? Afraid she'll realize her mistake?"
            
            justin "My mistake was not kicking your ass sooner."
            justin "Walking around campus like you're something special."
            justin "You're still the same pathetic loser who lost his girl to me."
            
            mc "Lost her? I'd say I dodged a bullet."
            mc "A cheating, lying bullet who can't keep a relationship."
            mc "How many girls have you fucked behind [girl_friend]'s back now?"
            
            $ update_character_state("jane", CharState.ANGRY)
            jane "What? Justin, what is he talking about?"
            
        "How many girls did you cheat on her with, Justin?":
            label test_choice_6zu5s:
            # Strong confrontation
            $ justin_humiliated = True
            
            mc "How many girls did you cheat on her with, Justin?"
            mc "Five? Ten? Did you lose count?"
            
            $ update_character_state("justin", CharState.ANGRY)
            justin "Shut your mouth!"
            
            mc "Emma told me everything."
            mc "How you only fuck her ass because you're scared of commitment."
            mc "How you treat her like a trophy, not a person."
            
            "The crowd murmurs. Emma's name carries weight."
            
            justin "You don't know what you're talking about!"
            justin "I'm the star here! Everyone wants to be me!"
            justin "I'm like a model... everyone wants to look like me!"
            
            menu:
                "You think you're a model?":
                    label test_choice_qibxv:
                    if justin_humiliated:
                        outline "Justin's ego is showing even while being exposed..."
                        outline "What do fashion models walk on?"
                        jump outfit_51_puzzle
                        label outfit_51_puzzle_success:
                            outline "His delusion is incredible even facing defeat!"
                        label outfit_51_puzzle_failure:
                            outline "Justin's self-image is completely detached from reality..."
                "Call Emma over to expose him":
                    label test_choice_mdgqv:
                    mc "Really? Should I call Emma over?"
            mc "Really? Should I call Emma over?"
            mc "Let her tell everyone how disappointing you are in bed?"
            mc "How you last maybe two minutes on a good day?"
            if emma_love >= 25:
                "Right on cue, Emma appears in the crowd."
                hide jane
                hide justin
                show emma at emma_convo
                $ update_character_state("emma", CharState.HAPPY)
                emma "He's not lying!"
                emma "Justin is terrible in bed! Selfish and quick!"
                emma "[player_name] made me cum harder than Justin ever could!"
                "The crowd explodes in laughter and shock."
        "*Say nothing and try to walk away*":
            label test_choice_2xbl6:
            $ lose_sound()
            $ submissive_choices += 2
            "I try to walk past them, avoiding conflict."
            "But Justin blocks my path."
            justin "Where do you think you're going?"
            justin "We're not done here."
            "He shoves me hard."
            "I stumble but keep my balance."
            jane "Justin, stop it!"
            justin "No! This loser needs to learn his place!"
            justin "Walking around campus like he's somebody now."
            justin "Dating my leftovers, thinking he's special."
    if gym_trap_success == True:
        menu:
            "Take a swing at Justin":
                label test_choice_42mqv:
                $ justin_humiliated = True
                $ justin_hate += 25
                "I've had enough."
                "All the training, all the growth, it comes down to this."
                "I throw a perfect right hook."
                "It connects with Justin's jaw with a satisfying crack."
                "He goes down hard, crashing to the ground."
                "The crowd gasps, then some start cheering."
                $ update_character_state("justin", CharState.ANGRY)
                justin "You... you hit me!"
                justin "You're dead!"
                "He tries to get up but stumbles."
                "Blood drips from his split lip."
                mc "That's for everything you did."
                mc "For [girl_friend], for the lies, for the humiliation."
                mc "We're even now."
                $ update_character_state("jane", CharState.AROUSED)
                jane "[player_name]... that was..."
                "She's looking at me with something like awe."
                "Like she's seeing me for the first time."
                # Justin's delusion outfit after being defeated
                if justin_humiliated:
                    outline "Justin is on the ground but still thinks he's the hero..."
                    outline "What's his level of self-awareness after this defeat?"
                    jump outfit_53_puzzle
                    label outfit_53_puzzle_success:
                        outline "Even bleeding on the ground, he thinks he's winning!"
                        outline "His delusion is truly complete!"
                    label outfit_53_puzzle_failure:
                        outline "Justin's delusion is strong even in defeat..."
            "Let him make the first move":
                label test_choice_dhtr2:
                "I stand my ground, ready."
                "Justin swings wildly."
                "But I dodge easily - the gym training paid off."
                "He stumbles past me, off balance."
                "The crowd laughs."
                justin "Stand still and fight!"
                mc "Why? You're doing fine embarrassing yourself."
                mc "Just like you embarrassed yourself with every girl you cheated with."
                mc "What are you going to do now, surf away from your problems?"
                menu:
                    "What do surfers ride to escape?":
                        label test_choice_gc0wh:
                        if justin_humiliated:
                            outline "Justin always runs from his problems..."
                            outline "What do surfers ride to get away?"
                            jump outfit_54_puzzle
                            label outfit_54_puzzle_success:
                                outline "But every wave eventually crashes on the shore!"
                            label outfit_54_puzzle_failure:
                                outline "Justin's escape attempts are pathetic..."
                    "Keep fighting":
                        label test_choice_pae6q:
                        mc "Just keep embarrassing yourself, Justin."
    else:
        "Justin shoves me again, harder this time."
        "I fall backward, landing hard."
        "The crowd laughs and jeers."
        justin "See? Still a weakling."
        justin "All that pretending to be tough, but you're still nothing."
    jump jane_truth_revelation

label jane_conditional_meeting:
    
    scene home_afternoon
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    "[girl_friend] agreed to my terms."
    "She's sending a written confession of everything."
    "My phone buzzes with her message."
    
    outline "'[player_name], here's my confession as requested:'"
    outline "'I, [girl_friend], admit to the following:'"
    outline "'1. I cheated on [player_name] with Justin while we were together.'"
    outline "'2. I spread false rumors about him being inadequate and pathetic.'"
    outline "'3. These rumors were lies born from my own guilt and Justin's manipulation.'"
    outline "'4. [player_name] was a caring, attentive partner who deserved better.'"
    outline "'5. I destroyed his reputation to hide my own shameful behavior.'"
    outline "'There's more I need to tell you in person. Please.'"
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.HAPPY)
    with pixellate
    
    bull_phone "Perfect! You have it in writing!"
    bull_phone "Post this online and clear your name completely!"
    
    mc "Not yet. I want to hear what else she has to say."
    mc "Then I'll decide what to do with this confession."
    
    bull_phone "You're learning. Good."
    bull_phone "Keep the leverage until you get everything you want."

    stop music fadeout 1.0
    
    "An hour later, [girl_friend] arrives."
    
    hide bull
    hide mc
    show jane at jane_convo
    $ update_character_state("jane", CharState.SAD)
    with fade
    
    jane "Thank you for giving me this chance."
    jane "I sent the confession. Did you receive it?"
    
    mc "I did. But you said there's more?"
    
    jane "Yes. About Craig, Matthews, and the others."
    jane "They're all in on it with Justin."
    
    mc "In on what?"
    
    jane "A bet. A competition."
    jane "Who could fuck the most girls, steal the most girlfriends."
    jane "You were a target because you had me."
    jane "And I was a prize because I was considered 'high value.'"
    
    mc "You're telling me this was all a game to them?"
    
    jane "Everything. Justin targeted me specifically to hurt you."
    jane "Craig spread rumors to make you seem weak."
    jane "Matthews used his position to seduce your female friends."
    jane "It was coordinated. Planned."
    
    $ update_character_state("mc", CharState.ANGRY)
    mc "And you fell for it."
    
    $ update_character_state("jane", CharState.SAD)
    jane "I did. I was vain and stupid and I fell for it."
    jane "But now I want to make it right."
    jane "I want to help you expose them all."
    
    jump jane_truth_revelation

label jane_truth_revelation:
    
    scene home_night
    show jane at jane_convo
    $ update_character_state("jane", CharState.SAD)
    with fade
    
    jane "The truth is uglier than you know."
    jane "Justin didn't just seduce me. He had help."
    jane "Craig, Matthews, even some of your supposed friends."
    jane "They all worked together to destroy you."
    
    mc "Why? What did I ever do to them?"
    
    jane "You had something they wanted. Me."
    jane "And you were happy. Genuinely happy."
    jane "That threatened them somehow."
    
    $ update_character_state("jane", CharState.ANGRY)
    jane "Justin showed me fake evidence of you cheating."
    jane "Messages, photos, all fabricated."
    jane "Craig backed up his lies, said he saw you with other girls."
    jane "Matthews hinted that you were failing classes because you were distracted by 'extracurriculars.'"
    
    mc "And you believed them over me?"
    
    $ update_character_state("jane", CharState.SAD)
    jane "I was insecure. You were becoming distant because of your studies."
    jane "Less time for dates, less attention..."
    jane "When they showed me the 'evidence,' it seemed to explain everything."
    
    menu:
        "Your insecurity destroyed us. Own that.":
            label test_choice_kt303:
            $ jane_love -= 8
            $ justin_hate += 10
            
            mc "Your insecurity destroyed us. Own that."
            mc "Don't blame them entirely. You made the choice."
            mc "You chose to believe lies over three years of love."
            
            jane "You're right. I own that."
            jane "I let my insecurities override my judgment."
            jane "And I've been paying for it ever since."
            
            mc "How exactly have you been paying?"
            mc "You got the popular boyfriend you wanted."
            
            jane "Who cheated constantly. Who used me."
            jane "Who only saw me as a trophy he won from you."
            jane "I traded real love for an illusion."
            
        "They played us both. We were both victims.":
            label test_choice_c93q6:
            $ win_sound()
            $ jane_love += 5
            
            mc "They played us both. We were both victims."
            mc "You of manipulation, me of conspiracy."
            mc "But you still chose to hurt me publicly."
            
            jane "I know. That was pure cruelty."
            jane "I wanted to hurt you like I thought you hurt me."
            jane "But multiplied by ten."
            
            mc "Well, congratulations. You succeeded."
            mc "I was destroyed. Completely broken."
            
            jane "I know. I saw the videos Justin took."
            jane "You crying, alone, destroyed..."
            jane "It broke my heart when I realized what I'd done to an innocent man."
            
        "It doesn't matter anymore. What's done is done.":
            label test_choice_h97c8:
            $ lose_sound()
            $ submissive_choices += 1
            
            mc "It doesn't matter anymore. What's done is done."
            mc "We can't change the past."
            
            jane "But we can change the future."
            jane "I want to make this right."
            jane "I'll tell everyone the truth. Clear your name."
            
            mc "Why now? Why do you suddenly care?"
            
            jane "Because I see what I lost."
            jane "And what you've become despite my attempts to destroy you."
            jane "You're stronger than ever."

    $ update_character_state("jane", CharState.AROUSED)
    jane "Can I be honest about something?"
    jane "Seeing you now, confident and strong..."
    jane "It's incredibly attractive."
    
    "She moves closer on the couch."
    "Her hand finds my thigh."
    
    jane "The way you stood up to Justin today..."
    jane "Or how you made me come to you..."
    jane "You never had that dominance before."
    
    mc "I had to develop it. Adapt or die."
    mc "Your betrayal forced me to evolve."
    
    jane "And you evolved magnificently."
    jane "The girls you've been with... they're lucky."
    jane "I hear the rumors now. The real ones."
    jane "How you satisfied Emma better than Justin ever could."
    jane "How devoted Nancy and Lauren are to you."
    
    $ jane_jealousy_level += 2
    
    jane "It makes me jealous. Insanely jealous."
    jane "Knowing other women are experiencing what I threw away."
    
    menu:
        "Good. I want you to suffer like I did.":
            label test_choice_rqt3i:
            $ jane_love -= 15
            $ justin_hate += 20
            
            mc "Good. I want you to suffer like I did."
            mc "Every night, think about what you lost."
            mc "While I'm with women who actually appreciate me."
            
            $ update_character_state("jane", CharState.AROUSED)
            jane "I do suffer. Every single night."
            jane "I touch myself thinking about you."
            jane "About what we had, what we could have had."
            
            mc "That's pathetic."
            
            jane "I know. But I can't help it."
            jane "You were the best lover I ever had."
            jane "Justin was selfish, quick, unsatisfying."
            jane "I faked every orgasm with him."
            jane "Now I'm working part-time at a coffee shop to pay bills..."
            jane "Serving people coffee all day... it's humbling..."
            
            menu:
                "What's the most important part of morning service?":
                    label test_choice_dt1y0:
                    if jane_humiliation_level >= 4:
                        jane "I... I serve coffee every morning now..."
                        jane "What drink do I make that brightens people's day?"
                        jump outfit_33_puzzle
                        label outfit_33_puzzle_success:
                            jane "I even have the cafe uniform... a constant reminder of how far I've fallen..."
                            jane "Maybe that's what I deserve... to serve others..."
                        label outfit_33_puzzle_failure:
                            jane "My life has become about serving others now..."
                "You deserve better than serving coffee":
                    label test_choice_8c3es:
                    jane "Do I though? After what I did to you?"
            mc "While I'm giving real ones to better women."
            jane "Prove it."
            jane "Show me what I missed out on."
            jane "Make me regret everything physically."
            if jane_love <= -20 and justin_hate >= 30 and previous_conquests >= 2:
                jump scene_18_angry_jane
                
        "Jealousy doesn't suit you.":
            label test_choice_2v4wy:
            $ win_sound()
            $ jane_jealousy_level += 5
            $ jane_love += 5
            
            mc "Jealousy doesn't suit you."
            mc "You were always above such petty emotions."
            mc "Or so you pretended."
            
            jane "I was never above anything."
            jane "I was just good at hiding my insecurities."
            jane "But seeing you with other women..."
            jane "It awakens something primal in me."
            
            mc "What do you want from me, [girl_friend]?"
            
            jane "One more night."
            jane "To remind myself what I lost."
            jane "To properly say goodbye to us."
            
            if jane_love >= 15:  # Balanced path
                jump scene_20_side_jane
                
        "The past is the past. I've moved on.":
            label test_choice_i1l8w:
            $ lose_sound()
            $ submissive_choices += 2
            
            mc "The past is the past. I've moved on."
            mc "You should too."
            
            jane "Have you though?"
            jane "Really moved on?"
            jane "Because you're here, talking to me."
            
            mc "Closure. Nothing more."
            
            jane "Liar."
            jane "I can see it in your eyes."
            jane "You still want me."

    "The tension between us is electric."
    "Part of me wants to throw her out."
    "Part wants to throw her on the bed."
    "The Bull Phone vibrates insistently."
    
    hide jane
    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate
    
    bull_phone "What are you waiting for?!"
    bull_phone "This is your chance!"
    bull_phone "Make her pay! Make her beg!"
    bull_phone "Show her what she threw away!"
    
    hide bull
    show jane at jane_convo
    $ update_character_state("jane", CharState.AROUSED)
    with pixellate
    
    jane "You're thinking about it, aren't you?"
    jane "What it would be like to have me again."
    jane "To fuck me with all that anger and passion."
    jane "To make me scream your name like I used to."
    
    "She stands up, slowly unbuttoning her shirt."
    
    jane "I'm not wearing anything underneath."
    jane "I came prepared to beg if necessary."
    jane "To do whatever it takes for forgiveness."
    jane "Or at least... for one last taste of what we had."
    
    if submissive_choices >= 3 or emma_love <= 0:
        "Suddenly, the door bursts open."
        "Justin stands there, grinning maliciously."
        
        $ witnessed_betrayal = True
        jump scene_21_betrayal
    elif nancy_love >= 30 and nancy_key_question_passed == True:
        "My phone buzzes. It's Nancy."
        outline "'Hey, want to hang out? I'm free tonight.'"
        
        menu:
            "Tell [girl_friend] to leave and go to Nancy":
                label test_choice_lvo09:
                mc "You need to go. Now."
                mc "I have somewhere to be. Someone worth my time."
                
                jane "What? But we were just-"
                
                mc "We were nothing. We are nothing."
                mc "Now leave before I post your confession online."
                
                # Nancy gets a good ending instead
                # Good outcome
                jump nancy_celebration_scene
                
            "Ignore Nancy and continue with [girl_friend]":
                label test_choice_25otv:
                $ jane_love += 10
                $ jane_jealousy_level += 10
                $ win_sound()
                "I silence my phone."
                "Nancy can wait. This needs to be finished."
                
                if jane_love <= -20 and justin_hate >= 30:
                    jump scene_18_angry_jane
                else:
                    jump scene_20_side_jane
    else:
        if jane_anger_points >= 4 and revenge_points >= 6 and previous_conquests >= 2:
            jump scene_18_angry_jane
        elif jane_love >= 10 and jane_confrontation_score >= 5:
            jump scene_20_side_jane
        else:
            jump scene_21_betrayal

label justin_confrontation:
    
    show justin at justin_convo
    hide jane
    $ update_character_state("justin", CharState.HAPPY)
    with fade
    
    justin "Well, well. The cuck and the whore together again."
    justin "How touching."
    
    $ update_character_state("jane", CharState.ANGRY)
    jane "Justin! I told you not to come here!"
    
    justin "And I told you that you're mine."
    justin "Even after our 'break,' you always come back."
    justin "Don't you, babe?"
    
    $ update_character_state("mc", CharState.ANGRY)
    mc "She's not your anything anymore."
    mc "From what I hear, you couldn't keep it in your pants."
    
    $ update_character_state("justin", CharState.ANGRY)
    justin "Like you're any better?"
    justin "Playing with my Emma? Nancy the bookworm?"
    justin "Lauren the social reject?"
    
    mc "They're all better than you deserve."
    mc "And they all say I'm better than you in every way."
    
    justin "Bullshit!"
    
    # Grant Justin destruction achievement if conditions met
    python:
        if emma_love >= 40 and justin_hate >= 30:
            grant_achievement("JUSTIN_DESTROYED")
    
    menu:
        "Ask Emma yourself. She'll tell you the truth.":
            label test_choice_47tfe:
            $ justin_humiliated = True
            
            mc "Ask Emma yourself. She'll tell you the truth."
            mc "How I satisfied her in ways you never could."
            mc "How I actually cared about her pleasure."
            
            justin "Emma would never-"
            
            mc "Touch me? Fuck me? Beg for more?"
            mc "She did all three. Enthusiastically."
            
            if emma_love >= 25:
                mc "She even said she loves me."
                mc "That I'm everything you're not."
                
                $ update_character_state("justin", CharState.ANGRY)
                justin "You're lying!"
                
                mc "Call her. Right now."
                mc "Put her on speaker. Let's see who's lying."
                
                "Justin hesitates, then pulls out his phone."
                "Emma answers on the second ring."
                
                outline "'Justin? What do you want?'"
                
                justin "Babe, tell this loser you never touched him."
                
                outline "'...[player_name]'s there?'"
                outline "'Actually, Justin, he's telling the truth.'"
                outline "'He's incredible. Better than you ever were.'"
                outline "'I'm done pretending otherwise.'"
                
                "She hangs up."
                "Justin's face is pure shock."
                
        "[girl_friend] knows the truth. She's had both of us.":
            label test_choice_at0uc:
            $ jane_jealousy_level += 1
            
            mc "[girl_friend] knows the truth. She's had both of us."
            mc "Why don't you ask her who was better?"
            
            "Both Justin and [girl_friend] freeze."
            
            $ update_character_state("jane", CharState.AROUSED)
            jane "I... that's not..."
            
            mc "Go ahead, [girl_friend]. Tell him."
            mc "Tell him how you faked it with him."
            mc "How unsatisfying he was compared to me."
            
            justin "[girl_friend]?"
            
            jane "..."
            jane "[player_name] was better. In every way."
            jane "You were selfish, quick, boring."
            jane "He actually cared if I enjoyed it."
            
        "I don't need to prove anything to you.":
            label test_choice_ggbcu:
            $ lose_sound()
            $ submissive_choices += 1
            
            mc "I don't need to prove anything to you."
            mc "Your opinion means nothing."
            
            justin "Because you can't prove it!"
            justin "You're still the same weak loser!"
            
            "He turns to [girl_friend]."
            
            justin "Come on, babe. We're leaving."
            justin "You don't need to waste time with this nobody."

    $ update_character_state("jane", CharState.ANGRY)
    jane "No."
    
    justin "What?"
    
    jane "I said no, Justin."
    jane "I'm done being controlled by you."
    jane "Done with your lies, your cheating, your manipulation."
    
    justin "You'll come crawling back. You always do."
    
    jane "Not this time."
    jane "I choose [player_name]."
    
    "The room goes silent."
    "Everyone processes what was just said."
    
    $ update_character_state("mc", CharState.NORMAL)
    mc "[girl_friend]..."
    
    jane "I know I don't deserve another chance."
    jane "But I'm choosing you anyway."
    jane "If you'll have me."
    
    if justin_humiliated == True:
        justin "This is bullshit!"
        justin "You're all crazy!"
        
        "He storms out, defeated."
        hide justin
        show jane at jane_convo
        with fade
        "His reign of terror finally over."
        
        $ update_character_state("jane", CharState.AROUSED)
        jane "Now, where were we?"
        jane "Oh right, I was apologizing..."
        jane "With my body."
        
        if jane_love <= -20 and justin_hate >= 30:
            jump scene_18_angry_jane
        else:
            jump scene_20_side_jane
    else:
        justin "Fine. But this isn't over."
        justin "I'll destroy both of you."
        justin "Everyone will know what pathetic losers you are."
        
        "He leaves, slamming the door."
        
        jump jane_final_choice

label jane_final_choice:
    
    $ update_character_state("jane", CharState.SAD)
    jane "I meant what I said."
    jane "I choose you. If you'll let me."
    jane "I want to move forward with grace... with elegance..."
    jane "Like a dancer choosing her perfect partner..."
    
    menu:
        "What does graceful movement mean to you?":
            label test_choice_xfo12:
            if jane_love >= 10:
                jane "It's about precision... beauty in motion..."
                jane "What do dancers display with every movement?"
                jump outfit_32_puzzle
                label outfit_32_puzzle_success:
                    jane "I actually took ballet when I was younger..."
                    jane "I still have my old ballerina outfit... it represents elegance and discipline..."
                    jane "Maybe... maybe I need to find that grace again..."
                label outfit_32_puzzle_failure:
                    jane "I want to move forward beautifully, but it's hard..."
        "Actions matter more than words":
            label test_choice_jjbz4:
            jane "You're right. I need to prove myself through actions."
    menu:
        "Prove it. Show me you've really changed.":
            label test_choice_uckev:
            # Moderate confrontation
            mc "Prove it. Show me you've really changed."
            mc "Words mean nothing from you anymore."
            jane "Then let me use actions."
            jane "Let me show you physically how sorry I am."
            jane "How much I've missed you."
            jane "How much I need you."
            if previous_conquests >= 2:
                jump scene_18_angry_jane
            else:
                jump scene_20_side_jane
                
        "It's too late for us. But we can have closure.":
            label test_choice_1nebt:
            $ win_sound()
            $ jane_love += 5
            
            mc "It's too late for us. But we can have closure."
            mc "One last time, to say goodbye properly."
            
            jane "I'll take whatever you're willing to give."
            jane "Even if it's just goodbye."
            
            jump scene_20_side_jane
            
        "I can't do this. Please leave.":
            label test_choice_wiyjh:
            $ lose_sound()
            $ submissive_choices += 3
            $ witnessed_betrayal = True
            
            mc "I can't do this. Please leave."
            mc "It's too much. Too painful."
            
            jane "Please, don't push me away."
            jane "Not when we're so close to..."
            
            "The door opens again."
            "Justin returns with a cruel smile."
            
            jump scene_21_betrayal

# Scene 18: Angry Missionary with [girl_friend]
label scene_18_angry_jane:
    
    scene black
    show scene_18
    stop music fadeout 1.0
    with fade
    
    $ persistent.scene_18 = True
    
    "I grab [girl_friend] roughly, all my anger and frustration boiling over."
    $ play_grab_sound()
    "She gasps as I throw her onto the bed."
    $ play_woman_pleasure_sound()
    
    mc "You want to see what you missed?"
    mc "Fine. I'll show you exactly what you threw away."
    $ play_man_pleasure_sound()
    
    jane "Yes! Show me!"
    jane "Punish me for what I did!"
    $ play_woman_pleasure_sound()
    
    "I rip her clothes off without ceremony."
    $ play_grab_sound()
    "No tenderness, no foreplay."
    "Just raw, angry passion."
    
    mc "This is what you gave up for Justin."
    mc "For quick bathroom fucks with a cheater."
    
    "I enter her roughly, making her cry out."
    $ play_penetration_sound()
    $ play_vagina_insertion_sound()
    
    jane "Oh god! You're so much bigger than I remembered!"
    jane "So much more aggressive!"
    $ play_woman_pleasure_sound()
    
    mc "You think you're such a stud now?"
    mc "Think you can just waltz back into my life?"
    
    jane "No! I know I fucked up!"
    jane "I know I don't deserve this!"
    $ play_woman_pleasure_sound()
    
    "I pound into her mercilessly."
    "Every thrust is payback for the pain she caused."
    $ play_penetration_sound()
    
    mc "Better than Justin ever was."
    mc "I learned from the best teachers."
    mc "Nancy, Lauren, Emma... they all taught me things."
    $ play_man_pleasure_sound()
    
    jane "Don't! Don't talk about them!"
    jane "I'm so jealous! So fucking jealous!"
    $ play_woman_pleasure_sound()
    
    mc "Good! Feel what I felt!"
    mc "When you were fucking him while we were together!"
    $ play_man_pleasure_sound()
    
    "Her pussy clenches around me."
    "Despite the anger, or maybe because of it, she's incredibly wet."
    $ play_vagina_insertion_sound()
    
    jane "I'm sorry! I'm so sorry!"
    jane "I was stupid! So stupid!"
    jane "You're amazing! Better than anyone!"
    $ play_woman_pleasure_sound()
    
    mc "Empty words from an empty person."
    
    "I fuck her harder, making the bed shake."
    "Her moans turn to screams of pleasure."
    $ play_penetration_sound()
    
    jane "I'm cumming! Oh god, I'm cumming!"
    jane "I never came like this with Justin!"
    jane "Never! Not once!"
    $ play_woman_pleasure_sound()
    
    mc "Because he never cared about anything but himself."
    mc "Just like you!"
    
    jane "Yes! I was selfish!"
    jane "But please! Don't stop!"
    jane "Make me yours again!"
    
    mc "You're not mine. You're just another conquest."
    mc "Another notch on my belt."
    mc "Just like I was to Justin."
    
    "The truth of it makes her sob even as she orgasms."
    "Tears stream down her face."
    
    jane "I love you! I never stopped!"
    jane "Please! Forgive me!"
    $ play_woman_pleasure_sound()
    
    mc "Too late for forgiveness."
    mc "This is goodbye, [girl_friend]."
    mc "The last time you'll ever have me."
    $ play_man_pleasure_sound()
    
    mc "I'm going to fill you up one last time!"
    jane "Yes! Fill me completely!"
    
    scene scene_18_final
    with fade
    
    "I finish inside her with a growl."
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    "Filling her with my cum one final time."
    "Then I pull out and get dressed without a word."
    
    scene home_night
    show mc at mc_convo
    $ update_character_state("mc", CharState.NORMAL)
    with fade
    
    mc "Get out."
    mc "We're done here."
    
    hide mc
    show jane at jane_convo
    $ update_character_state("jane", CharState.SAD)
    
    jane "Please... don't end it like this..."
    
    mc "You ended it when you chose Justin."
    mc "This was just closure."
    mc "Now leave."
    
    "She gathers her clothes, crying."
    "At the door, she turns one last time."
    
    jane "I'll always love you."
    jane "And I'll always regret losing you."
    
    mc "Good."
    
    "She leaves."
    "And with her goes the last of my attachment to the past."
    
    # Best outcome achieved
    jump episode_5_ending


# Scene 20: Side Position with [girl_friend] (Mixed Feelings)
label scene_20_side_jane:
    
    scene black
    show scene_20
    stop music fadeout 1.0
    with fade
    
    $ persistent.scene_20 = True
    
    "We end up in bed, but it's different from before."
    "Not angry, not passionate, just... complicated."
    
    jane "I don't know how to feel about this."
    
    mc "Neither do I."
    mc "Part of me hates you. Part still loves you."
    
    "We're on our sides, facing each other."
    "The position is intimate but guarded."
    
    jane "Is this goodbye?"
    
    mc "I think so."
    mc "We can't go back. Too much has happened."
    
    "I enter her slowly, gently."
    $ play_penetration_sound()
    "She gasps, then sighs."
    $ play_woman_pleasure_sound()
    
    jane "You've learned new things."
    jane "You're different. More confident."
    
    mc "I had to become someone else."
    mc "The person you left wouldn't have survived."
    
    "We move together slowly."
    "Like we're trying to memorize the feeling."
    $ play_vagina_insertion_sound()
    
    jane "I really did love you."
    jane "In my own broken way."
    
    mc "I know. And I loved you."
    mc "But love wasn't enough."
    
    jane "Do you love them? The others?"
    jane "Nancy, Lauren, Emma?"
    
    mc "In different ways, yes."
    mc "They see me for who I am now."
    mc "Not who I was with you."
    
    "She starts crying even as we continue."
    "Tears of regret, loss, and strangely, relief."
    
    jane "I'm glad you found them."
    jane "Glad you became this person."
    jane "Even if I can't be part of it."
    
    mc "This is closure, [girl_friend]."
    mc "We both needed this."
    
    jane "Yes. To say goodbye properly."
    jane "To what we were. What we had."
    
    "We climax together, quietly."
    
    scene scene_20_final
    with fade
    
    $ play_cum_sound()
    "No grand declarations or screams."
    "Just a soft, sad ending to our story."
    
    scene home_night
    show jane at jane_convo
    $ update_character_state("jane", CharState.SAD)
    with fade
    
    jane "Thank you. For this."
    jane "For letting me say goodbye."
    jane "I've shown you everything... my most vulnerable state..."
    jane "Completely open, nothing hidden..."
    
    menu:
        "What state shows complete vulnerability?":
            label test_choice_fyb3i:
            if jane_humiliation_level >= 10:
                jane "You've seen all of me... what word describes total exposure?"
                jump outfit_35_puzzle
                label outfit_35_puzzle_success:
                    jane "Stripped of all pretense... all pride..."
                    jane "Maybe that's what I needed... to be completely honest for once..."
                label outfit_35_puzzle_failure:
                    jane "I've never been this vulnerable with anyone..."
        "This is enough vulnerability":
            label test_choice_c113s:
            jane "You're probably right..."
    mc "Be well, [girl_friend]."
    mc "Try to be better for the next person."
    jane "I will. You taught me that."
    jane "By becoming better yourself."
    "She leaves quietly."
    "No drama, no tears."
    "Just the end of a chapter."
    # Good outcome achieved
    jump episode_5_ending

# Scene 21: Ultimate Betrayal (Failure)
label scene_21_betrayal:
    
    scene black
    stop music fadeout 1.0
    with fade
    
    "I arrive at [girl_friend]'s place as she requested."
    "But something feels wrong."
    "I hear sounds from inside. Familiar sounds."
    
    scene black
    show scene_21
    with fade
    
    $ persistent.scene_21 = True
    
    "Through the window, I see them."
    "[girl_friend] and Justin. Fucking."
    "She sees me watching and smiles cruelly."
    
    jane "Oh look, we have an audience."
    jane "Just like old times, right [player_name]?"
    
    justin "Thanks for warming her up for me all those years, loser."
    justin "She came crawling back, just like I said."
    
    "I stand frozen, unable to move."
    "It's happening again."
    "The same betrayal, the same humiliation."
    
    jane "Did you really think I wanted you back?"
    jane "This was Justin's idea. To break you completely."
    jane "And look, it worked!"
    
    justin "Get a good look, cuck."
    justin "This is where you belong."
    justin "Watching real men take what you can't keep."
    
    "They continue, making exaggerated sounds."
    "Performing for my humiliation."
    
    show bull at bull_convo
    $ update_character_state("bull", CharState.ANGRY)
    with pixellate
    
    bull_phone "Well, this is exactly what you deserve."
    bull_phone "You had every opportunity and you wasted them all."
    bull_phone "You're exactly where you started."
    bull_phone "A cuckold. A loser. A nothing."
    
    "The phone goes dead."
    "My last support, gone."
    
    justin "Still there, loser?"
    justin "Good. Watch me claim what you never could."
    justin "Watch me own her like you never did."
    
    jane "He's so much better than you!"
    jane "Bigger, stronger, everything!"
    jane "I was stupid to even pretend otherwise!"
    
    justin "I'm close, [girl_friend]. Going to fill you up!"
    jane "Yes! Fill me! Show him what a real man gives me!"
    
    scene scene_21_final
    with fade
    
    justin "There! Take all of it!"
    $ play_cum_sound()
    jane "YESSSS! So much cum! This is what I needed!"
    
    "I finally find the strength to leave."
    "But the damage is done."
    "I'm broken. Again. Permanently this time."
    
    # Worst outcome
    $ witnessed_betrayal = True
    jump episode_5_ending

label nancy_celebration_scene:
    
    "After [girl_friend] leaves, I immediately call Nancy."
    "She picks up on the first ring."
    
    mc "It's done. [girl_friend]'s gone."
    nancy "Thank god. How are you feeling?"
    mc "Free. Finally free."
    nancy "I'm coming over right now. We have some celebrating to do."
    
    scene black
    with fade
    
    "Twenty minutes later, Nancy arrives."
    
    scene home_night
    show nancy at nancy_convo
    $ update_character_state("nancy", CharState.HAPPY)
    with fade
    
    nancy "You did it. You actually stood up to her."
    nancy "I'm so proud of you, [player_name]."
    
    mc "I couldn't have done it without your support."
    mc "Having you there gave me the strength I needed."
    
    $ update_character_state("nancy", CharState.AROUSED)
    nancy "Now it's time for that celebration I promised you."
    nancy "Just you and me. No [girl_friend], no drama, no bullshit."
    nancy "Tonight is about us."
    
    "Nancy steps closer, her eyes filled with desire."
    "Her hands trace my chest as she looks up at me."
    
    nancy "You've been through so much..."
    nancy "Let me take care of you tonight."
    nancy "Let me show you what real devotion looks like."
    
    mc "Nancy..."
    
    nancy "Shh. Just relax and let me worship you."
    nancy "You deserve to be treated like a king."
    
    "She gently guides me to sit on the edge of the bed."
    "Her touch is electric, sending shivers through my body."
    
    nancy "I've been thinking about this all day."
    nancy "About how I wanted to celebrate your freedom with you."
    
    "Nancy kneels before me, her hands running up my thighs."
    "She looks up at me with pure adoration."
    
    nancy "You're so strong, so confident now."
    nancy "Nothing like what [girl_friend] said you were."
    nancy "She was such a fool to let you go."
    
    scene black
    show scene_7_initial
    stop music fadeout 1.0
    with fade
    
    outline "Nancy positions herself perfectly between my legs."
    outline "Her hands grip my thighs firmly, holding me steady."
    outline "The look in her eyes is pure hunger and devotion."
    
    nancy "Mmm... I've been craving this all day."
    $ play_woman_pleasure_sound()
    
    mc "God, Nancy... your mouth feels incredible."
    $ play_man_pleasure_sound()
    
    nancy "Mhmm..."
    $ play_woman_pleasure_sound()
    
    scene black
    show scene_7
    with fade
    
    $ persistent.scene_7 = True
    
    outline "Nancy holds my legs firmly as I start to take control."
    outline "Her dedication is absolute, letting me set the pace exactly how I want."
    outline "Every movement, every rhythm - she follows my lead perfectly."
    
    mc "That's it, Nancy. Just like that."
    $ play_man_pleasure_sound()
    
    nancy "Mmmph..."
    $ play_woman_pleasure_sound()
    
    mc "You're so good at this. So eager to please."
    mc "This is what I needed after dealing with [girl_friend]'s drama."
    $ play_man_pleasure_sound()
    
    outline "I guide the rhythm, feeling completely in control."
    outline "Nancy's hands squeeze my thighs, holding on as I increase the intensity."
    outline "Her eyes water slightly, but she never breaks eye contact."
    outline "Pure devotion and lust burning in her gaze."
    
    nancy "Mmm... mmmph..."
    $ play_woman_pleasure_sound()
    
    mc "You're perfect, Nancy. Absolutely perfect."
    mc "[girl_friend] could never compare to this."
    $ play_man_pleasure_sound()
    
    outline "The combination of her skilled mouth and my complete control is overwhelming."
    outline "I can feel myself approaching the edge."
    outline "Nancy senses it too, doubling her efforts."
    
    nancy "Mmmm!"
    $ play_woman_pleasure_sound()
    
    mc "I'm close, Nancy. So close."
    $ play_man_pleasure_sound()
    
    mc "Fuck! Nancy!"
    $ play_man_pleasure_sound()
    
    scene scene_7_final
    with fade
    
    outline "I reach my climax with Nancy's devoted attention."
    outline "She takes everything I give her, never pulling away."
    outline "When it's over, she looks up at me with satisfied eyes."
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    
    nancy "Mmm..."
    $ play_woman_pleasure_sound()
    $ play_woman_breathing_sound()
    
    scene home_night
    show nancy at nancy_convo
    $ update_character_state("nancy", CharState.HAPPY)
    with fade
    
    nancy "That was amazing..."
    nancy "You taste so good, [player_name]."
    
    mc "Nancy... that was incredible."
    mc "Thank you. For everything."
    
    nancy "Thank you for letting me celebrate with you."
    nancy "For letting me show you how a real woman treats her man."
    nancy "[girl_friend] never deserved you."
    
    "Nancy curls up next to me, completely satisfied."
    "We hold each other in the afterglow."
    
    nancy "I'm so proud of how you handled everything tonight."
    nancy "You've become such a strong, confident man."
    nancy "And I get to be yours."
    
    mc "I couldn't ask for anything better."
    
    # Nancy trust puzzle for her complete openness
    if nancy_love >= 30:
        outline "Nancy's complete trust in me is overwhelming..."
        outline "She holds nothing back, hides nothing from me..."
        outline "What represents total openness between lovers?"
        jump outfit_10_puzzle
        label outfit_10_puzzle_success:
            outline "No barriers, no walls, just pure connection..."
        label outfit_10_puzzle_failure:
            outline "Connection takes time and trust..."
    # Check if Nancy's ultimate fantasy can be unlocked
    if nancy_love >= 30 and nancy_key_question_passed == True:
        "As we lay in the afterglow, Nancy traces patterns on my chest."
        "Her breathing has steadied, but there's still a fire in her eyes."
        $ update_character_state("nancy", CharState.AROUSED)
        nancy "You know... there's something I've fantasized about."
        nancy "Something I've never told anyone before."
        mc "What is it?"
        nancy "I've been thinking about... letting you have complete control."
        nancy "Total submission. Trust beyond anything I've experienced."
        nancy "But it's... intense. Are you interested?"
        menu:
            "Tell me more about this fantasy":
                label test_choice_1i4ma:
                mc "Tell me more about this fantasy."
                mc "I want to understand what you need."
                nancy "I want to be completely at your mercy."
                nancy "Helpless, suspended, yours to take however you want."
                nancy "I trust you completely, [player_name]."
                nancy "More than I've ever trusted anyone."
                mc "Are you sure about this?"
                mc "Once we cross that line..."
                nancy "I've never been more sure of anything."
                nancy "I have everything we need. I've been planning this."
                nancy "The storage room at the gym. After hours, completely private."
                jump nancy_ultimate_scene
                
            "Maybe another time":
                label test_choice_cle2i:
                $ lose_sound()
                mc "That sounds intense. Maybe another time?"
                mc "When we've had more time to think about it."
                
                nancy "Of course. Whenever you're ready."
                nancy "I'll always be here for you."
                
                "Nancy seems slightly disappointed but understanding."
                "She cuddles closer, content with what we've shared tonight."
                
                jump episode_5_ending
    else:
        jump episode_5_ending

label nancy_ultimate_scene:
    
    scene black
    with fade
    
    "An hour later, Nancy leads me through the empty university campus."
    "Her hand trembles slightly in mine - not from fear, but from anticipation."
    
    nancy "The security guard owes me a favor."
    nancy "We have until dawn."
    
    "She produces a key card and leads me into the gym building."
    "The hallways are eerily quiet, our footsteps echoing softly."
    
    scene gym_morning
    with fade
    
    "The storage room is larger than I expected."
    "Nancy has transformed it into something intimate and private."
    "Rope systems hang from reinforced ceiling beams."
    "Soft lighting casts warm shadows on the walls."
    
    show nancy at nancy_convo
    $ update_character_state("nancy", CharState.AROUSED)
    with fade
    
    nancy "I've been preparing this for weeks."
    nancy "Ever since I realized how much I trust you."
    nancy "How much I want to give you everything."
    
    mc "Nancy... this is incredible."
    mc "You've thought of everything."
    
    nancy "I have one request though."
    nancy "Once we start... I want you to take complete control."
    nancy "Use me however you want. Don't hold back."
    nancy "I need to feel your dominance completely."
    
    "She moves to the rope setup, her movements graceful but nervous."
    
    nancy "Will you help me get ready?"
    
    mc "Are you absolutely certain about this?"
    
    nancy "More certain than I've ever been about anything."
    nancy "I've dreamed about this moment."
    nancy "About surrendering completely to you."
    
    scene black
    with fade
    
    "I help Nancy into the elaborate rope harness."
    "Her breathing quickens as each rope tightens into place."
    "Soon she's suspended, helpless, beautiful."
    "A cloth gag muffles her soft moans of anticipation."
    
    scene black
    show scene_22_initial
    stop music fadeout 1.0
    with fade
    
    outline "Nancy hangs suspended in the rope harness, completely at my mercy."
    outline "Her mouth is gagged, her eyes wide with trust and desire."
    outline "She's positioned perfectly, vulnerable and waiting."
    outline "Every curve of her body outlined by the rope."
    
    nancy "Mmmph..." 
    $ play_woman_pleasure_sound()
    
    mc "God, Nancy... you're absolutely perfect like this."
    $ play_man_pleasure_sound()
    
    outline "I position myself behind her suspended form."
    outline "She trembles with anticipation, completely helpless."
    outline "The trust in her eyes is overwhelming."
    
    scene black
    show scene_22
    with fade
    
    outline "I enter her from behind while she hangs helplessly in the ropes."
    outline "Her muffled moans fill the room as I begin to move."
    outline "The rope harness holds her perfectly in position."
    outline "She can't resist, can't control anything - exactly as she wanted."
    
    nancy "Mmmph! Mmmm!"
    $ play_woman_pleasure_sound()
    
    mc "This is what you wanted, isn't it?"
    mc "To be completely at my mercy."
    $ play_man_pleasure_sound()
    $ play_penetration_sound()
    
    nancy "Mmm-hmm!"
    $ play_woman_pleasure_sound()
    
    outline "I grip her hips, setting a rhythm that she can only follow."
    outline "The ropes hold her steady as I thrust deeper."
    outline "Her body responds to every movement, helpless to do anything but feel."
    
    mc "You're incredible, Nancy."
    mc "So beautiful, so trusting."
    $ play_man_pleasure_sound()
    $ play_penetration_sound()
    
    nancy "Mmmph! Mmm!"
    $ play_woman_pleasure_sound()
    
    outline "I can feel her approaching climax through the gag."
    outline "Her body tenses in the ropes, trembling with building pleasure."
    outline "She's completely surrendered to the sensations."
    
    mc "That's it, Nancy. Let go completely."
    mc "Give yourself over to this feeling."
    $ play_man_pleasure_sound()
    
    nancy "MMMPH!"
    $ play_woman_pleasure_sound()
    
    outline "Her muffled scream of pleasure fills the room."
    outline "Her body convulses in the ropes as she climaxes."
    outline "The sight and sound of her total surrender pushes me over the edge."
    
    mc "Nancy! I'm going to..."
    $ play_man_pleasure_sound()
    
    scene scene_22_final
    with fade
    
    outline "I reach my climax while she's still suspended and helpless."
    outline "Filling her completely as she hangs there, unable to move."
    outline "Her muffled moans of satisfaction mix with my groans of release."
    $ play_cum_sound()
    $ play_man_pleasure_sound()
    
    nancy "Mmm... mmmph..."
    $ play_woman_pleasure_sound()
    $ play_woman_breathing_sound()
    
    scene gym_morning
    with fade
    
    "I carefully help Nancy down from the rope harness."
    "She collapses into my arms, completely exhausted but glowing."
    
    show nancy at nancy_convo
    $ update_character_state("nancy", CharState.HAPPY)
    with fade
    
    "I remove her gag gently."
    
    nancy "Oh my god... [player_name]..."
    nancy "That was... that was everything I dreamed it would be."
    
    mc "Are you okay? Was it too intense?"
    
    nancy "It was perfect. You were perfect."
    nancy "I've never felt so... complete."
    nancy "So completely yours."
    
    "We sit together on the mat she's prepared."
    "She curls up against me, skin still flushed from the experience."
    
    nancy "Thank you for trusting me with this fantasy."
    nancy "For giving me exactly what I needed."
    nancy "I love you, [player_name]. Completely."
    
    mc "I love you too, Nancy."
    mc "Thank you for trusting me with something so intimate."
    
    nancy "We should probably head back before dawn."
    nancy "But... can we do this again sometime?"
    
    mc "Whenever you want."
    
    "Nancy smiles contentedly as we clean up the room."
    "This night has bonded us in ways I never imagined possible."
    "Her trust and surrender have made our connection unbreakable."
    
    $ persistent.scene_22 = True
    
    jump episode_5_ending

label episode_5_ending:
    
    # Grant episode 5 completion achievement
    call grant_episode_achievement(5) from _call_grant_episode_achievement_2
    
    # Check and grant ending achievements based on outcome
    $ check_ending_achievements()
    $ check_love_achievements()
    $ check_outfit_achievements()
    $ check_story_path_achievements()
    
    scene home_morning
    show mc at mc_convo
    with Fade(0.5, 5.0, 0.5)
    
    if get_total_conquests() >= 5 and jane_love <= -40:  # Perfect victory
        
        $ update_character_state("mc", CharState.HAPPY)
        play music "ES_You - SRA.mp3" volume 0.2
        
        "The next morning, I wake up feeling truly free."
        "[girl_friend] is finally out of my system."
        "The past is buried, and my future is bright."
        
        show bull at bull_convo
        $ update_character_state("bull", CharState.HAPPY)
        with pixellate
        
        bull_phone "You did it! You actually fucking did it!"
        bull_phone "You faced your past and conquered it!"
        bull_phone "[girl_friend] knows what she lost. Justin is humiliated."
        bull_phone "And you have a harem of women who adore you!"
        
        mc "I couldn't have done it without you."
        mc "You pushed me when I needed it."
        
        bull_phone "I just showed you the path."
        bull_phone "You walked it yourself."
        bull_phone "From cuckold to bull. Complete transformation."
        
        "My phone buzzes with messages."
        "Nancy wants to meet later."
        "Lauren is planning another date."
        "Emma sent explicit photos."
        "Even Gemmy and Ersa want another threesome."
        
        mc "Life is good."
        
        bull_phone "And getting better."
        bull_phone "Craig paid his child support in full."
        bull_phone "Matthews is under investigation for misconduct."
        bull_phone "Justin's reputation is destroyed."
        bull_phone "And [girl_friend]? She'll spend the rest of her life knowing she threw away the best thing she ever had."
        
        if jane_love <= -20 and justin_hate >= 30:
            outline "[girl_friend] has been completely defeated..."
            outline "What should she show now that the roles are reversed?"
            jump outfit_31_puzzle
            label outfit_31_puzzle_success:
                outline "The tables have completely turned!"
            label outfit_31_puzzle_failure:
                outline "[girl_friend] is learning her new role..."
        mc "What about you? What happens to you now?"
        bull_phone "My work here is done."
        bull_phone "You don't need me anymore."
        bull_phone "You've become everything I hoped for."
        bull_phone "A true bull. Confident, dominant, successful."
        bull_phone "You've become a warrior in the game of life..."
        menu:
            "What makes a true warrior?":
                label test_choice_canrf:
                if get_total_conquests() >= 5 and jane_love <= -40:  # Perfect victory
                    bull_phone "What am I when I face life's battles?"
                    jump outfit_36_puzzle
                    label outfit_36_puzzle_success:
                        bull_phone "You've earned the right to dress like the conqueror you've become!"
                    label outfit_36_puzzle_failure:
                        bull_phone "You'll understand warrior spirit in time..."
            "Thank you for everything":
                label test_choice_5z791:
                bull_phone "You earned every bit of this success yourself."
        mc "Will you leave?"
        bull_phone "I'll always be here if you truly need me."
        bull_phone "But you won't. You've graduated."
        bull_phone "You've learned discipline, honor, duty to those who trust you..."
        menu:
            "What drives soldiers to serve?":
                label test_choice_k8kj1:
                if get_total_conquests() >= 5 and jane_love <= -40:  # Perfect victory
                    bull_phone "What makes someone serve with dedication and pride?"
                    jump outfit_40_puzzle
                    label outfit_40_puzzle_success:
                        bull_phone "You serve your women with the dedication of a soldier!"
                        bull_phone "That's what true leadership looks like!"
                    label outfit_40_puzzle_failure:
                        bull_phone "You'll understand service and honor in time..."
            "I'll miss your guidance":
                label test_choice_w7y6w:
                bull_phone "You don't need guidance anymore."
        bull_phone "Now go. Your women are waiting."
        "The phone goes quiet."
        "But it's not sad. It's peaceful."
        "I don't need the voice anymore."
        "I've become my own man."
        "Later that day, I meet with all my girls."
        "Nancy, Lauren, Emma, Gemmy, and Ersa."
        "They all know about each other now."
        "And surprisingly, they're okay with sharing."
        scene home_night
        with fade
        show nancy at nancy_convo
        nancy "You saved us all in different ways."
        hide nancy
        show lauren at lauren_convo
        lauren "From loneliness."
        hide lauren
        show emma at emma_convo
        emma "From bad relationships."
        "Gemmy and Ersa arrive together."
        hide emma
        show gemmy at gemmy_right_pos
        show ersa at ersa_left
        outline "From deadbeat ex-husbands."
        hide gemmy
        hide ersa
        show nancy at nancy_convo
        nancy "So we've decided to share."
        hide nancy
        show emma at emma_convo
        emma "You've earned it."
        hide emma
        show lauren at lauren_convo
        lauren "By being the man none of us thought existed."
        lauren "Someone who plays by his own rules... like an athlete..."
        menu:
            "What sport represents playing by new rules?":
                label test_choice_2czhk:
                if jane_humiliation_level >= 5:
                    outline "[girl_friend] now has to play by my rules..."
                    outline "What's the winning move in volleyball?"
                    jump outfit_34_puzzle
                    label outfit_34_puzzle_success:
                        outline "She'll serve my way from now on!"
                    label outfit_34_puzzle_failure:
                        outline "[girl_friend] needs to learn the new game rules..."
            "Focus on the moment":
                label test_choice_jygnt:
                lauren "You're right, this moment is perfect."
        hide lauren
        show mc at mc_convo
        mc "This is really happening?"
        mc "All of you? Together?"
        nancy "If you want us."
        mc "How could I not?"
        scene black
        with fade
        "We spent the night together."
        "All of us. A tangle of bodies and pleasure."
        "The ultimate reward for my transformation."
        "From broken cuckold to successful bull."
        "From zero to hero."
        "From nothing to everything."
        "But the Bull Phone vibrates one more time..."
        bull_phone "You think we're done?"
        bull_phone "Oh no, my greatest student."
        bull_phone "There's still more to conquer."
        bull_phone "But that's a story for another time."
        $ update_character_state("mc", CharState.HAPPY)
        $ power_consolidated = True
        "I've come so far from where I started."
        "From broken cuckold to master of my own destiny."
        "Nancy trusts me completely, sharing her deepest fantasies."
        "Lauren adores me with innocent devotion."
        "Emma chose me over Justin definitively."
        "Gemmy and Ersa can't get enough of me."
        bull_phone "You've exceeded even my wildest expectations!"
        bull_phone "Complete transformation from victim to victor."
        bull_phone "You took control of your life, your desires, your destiny."
        mc "All thanks to you, I suppose."
        bull_phone "No. I just showed you the path."
        bull_phone "You walked it yourself."
        bull_phone "Every choice, every seduction, every conquest - that was all you."
        mc "So what now? What's next?"
        bull_phone "Now? Now you live the life you've built."
        bull_phone "You have Nancy for passion and trust."
        bull_phone "Lauren for sweet innocence."
        bull_phone "Emma for fire and competition."
        bull_phone "Gemmy and Ersa for pure lust."
        bull_phone "[girl_friend] knows she lost the best thing she ever had."
        bull_phone "Justin is humiliated and broken."
        mc "It's perfect. Everything I could want."
        bull_phone "More than that. It's everything you deserve."
        bull_phone "You've graduated from my program with highest honors."
        bull_phone "You don't need me anymore."
        mc "Wait, you're leaving?"
        bull_phone "My work here is complete."
        bull_phone "You are the bull now."
        bull_phone "You don't need a magic phone to tell you what to do."
        bull_phone "You have the confidence, the skill, the power."
        mc "But what if I mess up?"
        bull_phone "You won't. You've proven yourself."
        bull_phone "Besides, your women won't let you fail."
        bull_phone "They're invested in your success now."
        bull_phone "They need you as much as you need them."
        "The phone screen flickers."
        bull_phone "This is goodbye, [player_name]."
        bull_phone "Go live your perfect life."
        bull_phone "You've earned it."
        hide bull
        with pixellate
        "The phone goes completely dead."
        "Not just off - completely bricked."
        "But I don't feel lost or afraid."
        "I feel powerful. Complete."
        "My phone - my real phone - buzzes with messages."
        nancy "(text) Tomorrow night? My place? I have something special planned..."
        lauren "(text) Missing you. Can I come over?"
        emma "(text) Justin's been begging me to come back. Pathetic. You're so much better."
        gemmy "(text) Craig keeps calling but I blocked him. You've ruined me for other men."
        ersa "(text) That crypto tip paid off! Dinner to celebrate? My treat... and I'll be dessert."
        # Final transformation - ultimate confidence
        outline "I've transformed completely. I have nothing to hide anymore."
        outline "What represents ultimate confidence in who you are?"
        jump outfit_5_puzzle
        label outfit_5_puzzle_success:
            outline "Nothing can shake me now. I am who I choose to be."
        label outfit_5_puzzle_failure:
            outline "Confidence comes with time and experience..."
        mc "My perfect life indeed."
        # Ultimate completion reward - The Knight's Armor
        outline "I've reached the pinnacle of my journey..."
        outline "From broken boy to master of my destiny..."
        outline "What drives someone to achieve absolute perfection?"
        jump outfit_60_puzzle
        label outfit_60_puzzle_success:
            outline "The Knight's Armor - symbol of chivalry, honor, and complete mastery!"
            outline "I am the legendary knight who conquered all challenges!"
            outline "🏆 Master of all outfits, master of all women, master of life itself!"
        label outfit_60_puzzle_failure:
            outline "Perfection is a journey, not a destination..."
        "From zero to hero."
        "From cuckold to bull."
        "From nothing to everything."
        "And it's only the beginning."
        # Grant special achievement for perfect victory
        $ grant_achievement("PERFECT_VICTORY")
        # Ultimate Bull respect outfit - single prestigious unlock
        bull_phone "You've exceeded all expectations, kid."
        bull_phone "You've earned the ultimate sign of respect..."
        bull_phone "What currency matters most in our world?"
        jump outfit_38_puzzle
        label outfit_38_puzzle_success:
            bull_phone "You've earned the Mafia Boss look, kid!"
            bull_phone "Wear it with pride."
            bull_phone "You know what else you've earned? Freedom."
        label outfit_38_puzzle_failure:
            bull_phone "Respect is earned through actions, not words..."
        bull_phone "Freedom to ride your own path..."
        menu:
                "What represents freedom and the open road?":
                    label test_choice_tq7o3:
                    if get_total_conquests() >= 5 and jane_love <= -40:  # Perfect victory
                        bull_phone "What do I travel on when seeking freedom?"
                        jump outfit_37_puzzle
                        label outfit_37_puzzle_success:
                            bull_phone "You've earned the biker's freedom, kid!"
                        label outfit_37_puzzle_failure:
                            bull_phone "Freedom comes to those who take it..."
                "Thank you for everything":
                    label test_choice_cp5q4:
                    bull_phone "You earned it all yourself."
        
        jump the_end
        
    elif get_total_conquests() >= 3:  # Good ending
        
        $ update_character_state("mc", CharState.HAPPY)
        play music "ES_Something Special - Spectacles Wallet and Watch.mp3" volume 0.2
        
        "Things are good. Not perfect, but good."
        "I have closure with [girl_friend]."
        "Strong relationships with my girls."
        "And Justin's influence is weakened."
        
        # Grant good ending achievement
        $ grant_achievement("GOOD_ENDING")
        
        show bull at bull_convo
        $ update_character_state("bull", CharState.HAPPY)
        with pixellate
        
        bull_phone "Not bad, kid. You've grown real horns."
        bull_phone "Maybe not the sharpest, but definitely there."
        
        mc "It's enough. I'm happy."
        
        bull_phone "And that's what matters."
        bull_phone "You faced your demons and came out stronger."
        
        "Nancy and I grow closer every day."
        "She's become my main girl, loyal and loving."
        "Lauren and I grow closer every day."
        "Emma finally left Justin for good."
        "Gemmy and Ersa are regular visitors."
        
        mc "I never thought I'd have this."
        mc "Multiple women who actually want me."
        
        bull_phone "Because you became someone worth wanting."
        bull_phone "Remember that."
        
        "Life isn't perfect."
        "But it's mine."
        "And that's enough."
        
        "Or so I thought..."
        
        bull_phone "You've done well. Very well."
        bull_phone "Not perfect, but impressive nonetheless."
        bull_phone "You've built something meaningful here."
        
        mc "It feels good. Stable. Real."
        
        bull_phone "Because it is real. You earned every bit of it."
        bull_phone "Perfect is the enemy of good, and you have something good here."
        bull_phone "A great life, actually."
        
        "Nancy continues to trust me deeply."
        "We explore new things together, always pushing boundaries."
        "Lauren's sweetness balances everything perfectly."
        "Emma finally sees me as the better choice."
        "Gemmy and Ersa add spice to my life."
        
        bull_phone "You have multiple women who genuinely want you."
        bull_phone "That's more than most men ever achieve."
        bull_phone "Be proud of what you've built."
        
        mc "I am. It's just... sometimes I wonder if there could be more."
        
        bull_phone "There's always more. But sometimes, enough is enough."
        bull_phone "You've proven yourself. You've grown."
        bull_phone "From broken boy to confident man."
        bull_phone "That transformation is complete."
        
        mc "So this is it? The end of our journey together?"
        
        bull_phone "Every journey must end, [player_name]."
        bull_phone "But your story? That continues."
        bull_phone "With the women who love you."
        bull_phone "With the confidence you've built."
        bull_phone "With the life you've created."
        
        "The Bull Phone fades from the screen."
        "But I don't feel abandoned."
        "I feel ready."
        
        "Life is good."
        "I have women who care about me."
        "Enemies who fear me."
        "A future that's bright."
        
        "Not perfect, but definitely good."
        "And that's more than enough."

        jump the_end
        
    elif get_total_conquests() >= 1:  # Neutral ending
        
        $ update_character_state("mc", CharState.NORMAL)
        play music "ES_Annoying - Ludvig Moulin.mp3" volume 0.2
        
        "Things are... okay."
        "Not great, not terrible."
        "Just okay."
        
        show bull at bull_convo
        $ update_character_state("bull", CharState.NORMAL)
        with pixellate
        
        bull_phone "You had all the tools but lacked killer instinct."
        bull_phone "Still, you're better than where you started."
        bull_phone "That's something, I suppose."
        
        mc "It doesn't feel like victory."
        
        bull_phone "Because it isn't."
        bull_phone "It's survival. Mediocrity."
        bull_phone "You could have had so much more."
        
        "Some relationships worked out."
        "Others didn't."
        "[girl_friend] and Justin are still together, but their power over me is broken."
        "I'm not winning, but I'm not losing either."
        
        mc "At least I'm free of the past."
        
        bull_phone "Partially. You didn't conquer it."
        bull_phone "You just... moved past it."
        bull_phone "There's a difference."
        
        "Life goes on."
        "Not the life I dreamed of."
        "But it's mine."
        
        jump the_end
        
    else:  # Bad ending
        
        $ update_character_state("mc", CharState.SAD)
        play music "ES_Black Venom - Ruiqi Zhao.mp3" volume 0.2
        
        "I'm back where I started."
        "Alone. Broken. Humiliated."
        "Worse, actually, because now I know what I could have had."
        
        show bull at bull_convo
        $ update_character_state("bull", CharState.ANGRY)
        with pixellate
        
        bull_phone "You're exactly where you started."
        bull_phone "A cuckold watching others live your life."
        bull_phone "You had every opportunity and wasted them all."
        
        mc "I tried..."
        
        bull_phone "Not hard enough."
        bull_phone "You let fear control you."
        bull_phone "Let the past define you."
        
        mc "What now?"
        
        bull_phone "Now? Nothing."
        bull_phone "You're on your own."
        bull_phone "I don't help quitters."
        
        "The phone goes dead."
        "Permanently this time."
        
        "[girl_friend] and Justin are back together."
        "They mock me openly on campus."
        "Nancy gave up on me."
        "Lauren won't return my calls."
        "Emma posts the humiliating videos online."
        
        "I drop out of college."
        "Move back with my parents."
        "Become exactly what [girl_friend] said I was."
        "Nothing."
        
        # Ironic failure outfits
        outline "Even in failure, some consolations remain..."
        outline "What's the saying about someone who's all talk and no action?"
        jump outfit_2_puzzle
        label outfit_2_puzzle_success:
            outline "At least I can dress like the cowboy I never became."
        label outfit_2_puzzle_failure:
            outline "I guess some people are just born to lose."
        if justin_humiliated:
            outline "Justin still thinks he's winning somehow..."
            outline "What's his speed in life? Fast or slow?"
            jump outfit_52_puzzle
            label outfit_52_puzzle_success:
            label outfit_52_puzzle_failure:
                outline "Justin's speed is irrelevant when he's going nowhere..."
        
        jump the_end
