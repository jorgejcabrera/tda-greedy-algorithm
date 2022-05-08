from src.model.provider_service import SolutionNotFound


#
# PRE: The providers must be sorted, otherwise it won't work properly.
# #
def find_providers_to_hire(sorted_providers, target_position):
    last_position_covered = 0
    providers_to_hire = []

    while last_position_covered < target_position and len(sorted_providers) > 0:
        best_provider = sorted_providers.pop(0)
        if not best_provider.is_below(last_position_covered):
            print("There isn't an available provider between positions:", last_position_covered, "and",
                  best_provider.lower_position())
            raise SolutionNotFound()
        while len(sorted_providers) > 0 and sorted_providers[0].is_below(last_position_covered):
            next_provider = sorted_providers.pop(0)
            if next_provider.higher_position() >= best_provider.higher_position():
                best_provider = next_provider

        last_position_covered = best_provider.higher_position()
        providers_to_hire.append(best_provider)

    if last_position_covered < target_position:
        print("There aren't enough providers to cover the expected area.")
        raise SolutionNotFound()

    return providers_to_hire
