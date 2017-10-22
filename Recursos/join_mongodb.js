var cursor = db.entidades.find({},{id:1,"labels.en":1,"claims":1}).pretty();
cursor.forEach(
  function(x) {
    try {
      var claims = x["claims"];
      print("##");
      for (var claim in claims) {
        for (var prop in x["claims"][claim]) {
          var relatedIDP = x["claims"][claim][prop]["mainsnak"]["property"];
          var cursorP = (db.entidades.find({id: relatedIDP}, {id: 1, "labels.en": 1}).pretty());
          if (!cursorP.hasNext()) {
            print(relatedIDP + " - No hay propiedad en la BD!");
          }
          while (cursorP.hasNext()) {
            var latest = cursorP.next();
            var stringP = relatedIDP + " - Propiedad: " + latest["labels"]["en"]["value"];
            print(stringP);
          }
          var relatedIDQ = "Q" + x["claims"][claim][prop]["mainsnak"]["datavalue"]["value"]["numeric-id"];
          var cursorQ = (db.entidades.find({id: relatedIDQ},{id: 1, "labels.en": 1}).pretty());
          if (!cursorQ.hasNext()) {
            print(relatedIDQ + " - No hay Q en la BD!");
          }
          while (cursorQ.hasNext()) {
            var latest = cursorQ.next();
            var stringQ = relatedIDQ + " - Q Label: " + latest["labels"]["en"]["value"];
            print(stringQ);
          }
        }
      }
      print("##");
    }
    catch(e) {
      // print("GG", e);
    }
  }
);
