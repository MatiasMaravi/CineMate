import 'package:flutter/material.dart';
//import 'package:frontend/models/post.dart';
import 'package:frontend/models/movie.dart';
import 'package:frontend/services/remote_service.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<Movie>? movies;
  var isLoaded = false;
  var arrayMovies = ['Toy Story', 'The Lion King', 'The Incredibles', 'Shrek', 'The Lego Movie'];

  @override
  void initState() {
    super.initState();
    
    // Obtener los datos de la API
    getMovies();
  }

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
  }

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
        child: ListView.builder(
          itemCount: 5,
          itemBuilder: (context, index) {
            return Card(
              margin: const EdgeInsets.all(16),
              child: Row(
                children: [
                  // Poster de la pelicula
                  SizedBox(
                    width: 125.0,
                    child: Image.network(
                      movies![index].poster,
                      fit: BoxFit.cover,
                    ),
                  ),

                  // Información de la pelicula
                  Expanded(
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            movies![index].title,
                            style: const TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                            )
                          ),
                          const SizedBox(height: 8,),
                          Text(
                            'IMDB Rating: ${movies![index].imdbRating}',
                            style: const TextStyle(fontSize: 16),
                          ),
                          Text(
                            'Release year: ${movies![index].year}',
                            style: const TextStyle(fontSize: 16),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              )
            );
          }
        )
      )
    );
  }
}