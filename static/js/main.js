const btnDelete = document.querySelectorAll('.btn-delete')

if (btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click',(e) => {
            if (!confirm('¿Está seguro de eliminar este producto?')) {
                e.preventDefault();
            }
        });
    });
}

const btnLimpiar = document.querySelectorAll('.btn-left')

if (btnLimpiar) {
    const btnArray = Array.from(btnLimpiar);
    btnArray.forEach((btn) => {
        btn.addEventListener('click',(e) => {
            if (!confirm('Se borrarán todos los productos ¿Desea eliminarlos?')) {
                e.preventDefault();
            }
        });
    });
}