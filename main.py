# def main():
#     print("Hello from licenta!")


# if __name__ == "__main__":
#     main()

import streamlit as st
import streamlit.components.v1 as components
import os
import subprocess
from pathlib import Path

st.title("Geom8trie")
st.write("Invata si dezvolta-ti intuitia matematica prin animatii si figuri interactive pentru problema ta de geometrie")

st.write("Mai jos avem un exemplu simplu cu un cerc")
raza_cerc = st.slider("Alege raza cercului:",min_value=1.0,max_value=10.0,value=3.0,step=1.0)
culoare = st.selectbox("Alege culoarea:",["BLUE","GREEN","PINK","RED","YELLOW"])

if st.button("Animeaza"):
    st.info("Se genereaza")

    os.environ["MANIM_RAZA"]=str(raza_cerc)
    os.environ["MANIM_CULOARE"]=culoare

    comanda = ["manim","-ql","--media_dir","media","scene.py","CreateCircle"]

    process = subprocess.run(comanda, capture_output=True,text=True)

    if process.returncode!=0 :
        st.error("A aparut o eroare")
        st.code(process.stderr)
    else:
        st.success("E gata animatia")

        video_path = Path("media/videos/scene/480p15/CreateCircle.mp4")

        if video_path.exists():
            st.video(str(video_path),autoplay=True)
        else:
            st.error(f"Nu am gasit fisierul la {video_path}")


geogebra_id = st.text_input("Introdu Material ID:", value="xsPc5B4M")

ggb_url = f"https://www.geogebra.org/material/iframe/id/{geogebra_id}/width/600/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/true/ctl/false"

iframe_html = f"""
    <iframe 
        scrolling="no" 
        title="GeoGebra" 
        src="{ggb_url}" 
        width="100%" 
        height="500px" 
        style="border:0px;">
    </iframe>
    """

components.html(iframe_html, height=520) 