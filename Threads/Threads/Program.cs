using System.Text;
using System.Text.RegularExpressions;


namespace OSThreads
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            while (true)
            {
                bool flag = HashChoiceEnter();

                Console.WriteLine("Выберете принцип работы:");
                Console.WriteLine("1. Однопоточный");
                Console.WriteLine("2. Многопоточный");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        if (flag)
                        {
                           byte[] hash = StringHashToByteArray(HashEnter());
                           SingleThread.BruteHash(hash);
                        }
                        else
                        {
                            string path = HashesReadFromFile();
                            SingleThread.BruteHashFromFile(path);
                        }

                        break;
                    case "2":
                        if (flag)
                        {
                            byte[] hash = StringHashToByteArray(HashEnter());
                            MultiThreading.BruteHash(hash);
                        }  
                        else
                        {
                            string path = HashesReadFromFile();
                            MultiThreading.BruteHashFromFile(path);
                        }

                        break;
                    default:
                        Console.Clear();
                        Console.WriteLine("Неверное значение");
                        break;
                }
            }
        }
        public static byte[] StringHashToByteArray(string s)
        {
            return Enumerable.Range(0, s.Length / 2)
              .Select(i => (byte)Convert.ToInt16(s.Substring(i * 2, 2), 16)).ToArray();
        }

        private static string HashesReadFromFile()
        {
            while (true)
            {
                Console.WriteLine("Введите путь файла с хэшем");
                string path = Console.ReadLine()?.Trim('"');
                while (string.IsNullOrEmpty(path) || path.Trim() == string.Empty)
                {
                    Console.WriteLine("Введите путь файла с хэшем");
                    path = Console.ReadLine()?.Trim('"');
                }

                if (File.Exists(path)) return path;

                Console.WriteLine("Такого пути не существует");
            }
        }

        private static string HashEnter()
        {
            string hash = null;
            while (string.IsNullOrEmpty(hash) || hash.Trim() == string.Empty && !Regex.IsMatch(hash, @"^[A-Fa-f0-9]*$"))
            {
                Console.WriteLine("Введите хэш");
                hash = Console.ReadLine();
                if (!Regex.IsMatch(hash, @"^[A-Fa-f0-9]*$"))
                    Console.WriteLine("Хэш может содержать только цифры и буквы от A до F в любом регистре");
            }
            return hash;
        }

        private static bool HashChoiceEnter()
        {
            while(true)
            {
                Console.WriteLine("Как ввести хэш");
                Console.WriteLine("1. Ввести вручную хэш");
                Console.WriteLine("2. Считать хэш из файла");
                string choice = Console.ReadLine();
                switch (choice)
                {
                    case "1":
                        return true;
                    case "2":
                        return false;
                    default:
                        Console.Clear();
                        Console.WriteLine("Неверное значение");
                        break;
                }
            } 
        }
    }
}