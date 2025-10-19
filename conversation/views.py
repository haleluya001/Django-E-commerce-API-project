from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation, ConversationMessage
from .forms import ConversationMessageForm

# Conversation Detail View
@login_required
def detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    messages = ConversationMessage.objects.filter(conversation=conversation).order_by('created_at')

    # Handle new message submission
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

    # Assign colors to other members for styling
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


# Start New Conversation
@login_required
def new_conversation(request, item_pk):  # must match urls.py
    item = get_object_or_404(Item, pk=item_pk)

    # Prevent self-conversation
    if item.created_by == request.user:
        return redirect('dashbord:index')  # fix spelling if needed

    # Check if a conversation already exists
    conversation = Conversation.objects.filter(item=item, members=request.user).first()
    if conversation:
        return redirect('conversation:detail', pk=conversation.pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            # Create a new conversation
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user, item.created_by)

            # Save the first message
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()

            return redirect('conversation:detail', pk=conversation.pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form,
        'item': item
    })


# Inbox view
@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members=request.user).distinct()
    return render(request, 'conversation/inbox.html', {'conversations': conversations})
