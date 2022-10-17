using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace OSThreads
{
    internal static class MultiThreading
    {
        internal static void BruteHash(byte [] hash)
        {
            DateTime start = DateTime.Now;
            bool flag = false;
            Parallel.For(0, 26, a =>
            {
                SHA256 mySHA256 = SHA256.Create();
                byte[] password = new byte[5];
                password[0] = (byte)(97 + a);
                for (password[1] = 97; password[1] < 123; password[1]++)
                {
                    for (password[2] = 97; password[2] < 123; password[2]++)
                    {
                        for (password[3] = 97; password[3] < 123; password[3]++)
                        {
                            for (password[4] = 97; password[4] < 123; password[4]++)
                            {
                                byte [] hashed = mySHA256.ComputeHash(password);
                                if (!hash.SequenceEqual(hashed)) continue;
                                string passwordString = Encoding.ASCII.GetString(password);
                                Console.WriteLine($"Найден пароль {passwordString}, hash {BitConverter.ToString(hashed).Replace("-", string.Empty).ToLower()}");
                                Console.WriteLine(DateTime.Now - start);
                                flag = true;
                                break;
                            }

                            if (flag) break;
                        }

                        if (flag) break;
                    }

                    if (flag) break;
                }
            });
        }

        internal static void BruteHashFromFile(string path)
        {
            DateTime start = DateTime.Now;
            bool flag = false;
            byte[] hash = Program.StringHashToByteArray(File.ReadLines(path, Encoding.Default).First());
            Parallel.For(0, 26, a =>
            {
                SHA256 mySHA256 = SHA256.Create();
                byte[] password = new byte[5];
                password[0] = (byte)(97 + a);
                for (password[1] = 97; password[1] < 123; password[1]++)
                {
                    for (password[2] = 97; password[2] < 123; password[2]++)
                    {
                        for (password[3] = 97; password[3] < 123; password[3]++)
                        {
                            for (password[4] = 97; password[4] < 123; password[4]++)
                            {
                                byte[] hashed = mySHA256.ComputeHash(password);
                                if (!hash.SequenceEqual(hashed)) continue;
                                string passwordString = Encoding.ASCII.GetString(password);
                                Console.WriteLine($"Найден пароль {passwordString}, hash {BitConverter.ToString(hashed).Replace("-", string.Empty).ToLower()}");
                                Console.WriteLine(DateTime.Now - start);
                                flag = true;
                                break;
                            }

                            if (flag) break;
                        }

                        if (flag) break;
                    }

                    if (flag) break;
                }
            });
        }
    }
}
