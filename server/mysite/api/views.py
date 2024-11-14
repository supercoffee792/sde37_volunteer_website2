import datetime
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Volunteer, Event
from .serializers import *
from rest_framework.views import APIView
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.units import inch

# Login / Signup operations
@api_view(['POST'])
def login(request):
    volunteer_data = request.data
    serializer = VolunteerLoginSerializer(data=volunteer_data)
    if serializer.is_valid():
        user = serializer.validated_data
        serializer = VolunteerSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh":str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup(request):
    volunteer_data = request.data
    serializer = VolunteerSignupSerializer(data=volunteer_data)
    if serializer.is_valid():
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VolunteerLogout(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class VolunteerTokenInfo(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VolunteerSerializer

    def get(self, request, *args, **kwargs):
        volunteer_info = self.get_volunteer_info()
        serializer = self.get_serializer(volunteer_info)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_volunteer_info(self):
        return self.request.user

# Volunteer view operations
@api_view(['GET'])
def get_volunteers(request):
    volunteers = Volunteer.objects.all()
    serialized_data = VolunteerSerializer(volunteers, many=True).data
    return Response(serialized_data)

@api_view(['POST'])
def create_volunteer(request):
    volunteer_data = request.data
    serializer = VolunteerSerializer(data=volunteer_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'DELETE', 'PATCH'])
def manage_volunteer(request, pk):
    try:
        volunteer = Volunteer.objects.get(pk=pk)
    except Volunteer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        volunteer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = VolunteerSerializer(volunteer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = VolunteerSerializer(volunteer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_notifications(request, pk):
    try:
        volunteer = Volunteer.objects.get(pk=pk)
        notifications = volunteer.notifications.split(',') if volunteer.notifications else []
        return Response({'notifications': notifications})
    
    except Volunteer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
# Event view operations
@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serialized_data = EventSerializer(events, many=True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_one_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        serialized_data = EventSerializer(event).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_event(request):
    event_data = request.data
    serializer = EventSerializer(data=event_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def manage_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        event_data = request.data
        serializer = EventSerializer(event, data=event_data)
        if serializer.is_valid():
            serializer.save()

            # Send notification to all volunteers associated w/ the event
            notification = f"The organizer has made changes to event: {event.name}"
            for volunteer in event.volunteers.all():
                current_notifications = volunteer.notifications.split(',') if volunteer.notifications else []
                current_notifications.append(notification)

                volunteer.notifications = ','.join(filter(None, current_notifications))
                volunteer.save()


            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view for volunteers to signup for events
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def event_signup(request, pk):
    try:
        event = get_object_or_404(Event, id=pk)
        if request.user not in event.volunteers.all():
            event.volunteers.add(request.user)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Successfully signed up for the event!"}, status=status.HTTP_200_OK)

    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="volunteer_report.pdf"'
    
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    styles = getSampleStyleSheet()
    
    def draw_header(title, y_position):
        p.setFont("Helvetica-Bold", 16)
        p.drawString(50, y_position, title)
        p.setLineWidth(1)
        p.line(50, y_position - 5, width - 50, y_position - 5)
        return y_position - 30

    def add_page():
        p.showPage()
        p.setFont("Helvetica", 12)
        return height - 50

    # Volunteer Participation Report
    y_position = height - 50
    y_position = draw_header("Volunteer Participation Report", y_position)
    
    volunteers = Volunteer.objects.all().prefetch_related('events')
    
    # Volunteer
    for volunteer in volunteers:
        if y_position < 100:
            y_position = add_page()
            
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, y_position, f"Volunteer: {volunteer.profilename}")
        p.setFont("Helvetica", 10)
        y_position -= 15
        p.drawString(50, y_position, f"Email: {volunteer.email}")
        y_position -= 20
        
        # Event History
        events = volunteer.events.all()
        if events:
            data = [["Event Name", "Date", "Location", "Urgency"]]
            for event in events:
                data.append([
                    event.name,
                    event.date.strftime("%Y-%m-%d"),
                    event.location,
                    event.urgency
                ])
            
            table = Table(data, colWidths=[2*inch, 1.2*inch, 2*inch, 1*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            
            table.wrapOn(p, width, height)
            table.drawOn(p, 50, y_position - 20 - (len(data) * 20))
            y_position = y_position - 40 - (len(data) * 20)
        else:
            p.drawString(50, y_position, "No event participation history")
            y_position -= 20
            
        y_position -= 20
    
    # Event Summary Report
    p.showPage()
    y_position = height - 50
    y_position = draw_header("Event Summary Report", y_position)
    
    events = Event.objects.all().prefetch_related('volunteers')
    
    # Event
    for event in events:
        if y_position < 100:
            y_position = add_page()
            
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, y_position, f"Event: {event.name}")
        p.setFont("Helvetica", 10)
        y_position -= 15
        p.drawString(50, y_position, f"Date: {event.date.strftime('%Y-%m-%d')}")
        y_position -= 15
        p.drawString(50, y_position, f"Location: {event.location}")
        y_position -= 15
        p.drawString(50, y_position, f"Urgency: {event.urgency}")
        y_position -= 20
        
        # Volunteers for the event
        volunteers = event.volunteers.all()
        if volunteers:
            data = [["Volunteer Name", "Email"]]
            for volunteer in volunteers:
                data.append([
                    volunteer.profilename,
                    volunteer.email
                ])
            
            table = Table(data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 1.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            
            table.wrapOn(p, width, height)
            table.drawOn(p, 50, y_position - 20 - (len(data) * 20))
            y_position = y_position - 40 - (len(data) * 20)
        else:
            p.drawString(50, y_position, "No volunteers registered for this event")
            y_position -= 20
            
        y_position -= 20
    
    p.save()
    return response