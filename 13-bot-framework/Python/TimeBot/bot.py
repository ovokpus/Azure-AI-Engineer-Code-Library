# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from datetime import datetime
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        input_message = turn_context.activity.text
        response_message = 'Ask me what the time is.'
        if (input_message.lower().startswith('what') and 'time' in input_message.lower()):
            now = datetime.now()
            response_message = 'The time is {}:{:02d}.'.format(
                now.hour, now.minute)
        await turn_context.send_activity(response_message)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
