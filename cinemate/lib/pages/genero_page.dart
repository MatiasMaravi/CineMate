import 'package:flutter/material.dart';

class EmptyPage extends StatelessWidget {
  const EmptyPage({super.key});



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Agrega un botón "Siguiente" que redirige a la página de inicio de sesión
            ElevatedButton(
              onPressed: () {
                Navigator.pushReplacementNamed(context, '/signin');
              },
              child: const Text('Siguiente'),
            ),
          ],
        ),
      ),
    );
  }
}
