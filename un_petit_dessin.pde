void setup() {
  size(500, 500);
}

int taille = 0;
String sens = "aggrandi";

void draw() {
  nettoieLeTerrain();
  definiLeSensDeGrossissementDuCercle();
  changeLaTailleDuCercle();
  dessineLeCercle();
}

void nettoieLeTerrain() {
   background(color(255, 204, 0));
}

String definiLeSensDeGrossissementDuCercle() {
  if (tailleSuperieureA(300)) {
    sens = "diminue";
  }
  if (tropPetit()) {
    sens = "aggrandi";
  }
  return sens;
}

void changeLaTailleDuCercle() {
  if (sens == "aggrandi") {
    taille = taille + 1;
  } else {
    taille = taille - 1;
  }
}

void dessineLeCercle() {
  fill(color(25, 25, 80));
  circle(width / 2, height / 2, taille);
}

boolean tailleSuperieureA(int tailleMax) {
  return taille >= tailleMax;
}

boolean tropPetit() {
  return taille <= 0;
}
