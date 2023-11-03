import 'package:flutter/material.dart';
import 'vista_actores.dart';


class GenerosPage extends StatelessWidget {
  const GenerosPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    const title = 'Generos';
    List<String> generos = ["Action", "Adventure", "Animation", "Comedy",
                          "Crime", "Drama", "Documentary", "Family",
                          "Fantasy", "History", "Horror", "Music",
                          "Mystery", "Romance", "Science Fiction", "TV Movie",
                          "Thriller", "War", "Western"];
    List<String> selected = [];
    //String valor = "";
    void _select(String genero) {
      //setState(() {
        selected.add(genero);
      //});
    }

    return MaterialApp(
      title: title,
      theme: ThemeData(
        colorSchemeSeed: Colors.indigo,
        useMaterial3: true,
        brightness: Brightness.light,
      ),
      darkTheme: ThemeData(
        colorSchemeSeed: Colors.blue,
        useMaterial3: true,
        brightness: Brightness.dark,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text(title),
        ),
        body: GridView.count(
          // Create a grid with 2 columns. If you change the scrollDirection to
          // horizontal, this produces 2 rows.
          crossAxisCount: 3,
          // Generate 100 widgets that display their index in the List.
          children: 
          List.generate(generos.length, (index) {
            return Center(
              child: ElevatedButton(
                //style: style,
                onPressed: () {
                  _select(generos[index]);
                  //debugPrint('You just selected ${selected}');
                },
                child: Text('${generos[index]}'),
              ),
            );
          }),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => ActoresPage()),
                );
              },
              child: Text('Elegir Actores'),
        ),
      ),
    );
  }
}