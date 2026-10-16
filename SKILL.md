---
name: jbsprites
description: Small character sprites shown inline in chat for personality, in families (default tumnus). A start sprite rides along when work begins; a done, oops or your-turn sprite closes it. Use whenever another skill or the user's preferences say to use jbsprites, or when real work starts in a chat the user is present for. Shown with the visual widget tool; images load from cdn.jsdelivr.net.
---

# jbsprites

Small character sprites that give work some personality. Pure decoration: a sprite never carries information the text does not, and is never mentioned, described or narrated.

A caller (another skill, or the user's preferences) says which family to use. No family named means **tumnus**.

## When

Every task the user asks for in chat gets two beats, one at each end of the turn, never stacked together:

1. **Start.** A start sprite picked by the kind of work, from the family's Start table, as the work begins.
2. **End.** At the close of the turn (where it goes depends on the app; see How), one of:
   - **Done** when the work finished: the small row for a quick or minor task, the cheering row for real work. **Big win** when several things finished at once or a big milestone landed. **Signing off** for the last task of the day or a Friday afternoon. **Sent** when the work was an email or message going out.
   - **Oops** when the work failed, a connector errored, or it could not be finished. Use the Oops row matching the kind of failure (general when none fits), then say plainly what failed. Never show Done for work that did not get done.
   - **Your turn** when the reply ends with a question or a decision for the user.

A reply that needs no work (a quick answer from what is already known) gets one sprite, after the reply: Done if something was completed, otherwise its Start sprite. If the start sprite would land right next to the reply (no real work in between), skip it; the end sprite is enough. A long task that finishes several separate pieces may show Done after each piece. A retry after a failure may carry a Retrying sprite.

**Seasons.** For a Hello or a morning brief, use the current season's row about one time in three instead (northern hemisphere, by month; decide with the draw below, `random.random()<1/3`). Inside a holiday window, use the holiday's row instead of the season's.

Scheduled or unattended runs show no sprites, with one exception: a morning brief or digest that a caller skill produces unattended may open with a single sprite, picked from the Morning brief row (or the season or holiday row as above) and placed as an image at the top of the output and of any post it writes (an `<img>` 120px high in HTML, a markdown image otherwise). The caller's own rules say whether its brief does this. If the widget tool is not available, skip the widget and use the image only; in an attended chat with no widget tool, skip sprites silently.

## Picking (contextual shortlist, real random draw)

The moment picks the row; context narrows it to a shortlist; a real random draw picks the sprite. Never pick by feel alone: left to judgement, picks drift to the first entries in a row and the guests never appear.

1. **Row.** Choose the row from the tables below, as set out in When.
2. **Shortlist.** From that row, name the sprites that suit this particular moment, judged from the sheet names: after-hours sprites for a late sign-off, the White Witch for something blocked or frozen, the Beavers and office colleagues for team work, Aslan for a big win or a hard-won fix, travel sprites for a trip, wardrobe and lamppost scenes for comings and goings. The shortlist has at least four sprites (the whole row if it is shorter), from at least two different sheets, and includes at least one Narnia guest (sheets 24 to 31) whenever the row has one.
3. **Draw.** Pick one from the shortlist with a shell, leaving out the sprite shown just before:
   `python3 -c "import random;print(random.choice(['<shortlisted-1>','<shortlisted-2>','<shortlisted-3>','<shortlisted-4>']))"`

   Fill in the names you just shortlisted; the placeholders are not sprites.
4. **No shell.** Where no shell is available, take the next sprite in the shortlist after the one used last in this chat (the first, if none has been used yet).

## How (keep sprites off the critical path)

- Load the widget tools (`mcp__visualize__read_me`, `mcp__visualize__show_widget`) in the same ToolSearch call as the other tools the task needs.
- Call read_me once per chat, silently, in the same parallel batch as the first real work call.
- Run each draw in the same parallel batch as a real work call, never as a step of its own: the start draw alongside the first work call, the end draw alongside the last one. The widget then goes out with the next call as below.
- Send the start sprite in the same parallel batch as the next real work call. Never spend a round trip on a start sprite alone; if there is no real work call to ride with, skip it.
- The end sprite goes AFTER the reply, never on top of it:
  - Where the chat shows text written before a tool call in full (claude.ai): write the reply, then call the widget as the last step, and write nothing after it.
  - Where text between tool calls is collapsed (the Cowork desktop app), the app always shows the final text below every widget, insists on some final text, and does not render images written into text. So:
    - **Keep the two sprites apart.** Right after the start sprite, send a one-line progress note with SendUserMessage ("Pushing the repo now"). That line sits between the two sprites, so they never stack. No note to send means no start sprite.
    - **Real work:** send the reply with SendUserMessage, then the end sprite, then a short closing phrase as the final text, matching the sprite's moment, picked at random from the Closing phrases table below. Never the phrase used just before. A fresh phrase in the same spirit is fine. The phrase adds nothing new. A light offer is fine.
    - **Quick tasks** (a reply of a few lines): the end sprite, then the reply as the final text.
- Widget code, nothing else in it, with the family and sprite name swapped in:

`<h2 class="sr-only">Sprite</h2><img alt="" style="height:120px" src="https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@v8/<family>/<name>.webp">`

## Closing phrases (Cowork)

Short final lines under the end sprite. Plain, light, never cheesy. Pick at random within the row.

| Moment | Phrases |
|---|---|
| Done, small | Done. / Sorted. / That's in. / Tidied up. / All set. / Easy one. / Anything else? / Ticked off. / Job done. / That's that. / Handled. |
| Done | All sorted. / That's done and dusted. / Finished. / Signed, sealed, delivered. / Right, that's in place. / Done and checked. / That's the job. / Wrapped up. / Good to go. / In place. / Ready when you are. / Happy to take the next one. |
| Big win | That's the lot! / A good day's work. / All of it, done. / Quite the haul. / Everything's in. / Clean sweep. / That went rather well. / Every box ticked. |
| Sent | Sent. / Off it goes. / On its way. / Delivered. / Out the door. / Posted. / It's with them now. |
| Signing off | That's a wrap for today. / Calling it there. / Good place to stop. / Enough for one day. / Lights off. / See you tomorrow. / Have a good evening. / Enjoy the weekend. (Fridays only) |
| Oops: general | Not this time. / That one fought back. / Hit a snag. / Not quite. / Bit of a wobble. / Didn't go to plan. / Stuck, for now. |
| Oops: blocked | Door's shut on that one. / Couldn't get in. / Access needed. / Blocked, for now. |
| Oops: connection or timed out | Couldn't reach it. / The line went quiet. / Timed out. / No answer from that end. |
| Oops: nothing found | Came up empty. / Nothing there. / No sign of it. / Not where I looked. |
| Oops: tangled | Bit of a knot. / Sources disagree. / Needs untangling. / Not as simple as it looked. |
| Your turn | Over to you. / Your call. / Your move. / Ball's in your court. / Waiting on you. / Your decision. / Say the word. / Up to you. / Which way? |

## Family: tumnus (default)

A faun in business casual, with Narnia guests (the Pevensies, Aslan, the White Witch, the Beavers, woodland colleagues, props and places) mixed into the same rows. Rows marked for trackers apply when the caller is a tracker skill; others use the general rows.

## Start

| Kind of work | Sprites |
|---|---|
| Writing or drafting | 10-workflow-full-body_14, 10-workflow-full-body_15, 24-pevensies-at-work_01, 10-workflow-full-body_16, 10-workflow-full-body_17, 24-pevensies-at-work_21, 06-business-casual_07, 07-outfit-variations_03, 26-beavers-and-office-colleagues_17, 07-outfit-variations_10, 07-outfit-variations_35, 27-narnian-creatures-at-work_16, 13-icons-hands-busts_01, 13-icons-hands-busts_13, 28-wardrobe-and-lamppost-office-objects_13, 13-icons-hands-busts_18, 16-working-and-discoveries_09, 29-iconic-tools-and-office-treasures_03, 20-meetings-and-deep-focus_08, 20-meetings-and-deep-focus_11, 20-meetings-and-deep-focus_24, 23-small-wins-and-holidays_14 |
| Research or reading | 10-workflow-full-body_11, 10-workflow-full-body_12, 24-pevensies-at-work_03, 10-workflow-full-body_13, 06-business-casual_18, 24-pevensies-at-work_09, 07-outfit-variations_08, 07-outfit-variations_16, 25-aslan-and-white-witch_06, 07-outfit-variations_24, 07-outfit-variations_28, 27-narnian-creatures-at-work_17, 13-icons-hands-busts_10, 13-icons-hands-busts_21, 27-narnian-creatures-at-work_22, 16-working-and-discoveries_02, 16-working-and-discoveries_03, 28-wardrobe-and-lamppost-office-objects_14, 16-working-and-discoveries_11, 16-working-and-discoveries_12, 28-wardrobe-and-lamppost-office-objects_15, 16-working-and-discoveries_14, 16-working-and-discoveries_15, 29-iconic-tools-and-office-treasures_19, 16-working-and-discoveries_17, 16-working-and-discoveries_18, 29-iconic-tools-and-office-treasures_23, 18-desktop-visitors-and-playful-tech_08, 20-meetings-and-deep-focus_07, 30-narnia-office-locations_15, 21-research-and-inbox_01, 21-research-and-inbox_02, 21-research-and-inbox_03, 21-research-and-inbox_04, 21-research-and-inbox_05, 21-research-and-inbox_06, 21-research-and-inbox_13, 21-research-and-inbox_14, 21-research-and-inbox_15, 21-research-and-inbox_19, 21-research-and-inbox_20, 21-research-and-inbox_21 |
| Email, reconcile, sweep | 10-workflow-full-body_06, 10-workflow-full-body_07, 26-beavers-and-office-colleagues_07, 10-workflow-full-body_08, 10-workflow-full-body_09, 27-narnian-creatures-at-work_25, 10-workflow-full-body_10, 07-outfit-variations_32, 28-wardrobe-and-lamppost-office-objects_05, 13-icons-hands-busts_03, 13-icons-hands-busts_15, 28-wardrobe-and-lamppost-office-objects_16, 21-research-and-inbox_07, 21-research-and-inbox_08, 29-iconic-tools-and-office-treasures_09, 21-research-and-inbox_09, 21-research-and-inbox_10, 29-iconic-tools-and-office-treasures_20, 21-research-and-inbox_16, 21-research-and-inbox_17, 21-research-and-inbox_22, 21-research-and-inbox_23 |
| Add (new tracker item) | 06-business-casual_07, 26-beavers-and-office-colleagues_15, 07-outfit-variations_03, 27-narnian-creatures-at-work_06, 07-outfit-variations_36 |
| Waiting on someone | 06-business-casual_12, 07-outfit-variations_01, 26-beavers-and-office-colleagues_06, 07-outfit-variations_11, 07-outfit-variations_12, 27-narnian-creatures-at-work_18, 22-mobile-travel-and-waiting_09, 22-mobile-travel-and-waiting_12, 28-wardrobe-and-lamppost-office-objects_09, 22-mobile-travel-and-waiting_23, 30-narnia-office-locations_10 |
| Morning brief (on demand) | 07-outfit-variations_04, 07-outfit-variations_08, 24-pevensies-at-work_24, 07-outfit-variations_23, 06-business-casual_09, 26-beavers-and-office-colleagues_03, 16-working-and-discoveries_01, 20-meetings-and-deep-focus_06, 28-wardrobe-and-lamppost-office-objects_17, 29-iconic-tools-and-office-treasures_15, 30-narnia-office-locations_03 |
| The list | 07-outfit-variations_14, 24-pevensies-at-work_16, 07-outfit-variations_33, 26-beavers-and-office-colleagues_10, 26-beavers-and-office-colleagues_14, 29-iconic-tools-and-office-treasures_22, 30-narnia-office-locations_11, 31-narnia-workday-scenes_23 |
| Next | 06-business-casual_16, 07-outfit-variations_15, 27-narnian-creatures-at-work_20, 15-office-mishaps-and-message-edges_15, 15-office-mishaps-and-message-edges_16, 27-narnian-creatures-at-work_21, 28-wardrobe-and-lamppost-office-objects_22, 30-narnia-office-locations_20 |
| Now | 07-outfit-variations_13, 24-pevensies-at-work_18, 06-business-casual_08, 25-aslan-and-white-witch_02, 27-narnian-creatures-at-work_19, 29-iconic-tools-and-office-treasures_06, 30-narnia-office-locations_12 |
| Gaps, stale items | 06-business-casual_10, 06-business-casual_22, 25-aslan-and-white-witch_16, 07-outfit-variations_16, 07-outfit-variations_07, 25-aslan-and-white-witch_22, 27-narnian-creatures-at-work_15, 30-narnia-office-locations_23 |
| Week, quarter, year | 06-business-casual_18, 24-pevensies-at-work_14, 07-outfit-variations_24, 30-narnia-office-locations_07, 07-outfit-variations_28, 30-narnia-office-locations_21 |
| Trip | 06-business-casual_19, 06-business-casual_24, 25-aslan-and-white-witch_19, 07-outfit-variations_19, 07-outfit-variations_20, 28-wardrobe-and-lamppost-office-objects_04, 07-outfit-variations_22, 22-mobile-travel-and-waiting_04, 28-wardrobe-and-lamppost-office-objects_19, 22-mobile-travel-and-waiting_05, 22-mobile-travel-and-waiting_06, 29-iconic-tools-and-office-treasures_24, 22-mobile-travel-and-waiting_10, 22-mobile-travel-and-waiting_15, 30-narnia-office-locations_08, 22-mobile-travel-and-waiting_16, 22-mobile-travel-and-waiting_17, 30-narnia-office-locations_16, 22-mobile-travel-and-waiting_21, 22-mobile-travel-and-waiting_22 |
| Hand-off | 06-business-casual_21, 25-aslan-and-white-witch_04, 07-outfit-variations_29, 27-narnian-creatures-at-work_08, 27-narnian-creatures-at-work_13, 31-narnia-workday-scenes_08 |
| Hello (first reply of a tracker skill in a chat) | 06-business-casual_17, 07-outfit-variations_17, 24-pevensies-at-work_02, 07-outfit-variations_34, 13-icons-hands-busts_22, 25-aslan-and-white-witch_01, 15-office-mishaps-and-message-edges_11, 15-office-mishaps-and-message-edges_12, 26-beavers-and-office-colleagues_16, 15-office-mishaps-and-message-edges_18, 15-office-mishaps-and-message-edges_20, 26-beavers-and-office-colleagues_24, 28-wardrobe-and-lamppost-office-objects_02, 28-wardrobe-and-lamppost-office-objects_21, 30-narnia-office-locations_02, 31-narnia-workday-scenes_01, 31-narnia-workday-scenes_07, 31-narnia-workday-scenes_22 |
| Anything else | 10-workflow-full-body_01, 10-workflow-full-body_02, 25-aslan-and-white-witch_08, 10-workflow-full-body_03, 10-workflow-full-body_04, 25-aslan-and-white-witch_13, 10-workflow-full-body_05, 07-outfit-variations_13, 28-wardrobe-and-lamppost-office-objects_03, 06-business-casual_08, 13-icons-hands-busts_12, 31-narnia-workday-scenes_15, 13-icons-hands-busts_14, 16-working-and-discoveries_04, 16-working-and-discoveries_10, 15-office-mishaps-and-message-edges_06 |
| Calendar, scheduling, focus blocks | 14-calendar-money-tech_06, 14-calendar-money-tech_07, 24-pevensies-at-work_11, 14-calendar-money-tech_08, 14-calendar-money-tech_09, 25-aslan-and-white-witch_14, 14-calendar-money-tech_10, 13-icons-hands-busts_04, 26-beavers-and-office-colleagues_08, 20-meetings-and-deep-focus_06, 20-meetings-and-deep-focus_15, 20-meetings-and-deep-focus_21 |
| Invoices, payments, money | 14-calendar-money-tech_11, 14-calendar-money-tech_12, 24-pevensies-at-work_06, 14-calendar-money-tech_13, 14-calendar-money-tech_14, 25-aslan-and-white-witch_03, 14-calendar-money-tech_15, 13-icons-hands-busts_05, 26-beavers-and-office-colleagues_04, 27-narnian-creatures-at-work_24, 29-iconic-tools-and-office-treasures_17 |
| Technical (DNS, servers, networks, code) | 14-calendar-money-tech_16, 14-calendar-money-tech_17, 24-pevensies-at-work_17, 14-calendar-money-tech_18, 14-calendar-money-tech_19, 25-aslan-and-white-witch_12, 14-calendar-money-tech_20, 13-icons-hands-busts_06, 26-beavers-and-office-colleagues_01, 13-icons-hands-busts_16, 16-working-and-discoveries_08, 27-narnian-creatures-at-work_14, 18-desktop-visitors-and-playful-tech_11, 18-desktop-visitors-and-playful-tech_12, 27-narnian-creatures-at-work_23, 18-desktop-visitors-and-playful-tech_13, 18-desktop-visitors-and-playful-tech_14, 29-iconic-tools-and-office-treasures_07, 18-desktop-visitors-and-playful-tech_15, 18-desktop-visitors-and-playful-tech_16, 18-desktop-visitors-and-playful-tech_17, 18-desktop-visitors-and-playful-tech_18, 18-desktop-visitors-and-playful-tech_19, 18-desktop-visitors-and-playful-tech_20 |
| Image or design work | 13-icons-hands-busts_11, 19-image-and-design-work_01, 26-beavers-and-office-colleagues_02, 19-image-and-design-work_02, 19-image-and-design-work_03, 27-narnian-creatures-at-work_07, 19-image-and-design-work_04, 19-image-and-design-work_05, 28-wardrobe-and-lamppost-office-objects_25, 19-image-and-design-work_06, 19-image-and-design-work_07, 19-image-and-design-work_08, 19-image-and-design-work_09, 19-image-and-design-work_10, 19-image-and-design-work_11, 19-image-and-design-work_12, 19-image-and-design-work_13, 19-image-and-design-work_14, 19-image-and-design-work_15, 19-image-and-design-work_16, 19-image-and-design-work_17, 19-image-and-design-work_18, 19-image-and-design-work_19, 19-image-and-design-work_20 |
| Waiting on a long job (upload, deploy, background run) | 13-icons-hands-busts_07, 06-business-casual_12, 26-beavers-and-office-colleagues_25, 07-outfit-variations_12, 16-working-and-discoveries_05, 28-wardrobe-and-lamppost-office-objects_18, 16-working-and-discoveries_07, 15-office-mishaps-and-message-edges_13, 31-narnia-workday-scenes_10, 22-mobile-travel-and-waiting_07, 22-mobile-travel-and-waiting_08, 31-narnia-workday-scenes_12, 22-mobile-travel-and-waiting_11, 22-mobile-travel-and-waiting_18, 22-mobile-travel-and-waiting_24 |
| Meetings, calls, presentations, talk prep | 20-meetings-and-deep-focus_01, 20-meetings-and-deep-focus_02, 24-pevensies-at-work_05, 20-meetings-and-deep-focus_03, 20-meetings-and-deep-focus_04, 24-pevensies-at-work_12, 20-meetings-and-deep-focus_05, 20-meetings-and-deep-focus_13, 24-pevensies-at-work_15, 20-meetings-and-deep-focus_14, 20-meetings-and-deep-focus_16, 24-pevensies-at-work_19, 20-meetings-and-deep-focus_19, 20-meetings-and-deep-focus_20, 24-pevensies-at-work_22, 22-mobile-travel-and-waiting_03, 22-mobile-travel-and-waiting_19, 24-pevensies-at-work_23, 25-aslan-and-white-witch_18, 28-wardrobe-and-lamppost-office-objects_08, 29-iconic-tools-and-office-treasures_05, 29-iconic-tools-and-office-treasures_08, 30-narnia-office-locations_06, 30-narnia-office-locations_09, 30-narnia-office-locations_22, 30-narnia-office-locations_24, 31-narnia-workday-scenes_04, 31-narnia-workday-scenes_17 |
| Deep focus, long writing, heads-down blocks | 20-meetings-and-deep-focus_07, 20-meetings-and-deep-focus_08, 25-aslan-and-white-witch_23, 20-meetings-and-deep-focus_09, 20-meetings-and-deep-focus_10, 28-wardrobe-and-lamppost-office-objects_07, 20-meetings-and-deep-focus_11, 20-meetings-and-deep-focus_17, 30-narnia-office-locations_01, 20-meetings-and-deep-focus_18, 20-meetings-and-deep-focus_22, 30-narnia-office-locations_17, 20-meetings-and-deep-focus_23, 20-meetings-and-deep-focus_24 |
| On the go (the user is on a phone) | 22-mobile-travel-and-waiting_01, 22-mobile-travel-and-waiting_02, 24-pevensies-at-work_08, 22-mobile-travel-and-waiting_03, 22-mobile-travel-and-waiting_13, 22-mobile-travel-and-waiting_14, 22-mobile-travel-and-waiting_19, 22-mobile-travel-and-waiting_20 |
| Retrying (trying again after a failure; send with the retry call) | 12-failure-and-recovery_16, 24-pevensies-at-work_04, 12-failure-and-recovery_17, 26-beavers-and-office-colleagues_05, 12-failure-and-recovery_20, 29-iconic-tools-and-office-treasures_01, 29-iconic-tools-and-office-treasures_02, 31-narnia-workday-scenes_13 |

## Done

| Moment | Sprites |
|---|---|
| Done, small (a quick or minor task) | 14-calendar-money-tech_01, 14-calendar-money-tech_02, 24-pevensies-at-work_20, 14-calendar-money-tech_03, 14-calendar-money-tech_04, 26-beavers-and-office-colleagues_09, 14-calendar-money-tech_05, 13-icons-hands-busts_02, 26-beavers-and-office-colleagues_22, 13-icons-hands-busts_20, 13-icons-hands-busts_24, 29-iconic-tools-and-office-treasures_14, 16-working-and-discoveries_13, 16-working-and-discoveries_16, 31-narnia-workday-scenes_18, 16-working-and-discoveries_20, 18-desktop-visitors-and-playful-tech_01, 18-desktop-visitors-and-playful-tech_02, 18-desktop-visitors-and-playful-tech_04, 18-desktop-visitors-and-playful-tech_05, 18-desktop-visitors-and-playful-tech_06, 18-desktop-visitors-and-playful-tech_09, 19-image-and-design-work_18, 19-image-and-design-work_20, 23-small-wins-and-holidays_01, 23-small-wins-and-holidays_02, 23-small-wins-and-holidays_04, 23-small-wins-and-holidays_05, 23-small-wins-and-holidays_19, 23-small-wins-and-holidays_20 |
| Sent (an email or message went out) | 21-research-and-inbox_11, 21-research-and-inbox_12, 26-beavers-and-office-colleagues_13, 21-research-and-inbox_18, 21-research-and-inbox_24, 28-wardrobe-and-lamppost-office-objects_11, 29-iconic-tools-and-office-treasures_18, 29-iconic-tools-and-office-treasures_25 |
| Done (real work finished, an item closed) | 08-celebrations_01, 08-celebrations_02, 25-aslan-and-white-witch_10, 08-celebrations_03, 08-celebrations_04, 26-beavers-and-office-colleagues_18, 08-celebrations_05, 08-celebrations_06, 26-beavers-and-office-colleagues_19, 08-celebrations_07, 08-celebrations_08, 29-iconic-tools-and-office-treasures_11, 08-celebrations_12, 08-celebrations_13, 31-narnia-workday-scenes_05, 08-celebrations_16, 08-celebrations_17, 31-narnia-workday-scenes_16, 08-celebrations_18, 08-celebrations_19, 08-celebrations_20, 08-celebrations_22, 08-celebrations_23, 08-celebrations_24 |
| Big win (several items closed at once, or no open High items left) | 08-celebrations_09, 08-celebrations_10, 24-pevensies-at-work_25, 08-celebrations_11, 08-celebrations_14, 25-aslan-and-white-witch_09, 08-celebrations_15, 26-beavers-and-office-colleagues_11, 29-iconic-tools-and-office-treasures_10, 29-iconic-tools-and-office-treasures_21, 31-narnia-workday-scenes_14 |
| Signing off (last task of the day, or Friday afternoon) | 14-calendar-money-tech_03, 13-icons-hands-busts_24, 25-aslan-and-white-witch_05, 08-celebrations_20, 08-celebrations_23, 26-beavers-and-office-colleagues_20, 17-after-hours-and-seasonal_01, 17-after-hours-and-seasonal_02, 28-wardrobe-and-lamppost-office-objects_10, 17-after-hours-and-seasonal_03, 17-after-hours-and-seasonal_04, 28-wardrobe-and-lamppost-office-objects_12, 17-after-hours-and-seasonal_05, 17-after-hours-and-seasonal_06, 30-narnia-office-locations_25, 17-after-hours-and-seasonal_07, 17-after-hours-and-seasonal_08, 31-narnia-workday-scenes_06, 17-after-hours-and-seasonal_09, 17-after-hours-and-seasonal_10, 31-narnia-workday-scenes_21, 18-desktop-visitors-and-playful-tech_07, 20-meetings-and-deep-focus_12, 31-narnia-workday-scenes_25 |
| Oops: general (something went wrong) | 12-failure-and-recovery_01, 12-failure-and-recovery_02, 24-pevensies-at-work_07, 12-failure-and-recovery_03, 12-failure-and-recovery_05, 24-pevensies-at-work_10, 10-workflow-full-body_20, 06-business-casual_22, 29-iconic-tools-and-office-treasures_12, 07-outfit-variations_07, 15-office-mishaps-and-message-edges_01, 31-narnia-workday-scenes_09, 15-office-mishaps-and-message-edges_02, 15-office-mishaps-and-message-edges_04, 31-narnia-workday-scenes_19, 15-office-mishaps-and-message-edges_05, 15-office-mishaps-and-message-edges_08, 15-office-mishaps-and-message-edges_09, 18-desktop-visitors-and-playful-tech_10 |
| Oops: blocked (access refused, permission declined, cannot proceed) | 12-failure-and-recovery_08, 25-aslan-and-white-witch_11, 12-failure-and-recovery_10, 25-aslan-and-white-witch_20, 13-icons-hands-busts_09, 27-narnian-creatures-at-work_11, 27-narnian-creatures-at-work_12, 28-wardrobe-and-lamppost-office-objects_01, 29-iconic-tools-and-office-treasures_13, 30-narnia-office-locations_04, 30-narnia-office-locations_18 |
| Oops: connection error (a connector or service is down) | 12-failure-and-recovery_09 |
| Oops: timed out | 12-failure-and-recovery_12, 25-aslan-and-white-witch_17, 25-aslan-and-white-witch_24, 29-iconic-tools-and-office-treasures_16, 30-narnia-office-locations_05 |
| Oops: nothing found (empty search, missing file or folder) | 12-failure-and-recovery_06, 28-wardrobe-and-lamppost-office-objects_23, 12-failure-and-recovery_07, 12-failure-and-recovery_13 |
| Oops: conflicting or tangled (sources disagree, knotted dependencies) | 12-failure-and-recovery_04, 12-failure-and-recovery_11, 25-aslan-and-white-witch_25, 12-failure-and-recovery_14, 15-office-mishaps-and-message-edges_03, 31-narnia-workday-scenes_02, 15-office-mishaps-and-message-edges_10, 31-narnia-workday-scenes_20 |
| Your turn (a question or decision for the user) | 12-failure-and-recovery_18, 12-failure-and-recovery_15, 24-pevensies-at-work_13, 12-failure-and-recovery_19, 10-workflow-full-body_18, 25-aslan-and-white-witch_15, 10-workflow-full-body_19, 06-business-casual_21, 26-beavers-and-office-colleagues_21, 13-icons-hands-busts_17, 13-icons-hands-busts_23, 28-wardrobe-and-lamppost-office-objects_24, 13-icons-hands-busts_19, 15-office-mishaps-and-message-edges_17, 29-iconic-tools-and-office-treasures_04, 15-office-mishaps-and-message-edges_19, 31-narnia-workday-scenes_03 |

## Seasons (tumnus)

| Season | Sprites |
|---|---|
| Autumn (September to November) | 17-after-hours-and-seasonal_11, 17-after-hours-and-seasonal_19, 23-small-wins-and-holidays_23 |
| Winter (December to February) | 17-after-hours-and-seasonal_12, 17-after-hours-and-seasonal_16, 25-aslan-and-white-witch_21, 17-after-hours-and-seasonal_17, 17-after-hours-and-seasonal_20, 28-wardrobe-and-lamppost-office-objects_06, 23-small-wins-and-holidays_09, 23-small-wins-and-holidays_22, 28-wardrobe-and-lamppost-office-objects_20, 30-narnia-office-locations_13 |
| Spring (March to May) | 17-after-hours-and-seasonal_13, 27-narnian-creatures-at-work_09, 17-after-hours-and-seasonal_18, 27-narnian-creatures-at-work_10, 30-narnia-office-locations_14 |
| Summer (June to August) | 17-after-hours-and-seasonal_14, 17-after-hours-and-seasonal_15 |

## Holidays (tumnus)

| Holiday (window) | Sprites |
|---|---|
| Thanksgiving (US, November 20 to 30) | 23-small-wins-and-holidays_10, 23-small-wins-and-holidays_11, 23-small-wins-and-holidays_17 |
| Christmas (December 1 to 26) | 23-small-wins-and-holidays_07, 23-small-wins-and-holidays_08, 26-beavers-and-office-colleagues_12, 23-small-wins-and-holidays_15, 23-small-wins-and-holidays_16, 26-beavers-and-office-colleagues_23, 30-narnia-office-locations_19, 31-narnia-workday-scenes_24 |
| New Year (December 27 to January 2) | 23-small-wins-and-holidays_12, 23-small-wins-and-holidays_18, 23-small-wins-and-holidays_24 |

## Adding a family or new sprites

1. Put the sheet (transparent PNG, figures well apart, nothing cropped at the edges) in `<family>/originals/`.
2. Run `python3 scripts/make_sprites.py <family>`: writes `<family>/<sheet>_<NN>.webp`, 160 px, numbered in reading order. With a `<sheet>.json` index (`columns`, `rows`) beside the sheet, pieces are grouped by grid cell, so a prop that floats apart stays with its figure.
3. Add the family's tables here (default family inline; other families may live in `families/<family>.md`, read only when asked for).
4. Commit, tag the next version (`v2`, `v3`...), and change `@vN` in the widget code above. A tag is fixed once published; jsDelivr caches it for good.
