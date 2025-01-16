using System;
using System.IO;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter your message");
        string original = Console.ReadLine();
        string hardcodedValue = "this_string_is_relevant";

        byte[] derivedKey, derivedIV;
        DeriveKeyAndIV(hardcodedValue, out derivedKey, out derivedIV);

        string encrypted = Encrypt(original, derivedKey, derivedIV);
        Console.WriteLine("Encrypted: " + encrypted);

    }
    public static void DeriveKeyAndIV(string hardcodedValue, out byte[] key, out byte[] iv)
    {
        using (SHA256 sha256 = SHA256.Create())
        {
            byte[] hash = sha256.ComputeHash(Encoding.UTF8.GetBytes(hardcodedValue));
            key = new byte[16];
            Array.Copy(hash, 0, key, 0, 16);
            iv = new byte[16];
            Array.Copy(hash, 16, iv, 0, 16);
        }
    }
    public static string Encrypt(string plainText, byte[] key, byte[]IV)
    {
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.IV = IV; 

            using (MemoryStream ms = new MemoryStream())
            using (CryptoStream cs = new CryptoStream(ms, aes.CreateEncryptor(), CryptoStreamMode.Write))
            {
                using (StreamWriter sw = new StreamWriter(cs))
                {
                    sw.Write(plainText);
                }
                return Convert.ToBase64String(ms.ToArray());
            }
        }
    }
}

