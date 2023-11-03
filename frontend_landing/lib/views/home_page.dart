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
  //var arrayMovies = ['Toy Story', 'The Lion King', 'The Incredibles', 'Shrek', 'The Lego Movie'];
  var arrayMovies = [];
  @override
  void initState() {
    super.initState();
    
    // Obtener los datos de la API
    //getMovies();
    loadMovies();
  }

  Future<void> loadMovies() async {
    final url = Uri.parse('http://204.199.168.25:5000');
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
      print('Solicitud POST exitosa: ${response.body}');
    } else {
      print('Error en la solicitud POST: ${response.statusCode}');
    }
  }

  /*
  getMovies() async {
    movies = await RemoteService().getMovies(arrayMovies);
    if (movies != null) {
      movies!.sort((a, b) {
        final double ratingA = double.parse(a.imdbRating);
        final double ratingB = double.parse(b.imdbRating);
        return ratingB.compareTo(ratingA);
      });

      setState(() {
        isLoaded = true;
      });
    }
  }*/

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Cinemate',
          style: TextStyle(
            fontWeight: FontWeight.bold,
          )
        ),
        centerTitle: true,
        backgroundColor: Colors.black,
      ),
      body: Visibility(
        visible: isLoaded,
        replacement: const Center(
          child: CircularProgressIndicator(),
        ),
        child: const Text(
          'Hola',
          style: TextStyle(
            fontWeight: FontWeight.bold, 
          ),
        ),
      ),
    );
  }
}