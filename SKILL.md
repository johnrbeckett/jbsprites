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
2. **End.** After the reply, as the very last thing in the turn, one of:
   - **Done** when the work finished: the small row for a quick or minor task, the cheering row for real work. **Big win** when several things finished at once or a big milestone landed. **Signing off** for the last task of the day or a Friday afternoon. **Sent** when the work was an email or message going out.
   - **Oops** when the work failed, a connector errored, or it could not be finished. Use the Oops row matching the kind of failure (general when none fits), then say plainly what failed. Never show Done for work that did not get done.
   - **Your turn** when the reply ends with a question or a decision for the user.

A reply that needs no work (a quick answer from what is already known) gets one sprite, after the reply: Done if something was completed, otherwise its Start sprite. If the start sprite would land right next to the reply (no real work in between), skip it; the end sprite is enough. A long task that finishes several separate pieces may show Done after each piece. A retry after a failure may carry a Retrying sprite.

**Seasons.** For a Hello or a morning brief, use the current season's row about one time in three instead (northern hemisphere, by month). Inside a holiday window, use the holiday's row instead of the season's.

Never in scheduled or unattended runs. If the widget tool is not available, skip sprites silently.

Pick at random within a row, avoiding the sprite used just before when there is a choice.

## How (keep sprites off the critical path)

- Load the widget tools (`mcp__visualize__read_me`, `mcp__visualize__show_widget`) in the same ToolSearch call as the other tools the task needs.
- Call read_me once per chat, silently, in the same parallel batch as the first real work call.
- Send the start sprite in the same parallel batch as the next real work call. Never spend a round trip on a start sprite alone; if there is no real work call to ride with, skip it.
- The end sprite goes AFTER the reply, never on top of it:
  - Where the chat shows text written before a tool call in full (claude.ai): write the reply, then call the widget as the last step, and write nothing after it.
  - Where text between tool calls is collapsed (the Cowork desktop app): send the reply with the SendUserMessage tool, then call the widget as the last step, and end the turn with no further text.
- Widget code, nothing else in it, with the family and sprite name swapped in:

`<h2 class="sr-only">Sprite</h2><img alt="" style="height:120px" src="https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@v6/<family>/<name>.webp">`

## Family: tumnus (default)

A faun in business casual. Rows marked for trackers apply when the caller is a tracker skill; others use the general rows.

## Start

| Kind of work | Sprites |
|---|---|
| Writing or drafting | 10-workflow-full-body_14, 10-workflow-full-body_15, 10-workflow-full-body_16, 10-workflow-full-body_17, 06-business-casual_07, 07-outfit-variations_03, 07-outfit-variations_10, 07-outfit-variations_35, 13-icons-hands-busts_01, 13-icons-hands-busts_13, 13-icons-hands-busts_18, 16-working-and-discoveries_09, 20-meetings-and-deep-focus_08, 20-meetings-and-deep-focus_11, 20-meetings-and-deep-focus_24, 23-small-wins-and-holidays_14 |
| Research or reading | 10-workflow-full-body_11, 10-workflow-full-body_12, 10-workflow-full-body_13, 06-business-casual_18, 07-outfit-variations_08, 07-outfit-variations_16, 07-outfit-variations_24, 07-outfit-variations_28, 13-icons-hands-busts_10, 13-icons-hands-busts_21, 16-working-and-discoveries_02, 16-working-and-discoveries_03, 16-working-and-discoveries_11, 16-working-and-discoveries_12, 16-working-and-discoveries_14, 16-working-and-discoveries_15, 16-working-and-discoveries_17, 16-working-and-discoveries_18, 18-desktop-visitors-and-playful-tech_08, 20-meetings-and-deep-focus_07, 21-research-and-inbox_01, 21-research-and-inbox_02, 21-research-and-inbox_03, 21-research-and-inbox_04, 21-research-and-inbox_05, 21-research-and-inbox_06, 21-research-and-inbox_13, 21-research-and-inbox_14, 21-research-and-inbox_15, 21-research-and-inbox_19, 21-research-and-inbox_20, 21-research-and-inbox_21 |
| Email, reconcile, sweep | 10-workflow-full-body_06, 10-workflow-full-body_07, 10-workflow-full-body_08, 10-workflow-full-body_09, 10-workflow-full-body_10, 07-outfit-variations_32, 13-icons-hands-busts_03, 13-icons-hands-busts_15, 21-research-and-inbox_07, 21-research-and-inbox_08, 21-research-and-inbox_09, 21-research-and-inbox_10, 21-research-and-inbox_16, 21-research-and-inbox_17, 21-research-and-inbox_22, 21-research-and-inbox_23 |
| Add (new tracker item) | 06-business-casual_07, 07-outfit-variations_03, 07-outfit-variations_36 |
| Waiting on someone | 06-business-casual_12, 07-outfit-variations_01, 07-outfit-variations_11, 07-outfit-variations_12, 22-mobile-travel-and-waiting_09, 22-mobile-travel-and-waiting_12, 22-mobile-travel-and-waiting_23 |
| Morning brief (on demand) | 07-outfit-variations_04, 07-outfit-variations_08, 07-outfit-variations_23, 06-business-casual_09, 16-working-and-discoveries_01, 20-meetings-and-deep-focus_06 |
| The list | 07-outfit-variations_14, 07-outfit-variations_33 |
| Next | 06-business-casual_16, 07-outfit-variations_15, 15-office-mishaps-and-message-edges_15, 15-office-mishaps-and-message-edges_16 |
| Now | 07-outfit-variations_13, 06-business-casual_08 |
| Gaps, stale items | 06-business-casual_10, 06-business-casual_22, 07-outfit-variations_16, 07-outfit-variations_07 |
| Week, quarter, year | 06-business-casual_18, 07-outfit-variations_24, 07-outfit-variations_28 |
| Trip | 06-business-casual_19, 06-business-casual_24, 07-outfit-variations_19, 07-outfit-variations_20, 07-outfit-variations_22, 22-mobile-travel-and-waiting_04, 22-mobile-travel-and-waiting_05, 22-mobile-travel-and-waiting_06, 22-mobile-travel-and-waiting_10, 22-mobile-travel-and-waiting_15, 22-mobile-travel-and-waiting_16, 22-mobile-travel-and-waiting_17, 22-mobile-travel-and-waiting_21, 22-mobile-travel-and-waiting_22 |
| Hand-off | 06-business-casual_21, 07-outfit-variations_29 |
| Hello (first reply of a tracker skill in a chat) | 06-business-casual_17, 07-outfit-variations_17, 07-outfit-variations_34, 13-icons-hands-busts_22, 15-office-mishaps-and-message-edges_11, 15-office-mishaps-and-message-edges_12, 15-office-mishaps-and-message-edges_18, 15-office-mishaps-and-message-edges_20 |
| Anything else | 10-workflow-full-body_01, 10-workflow-full-body_02, 10-workflow-full-body_03, 10-workflow-full-body_04, 10-workflow-full-body_05, 07-outfit-variations_13, 06-business-casual_08, 13-icons-hands-busts_12, 13-icons-hands-busts_14, 16-working-and-discoveries_04, 16-working-and-discoveries_10, 15-office-mishaps-and-message-edges_06 |
| Calendar, scheduling, focus blocks | 14-calendar-money-tech_06, 14-calendar-money-tech_07, 14-calendar-money-tech_08, 14-calendar-money-tech_09, 14-calendar-money-tech_10, 13-icons-hands-busts_04, 20-meetings-and-deep-focus_06, 20-meetings-and-deep-focus_15, 20-meetings-and-deep-focus_21 |
| Invoices, payments, money | 14-calendar-money-tech_11, 14-calendar-money-tech_12, 14-calendar-money-tech_13, 14-calendar-money-tech_14, 14-calendar-money-tech_15, 13-icons-hands-busts_05 |
| Technical (DNS, servers, networks, code) | 14-calendar-money-tech_16, 14-calendar-money-tech_17, 14-calendar-money-tech_18, 14-calendar-money-tech_19, 14-calendar-money-tech_20, 13-icons-hands-busts_06, 13-icons-hands-busts_16, 16-working-and-discoveries_08, 18-desktop-visitors-and-playful-tech_11, 18-desktop-visitors-and-playful-tech_12, 18-desktop-visitors-and-playful-tech_13, 18-desktop-visitors-and-playful-tech_14, 18-desktop-visitors-and-playful-tech_15, 18-desktop-visitors-and-playful-tech_16, 18-desktop-visitors-and-playful-tech_17, 18-desktop-visitors-and-playful-tech_18, 18-desktop-visitors-and-playful-tech_19, 18-desktop-visitors-and-playful-tech_20 |
| Image or design work | 13-icons-hands-busts_11, 19-image-and-design-work_01, 19-image-and-design-work_02, 19-image-and-design-work_03, 19-image-and-design-work_04, 19-image-and-design-work_05, 19-image-and-design-work_06, 19-image-and-design-work_07, 19-image-and-design-work_08, 19-image-and-design-work_09, 19-image-and-design-work_10, 19-image-and-design-work_11, 19-image-and-design-work_12, 19-image-and-design-work_13, 19-image-and-design-work_14, 19-image-and-design-work_15, 19-image-and-design-work_16, 19-image-and-design-work_17, 19-image-and-design-work_18, 19-image-and-design-work_19, 19-image-and-design-work_20 |
| Waiting on a long job (upload, deploy, background run) | 13-icons-hands-busts_07, 06-business-casual_12, 07-outfit-variations_12, 16-working-and-discoveries_05, 16-working-and-discoveries_07, 15-office-mishaps-and-message-edges_13, 22-mobile-travel-and-waiting_07, 22-mobile-travel-and-waiting_08, 22-mobile-travel-and-waiting_11, 22-mobile-travel-and-waiting_18, 22-mobile-travel-and-waiting_24 |
| Meetings, calls, presentations, talk prep | 20-meetings-and-deep-focus_01, 20-meetings-and-deep-focus_02, 20-meetings-and-deep-focus_03, 20-meetings-and-deep-focus_04, 20-meetings-and-deep-focus_05, 20-meetings-and-deep-focus_13, 20-meetings-and-deep-focus_14, 20-meetings-and-deep-focus_16, 20-meetings-and-deep-focus_19, 20-meetings-and-deep-focus_20, 22-mobile-travel-and-waiting_03, 22-mobile-travel-and-waiting_19 |
| Deep focus, long writing, heads-down blocks | 20-meetings-and-deep-focus_07, 20-meetings-and-deep-focus_08, 20-meetings-and-deep-focus_09, 20-meetings-and-deep-focus_10, 20-meetings-and-deep-focus_11, 20-meetings-and-deep-focus_17, 20-meetings-and-deep-focus_18, 20-meetings-and-deep-focus_22, 20-meetings-and-deep-focus_23, 20-meetings-and-deep-focus_24 |
| On the go (the user is on a phone) | 22-mobile-travel-and-waiting_01, 22-mobile-travel-and-waiting_02, 22-mobile-travel-and-waiting_03, 22-mobile-travel-and-waiting_13, 22-mobile-travel-and-waiting_14, 22-mobile-travel-and-waiting_19, 22-mobile-travel-and-waiting_20 |
| Retrying (trying again after a failure; send with the retry call) | 12-failure-and-recovery_16, 12-failure-and-recovery_17, 12-failure-and-recovery_20 |

## Done

| Moment | Sprites |
|---|---|
| Done, small (a quick or minor task) | 14-calendar-money-tech_01, 14-calendar-money-tech_02, 14-calendar-money-tech_03, 14-calendar-money-tech_04, 14-calendar-money-tech_05, 13-icons-hands-busts_02, 13-icons-hands-busts_20, 13-icons-hands-busts_24, 16-working-and-discoveries_13, 16-working-and-discoveries_16, 16-working-and-discoveries_20, 18-desktop-visitors-and-playful-tech_01, 18-desktop-visitors-and-playful-tech_02, 18-desktop-visitors-and-playful-tech_04, 18-desktop-visitors-and-playful-tech_05, 18-desktop-visitors-and-playful-tech_06, 18-desktop-visitors-and-playful-tech_09, 19-image-and-design-work_18, 19-image-and-design-work_20, 23-small-wins-and-holidays_01, 23-small-wins-and-holidays_02, 23-small-wins-and-holidays_04, 23-small-wins-and-holidays_05, 23-small-wins-and-holidays_19, 23-small-wins-and-holidays_20 |
| Sent (an email or message went out) | 21-research-and-inbox_11, 21-research-and-inbox_12, 21-research-and-inbox_18, 21-research-and-inbox_24 |
| Done (real work finished, an item closed) | 08-celebrations_01, 08-celebrations_02, 08-celebrations_03, 08-celebrations_04, 08-celebrations_05, 08-celebrations_06, 08-celebrations_07, 08-celebrations_08, 08-celebrations_12, 08-celebrations_13, 08-celebrations_16, 08-celebrations_17, 08-celebrations_18, 08-celebrations_19, 08-celebrations_20, 08-celebrations_22, 08-celebrations_23, 08-celebrations_24 |
| Big win (several items closed at once, or no open High items left) | 08-celebrations_09, 08-celebrations_10, 08-celebrations_11, 08-celebrations_14, 08-celebrations_15 |
| Signing off (last task of the day, or Friday afternoon) | 14-calendar-money-tech_03, 13-icons-hands-busts_24, 08-celebrations_20, 08-celebrations_23, 17-after-hours-and-seasonal_01, 17-after-hours-and-seasonal_02, 17-after-hours-and-seasonal_03, 17-after-hours-and-seasonal_04, 17-after-hours-and-seasonal_05, 17-after-hours-and-seasonal_06, 17-after-hours-and-seasonal_07, 17-after-hours-and-seasonal_08, 17-after-hours-and-seasonal_09, 17-after-hours-and-seasonal_10, 18-desktop-visitors-and-playful-tech_07, 20-meetings-and-deep-focus_12 |
| Oops: general (something went wrong) | 12-failure-and-recovery_01, 12-failure-and-recovery_02, 12-failure-and-recovery_03, 12-failure-and-recovery_05, 10-workflow-full-body_20, 06-business-casual_22, 07-outfit-variations_07, 15-office-mishaps-and-message-edges_01, 15-office-mishaps-and-message-edges_02, 15-office-mishaps-and-message-edges_04, 15-office-mishaps-and-message-edges_05, 15-office-mishaps-and-message-edges_08, 15-office-mishaps-and-message-edges_09, 18-desktop-visitors-and-playful-tech_10 |
| Oops: blocked (access refused, permission declined, cannot proceed) | 12-failure-and-recovery_08, 12-failure-and-recovery_10, 13-icons-hands-busts_09 |
| Oops: connection error (a connector or service is down) | 12-failure-and-recovery_09 |
| Oops: timed out | 12-failure-and-recovery_12 |
| Oops: nothing found (empty search, missing file or folder) | 12-failure-and-recovery_06, 12-failure-and-recovery_07, 12-failure-and-recovery_13 |
| Oops: conflicting or tangled (sources disagree, knotted dependencies) | 12-failure-and-recovery_04, 12-failure-and-recovery_11, 12-failure-and-recovery_14, 15-office-mishaps-and-message-edges_03, 15-office-mishaps-and-message-edges_10 |
| Your turn (a question or decision for the user) | 12-failure-and-recovery_18, 12-failure-and-recovery_15, 12-failure-and-recovery_19, 10-workflow-full-body_18, 10-workflow-full-body_19, 06-business-casual_21, 13-icons-hands-busts_17, 13-icons-hands-busts_23, 13-icons-hands-busts_19, 15-office-mishaps-and-message-edges_17, 15-office-mishaps-and-message-edges_19 |

## Seasons (tumnus)

| Season | Sprites |
|---|---|
| Autumn (September to November) | 17-after-hours-and-seasonal_11, 17-after-hours-and-seasonal_19, 23-small-wins-and-holidays_23 |
| Winter (December to February) | 17-after-hours-and-seasonal_12, 17-after-hours-and-seasonal_16, 17-after-hours-and-seasonal_17, 17-after-hours-and-seasonal_20, 23-small-wins-and-holidays_09, 23-small-wins-and-holidays_22 |
| Spring (March to May) | 17-after-hours-and-seasonal_13, 17-after-hours-and-seasonal_18 |
| Summer (June to August) | 17-after-hours-and-seasonal_14, 17-after-hours-and-seasonal_15 |

## Holidays (tumnus)

| Holiday (window) | Sprites |
|---|---|
| Thanksgiving (US, November 20 to 30) | 23-small-wins-and-holidays_10, 23-small-wins-and-holidays_11, 23-small-wins-and-holidays_17 |
| Christmas (December 1 to 26) | 23-small-wins-and-holidays_07, 23-small-wins-and-holidays_08, 23-small-wins-and-holidays_15, 23-small-wins-and-holidays_16 |
| New Year (December 27 to January 2) | 23-small-wins-and-holidays_12, 23-small-wins-and-holidays_18, 23-small-wins-and-holidays_24 |

## Narnia guests (tumnus)

Office-life fan art of the Narnia cast: the Pevensies, Aslan, the White Witch, the Beavers, woodland colleagues, props and places. About one beat in four, when the moment's row appears below, pick from it instead of the main table. Same rules otherwise: random within the row, no repeat of the sprite just shown. For a Hello or morning brief inside a season or holiday window, the guest season rows count the same way.

### Start

| Kind of work | Sprites |
|---|---|
| Writing or drafting | 24-pevensies-at-work_01, 24-pevensies-at-work_21, 26-beavers-and-office-colleagues_17, 27-narnian-creatures-at-work_16, 28-wardrobe-and-lamppost-office-objects_13, 29-iconic-tools-and-office-treasures_03 |
| Research or reading | 24-pevensies-at-work_03, 24-pevensies-at-work_09, 25-aslan-and-white-witch_06, 27-narnian-creatures-at-work_17, 27-narnian-creatures-at-work_22, 28-wardrobe-and-lamppost-office-objects_14, 28-wardrobe-and-lamppost-office-objects_15, 29-iconic-tools-and-office-treasures_19, 29-iconic-tools-and-office-treasures_23, 30-narnia-office-locations_15 |
| Email, reconcile, sweep | 26-beavers-and-office-colleagues_07, 27-narnian-creatures-at-work_25, 28-wardrobe-and-lamppost-office-objects_05, 28-wardrobe-and-lamppost-office-objects_16, 29-iconic-tools-and-office-treasures_09, 29-iconic-tools-and-office-treasures_20 |
| Add (new tracker item) | 26-beavers-and-office-colleagues_15, 27-narnian-creatures-at-work_06 |
| Waiting on someone | 26-beavers-and-office-colleagues_06, 27-narnian-creatures-at-work_18, 28-wardrobe-and-lamppost-office-objects_09, 30-narnia-office-locations_10 |
| Morning brief (on demand) | 24-pevensies-at-work_24, 26-beavers-and-office-colleagues_03, 28-wardrobe-and-lamppost-office-objects_17, 29-iconic-tools-and-office-treasures_15, 30-narnia-office-locations_03 |
| The list | 24-pevensies-at-work_16, 26-beavers-and-office-colleagues_10, 26-beavers-and-office-colleagues_14, 29-iconic-tools-and-office-treasures_22, 30-narnia-office-locations_11, 31-narnia-workday-scenes_23 |
| Next | 27-narnian-creatures-at-work_20, 27-narnian-creatures-at-work_21, 28-wardrobe-and-lamppost-office-objects_22, 30-narnia-office-locations_20 |
| Now | 24-pevensies-at-work_18, 25-aslan-and-white-witch_02, 27-narnian-creatures-at-work_19, 29-iconic-tools-and-office-treasures_06, 30-narnia-office-locations_12 |
| Gaps, stale items | 25-aslan-and-white-witch_16, 25-aslan-and-white-witch_22, 27-narnian-creatures-at-work_15, 30-narnia-office-locations_23 |
| Week, quarter, year | 24-pevensies-at-work_14, 30-narnia-office-locations_07, 30-narnia-office-locations_21 |
| Trip | 25-aslan-and-white-witch_19, 28-wardrobe-and-lamppost-office-objects_04, 28-wardrobe-and-lamppost-office-objects_19, 29-iconic-tools-and-office-treasures_24, 30-narnia-office-locations_08, 30-narnia-office-locations_16 |
| Hand-off | 25-aslan-and-white-witch_04, 27-narnian-creatures-at-work_08, 27-narnian-creatures-at-work_13, 31-narnia-workday-scenes_08 |
| Hello (first reply of a tracker skill in a chat) | 24-pevensies-at-work_02, 25-aslan-and-white-witch_01, 26-beavers-and-office-colleagues_16, 26-beavers-and-office-colleagues_24, 28-wardrobe-and-lamppost-office-objects_02, 28-wardrobe-and-lamppost-office-objects_21, 30-narnia-office-locations_02, 31-narnia-workday-scenes_01, 31-narnia-workday-scenes_07, 31-narnia-workday-scenes_22 |
| Anything else | 25-aslan-and-white-witch_08, 25-aslan-and-white-witch_13, 28-wardrobe-and-lamppost-office-objects_03, 31-narnia-workday-scenes_15 |
| Calendar, scheduling, focus blocks | 24-pevensies-at-work_11, 25-aslan-and-white-witch_14, 26-beavers-and-office-colleagues_08 |
| Invoices, payments, money | 24-pevensies-at-work_06, 25-aslan-and-white-witch_03, 26-beavers-and-office-colleagues_04, 27-narnian-creatures-at-work_24, 29-iconic-tools-and-office-treasures_17 |
| Technical (DNS, servers, networks, code) | 24-pevensies-at-work_17, 25-aslan-and-white-witch_12, 26-beavers-and-office-colleagues_01, 27-narnian-creatures-at-work_14, 27-narnian-creatures-at-work_23, 29-iconic-tools-and-office-treasures_07 |
| Image or design work | 26-beavers-and-office-colleagues_02, 27-narnian-creatures-at-work_07, 28-wardrobe-and-lamppost-office-objects_25 |
| Waiting on a long job (upload, deploy, background run) | 26-beavers-and-office-colleagues_25, 28-wardrobe-and-lamppost-office-objects_18, 31-narnia-workday-scenes_10, 31-narnia-workday-scenes_12 |
| Retrying (trying again after a failure; send with the retry call) | 24-pevensies-at-work_04, 26-beavers-and-office-colleagues_05, 29-iconic-tools-and-office-treasures_01, 29-iconic-tools-and-office-treasures_02, 31-narnia-workday-scenes_13 |
| Meetings, calls, presentations, talk prep | 24-pevensies-at-work_05, 24-pevensies-at-work_12, 24-pevensies-at-work_15, 24-pevensies-at-work_19, 24-pevensies-at-work_22, 24-pevensies-at-work_23, 25-aslan-and-white-witch_18, 28-wardrobe-and-lamppost-office-objects_08, 29-iconic-tools-and-office-treasures_05, 29-iconic-tools-and-office-treasures_08, 30-narnia-office-locations_06, 30-narnia-office-locations_09, 30-narnia-office-locations_22, 30-narnia-office-locations_24, 31-narnia-workday-scenes_04, 31-narnia-workday-scenes_17 |
| Deep focus, long writing, heads-down blocks | 25-aslan-and-white-witch_23, 28-wardrobe-and-lamppost-office-objects_07, 30-narnia-office-locations_01, 30-narnia-office-locations_17 |
| On the go (the user is on a phone) | 24-pevensies-at-work_08 |

### Done

| Moment | Sprites |
|---|---|
| Done, small (a quick or minor task) | 24-pevensies-at-work_20, 26-beavers-and-office-colleagues_09, 26-beavers-and-office-colleagues_22, 29-iconic-tools-and-office-treasures_14, 31-narnia-workday-scenes_18 |
| Sent (an email or message went out) | 26-beavers-and-office-colleagues_13, 28-wardrobe-and-lamppost-office-objects_11, 29-iconic-tools-and-office-treasures_18, 29-iconic-tools-and-office-treasures_25 |
| Done (real work finished, an item closed) | 25-aslan-and-white-witch_10, 26-beavers-and-office-colleagues_18, 26-beavers-and-office-colleagues_19, 29-iconic-tools-and-office-treasures_11, 31-narnia-workday-scenes_05, 31-narnia-workday-scenes_16 |
| Big win (several items closed at once, or no open High items left) | 24-pevensies-at-work_25, 25-aslan-and-white-witch_09, 26-beavers-and-office-colleagues_11, 29-iconic-tools-and-office-treasures_10, 29-iconic-tools-and-office-treasures_21, 31-narnia-workday-scenes_14 |
| Signing off (last task of the day, or Friday afternoon) | 25-aslan-and-white-witch_05, 26-beavers-and-office-colleagues_20, 28-wardrobe-and-lamppost-office-objects_10, 28-wardrobe-and-lamppost-office-objects_12, 30-narnia-office-locations_25, 31-narnia-workday-scenes_06, 31-narnia-workday-scenes_21, 31-narnia-workday-scenes_25 |
| Oops: general (something went wrong) | 24-pevensies-at-work_07, 24-pevensies-at-work_10, 29-iconic-tools-and-office-treasures_12, 31-narnia-workday-scenes_09, 31-narnia-workday-scenes_19 |
| Oops: blocked (access refused, permission declined, cannot proceed) | 25-aslan-and-white-witch_11, 25-aslan-and-white-witch_20, 27-narnian-creatures-at-work_11, 27-narnian-creatures-at-work_12, 28-wardrobe-and-lamppost-office-objects_01, 29-iconic-tools-and-office-treasures_13, 30-narnia-office-locations_04, 30-narnia-office-locations_18 |
| Oops: timed out | 25-aslan-and-white-witch_17, 25-aslan-and-white-witch_24, 29-iconic-tools-and-office-treasures_16, 30-narnia-office-locations_05 |
| Oops: nothing found (empty search, missing file or folder) | 28-wardrobe-and-lamppost-office-objects_23 |
| Oops: conflicting or tangled (sources disagree, knotted dependencies) | 25-aslan-and-white-witch_25, 31-narnia-workday-scenes_02, 31-narnia-workday-scenes_20 |
| Your turn (a question or decision for the user) | 24-pevensies-at-work_13, 25-aslan-and-white-witch_15, 26-beavers-and-office-colleagues_21, 28-wardrobe-and-lamppost-office-objects_24, 29-iconic-tools-and-office-treasures_04, 31-narnia-workday-scenes_03 |

### Seasons and holidays

| Season or holiday | Sprites |
|---|---|
| Winter (December to February) | 25-aslan-and-white-witch_21, 28-wardrobe-and-lamppost-office-objects_06, 28-wardrobe-and-lamppost-office-objects_20, 30-narnia-office-locations_13 |
| Spring (March to May) | 27-narnian-creatures-at-work_09, 27-narnian-creatures-at-work_10, 30-narnia-office-locations_14 |
| Christmas (December 1 to 26) | 26-beavers-and-office-colleagues_12, 26-beavers-and-office-colleagues_23, 30-narnia-office-locations_19, 31-narnia-workday-scenes_24 |

## Adding a family or new sprites

1. Put the sheet (transparent PNG, figures well apart, nothing cropped at the edges) in `<family>/originals/`.
2. Run `python3 scripts/make_sprites.py <family>`: writes `<family>/<sheet>_<NN>.webp`, 160 px, numbered in reading order. With a `<sheet>.json` index (`columns`, `rows`) beside the sheet, pieces are grouped by grid cell, so a prop that floats apart stays with its figure.
3. Add the family's tables here (default family inline; other families may live in `families/<family>.md`, read only when asked for).
4. Commit, tag the next version (`v2`, `v3`...), and change `@vN` in the widget code above. A tag is fixed once published; jsDelivr caches it for good.
