from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    try:
        send_mail(
            'Test Email',
            'This is a test email.',
            'ivanochka.ivanoff@yandex.ru',
            ['aliensen65@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")
