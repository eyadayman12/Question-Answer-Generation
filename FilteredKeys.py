def filtered_keys(common_keyPhrases, threshold):
    count = 0
    filtered_keys_l = []
    for counter in common_keyPhrases:
        if count == threshold:
            break
        filtered_keys_l.append(counter[0])
        count += 1

    return filtered_keys_l