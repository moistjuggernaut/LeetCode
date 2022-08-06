using System;
public class Program {
  public static void Main() {
    RomanToInt converter = new RomanToInt();
    Console.WriteLine(converter.GetInt("III"));
    Console.WriteLine(converter.GetInt("LVIII"));
    Console.WriteLine(converter.GetInt("MCMXCIV"));
    Console.ReadLine();
  }
}
