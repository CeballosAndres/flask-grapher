$(document).ready(function () {
    // Hacer que aparezca el select de Color solo si el tipo es de Barras
    $('#graph-type').change(function () {
        $(this).val() == 'Barras' || $(this).val() == 'Lineas' || $(this).val() == 'Puntos' ? $('#colors').show() : $('#colors').hide();
    });
});

