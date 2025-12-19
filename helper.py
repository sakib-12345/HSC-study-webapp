
def pdf_view(pdf_url):
    return f"""
    <style>
        .pdf-wrapper {{
            position: relative;
            width: 100%;
            height: 400px;
            background: black;
        }}

        .pdf-wrapper iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}

        .fullscreen-btn {{
            position: absolute;
            top: 12px;
            right: 12px;
            z-index: 10000;
            padding: 8px 12px;
            background: rgba(0,0,0,0.7);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
        }}
    </style>

    <div class="pdf-wrapper" id="pdfWrapper">
        <button class="fullscreen-btn" onclick="toggleFullscreen()">⛶</button>
        <iframe src="{pdf_url}" allowfullscreen></iframe>
    </div>

    <script>
        function toggleFullscreen() {{
            const wrapper = document.getElementById("pdfWrapper");

            if (!document.fullscreenElement) {{
                wrapper.requestFullscreen().catch(err => {{
                    alert("Fullscreen failed: " + err.message);
                }});
            }} else {{
                document.exitFullscreen();
            }}
        }}
    </script>

    """

