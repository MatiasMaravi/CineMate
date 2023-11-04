import 'dart:ffi';

import 'package:flutter/material.dart';
//import 'package:frontend/models/post.dart';
import 'package:frontend/models/movie.dart';
//import 'package:frontend/services/remote_service.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<Movie>? movies;
  var isLoaded = false;
  var arrayMovies = [];

  @override
  void initState() {
    super.initState();
    loadMovies();
    print("Test: ");
    print(arrayMovies);
  }

  Future<void> loadMovies() async {
  final url = Uri.parse('http://10.0.2.2:5000/movies');
  final response = await http.post(
    url,
    headers: <String, String>{
      'Content-Type': 'application/json',
    },
    body: jsonEncode(<String, dynamic>{
      'usuario': 'matias@gozu.com',
      'generos': ['accion', 'drama'],
      'actores': ['tom cruise', 'brad pitt'],
    }),
  );
  if (response.statusCode == 200) {
    final responseData = jsonDecode(response.body);
    isLoaded = true;
    if (responseData.containsKey('movies')) {
      setState(() {
        arrayMovies = json.decode(response.body)['movies'];
      });
      print('Solicitud POST exitosa: ${response.body}');
    } else {
      print('Error en la solicitud POST: No se encontró la propiedad "movies" en la respuesta.');
    }
  } else {
    print('Error en la solicitud POST: ${response.statusCode}');
  }
  print(arrayMovies);
  isLoaded = true;
}

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Cinemate',
          style: TextStyle(
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.black,
      ),
      body: isLoaded ? Text(arrayMovies.toString()) : CircularProgressIndicator(),
    );
  }
}
