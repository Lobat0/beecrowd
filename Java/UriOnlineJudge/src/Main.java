import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //1000
        //System.out.println("Hello World!");

        //1001
        /*
        Scanner teclado = new Scanner(System.in);
        int A = teclado.nextInt();
        int B = teclado.nextInt();
        int X = A + B;
        System.out.println("X = " + X);
         */

        //1002
        /*
        Scanner teclado = new Scanner(System.in);
        double pi = 3.14159;
        double r = teclado.nextDouble();
        double a = pi * r * r;
        System.out.printf("A=%.4f\n",a);
         */

        //1003
        /*
        Scanner teclado = new Scanner(System.in);
        int A = teclado.nextInt();
        int B = teclado.nextInt();
        int SOMA = A + B;
        System.out.println("SOMA = " + SOMA);
         */

        //1004
        /*
        Scanner teclado = new Scanner(System.in);
        int A = teclado.nextInt();
        int B = teclado.nextInt();
        int PROD = A * B;
        System.out.println("PROD = " + PROD);
         */

        //1005
        /*
        Scanner teclado = new Scanner(System.in);
        float A = teclado.nextFloat();
        float B = teclado.nextFloat();
        double MEDIA = (A*3.5 + B*7.5) / 11;
        System.out.printf("MEDIA = %.5f\n", MEDIA);
         */

        //1006
        /*
        Scanner teclado = new Scanner(System.in);
        float A = teclado.nextFloat();
        float B = teclado.nextFloat();
        float C = teclado.nextFloat();
        double MEDIA = (A*2 + B*3 + C*5) / 10;
        System.out.printf("MEDIA = %.1f\n", MEDIA);
         */

        //1007
        /*
        Scanner teclado = new Scanner(System.in);
        int A = teclado.nextInt();
        int B = teclado.nextInt();
        int C = teclado.nextInt();
        int D = teclado.nextInt();
        int DIFERENCA = (A* B - C * D);
        System.out.println("DIFERENCA = " + DIFERENCA);
         */

        //1008
        /*
        Scanner teclado = new Scanner(System.in);
        int A = teclado.nextInt();
        int B = teclado.nextInt();
        float C = teclado.nextFloat();
        System.out.println("NUMBER = " + A);
        System.out.printf("SALARY = U$ %.2f\n", (B * C));
         */

        //1009
        /*
        Scanner teclado = new Scanner(System.in);
        String A = teclado.next();
        float B = teclado.nextFloat();
        float C = teclado.nextFloat();
        double sal = B + (C * 0.15);
        System.out.printf("TOTAL = R$ %.2f\n", sal);
         */

        //1010
        /*
        Scanner teclado = new Scanner(System.in);
        int cod1 = teclado.nextInt(); int num1 = teclado.nextInt(); float prec1 = teclado.nextFloat();
        int cod2 = teclado.nextInt(); int num2 = teclado.nextInt(); float prec2 = teclado.nextFloat();

        double total = (num1 * prec1) + (num2 * prec2);
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", total);

         */

        //1011
        /*
        Scanner teclado = new Scanner(System.in);
        float raio = teclado.nextFloat();
        double area = (4.0/3.0) * 3.14159 * Math.pow(raio, 3);
        System.out.printf("VOLUME = %.3f\n", area);

         */

        //1012
        /*
        Scanner teclado = new Scanner(System.in);
        float a = teclado.nextFloat(); float b = teclado.nextFloat(); float c = teclado.nextFloat();

        double triangulo = (a * c) / 2;
        double circulo = 3.14159 * Math.pow(c, 2);
        double trapezio = ((a + b) * c) / 2;
        double quadrado = Math.pow(b, 2);
        double retangulo = a * b;

        System.out.printf("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f\n", triangulo, circulo, trapezio, quadrado, retangulo);

         */

        //1013
        /*
        Scanner teclado = new Scanner(System.in);
        int a = teclado.nextInt(); int b = teclado.nextInt(); int c = teclado.nextInt();
        int maiorab = (a + b + Math.abs(a-b)) / 2;
        int maior = (maiorab + c + Math.abs(maiorab-c)) / 2;
        System.out.println(maior + " eh o maior");

         */

        //1014
        /*
        Scanner teclado = new Scanner(System.in);
        int x = teclado.nextInt();
        float y = teclado.nextFloat();

        double consumo = x / y;
        System.out.printf("%.3f km/l\n", consumo);

         */

        //1015
        /*
        Scanner teclado = new Scanner(System.in);
        float x1 = teclado.nextFloat(); float y1 = teclado.nextFloat();
        float x2 = teclado.nextFloat(); float y2 = teclado.nextFloat();

        double distancia = Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));

        System.out.printf("%.4f\n", distancia);

         */

        //1016
        /*
        Scanner teclado = new Scanner(System.in);
        int distancia = teclado.nextInt();

        int tempo = distancia * 2;
        System.out.printf("%d minutos\n", tempo);

         */

        //1017
        /*
        Scanner teclado = new Scanner(System.in);
        int tempo = teclado.nextInt();
        int velocidade = teclado.nextInt();

        double kml = (tempo * velocidade) / 12.0;
        System.out.printf("%.3f\n", kml);

         */

        //1018
        /*
        Scanner teclado = new Scanner(System.in);
        int valor = teclado.nextInt();

        //int[] a = {100, 50, 20, 10, 5, 2, 1};
        //System.out.println(valor);
       // for(int i=0; i < a.length; i++){
            //System.out.println(valor / a[i] + " nota(s) de R$ " + a[i]+",00");
            //System.out.printf("%d nota(s) de R$ %d,00\n", valor / a[i], a[i]);
           // valor -= (valor / a[i]) * a[i];
           // }



        System.out.println(valor / 100 + " nota(s) de R$ 100,00");
        valor %= 100;
        System.out.println(valor / 50 + " nota(s) de R$ 50,00");
        valor %= 50;
        System.out.println(valor / 20 + " nota(s) de R$ 20,00");
        valor %= 20;
        System.out.println(valor / 10 + " nota(s) de R$ 10,00");
        valor %= 10;
        System.out.println(valor / 5 + " nota(s) de R$ 5,00");
        valor %= 5;
        System.out.println(valor / 2 + " nota(s) de R$ 2,00");
        valor %= 2;
        System.out.println(valor + " nota(s) de R$ 1,00");

        */

        //1019
        /*
        Scanner teclado = new Scanner(System.in);
        int segundos = teclado.nextInt();
        int hr; int min; int seg;
        hr = segundos / 3600;
        min = (segundos % 3600) / 60;
        if(min > 59){
            min -= 60;
            hr += 1;
        }
        seg = ((segundos % 3600) - min * 60);
        System.out.printf("%d:%d:%d\n", hr, min, seg);

         */

        //1020
        /*
        Scanner teclado = new Scanner(System.in);
        int dias = teclado.nextInt();
        int ano; int mes; int dia;
        ano = dias / 365;
        mes = (dias % 365) / 30;
        dia = (dias % 365) - (mes * 30);
        System.out.println(ano + " ano(s)");
        System.out.println(mes + " mes(es)");
        System.out.println(dia + " dia(s)");

         */

        //1021

        Scanner teclado = new Scanner(System.in);
        float valor = teclado.nextFloat();

        int[] notas = {100, 50, 20, 10, 5, 2};
        double[] modedas = {1, 0.50, 0.25, 0.10, 0.05, 0.01};

        System.out.println("NOTAS:");
        for (int nota : notas) {
            int quantidadeNotas = (int) valor / nota;
            System.out.printf("%d nota(s) de R$ %.2f\n", quantidadeNotas, (double) nota);
            valor -= quantidadeNotas * nota;

        }





    }
}
