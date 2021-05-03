from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Room, Chat
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'AlphaChats/home.html')

@csrf_exempt
def create_room(request):
    if(request.method) == 'POST':
                # capturing ip 
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        room_name = request.POST.get('room_name')
        if (' ' in room_name):
            return HttpResponse("Room name must not contain any spaces!")
        elif ('<' in room_name or '>' in room_name or '/' in room_name):
        	return HttpResponse(r"Room name must not contain characters '<, >, /, (), {},[]'")    
        
        else:
            all_rooms = Room.objects.all()
            
            for i in all_rooms:
                if room_name == i.room_name:
                    return HttpResponse('Room already exists!')
                else:
                    pass
            room_link = f'https://alphachats.cf/room-{room_name}' 
            ip_address = ip   
            room = Room(room_name=room_name, room_link=room_link, ip_address=ip_address)
            room.save()
            return HttpResponse('Success! You can chat now.')
    else:
        raise Http404




def room(request, rn):
    print(rn)
    if ("<" in rn or ">" in rn):
    	return HttpResponse("<p>Room doesn't exist</p>")
    if(Room.objects.filter(room_name__icontains=rn)):
        # chats = Chat.objects.filter(room_name__room_name=rn) 
        return render(request, 'AlphaChats/room.html', {'roomname':rn})
    else:
        return HttpResponse("<p>Room doesn't exist</p>")

@csrf_exempt
def chatwork(request):
    if request.method == "POST":
        # capturing ip 
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        room_name = request.POST.get('room_name')
        chater = Chat.objects.filter(room_name__room_name=room_name)
    
        res = ""
        for c in chater:
            if c.ip_address == ip:
                res = res + f"""
                <div class="d-flex align-items-center text-right justify-content-end">
                    <div class="pr-2">
                        <span class="name">{c.person}</span>
                        <p class="msg">{c.message}</p>
                    </div>
                    <div>
                        <img src="https://cdn.pixabay.com/photo/2017/07/18/23/23/user-2517433_960_720.png" width="30" class="img1"/>
                    </div>
                </div>"""
            else:    
                res = res + f"""
                    <div class="d-flex align-items-center">
                        <div class="text-left pr-1"><img src="https://cdn.pixabay.com/photo/2017/07/18/23/23/user-2517433_960_720.png" width="30" class="img1"/>
                        </div>
                        <div class="pr-2 pl-1"> <span class="name">{c.person}</span>
                            <p class="msg">{c.message}</p>
                        </div>
                    </div>
                    """
        return HttpResponse(res)
    else:
        return redirect('/')    

@csrf_exempt
def get_msg(request):
    if request.method == "POST":
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        print(ip)
        msg = Chat(
            room_name = Room.objects.get(room_name=request.POST.get('room_name')),
            message = request.POST.get('message'),
            person = request.POST.get('person'),
            ip_address = ip
        )
        msg.save()
        
        return HttpResponse('success')
    else:
        return redirect('/')        