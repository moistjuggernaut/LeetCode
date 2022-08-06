using System;
using System.Collections.Generic;

public class RomanToInt
{
    public int GetInt(string s)
    {
        char[] chars = s.ToCharArray();
        var numberValues = new Dictionary<char, int>{
          {'I', 1},
          {'V', 5},
          {'X', 10},
          {'L', 50},
          {'C', 100},
          {'D', 500},
          {'M', 1000}
        };

        var sum = 0;
        for (int i = 0; i < chars.Length; i++)
        {
            if (i != chars.Length - 1)
            {
                if (numberValues[chars[i]] < numberValues[chars[i + 1]])
                {
                    sum -= numberValues[chars[i]];
                }
                else
                {
                    sum += numberValues[chars[i]];
                }
            }
            else
            {
                sum += numberValues[chars[i]];
            }
        }
        return sum;
    }
}