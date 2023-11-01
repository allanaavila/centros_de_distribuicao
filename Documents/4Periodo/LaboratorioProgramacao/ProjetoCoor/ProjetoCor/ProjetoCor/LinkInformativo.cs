using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCor
{
    internal class LinkInformativo
    {
        private int idLinkInformativo;
        private string descricaoInformativo;
        private string urlllinkInformativo;

        public int IdLinkInformativo { get => idLinkInformativo; set => idLinkInformativo = value; }
        public string DescricaoInformativo { get => descricaoInformativo; set => descricaoInformativo = value; 
        public string UrlllinkInformativo { get => urlllinkInformativo; set => urlllinkInformativo = value; }
    }
}
