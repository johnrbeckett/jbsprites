---
name: jbsprites
description: Small character sprites shown inline in chat for personality, in families (default tumnus). A start sprite rides along when work begins; a done, oops or your-turn sprite closes it. Use whenever another skill or the user's preferences say to use jbsprites, or when real work starts in a chat the user is present for. Shown with the visual widget tool; images load from cdn.jsdelivr.net.
---

# jbsprites

Small character sprites that give work some personality. Pure decoration: a sprite never carries information the text does not, and is never mentioned, described or narrated.

A caller (another skill, or the user's preferences) says which family to use. No family named means **tumnus**.

## When

Every task the user asks for in chat gets two beats:

1. **Start.** A start sprite picked by the kind of work, from the family's Start table.
2. **End.** When the outcome is known, one of:
   - **Done** when the work finished. **Big win** when several things finished at once or a big milestone landed.
   - **Oops** when the work failed, a connector errored, or it could not be finished. Use the Oops row matching the kind of failure (general when none fits), then say plainly what failed. Never show Done for work that did not get done.
   - **Your turn** when the reply ends with a question or a decision for the user.

A reply that needs no work (a quick answer from what is already known) gets one sprite: Done if something was completed, otherwise its Start sprite. A long task that finishes several separate pieces may show Done after each piece. A retry after a failure may carry a Retrying sprite.

Never in scheduled or unattended runs. If the widget tool is not available, skip sprites silently.

Pick at random within a row, avoiding the sprite used just before when there is a choice.

## How (keep sprites off the critical path)

- Load the widget tools (`mcp__visualize__read_me`, `mcp__visualize__show_widget`) in the same ToolSearch call as the other tools the task needs.
- Call read_me once per chat, silently, in the same parallel batch as the first real work call.
- Send the start sprite in the same parallel batch as the next real work call. Never spend a round trip on a start sprite alone; if there is no real work call to ride with, skip it.
- The end sprite waits for the outcome; it is the one sprite allowed its own step, right before the reply.
- Widget code, nothing else in it, with the family and sprite name swapped in:

`<h2 class="sr-only">Sprite</h2><img alt="" style="height:120px" src="https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@v1/<family>/<name>.webp">`

## Family: tumnus (default)

A faun in business casual. Rows marked for trackers apply when the caller is a tracker skill; others use the general rows.

## Start

| Kind of work | Sprites |
|---|---|
| Writing or drafting | 10-workflow-full-body_14, 10-workflow-full-body_15, 10-workflow-full-body_16, 10-workflow-full-body_17, 06-business-casual_07, 07-outfit-variations_03, 07-outfit-variations_10, 07-outfit-variations_35 |
| Research or reading | 10-workflow-full-body_11, 10-workflow-full-body_12, 10-workflow-full-body_13, 06-business-casual_18, 07-outfit-variations_08, 07-outfit-variations_16, 07-outfit-variations_24, 07-outfit-variations_28 |
| Email, reconcile, sweep | 10-workflow-full-body_06, 10-workflow-full-body_07, 10-workflow-full-body_08, 10-workflow-full-body_09, 10-workflow-full-body_10, 07-outfit-variations_32 |
| Add (new tracker item) | 06-business-casual_07, 07-outfit-variations_03, 07-outfit-variations_36 |
| Waiting on someone | 06-business-casual_12, 07-outfit-variations_01, 07-outfit-variations_11, 07-outfit-variations_12 |
| Morning brief (on demand) | 07-outfit-variations_04, 07-outfit-variations_08, 07-outfit-variations_23, 06-business-casual_09 |
| The list | 07-outfit-variations_14, 07-outfit-variations_33 |
| Next | 06-business-casual_16, 07-outfit-variations_15, 07-outfit-variations_27 |
| Now | 07-outfit-variations_13, 06-business-casual_08 |
| Gaps, stale items | 06-business-casual_10, 06-business-casual_22, 07-outfit-variations_16, 07-outfit-variations_07 |
| Week, quarter, year | 06-business-casual_18, 07-outfit-variations_24, 07-outfit-variations_28 |
| Trip | 06-business-casual_19, 06-business-casual_24, 07-outfit-variations_19, 07-outfit-variations_20, 07-outfit-variations_22 |
| Hand-off | 06-business-casual_21, 07-outfit-variations_29 |
| Hello (first reply of a tracker skill in a chat) | 06-business-casual_17, 07-outfit-variations_17, 07-outfit-variations_34 |
| Anything else | 10-workflow-full-body_01, 10-workflow-full-body_02, 10-workflow-full-body_03, 10-workflow-full-body_04, 10-workflow-full-body_05, 07-outfit-variations_13, 06-business-casual_08 |
| Retrying (trying again after a failure; send with the retry call) | 12-failure-and-recovery_16, 12-failure-and-recovery_17, 12-failure-and-recovery_20 |

## Done

| Moment | Sprites |
|---|---|
| Done (any task finished, an item closed) | 08-celebrations_01, 08-celebrations_02, 08-celebrations_03, 08-celebrations_04, 08-celebrations_05, 08-celebrations_06, 08-celebrations_07, 08-celebrations_08, 08-celebrations_12, 08-celebrations_13, 08-celebrations_16, 08-celebrations_17, 08-celebrations_18, 08-celebrations_19, 08-celebrations_20, 08-celebrations_22, 08-celebrations_23, 08-celebrations_24 |
| Big win (several items closed at once, or no open High items left) | 08-celebrations_09, 08-celebrations_10, 08-celebrations_11, 08-celebrations_14, 08-celebrations_15 |
| Oops: general (something went wrong) | 12-failure-and-recovery_01, 12-failure-and-recovery_02, 12-failure-and-recovery_03, 12-failure-and-recovery_05, 10-workflow-full-body_20, 06-business-casual_22, 07-outfit-variations_07 |
| Oops: blocked (access refused, permission declined, cannot proceed) | 12-failure-and-recovery_08, 12-failure-and-recovery_10 |
| Oops: connection error (a connector or service is down) | 12-failure-and-recovery_09 |
| Oops: timed out | 12-failure-and-recovery_12 |
| Oops: nothing found (empty search, missing file or folder) | 12-failure-and-recovery_06, 12-failure-and-recovery_07, 12-failure-and-recovery_13 |
| Oops: conflicting or tangled (sources disagree, knotted dependencies) | 12-failure-and-recovery_04, 12-failure-and-recovery_11, 12-failure-and-recovery_14 |
| Your turn (a question or decision for the user) | 12-failure-and-recovery_18, 12-failure-and-recovery_15, 12-failure-and-recovery_19, 10-workflow-full-body_18, 10-workflow-full-body_19, 06-business-casual_21 |

## Adding a family or new sprites

1. Put the sheet (transparent PNG, figures well apart, nothing cropped at the edges) in `<family>/originals/`.
2. Run `python3 scripts/make_sprites.py <family>`: writes `<family>/<sheet>_<NN>.webp`, 160 px, numbered in reading order.
3. Add the family's tables here (default family inline; other families may live in `families/<family>.md`, read only when asked for).
4. Commit, tag the next version (`v2`, `v3`...), and change `@v1` in the widget code above. A tag is fixed once published; jsDelivr caches it for good.
