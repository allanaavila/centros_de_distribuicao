using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCor
{
    internal class Jogos
    {
        private int idJogos;
        private string nomeJogos;
        private string urlJogos;

        public string NomeJogos { get => nomeJogos; set => nomeJogos = value; }
        public string UrlJogos { get => urlJogos; set => urlJogos = value; }
        public int IdJogos { get => idJogos; set => idJogos = value; }
    }
}
