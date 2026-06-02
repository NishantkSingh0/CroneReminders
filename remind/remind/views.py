from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .utils import remindByMessage

@api_view(["GET"])
def run_reminders(request):
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