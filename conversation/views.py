from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .models import Conversation, ConversationMessage
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

def detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    messages = ConversationMessage.objects.filter(conversation=conversation).order_by('created_at')

    # Handle POST form submission
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    # Assign colors to other members
    palette = [
        "bg-green-200 dark:bg-green-600",
        "bg-yellow-200 dark:bg-yellow-600",
        "bg-purple-200 dark:bg-purple-600",
        "bg-pink-200 dark:bg-pink-600",
        "bg-indigo-200 dark:bg-indigo-600",
    ]

    member_colors = {}
    other_members = [m for m in conversation.members.all() if m != request.user]
    for i, member in enumerate(other_members):
        member_colors[member.id] = palette[i % len(palette)]

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'messages': messages,
        'form': form,
        'member_colors': member_colors,
    })
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    # Prevent the item owner from starting a conversation with themselves
    if item.created_by == request.user:
        return redirect('dashbord:index')  # fix spelling if needed

    # Check for existing conversation
    conversations = Conversation.objects.filter(item=item, members__in=[request.user.id])

    if conversations.exists():
        conversation = conversations.first()
        return redirect('conversation:detail', pk=conversation.id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)

            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {'form': form})

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {'conversations':conversations})

