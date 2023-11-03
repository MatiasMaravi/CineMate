import 'package:flutter/material.dart';
import 'package:cinemate/utils/constant.dart';

class SignUpPage extends StatefulWidget {
  const SignUpPage({super.key});
  @override
  State<SignUpPage> createState() => _SignUpPageState();
}

class _SignUpPageState extends State<SignUpPage> {
  /// Initialize controllers
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
 
  ///[createUser] function that handles user creation
  Future<bool> createUser({
    required String email,
    required String password,
  }) async{
    final response = await client.auth.signUp(
      email,
      password,
    );
    final error = response.error;
    if(error == null){
      return true;
    } else{
      return false;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Container (
        decoration: BoxDecoration(
          color: Colors.black, //fondo negro
        ),
        child: Column(
      children: [
        Container(
          decoration: BoxDecoration(
            color: Colors.white, // Fondo blanco
          ),
          
          child: Image.network(
            'https://imagenes.muyinteresante.es/files/composte_image/uploads/2023/06/22/64945b863c28f.jpeg',
            width: double.infinity, // Ancho de la imagen
            height: 200, // Alto de la imagen
            fit: BoxFit.cover, // Ajustar la imagen al tamaño del contenedor
          ),
        ),
        largeGap,

             // Fondo rectangular blanco para el campo de email
              Container(
                width: 350, // Ancho personalizado del fondo rectangular
                height: 70, // Alto personalizado del fondo rectangular
                padding: const EdgeInsets.symmetric(horizontal: 20), // Añade relleno
                decoration: BoxDecoration(
                  color: Colors.white, // Fondo blanco
                  borderRadius: BorderRadius.circular(10), // Bordes redondeados
                ),
                child: Column(
                  children: [
                    // Email Input
                    TextFormField(
                      controller: _emailController,
                      decoration: const InputDecoration(
                        labelText: 'Email',
                      ),
                    ),
                  ],
                ),
              ),
              smallGap,

              
              // Fondo rectangular blanco para el campo de contraseña
              Container(
                width: 350, // Ancho personalizado del fondo rectangular
                height: 70, // Alto personalizado del fondo rectangular
                padding: EdgeInsets.symmetric(horizontal: 20), // Añade relleno
                decoration: BoxDecoration(
                  color: Colors.white, // Fondo blanco
                  borderRadius: BorderRadius.circular(10), // Bordes redondeados
                ),
                child: Column(
                  children: [
                    // Password Input
                    TextFormField(
                      controller: _passwordController,
                      decoration: const InputDecoration(
                        labelText: 'Password',
                      ),
                      obscureText: true,
                    ),
                  ],
                ),
              ),
              largeGap,
        
            ///Sign Up Button
              OutlinedButton(
              onPressed: () async{
                final userValue = await createUser(
                  email: _emailController.text, 
                  password: _passwordController.text);
                if(userValue == true){
                  Navigator.pushReplacementNamed(context, '/signin');
                  context.showErrorMessage('Success');
                }
              }, 
              style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all(Colors.red),
                foregroundColor: MaterialStateProperty.all(Colors.white),
              ),
              child: const Text('Sign Up'),
            ),
          ],
        ),
      ),
     );
  }
}