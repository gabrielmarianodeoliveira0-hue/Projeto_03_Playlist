import streamlit as st

musicas = {
    "Michael Jackson": {
        "Billie Jean": "https://www.youtube.com/watch?v=Zi_XLOBDo_Y&list=RDZi_XLOBDo_Y",
        "Thriller": "https://www.youtube.com/watch?v=4V90AmXnguw&list=RD4V90AmXnguw",
    },
    "50 Cent": {
        "In Da Club": "https://www.youtube.com/watch?v=5qm8PH4xAss&list=RD5qm8PH4xAss",
        "Many Men": "https://www.youtube.com/watch?v=5D3crqpClPY&list=RD5D3crqpClPY",
    },
    "Billie Eilish": {
        "Birds of a Feather": "https://www.youtube.com/watch?v=V9PVRfjEBTI&list=RDV9PVRfjEBTI"
    },
}


st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("Selecione o artista",musicas.keys())
musicas_artista = musicas[artista]

st.title(artista)
video,sobre = st.tabs(['video','sobre'])
with video:
    for musica in musicas_artista.items():
        titulo, link = musica
        st.subheader(titulo) 
        st.video(link)

with sobre:
    if artista == "Michael Jackson":
        st.markdown("Teste")
        st.markdown("Michael Jackson foi um cantor, compositor e dançarino norte-americano.")
        st.markdown("Ele nasceu em 29 de agosto de 1958 e é conhecido como o 'Rei do Pop'.")
        st.markdown("Entre seus maiores sucessos estão 'Thriller', 'Billie Jean' e 'Beat It")
        st.markdown("Seu álbum 'Thriller' é um dos mais vendidos da história da música.")
        st.markdown("""
# Michael Jackson

**Michael Jackson** foi um cantor, compositor e dançarino norte-americano, conhecido mundialmente como o **"Rei do Pop"**.

Nascido em **29 de agosto de 1958**, ele se destacou por sua voz, coreografias inovadoras e videoclipes marcantes. Entre seus maiores sucessos estão:

- Thriller
- Billie Jean
- Beat It
- Smooth Criminal
- Black or White

O álbum **Thriller** é considerado um dos mais vendidos da história da música.

Michael Jackson deixou um legado duradouro na música, na dança e na cultura popular, influenciando artistas de diversas gerações.
""")
        st.image('https://www.estadao.com.br/resizer/v2/TLY3UELCKBAYTFPWE6NZKFGBN4.jpg?quality=80&auth=6f3f64703b3879fe1716ecb53cdd6fbbafc19b136d09ae8911e605c501c7edb5&width=380')
    
    elif artista == "50 Cent":
        st.markdown("""
# 50 Cent

**50 Cent**, nome artístico de **Curtis James Jackson III**, é um rapper, cantor, compositor, ator e empresário norte-americano.

Nascido em **6 de julho de 1975**, em Nova York, ele ganhou fama mundial no início dos anos 2000 com o álbum **Get Rich or Die Tryin'**, que inclui sucessos como:

- In da Club
- 21 Questions
- P.I.M.P.
- Candy Shop
- Just a Lil Bit

Além da música, 50 Cent também se destacou como ator e produtor de televisão, participando de diversos filmes e séries. Ele é reconhecido por sua influência no hip-hop e por seu sucesso nos negócios.

Seu trabalho continua inspirando artistas e fãs ao redor do mundo.
""")
        st.image('https://ligadoamusica.com.br/wp-content/uploads/2022/08/50-Cents.jpg')
        st.markdown("Teste 2")
    elif artista == "Billie Eilish":
        st.markdown("""
# Billie Eilish

**Billie Eilish Pirate Baird O'Connell**, conhecida artisticamente como **Billie Eilish**, é uma cantora e compositora norte-americana.

Nascida em **18 de dezembro de 2001**, em Los Angeles, Califórnia, ela ganhou destaque mundial com seu estilo musical único e sua voz marcante. Seu sucesso começou com a música **"Ocean Eyes"**, lançada em 2015.

Entre seus maiores sucessos estão:

- Bad Guy
- Happier Than Ever
- Ocean Eyes
- Everything I Wanted
- Lovely

Billie Eilish é reconhecida por suas letras criativas, seu estilo autêntico e por ter conquistado diversos prêmios importantes da música, incluindo vários Grammys. Ela se tornou uma das artistas mais influentes de sua geração.
""")
        st.markdown("Teste 3")
        st.image('https://m.media-amazon.com/images/I/71UeipBivfL._AC_UF1000,1000_QL80_.jpg')

    
