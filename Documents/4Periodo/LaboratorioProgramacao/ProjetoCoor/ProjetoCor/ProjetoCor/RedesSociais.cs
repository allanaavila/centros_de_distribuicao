using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCor
{
    internal class RedesSociais
    {
        private int idRedesSociais;
        private string nomeRedeSocial;
        private string urlRedesSociais;

        public string NomeRedeSocial { get => nomeRedeSocial; set => nomeRedeSocial = value; }
        public string UrlRedesSociais { get => urlRedesSociais; set => urlRedesSociais = value; }
        public int IdRedesSociais { get => idRedesSociais; set => idRedesSociais = value; }
    }
}
