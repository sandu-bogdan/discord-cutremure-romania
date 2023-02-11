# discord-cutremure-romania
Bot Discord pentru cutremurele din Romania
Acest bot a fost creat din curiozitatea pentru miscarea seismologica in Romania. <br>
*Disclainer: Acesta nu este un bot oficial, ca urmare nu ne putem asuma corectitudinea datelor furnizate de aceasta platforma. Tratati ca atare orice informatie, in scop pur informativ.

<h1>Cum functioneaza?</h1>
Pentru o functionare corecta este necesar un server Apache cu PHP, precum si un domeniu sau un IP public. 
Serverul Apache v-a servi drept intermediar pentru datele ce vor fi servite de acesta catre bot-ul Discord. Scriptul PHP functioneaza ca un API, ce returneaza datele prelucrate necesare.
<br><br>

La fiecare 4 secunde, scriptul Python preia datele din API-ul furnizat, apoi le verifica. Daca indeplineste criteriile necesare, mesajul este trimis pe canalul setat.

<h1> Exemple de mesaje </h1>

- Cutremur nou inregistrat:
![image](https://user-images.githubusercontent.com/12985385/218282284-f04c5d7e-5e7e-4144-b770-cb3b02a974fb.png)

- Cutremur mai mare de 4.5 grade:
![image](https://user-images.githubusercontent.com/12985385/218282267-3b491841-eae8-4170-a89d-3440f0a1c3e1.png)

