using System.Security.Cryptography;
using System.Text;

namespace OSThreads
{
    internal static class SingleThread
    {
        static SHA256 mySHA256 = SHA256.Create();

        internal static void BruteHash(byte[] hash)
        {
            DateTime start = DateTime.Now;
            bool flag = false;
            byte[] password = new byte[5];
            for (password[0] = 97; password[0] < 123; password[0]++)
            {
                for (password[1] = 97; password[1] < 123; password[1]++)
                {
                    for (password[2] = 97; password[2] < 123; password[2]++)
                    {
                        for (password[3] = 97; password[3] < 123; password[3]++)
                        {
                            for (password[4] = 97; password[4] < 123; password[4]++)
                            {
                                //password = Encoding.ASCII.GetBytes("mmmmm");
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
                if (flag) break;
            }
        }

        internal static void BruteHashFromFile(string path)
        {
            DateTime start = DateTime.Now;
            bool flag = false;
            byte[] hash = Program.StringHashToByteArray(File.ReadLines(path, Encoding.Default).First());
            byte[] password = new byte[5];
            for (password[0] = 97; password[0] < 123; password[0]++)
            {
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
                if (flag) break;
            }
        }
    }
}
