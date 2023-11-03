import 'package:flutter/material.dart';
import 'package:cinemate/utils/constant.dart';

class SignInPage extends StatefulWidget {
  const SignInPage({super.key});

  @override
  State<SignInPage> createState() => _SignInPageState();
}

class _SignInPageState extends State<SignInPage> {
  /// Initialize controller for email and password
  final TextEditingController _emailCrontroller = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  bool isLoading = false;

  /// [userLogin] function that handles
  Future<String?> userLogin({
    required final String email,
    required final String password,
  }) async {
    final response = await client.auth.signIn(
      email: email,
      password: password,
    );
    final user = response.data?.user;
    return user?.id;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),

      body: Stack(
        children: [
                    Image.asset(
            'assets/login.png',  // Ruta relativa a tu imagen en la carpeta de activos
            width: double.infinity,
            height: double.infinity,
            fit: BoxFit.cover,
          ),
          
       Center(
        child: Container(
          margin: const EdgeInsets.all(20),
        
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
                  decoration: BoxDecoration(
                    color: Colors.black.withOpacity(0.9),
                    borderRadius: BorderRadius.circular(30), // Bordes redondeados
                  ),
                  padding: const EdgeInsets.symmetric(horizontal: 31, vertical: 90),
                  child: Column(
                    children: [ 
                    Container(
                    width: 300, // Ancho personalizado del fondo rectangular
                    height: 70, // Alto personalizado del fondo rectangular
                    padding: const EdgeInsets.symmetric(horizontal: 20), // Añade relleno
                    decoration: BoxDecoration(
                      color: Color.fromARGB(255, 146, 75, 75), // Fondo blanco
                      borderRadius: BorderRadius.circular(24), // Bordes redondeados
                    ),
                    child: Column(
                      children: [
                  ///Email TextInput
                  TextFormField(
                    controller: _emailCrontroller,
                    decoration: 
                    const InputDecoration(
                      label: Text('Email', style: TextStyle(color: Colors.white)),
                    ),
                    
                        ),
                      ],
                    ),
                  ),
                  largeGap,
            
            

            ///Password TextInput
            Container(
                width: 300, // Ancho personalizado del fondo rectangular
                height: 70, // Alto personalizado del fondo rectangular
                padding: EdgeInsets.symmetric(horizontal: 20), // Añade relleno
                decoration: BoxDecoration(
                  color: Color.fromARGB(255, 146, 75, 75), // Fondo blanco
                  borderRadius: BorderRadius.circular(24), // Bordes redondeados
                ),
                child: Column(
                  children: [
            TextFormField(
                controller: _passwordController,
                decoration: const InputDecoration(label: Text('Password',style: TextStyle(color: Colors.white))),
                obscureText: true,
             ),
                  ],
                ),
              ),
              largeGap,
        

            ///Sign In Button
            isLoading 
              ? Container(
                height: 30,
                width: 30,
                decoration: const BoxDecoration(
                  color: Colors.white,
                ),
                child: const Center(
                  child: CircularProgressIndicator(),
                ),
              )
              : OutlinedButton(
                  onPressed: () async{
                    setState((){
                      isLoading = true;
                    });
                    dynamic loginValue = await userLogin(
                      email:_emailCrontroller.text, password: _passwordController.text,
                    );
                    setState(() {
                      isLoading = false;
                    });
                    if (loginValue != null) {
                      Navigator.pushReplacementNamed(context, '/simpleapp',);
                    } else {
                      context.showErrorMessage('Invalid Email or Password');
                    }
                  }, 
                  style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(const Color.fromARGB(255, 132, 125, 125)),
                  foregroundColor: MaterialStateProperty.all(Colors.white),
                  ),
                  
                  child:  const Text('Inicar sesión'),
                  ),
                 ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}