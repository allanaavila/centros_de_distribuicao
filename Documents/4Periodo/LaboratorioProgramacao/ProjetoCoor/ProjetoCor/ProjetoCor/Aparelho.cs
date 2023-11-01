using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCor
{
    internal class Aparelho
    {
        private int idAparelho;
        private string tipoAparelho;
        private string urlAparelho;

        public int IdAparelho { get => idAparelho; set => idAparelho = value; }
        public string TipoAparelho { get => tipoAparelho; set => tipoAparelho = value; }
        public string UrlAparelho { get => urlAparelho; set => urlAparelho = value; }
    }
}
