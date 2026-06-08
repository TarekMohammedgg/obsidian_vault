---
tags:
  - flutter
  - moc
  - summary
aliases:
  - Flutter Knowledge Summary
  - ملخص موضوعات Flutter
created: 2026-06-08
---

# ملخص موضوعات Flutter

> [!summary]
> خريطة مختصرة للموضوعات الموجودة حاليًا داخل الـVault عن Flutter، بهدف تسهيل المراجعة والوصول للملاحظات المرتبطة.

## نقطة البداية

- [[flutter]] — الـMOC الأساسي الحالي لملاحظات Flutter.
- [[flutter roadmap]] — الموضوعات والخطوات المتبقية في خطة التعلم.
- [[flutter log journey]] — سجل رحلة التعلم والتقدم.

## أساسيات Flutter والـFramework

- [[Flutter Framework Architecture]] — نظرة على بنية Flutter والـWidget Tree وElement Tree وRender Tree والـEngine والـEmbedders.
- [[how flutter framework build]] — كيفية بناء وعمل Flutter Framework.
- [[widgets]] — مفهوم الـWidgets واستخدامها.
- [[when the flutter sdk not work well]] — حلول لمشكلات Flutter SDK.
- [[Flutter packages]] — حزم Flutter المهمة.
- [[Flutter Awesome Icons]] — الأيقونات واستخدامها داخل التطبيقات.

## State Management

- [[Flutter Cubit & Bloc]] — إدارة الحالة باستخدام Cubit وBloc.
- [[flutter provider]] — إدارة الحالة باستخدام Provider.
- [[Flutter Advanced Course Bloc and MVVM Pattern Arabic]] — تطبيق Bloc مع MVVM بصورة متقدمة.

## Architecture وتنظيم المشروع

- [[Deep Dive into Clean Architecture in Flutter - Arabic]] — شرح Clean Architecture في Flutter.
- [[MVVM Design pattern]] — نمط MVVM وتنظيم المسؤوليات.
- [[flutter services and models constants]] — تنظيم Services وModels وConstants.
- [[Flutter Framework Architecture]] — المعمارية الداخلية للـFramework.
- موضوعات مرتبطة بخطة التعلم: SOLID، Error Handling، Caching، Refresh Token وتنظيم طبقات التطبيق.

## APIs والتعامل مع البيانات

- [[Flutter API]] — التعامل مع APIs داخل تطبيقات Flutter.
- [[Sqflite]] — التخزين المحلي باستخدام SQLite.
- [[handle upload file to google drive app script and flutter code]] — رفع الملفات إلى Google Drive باستخدام Flutter وApps Script.
- [[Flutter Google Gemini Chat App Tutorial - Flutter Gemini API Chat Application Guide]] — دمج Gemini API داخل تطبيق Flutter.

## UI وResponsive Design

- [[Mastering Flutter Responsive & Adaptive UI Design]] — تصميم واجهات Responsive وAdaptive.
- [[Flutter Animation Core]] — أساسيات Animation في Flutter.
- [[how to make a clip path curve in flutter]] — إنشاء واجهات منحنية باستخدام ClipPath.
- [[double list view in flutter]] — التعامل مع أكثر من ListView.
- [[star Rating in flutter]] — تنفيذ Star Rating.
- [[text input formarter of pricing onchange in textform in flutter]] — تنسيق أسعار الإدخال داخل TextFormField.
- [[flutter splash screen]] — إعداد Splash Screen.
- [[build QR code in flutter]] — إنشاء QR Code.

## Notifications والتكامل مع النظام

- [[notifications in flutter]] — نظرة عامة على الإشعارات.
- [[Flutter Local Notifications]] — تنفيذ Local Notifications.
- [[native channel in flutter]] — التكامل مع Native Code باستخدام Method Channels.

## Testing والجودة

- [[Testing in flutter]] — Unit Testing وWidget Testing وIntegration Testing.
- موضوعات ما زالت في الـRoadmap:
  - Flutter DevTools.
  - Error handling وDio errors.
  - Caching.
  - SOLID practice.

## Deployment وCI/CD

- [[Flutter Deployment]] — نشر تطبيقات Flutter.
- [[flutter ci-cd workflow for complete app with secret action keys]] — إعداد CI/CD باستخدام GitHub Actions.
- [[how to upload flutter web into GitHub]] — نشر Flutter Web على GitHub.

## Payments

- [[flutter payment]] — دمج وسائل الدفع في Flutter.
- [[Flutter payment method]] — Canvas مرتبط بتدفق الدفع.

## مشاريع Flutter داخل الـVault

- [[Flutter Ai Image edit  project and notes]] — مشروع Flutter لمعالجة أو تعديل الصور بالذكاء الاصطناعي.
- [[fit fusion Overview]] — مشروع Fit Fusion.
- [[Review application]] — مراجعة تطبيق Flutter الخاص بمشروع التخرج Skinteligen.

## الموضوعات الرئيسية الموجودة حاليًا

1. Flutter fundamentals and framework internals.
2. State management باستخدام Bloc وCubit وProvider.
3. Clean Architecture وMVVM وتنظيم المشاريع.
4. APIs والتخزين المحلي والتكامل مع خدمات خارجية.
5. Responsive UI وAnimations وUI snippets.
6. Notifications وNative integration.
7. Testing وDebugging وDevTools.
8. Deployment وGitHub Actions وCI/CD.
9. Payments.
10. تطبيقات Flutter مرتبطة بالذكاء الاصطناعي ومشروع التخرج.

## الفجوات الظاهرة في المحتوى

- لا توجد خريطة واضحة ومتدرجة لتعلم Dart بصورة مستقلة.
- موضوع Dependency Injection غير ظاهر كملاحظة رئيسية مستقلة.
- Navigation وRouting، خصوصًا GoRouter، يحتاجان قسمًا واضحًا.
- Error handling وCaching وAuthentication موجودة في الـRoadmap أكثر من وجودها كملاحظات مكتملة.
- لا توجد ملاحظة مركزية واضحة عن Performance Optimization وFlutter DevTools.
- Testing موجود، لكن يحتاج ربطًا بأمثلة عملية من المشاريع.

## الخطوة التالية المقترحة

- استخدام هذه الملاحظة كصفحة مراجعة عليا.
- الإبقاء على [[flutter]] كـMOC ديناميكي يعتمد على Dataview.
- استكمال Properties وTags للملاحظات حتى تظهر تلقائيًا تحت الأقسام الصحيحة.
- تحويل فجوات المحتوى إلى خطة تعلم قابلة للتنفيذ داخل [[flutter roadmap]].
