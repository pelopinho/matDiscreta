/* O programa a seguir calcula a sequência de Fibonacci de acordo com o número de termos que o usuário determinará. */

import java.util.Scanner;

public class programa08{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        /* A seguinte mensagem é impressa ao usuário, este terá que digitar a quantidade de termos desejados */
        System.out.print("Digite a quantidade de termos da sequência de Fibonacci que você deseja gerar: ");
        int n = scanner.nextInt();

        System.out.println("Sequência de Fibonacci com " + n + " termos:");
        for (int i = 0; i < n; i++) {
            System.out.print(calcularFibonacci(i) + " ");
        }

        scanner.close();
    }

    /* A função "calcularFibonacci" recebe um número inteiro como parâmetro e retorna o termo da sequência de Fibonacci. Se este termo for 0 ou 1, a função retorna o número passado como parâmetro. */
    
    public static int calcularFibonacci(int numero) {
        if (numero <= 1) {
            return numero;
        } else {
            return calcularFibonacci(numero - 1) + calcularFibonacci(numero - 2);
        }
    }
}