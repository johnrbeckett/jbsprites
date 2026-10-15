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
   - **Done** when the work finished: the small row for a quick or minor task, the cheering row for real work. **Big win** when several things finished at once or a big milestone landed. **Signing off** for the last task of the day or a Friday afternoon.
   - **Oops** when the work failed, a connector errored, or it could not be finished. Use the Oops row matching the kind of failure (general when none fits), then say plainly what failed. Never show Done for work that did not get done.
   - **Your turn** when the reply ends with a question or a decision for the user.

A reply that needs no work (a quick answer from what is already known) gets one sprite, after the reply: Done if something was completed, otherwise its Start sprite. If the start sprite would land right next to the reply (no real work in between), skip it; the end sprite is enough. A long task that finishes several separate pieces may show Done after each piece. A retry after a failure may carry a Retrying sprite.

**Seasons.** For a Hello or a morning brief, use the current season's row about one time in three instead (northern hemisphere, by month).

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

`<h2 class="sr-only">Sprite</h2><img alt="" style="height:120px" src="https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@v3/<family>/<name>.webp">`

## Family: tumnus (default)

A faun in business casual. Rows marked for trackers apply when the caller is a tracker skill; others use the general rows.

## Start

| Kind of work | Sprites |
|---|---|
| Writing or drafting | 10-workflow-full-body_14, 10-workflow-full-body_15, 10-workflow-full-body_16, 10-workflow-full-body_17, 06-business-casual_07, 07-outfit-variations_03, 07-outfit-variations_10, 07-outfit-variations_35, 13-icons-hands-busts_01, 13-icons-hands-busts_13, 13-icons-hands-busts_18, 16-working-and-discoveries_09 |
| Research or reading | 10-workflow-full-body_11, 10-workflow-full-body_12, 10-workflow-full-body_13, 06-business-casual_18, 07-outfit-variations_08, 07-outfit-variations_16, 07-outfit-variations_24, 07-outfit-variations_28, 13-icons-hands-busts_10, 13-icons-hands-busts_21, 16-working-and-discoveries_02, 16-working-and-discoveries_03, 16-working-and-discoveries_11, 16-working-and-discoveries_12, 16-working-and-discoveries_14, 16-working-and-discoveries_15, 16-working-and-discoveries_17, 16-working-and-discoveries_18, 16-working-and-discoveries_19, 18-desktop-visitors-and-playful-tech_08 |
| Email, reconcile, sweep | 10-workflow-full-body_06, 10-workflow-full-body_07, 10-workflow-full-body_08, 10-workflow-full-body_09, 10-workflow-full-body_10, 07-outfit-variations_32, 13-icons-hands-busts_03, 13-icons-hands-busts_15 |
| Add (new tracker item) | 06-business-casual_07, 07-outfit-variations_03, 07-outfit-variations_36 |
| Waiting on someone | 06-business-casual_12, 07-outfit-variations_01, 07-outfit-variations_11, 07-outfit-variations_12 |
| Morning brief (on demand) | 07-outfit-variations_04, 07-outfit-variations_08, 07-outfit-variations_23, 06-business-casual_09, 16-working-and-discoveries_01 |
| The list | 07-outfit-variations_14, 07-outfit-variations_33, 16-working-and-discoveries_06 |
| Next | 06-business-casual_16, 07-outfit-variations_15, 07-outfit-variations_27, 15-office-mishaps-and-message-edges_15, 15-office-mishaps-and-message-edges_16 |
| Now | 07-outfit-variations_13, 06-business-casual_08 |
| Gaps, stale items | 06-business-casual_10, 06-business-casual_22, 07-outfit-variations_16, 07-outfit-variations_07 |
| Week, quarter, year | 06-business-casual_18, 07-outfit-variations_24, 07-outfit-variations_28 |
| Trip | 06-business-casual_19, 06-business-casual_24, 07-outfit-variations_19, 07-outfit-variations_20, 07-outfit-variations_22 |
| Hand-off | 06-business-casual_21, 07-outfit-variations_29 |
| Hello (first reply of a tracker skill in a chat) | 06-business-casual_17, 07-outfit-variations_17, 07-outfit-variations_34, 13-icons-hands-busts_22, 15-office-mishaps-and-message-edges_11, 15-office-mishaps-and-message-edges_12, 15-office-mishaps-and-message-edges_18, 15-office-mishaps-and-message-edges_20 |
| Anything else | 10-workflow-full-body_01, 10-workflow-full-body_02, 10-workflow-full-body_03, 10-workflow-full-body_04, 10-workflow-full-body_05, 07-outfit-variations_13, 06-business-casual_08, 13-icons-hands-busts_12, 13-icons-hands-busts_14, 16-working-and-discoveries_04, 16-working-and-discoveries_10, 15-office-mishaps-and-message-edges_06 |
| Calendar, scheduling, focus blocks | 14-calendar-money-tech_06, 14-calendar-money-tech_07, 14-calendar-money-tech_08, 14-calendar-money-tech_09, 14-calendar-money-tech_10, 13-icons-hands-busts_04 |
| Invoices, payments, money | 14-calendar-money-tech_11, 14-calendar-money-tech_12, 14-calendar-money-tech_13, 14-calendar-money-tech_14, 14-calendar-money-tech_15, 13-icons-hands-busts_05 |
| Technical (DNS, servers, networks, code) | 14-calendar-money-tech_16, 14-calendar-money-tech_17, 14-calendar-money-tech_18, 14-calendar-money-tech_19, 14-calendar-money-tech_20, 13-icons-hands-busts_06, 13-icons-hands-busts_16, 16-working-and-discoveries_08, 18-desktop-visitors-and-playful-tech_11, 18-desktop-visitors-and-playful-tech_12, 18-desktop-visitors-and-playful-tech_13, 18-desktop-visitors-and-playful-tech_14, 18-desktop-visitors-and-playful-tech_15, 18-desktop-visitors-and-playful-tech_16, 18-desktop-visitors-and-playful-tech_17, 18-desktop-visitors-and-playful-tech_18, 18-desktop-visitors-and-playful-tech_19, 18-desktop-visitors-and-playful-tech_20 |
| Image or design work | 13-icons-hands-busts_11 |
| Waiting on a long job (upload, deploy, background run) | 13-icons-hands-busts_07, 06-business-casual_12, 07-outfit-variations_12, 16-working-and-discoveries_05, 16-working-and-discoveries_07, 15-office-mishaps-and-message-edges_13 |
| Retrying (trying again after a failure; send with the retry call) | 12-failure-and-recovery_16, 12-failure-and-recovery_17, 12-failure-and-recovery_20 |

## Done

| Moment | Sprites |
|---|---|
| Done, small (a quick or minor task) | 14-calendar-money-tech_01, 14-calendar-money-tech_02, 14-calendar-money-tech_03, 14-calendar-money-tech_04, 14-calendar-money-tech_05, 13-icons-hands-busts_02, 13-icons-hands-busts_20, 13-icons-hands-busts_24, 16-working-and-discoveries_13, 16-working-and-discoveries_16, 16-working-and-discoveries_20, 18-desktop-visitors-and-playful-tech_01, 18-desktop-visitors-and-playful-tech_02, 18-desktop-visitors-and-playful-tech_04, 18-desktop-visitors-and-playful-tech_05, 18-desktop-visitors-and-playful-tech_06, 18-desktop-visitors-and-playful-tech_09 |
| Done (real work finished, an item closed) | 08-celebrations_01, 08-celebrations_02, 08-celebrations_03, 08-celebrations_04, 08-celebrations_05, 08-celebrations_06, 08-celebrations_07, 08-celebrations_08, 08-celebrations_12, 08-celebrations_13, 08-celebrations_16, 08-celebrations_17, 08-celebrations_18, 08-celebrations_19, 08-celebrations_20, 08-celebrations_22, 08-celebrations_23, 08-celebrations_24 |
| Big win (several items closed at once, or no open High items left) | 08-celebrations_09, 08-celebrations_10, 08-celebrations_11, 08-celebrations_14, 08-celebrations_15 |
| Signing off (last task of the day, or Friday afternoon) | 14-calendar-money-tech_03, 13-icons-hands-busts_24, 08-celebrations_20, 08-celebrations_23, 17-after-hours-and-seasonal_01, 17-after-hours-and-seasonal_02, 17-after-hours-and-seasonal_03, 17-after-hours-and-seasonal_04, 17-after-hours-and-seasonal_05, 17-after-hours-and-seasonal_06, 17-after-hours-and-seasonal_07, 17-after-hours-and-seasonal_08, 17-after-hours-and-seasonal_09, 17-after-hours-and-seasonal_10, 18-desktop-visitors-and-playful-tech_07 |
| Oops: general (something went wrong) | 12-failure-and-recovery_01, 12-failure-and-recovery_02, 12-failure-and-recovery_03, 12-failure-and-recovery_05, 10-workflow-full-body_20, 06-business-casual_22, 07-outfit-variations_07, 15-office-mishaps-and-message-edges_01, 15-office-mishaps-and-message-edges_02, 15-office-mishaps-and-message-edges_04, 15-office-mishaps-and-message-edges_05, 15-office-mishaps-and-message-edges_07, 15-office-mishaps-and-message-edges_08, 15-office-mishaps-and-message-edges_09, 18-desktop-visitors-and-playful-tech_10 |
| Oops: blocked (access refused, permission declined, cannot proceed) | 12-failure-and-recovery_08, 12-failure-and-recovery_10, 13-icons-hands-busts_09 |
| Oops: connection error (a connector or service is down) | 12-failure-and-recovery_09 |
| Oops: timed out | 12-failure-and-recovery_12 |
| Oops: nothing found (empty search, missing file or folder) | 12-failure-and-recovery_06, 12-failure-and-recovery_07, 12-failure-and-recovery_13 |
| Oops: conflicting or tangled (sources disagree, knotted dependencies) | 12-failure-and-recovery_04, 12-failure-and-recovery_11, 12-failure-and-recovery_14, 15-office-mishaps-and-message-edges_03, 15-office-mishaps-and-message-edges_10 |
| Your turn (a question or decision for the user) | 12-failure-and-recovery_18, 12-failure-and-recovery_15, 12-failure-and-recovery_19, 10-workflow-full-body_18, 10-workflow-full-body_19, 06-business-casual_21, 13-icons-hands-busts_17, 13-icons-hands-busts_23, 13-icons-hands-busts_19, 15-office-mishaps-and-message-edges_17, 15-office-mishaps-and-message-edges_19 |

## Seasons (tumnus)

| Season | Sprites |
|---|---|
| Autumn (September to November) | 17-after-hours-and-seasonal_11, 17-after-hours-and-seasonal_19 |
| Winter (December to February) | 17-after-hours-and-seasonal_12, 17-after-hours-and-seasonal_16, 17-after-hours-and-seasonal_17, 17-after-hours-and-seasonal_20 |
| Spring (March to May) | 17-after-hours-and-seasonal_13, 17-after-hours-and-seasonal_18 |
| Summer (June to August) | 17-after-hours-and-seasonal_14, 17-after-hours-and-seasonal_15 |

## Adding a family or new sprites

1. Put the sheet (transparent PNG, figures well apart, nothing cropped at the edges) in `<family>/originals/`.
2. Run `python3 scripts/make_sprites.py <family>`: writes `<family>/<sheet>_<NN>.webp`, 160 px, numbered in reading order. With a `<sheet>.json` index (`columns`, `rows`) beside the sheet, pieces are grouped by grid cell, so a prop that floats apart stays with its figure.
3. Add the family's tables here (default family inline; other families may live in `families/<family>.md`, read only when asked for).
4. Commit, tag the next version (`v2`, `v3`...), and change `@vN` in the widget code above. A tag is fixed once published; jsDelivr caches it for good.
