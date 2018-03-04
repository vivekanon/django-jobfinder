import collections
import operator

from job.models import Job
from user.models import WorkSchedule


def check_abilities_for_employer(abilities_needed, field_of_work):
    schedules = WorkSchedule.objects.filter(field_of_work=field_of_work)

    ability_conformity = 0
    conformity_result = {}
    for schedule in schedules:
        for ability in abilities_needed:
            for ability_have in schedule.abilities_have:
                if ability_have == ability:
                    print(ability_have)
                    print(ability)
                    ability_conformity += 1
        conformity_result.update({schedule.employee.id: ability_conformity})
        ability_conformity = 0

    # ability_conformity_ordered = collections.OrderedDict(sorted(conformity_result.items()))
    # print(ability_conformity_ordered)

    print(max(conformity_result.items(), key=operator.itemgetter(1))[0])
    return max(conformity_result.items(), key=operator.itemgetter(1))[0]


def check_abilities_for_employee(abilities_have, field_of_work):
    jobs = Job.objects.filter(field_of_work=field_of_work)

    ability_conformity = 0
    conformity_result = {}
    for job in jobs:
        for ability in abilities_have:
            for ability_needed in jobs.abilities_have:
                if ability_needed == ability:
                    print(ability_needed)
                    print(ability)
                    ability_conformity += 1
        conformity_result.update({job.employer.id: ability_conformity})
        ability_conformity = 0

    # ability_conformity_ordered = collections.OrderedDict(sorted(conformity_result.items()))
    # print(ability_conformity_ordered)

    print(max(conformity_result.items(), key=operator.itemgetter(1))[0])
    return max(conformity_result.items(), key=operator.itemgetter(1))[0]
