from unittest.mock import patch, MagicMock
from django.http import HttpRequest
from django.test import TestCase
from display.views import (
    get_template_dashboard,
)  # Reemplaza 'your_module' con el nombre de tu módulo


class TestGetTemplateDashboard(TestCase):
    @patch(
        "display.views.DecisionMachineForm"
    )  # Reemplaza 'apps.analytics' con el nombre de tu módulo
    def test_get_template_dashboard(self, mock_data_form):
        # Configura los objetos simulados
        mock_request = MagicMock(spec=HttpRequest)
        mock_request.POST = {}
        mock_request.META = {}
        mock_data_form.return_value = MagicMock()

        # Llama a la función que estás probando
        response = get_template_dashboard(mock_request)

        # Verifica que la respuesta es correcta
        self.assertEqual(response.status_code, 200)
        # Asegúrate de que los métodos se llamaron de la manera esperada
        mock_data_form.assert_called_once_with(mock_request.POST)
