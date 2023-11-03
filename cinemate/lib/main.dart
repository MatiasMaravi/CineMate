import 'package:cinemate/pages/signin_page.dart';
import 'package:cinemate/pages/signup_page.dart';
import 'package:cinemate/pages/home_page.dart';
import 'package:cinemate/pages/simpleapp_page.dart';
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:cinemate/utils/constant.dart'; 

void main() async{
  await Supabase.initialize(
    url: 'https://abesjycaynsvqfyzkagu.supabase.co',
    anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiZXNqeWNheW5zdnFmeXprYWd1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTg4ODM5MTcsImV4cCI6MjAxNDQ1OTkxN30.cp-RUGTasauzkT2Qy9l0aH26yDm-6n6uTZ6C_w3rYfw',
  );

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Cinemate',
      theme: ThemeData(
       primarySwatch: Colors.red,
      ),
      initialRoute: client.auth.currentSession != null ? '/simpleapp': '/',
      routes: {
      '/': (context) => const HomePage(),
      '/signin': (context) => const SignInPage(),
      '/signup': (context) => const SignUpPage(),
      '/simpleapp': (context) => const SimpleAppPage(),
    },
    );
  }
}