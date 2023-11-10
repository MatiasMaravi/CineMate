import 'package:frontend/models/post.dart';
import 'package:frontend/models/movie.dart';
import 'package:http/http.dart' as http;

mixin RemoteService {
  Future<List<Post>?> getPosts() async {
    var client = http.Client();
    var uri = Uri.parse(
        'https://api.themoviedb.org/3/movie/popular?api_key=c648045dfc27706ac42d6ac0ae9bffd1');

    var response = await client.get(uri);
    if (response.statusCode == 200) {
      var json = response.body;
      return postFromJson(json);
    }
  }
}


class RemoteService {
{
  Future<List<Movie>?> getMovies(arrayMovie) async {
    var client = http.Client();
    var arrayJson = [];

    for (String movie in arrayMovie) {
      var uri = Uri.parse('https://www.omdbapi.com/?t=$movie&apikey=5161e29');

      var response = await client.get(uri);
      if (response.statusCode == 200) {
        var json = response.body;
        arrayJson.add(json);
      }
    }

    return movieFromJson(arrayJson.toString());
  }
}
}