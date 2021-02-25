![](https://i.postimg.cc/Vv1rDTPQ/youtube-peertube-scaled.png "YouTube to PeerTube")

# YouTube -> PeerTube
Estos scripts están escritos en Python3, descarga (videos/ playlists) de YouTube y los carga a [PeerTube](https://joinpeertube.org). Puedes usarlo para respaldar videos que YouTube potenciales a ser eliminados o censurados. 

### ¿Qué es PeerTube?
`PeerTube` es una aplicación web de software libre, descentralizada, federada y que usa la tecnología peer-to-peer para reducir la carga de los servidores individuales al visualizar videos. El objetivo del proyecto es proveer una alternativa a las plataformas centralizadas como `YouTube`, `Vimeo` y `Dailymotion`.

## ¿Comó configurar el entorno?
1. Crear una cuenta en alguna instancia de PeerTube. Para respaldar videos educativos les recomiendo [[TubEdu.org]](https://tubedu.org/).
    > Recordar `username`, `password`, `nombre del canal` y `url(instancia)`.  
2. Crear una cuenta en [[Gesis]](tps://login.gesis.org/), no olvides verificar tu correo con la ulr que te enviaran.
    - Luego de registrarte dirígete a [[Notebooks Gesis]](https://notebooks.gesis.org/) e inicia secion con el correo y la contraseña con las que te registraste en gesis.

    - Copiar y pegar la url como se muestra en la imagen y luego pinchar en `launch`.
    ```bash
    https://github.com/ivansaul/YouTube-PeerTube.git
    ```
    ![Alt text](https://i.postimg.cc/ZYpDnDb8/ge2.png)
    - Modificar la url. Remplazar `tree` por `lab`.
    ![Alt text](https://i.postimg.cc/T3Npb0d0/g4.png)
    - Si todos los pasos anteriores no te dio ningun error te mostrara una computadora Linux virtual.
    ![](https://i.postimg.cc/mDLL6Fgk/g5.png)
    
3. Click derecho y renombrar el archivo `config_example.toml` a `config.toml`.
    ![](https://i.postimg.cc/tg0tP9C2/g6-png.png)

4. Doble click para editar el archivo `config.toml`. Remplaza los campos con tus credenciales creadas en el `paso 1`. Luego de editar el archivo debería quedarte algo asi:
    ```md
    peertube_instance = "https://tubedu.org"
    peertube_channel = "San Marcos"
    peertube_username = "pablito"
    peertube_password = "pablito123"
    peertube_channel_category = "education"
    default_lang = "spanish"
    delete_videos = "False"
    privacy_videos = "public"
    ```
    > Para guardar los cambios `File` -> `Save File`. Para más información sobre los campos [[Leer]](README.md)

5. Si desea descargar una `lista de videos` de YouTube y luego subirlos a PeerTube.
    - Abre `videos.txt` y pegué las URL de los videos de YouTube que desea cargar en PeeTube.
    - Ejecute `videos.py`.
    - El script le pedirá el nombre de la lista de reproducción donde desea que se guarden los videos.

6. Si desea descargar una `lista de Playlists` de YouTube y luego cargarlas en PeerTube.
     - Abra `playlist.txt` y pegue las URL de las listas de reproducción de YouTube que desea cargar en PeeTube.
     - Ejecute `playlist.py`. 
     
## ¿Comó ejecutar los scripts?

1. Abre una terminal.
    ![](https://i.postimg.cc/FHtb2953/g7.png)

2. Escribir `python` seguido del nombre del script, por ejemplo:
    ```bash
    python videos.py
    ```
    ```bash
    python playlist.py
    ```
    ![](https://i.postimg.cc/CxSTHnMQ/g8.png)

3. Eso es todo 😊.