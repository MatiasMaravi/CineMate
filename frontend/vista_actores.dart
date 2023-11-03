import 'package:flutter/material.dart';

class ActoresPage extends StatelessWidget {
  const ActoresPage({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
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
          title: const Text('Actores'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(
                  'Escriba 5 actores que le interesen:'),
              const ActoresAutoComplete(),
            ],
          ),
        ),
      ),
    );
  }
}
/*
@immutable
class User {
  const User({
    required this.email,
    required this.name,
  });

  final String email;
  final String name;

  @override
  String toString() {
    return '$name, $email';
  }

  @override
  bool operator ==(Object other) {
    if (other.runtimeType != runtimeType) {
      return false;
    }
    return other is User && other.name == name && other.email == email;
  }

  @override
  int get hashCode => Object.hash(email, name);
}
*/
class ActoresAutoComplete extends StatelessWidget {
  const ActoresAutoComplete({super.key});
/*
  static const List<User> _userOptions = <User>[
    User(name: 'Alice', email: 'alice@example.com'),
    User(name: 'Bob', email: 'bob@example.com'),
    User(name: 'Charlie', email: 'charlie123@gmail.com'),
  ];
*/
  static const List<String> _actoresOptions = ["Action", "Adventure", "Animation", "Comedy",
                          "Crime", "Drama", "Documentary", "Family",
                          "Fantasy", "History", "Horror", "Music",
                          "Mystery", "Romance", "Science Fiction", "TV Movie",
                          "Thriller", "War", "Western"]; //reemplazar con nombres de actores
  static String _displayStringForOption(String option) => option;

  @override
  Widget build(BuildContext context) {
    return Autocomplete<String>(
      displayStringForOption: _displayStringForOption,
      optionsBuilder: (TextEditingValue textEditingValue) {
        if (textEditingValue.text == '') {
          return const Iterable<String>.empty();
        }
        return _actoresOptions.where((String option) {
          return option
              .toString()
              .contains(textEditingValue.text.toLowerCase());
        });
      },
      onSelected: (String selection) {
        debugPrint('You just selected ${_displayStringForOption(selection)}');
      },
    );
  }
}
