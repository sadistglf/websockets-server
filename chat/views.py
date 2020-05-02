from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# Create your views here.

def index(request):
    return JsonResponse({'foo': 'bar'})

@csrf_exempt
def postMessage(request, roomId, username):
	if request.method == 'GET':
		return JsonResponse({'status': 'error', 'msg': "GET method not supported", data: {}})

	channel_layer = get_channel_layer()
	chat_name = 'chat_'+roomId
	## If the post is sent as a form-data we use the following line
	# message = request.POST.get('message', "No message received")
	## if the post is sent as a raw-body we need to manually parse it
	body = json.loads(request.body.decode("utf-8"))
	message = body['message']
	response = {
		"text": message,
		"username": username
	}
	async_to_sync(channel_layer.group_send)(chat_name, {"type": "chat.message", "message": json.dumps(response)})
	return JsonResponse({'username': username, 'roomId': roomId})