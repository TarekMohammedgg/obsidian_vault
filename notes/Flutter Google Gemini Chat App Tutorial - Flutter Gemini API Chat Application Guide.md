---
title: Flutter Google Gemini Chat App Tutorial - Flutter Gemini API Chat Application Guide
source: https://www.youtube.com/watch?v=PoZ9iRL16As
author:
  - "[[@moneyman-ne9lw]]"
published: 2024-03-30
created: 2025-10-26
description: "💼 Book a meeting: https://cutt.ly/Ke2x7QQ3💎 Ultimate Flutter UI Kit: https://cutt.ly/3w6tqwFAIn this video we will learn how to create an AI powered chat a..."
tags:
  - "#Flutter"
  -  
---


>[!note] Key points 
```dart 
  void _onSendMessage(ChatMessage newMessage) {

    setState(() {

      messages = [newMessage, ...messages];

    });

    try {

      String request = newMessage.text;

      gemini.promptStream(parts: [Part.text(request)]).listen((response) {

        ChatMessage? lastMessage = messages.firstOrNull;

        if (lastMessage != null && lastMessage.user == geminiUser) {

          lastMessage = messages.removeAt(0);

          String text =

              response?.content?.parts?.fold(

                "",

                (value, element) => "${value} ${element}",

              ) ??

              "";

          lastMessage.text += text;

          setState(() {

            messages = [lastMessage!, ...messages];

          });

        } else {

          String text =

              response?.content?.parts?.fold(

                "",

                (value, element) => "${value} ${element}",

              ) ??

              "";

          ChatMessage message = ChatMessage(

            user: geminiUser,

            createdAt: DateTime.now(),

            text: text,

          );

          setState(() {

            messages = [message, ...messages];

          });

        }
```

- خلي بالك في الكود ده `stream` هنا معناها انه بيرجع chunk by chunk ، و انا عملت ال `if and else ` عشان اتأكد في اول مره لو الرسالة الاخيرة في ال `messages list ` من `gemini` بعملها `append` عشان تبان في ال UI اكنها رسالة واحده طويلة رد من ال `gemini` بدل ما يبعت اكتر من رسالة  هيبقي شكله غير منطقي ، و في حالة ان الرسالة جية من ال `user` بعمل رسالة جديدة فيها الرد بتاع `gemini` علي الرسالة .

>[!note]-  Used Packages 
>`Flutter gemini`
>`Dash_chat_2` 




[ChatGpt conversation chat ](https://chatgpt.com/c/68f93dae-1f0c-8328-ab45-6ab15b353a00)
this that include `WidgetBinding.instance.addPostFrame((){});` and how to solve the problem of scroll to bottom using `reverse` method . 