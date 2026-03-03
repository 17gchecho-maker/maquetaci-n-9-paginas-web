$directory = "c:\Users\17gch\OneDrive\Escritorio\Checho\programación\diagramaMaquetación"
$cssFiles = Get-ChildItem -Path $directory -Filter *.css

$responsiveCss = @"

/* --- RESPONSIVE FIXES PARA MÓVIL Y TABLET --- */
@media screen and (max-width: 992px) {
    * {
        max-width: 100% !important;
    }
    
    body {
        overflow-x: hidden;
    }

    div, section, article, header, nav, footer {
        /* Prevenir que anchos fijos o márgenes grandes rompan el layout */
        margin-left: auto !important;
        margin-right: auto !important;
    }

    .container, .container-fluid, .row, .col-12, .col-sm-6, .col-md-8, .col-lg-8, .col-xl-6, .col-xxl-6, .col-sm-12, .col-md-4, .col-lg-4 {
        margin-left: 0 !important;
        margin-right: 0 !important;
        max-width: 100% !important;
    }

    /* Resetear márgenes enormes como margin: 250px 0px 0px 350px */
    .botonesInteriores, .botonesInterioresallado, .cuadradodeimagen, .cuadradodeimagen2, .lineasdetexto1, .lineasdetexto2, .lineasdetexto3, .lineasdetexto4, .lineasdetexto5, .cuadradodeimagen1, .cuadradodeimagen3, .cuadradodeimagenpequeña1, .lineadetexto, .lineadetextopequeña1, .lineadetextopequeña2, .botongrandesito {
        margin-left: auto !important;
        margin-right: auto !important;
        margin-top: 15px !important;
        margin-bottom: 15px !important;
    }

    /* Ajustar menús y headers para que no tengan padding/margin excesivos */
    .menu, .navbar {
        height: auto !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
    }

    .sidebar, .bloquePrincipal, .cuerpo, .contenido-principal {
        min-width: 100% !important;
        width: 100% !important;
        padding: 10px !important;
        margin: 10px 0 !important;
    }

    /* Centramos el logo para formatos pequeños */
    .logo {
        margin-left: auto !important;
        margin-right: auto !important;
    }
}
"@

foreach ($file in $cssFiles) {
    $content = Get-Content $file.FullName | Out-String
    if ($content -notmatch "\/\* --- RESPONSIVE FIXES PARA MÓVIL Y TABLET --- \*\/") {
        Add-Content -Path $file.FullName -Value $responsiveCss
    }
}
Write-Output "Appended responsive CSS to $($cssFiles.Count) files."
