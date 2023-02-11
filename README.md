# discord-cutremure-romania
Bot Discord pentru cutremurele din Romania
Acest bot a fost creat din curiozitatea pentru miscarea seismologica in Romania. <br>
*Disclainer: Acesta nu este un bot oficial, ca urmare nu ne putem asuma corectitudinea datelor furnizate de aceasta platforma. Tratati ca atare orice informatie, in scop pur informativ.

<h1>Cum functioneaza?</h1>
Pentru o functionare corecta este necesar un server Apache cu PHP, precum si un domeniu sau un IP public. 
Serverul Apache v-a servi drept intermediar pentru datele ce vor fi servite de acesta catre bot-ul Discord. Scriptul PHP functioneaza ca un API, ce returneaza datele prelucrate necesare.
<br><br>

La fiecare 4 secunde, scriptul Python preia datele din API-ul furnizat, apoi le verifica. Daca indeplineste criteriile necesare, mesajul este trimis pe canalul setat.
![image](https://user-images.githubusercontent.com/12985385/218281961-7ffe374f-04c3-423c-8fa8-73958703cf51.png)
