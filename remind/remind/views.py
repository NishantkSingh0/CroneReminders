from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
import os
from .utils import remindByMessage
from dotenv import load_dotenv
load_dotenv()

@api_view(["GET", "POST"])
@renderer_classes([JSONRenderer])
def run_reminders(request):
    secret = request.headers.get("CRON_KEY")

    if secret != os.getenv("CRON_SECRET"):
        return Response(
            {"error": "Unauthorized"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    try:
        result = remindByMessage()

        return Response(
            {
                "success": True,
                "message": "Reminders processed successfully",
                "data": result
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        # Cron-job.org and most schedulers detect failures from HTTP status codes.
        # Returning 500 will mark the execution as failed.
        return Response(
            {
                "success": False,
                "message": "Reminder processing failed",
                "error": str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )