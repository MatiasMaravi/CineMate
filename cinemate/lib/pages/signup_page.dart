// signup_page.dart

import 'package:flutter/material.dart';
import 'package:cinemate/utils/constant.dart';

class SignUpPage extends StatefulWidget {
  const SignUpPage({super.key});

  @override
  State<SignUpPage> createState() => _SignUpPageState();
}

class _SignUpPageState extends State<SignUpPage> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final TextEditingController _nameController = TextEditingController(); // Nuevo campo "name"

  Future<bool> createUser({
    required String email,
    required String password,
    required String name, // Nuevo campo "name"
  }) async {
    final response = await client.auth.signUp(email, password);
    final error = response.error;
    if (error == null) {
      final user = response.data?.user;
      if (user != null) {
        final data = {
          'email': user.email,
          'name': name,
          'password': password,
        };
        final userResponse = await client.from('usuario').upsert([data]).execute();
        if (userResponse.error == null) {
          return true;
        }
      }
    }
    return false;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Container(
  decoration: BoxDecoration(
    image: DecorationImage(
      image: AssetImage('assets/register.png'), // Reemplaza con la ruta de tu imagen
      fit: BoxFit.cover,
    ),
  ),
  child: Align(
        alignment: Alignment.center,
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Expanded(child: Container()),
            Container(
              width: 350,
              height: 70,
              padding: const EdgeInsets.symmetric(horizontal: 20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Column(
                children: [
                  TextFormField(
                    controller: _nameController, // Nuevo campo "name"
                    decoration: const InputDecoration(
                      labelText: 'Name',
                    ),
                  ),
                ],
              ),
            ),
            smallGap,
            Container(
              width: 350,
              height: 70,
              padding: const EdgeInsets.symmetric(horizontal: 20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Column(
                children: [
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
            Container(
              width: 350,
              height: 70,
              padding: EdgeInsets.symmetric(horizontal: 20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Column(
                children: [
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
            OutlinedButton(
              onPressed: () async {
                final userValue = await createUser(
                  email: _emailController.text,
                  password: _passwordController.text,
                  name: _nameController.text, // Pasa el valor del campo "name"
                );
                if (userValue == true) {
                  Navigator.pushReplacementNamed(context, '/empty');
                  context.showErrorMessage('Success');
                }
              },
              style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all(Colors.red),
                foregroundColor: MaterialStateProperty.all(Colors.white),
              ),
              child: const Text('Registrarme'),
            ),
            largeGap,
          ],
        ),
        ),
      ),
    );
  }
}
