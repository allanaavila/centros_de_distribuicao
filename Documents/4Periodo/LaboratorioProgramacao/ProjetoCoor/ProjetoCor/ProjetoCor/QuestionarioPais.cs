using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCor
{
    internal class QuestionarioPais
    {
        private int idQuestionarioPais;
        private string pergunta;

        public string Pergunta { get => pergunta; set => pergunta = value; }
        public int IdQuestionarioPais { get => idQuestionarioPais; set => idQuestionarioPais = value; }
    }
}
