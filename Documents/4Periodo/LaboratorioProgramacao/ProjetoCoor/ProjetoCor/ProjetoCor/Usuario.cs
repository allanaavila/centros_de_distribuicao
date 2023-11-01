using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;

namespace ProjetoCor
{
    internal class Usuario
    {
        private int idUsuario;
        private string nomeUsuario;
        private string email;
        private string telefone;
        private DateTime dataNascimento;
         

        public string NomeUsuario { get => nomeUsuario; set => nomeUsuario = value; }
        public string Email { get => email; set => email = value; }
        public string Telefone { get => telefone; set => telefone = value; }
        public DateTime DataNascimento { get => dataNascimento; set => dataNascimento = value; }
        public int IdUsuario { get => idUsuario; set => idUsuario = value; }
    }
}
