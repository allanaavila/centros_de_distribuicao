using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCor
{
    internal class Resposta
    {
        private int idResposta;
        private int qtdDias;
        private float qtdHoras;
        private string periodo;

        public int QtdDias { get => qtdDias; set => qtdDias = value; }
        public float QtdHoras { get => qtdHoras; set => qtdHoras = value; }
        public string Periodo { get => periodo; set => periodo = value; }
        public int IdResposta { get => idResposta; set => idResposta = value; }
    }
}
