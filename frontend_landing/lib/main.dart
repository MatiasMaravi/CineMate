import 'package:flutter/material.dart';
import 'package:frontend/views/home_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Cinemate',
      theme: ThemeData(
        primarySwatch: const MaterialColor(0xFFBE0000, <int, Color>{
          50: Color(0xFFBE0000), // 10% de opacidad
          100: Color(0xFFBE0000), // 20% de opacidad
          200: Color(0xFFBE0000), // 40% de opacidad
          300: Color(0xFFBE0000), // 60% de opacidad
          400: Color(0xFFBE0000), // 80% de opacidad
          500: Color(0xFFBE0000), // 100% de opacidad
          600: Color(0xFFBE0000), // 100% de opacidad
          700: Color(0xFFBE0000), // 100% de opacidad
          800: Color(0xFFBE0000), // 100% de opacidad
          900: Color(0xFFBE0000), // 100% de opacidad
        }),
      ),
      home: const HomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}