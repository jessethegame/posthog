STEP_ACTION_SQL = """
    arrayFilter(
        (timestamp, event, uuid, properties, distinct_id {person_prop_param}) ->
            {is_first_step} AND
            (team_id = {team_id}) AND
            uuid IN {actions_query} {filters}
        , timestamps, eventsArr, event_ids, event_props, distinct_ids {person_prop_arg}
    )[1] AS step_{step}
"""
