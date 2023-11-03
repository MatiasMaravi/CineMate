import 'package:flutter/material.dart';
import 'package:cinemate/utils/constant.dart';

class SimpleAppPage extends StatefulWidget {
  const SimpleAppPage({super.key});
  @override
  State<SimpleAppPage> createState() => _SimpleAppPageState();
}

class _SimpleAppPageState extends State<SimpleAppPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: Builder(
          builder: (context) {
            return IconButton(
              onPressed: () {
                client.auth.signOut();
                Navigator.pushNamedAndRemoveUntil(
                  context, '/', (route) => false);               
              }, 
              icon: const Icon(Icons.logout),
              );
          },
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ///Icon
            const Icon(Icons.sailing_rounded,size: 150, color: Colors.redAccent,),
            smallGap,

            ///Text
            const Text(
              'Welcome',
              style: TextStyle(
                color: Colors.redAccent, 
                fontSize: 50,
                ),
              ),
              Text(
                'Hello! ${client.auth.currentUser?.email}',
                style: const TextStyle(
                  color:Colors.redAccent,
                  fontSize: 20,
                ),
              ),
              largeGap,

            ///Sign Out Button
            OutlinedButton(
              onPressed: () {
                client.auth.signOut();
                Navigator.pushNamedAndRemoveUntil(
                context, '/', (route) => false);  
              }, 
              child: const Text('Sign Out'),
            )
          ],
        ),
      ),
    );
  }
}