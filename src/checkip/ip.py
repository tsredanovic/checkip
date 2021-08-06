from checkip.providers import providers_dict


def get_ip(obtainer):
    if isinstance(obtainer, str):
        return providers_dict[obtainer]().get_ip()
    else:
        return obtainer().get_ip()
