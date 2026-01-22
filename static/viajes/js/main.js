// JavaScript para funcionalidades adicionales de la aplicación CONALCA

function toggleValidado(vehiculoId, checkbox) {
    const statusSpan = document.getElementById('status-' + vehiculoId);
    const originalChecked = checkbox.checked;
    
    // Deshabilitar el checkbox mientras se procesa
    checkbox.disabled = true;
    
    // Obtener el token CSRF de las cookies
    const csrftoken = getCookie('csrftoken');
    
    fetch(`/toggle-validado/${vehiculoId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            checkbox.checked = data.validado;
            if (statusSpan) {
                statusSpan.textContent = data.validado ? 'Validado' : 'Pendiente';
            }
        } else {
            // Revertir el cambio si hay error
            checkbox.checked = !originalChecked;
            alert('Error al actualizar el estado: ' + (data.error || 'Error desconocido'));
        }
    })
    .catch(error => {
        // Revertir el cambio si hay error
        checkbox.checked = !originalChecked;
        console.error('Error:', error);
        alert('Error al comunicarse con el servidor');
    })
    .finally(() => {
        checkbox.disabled = false;
    });
}

// Función auxiliar para obtener el token CSRF de las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
