#include "Ai_AP3216_AmbientLightAndProximity.h"

// Pines personalizados (ajusta según tu conexión)
Ai_AP3216_AmbientLightAndProximity aps = Ai_AP3216_AmbientLightAndProximity(D2, D1);

void setup() {
  Serial.begin(115200);
  aps.begin();
  aps.startAmbientLightAndProximitySensor();
}

void loop() {
  long alsValue = aps.getAmbientLight(); // Valor de luz en lux

  // Convertir lux a irradiancia solar estimada en W/m²
  float irradianciaSolar = alsValue * 0.0079;

  Serial.print("Luz ambiental (lux): ");
  Serial.print(alsValue);
  Serial.print(" | Radiación solar estimada (W/m²): ");
  Serial.println(irradianciaSolar);

  delay(1000);
}
