import 'package:flutter/material.dart';
import 'package:cinemate/utils/constant.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Container(
        color: Color.fromARGB(255, 42, 40, 40),
        child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ///Icon
             Image.asset(
                'assets/logo_cinemate.png', // Reemplaza 'your_image.png' con la ruta de tu imagen en los activos
                width: 300, // Ancho personalizado
                height: 300, // Alto personalizado
                fit: BoxFit.contain, // Ajusta el tamaño de la imagen
              ),
              
            ///Text
            /*const Text('CineMate', style: TextStyle(
              fontSize: 40,
              color: Colors.white,
            ),),
            largeGap,*/

            const Text(
                'Tu próxima película favorita está aquí', // Frase
                style: TextStyle(
                  fontSize: 18, // Tamaño más pequeño
                  color: Colors.white, // Color blanco
                ),
              ),
              largeGap,

            ///Sign In Button
            OutlinedButton(onPressed: (){
              Navigator.pushNamed(context, '/signin');
            }, 
            style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all(Colors.red),
                foregroundColor: MaterialStateProperty.all(Colors.white),
              ),
            child: const Text('Inicia sesión'),),
            smallGap,

            ///Sign Up Button
            OutlinedButton(onPressed: (){
              Navigator.pushNamed(context, '/signup');
            }, 
            style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all(Colors.red),
                foregroundColor: MaterialStateProperty.all(Colors.white),
              ),
            child: const Text('Regístrate'),),
          ],
        ),
       ),
      ),
    );
  }
}