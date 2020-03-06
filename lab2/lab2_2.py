def packet_size(packet):
    '''(list --> num)
	Checks the size of the packet list.
    '''
    return len(packet)

def error_indices(packet1, packet2):
    '''(list --> list)
	Checks if there are differences in the list and returns their places in the index.
    '''
    err_list = []
    i = 0

    while i < len(packet1):
        if packet1[i] != packet2[i]:
            err_list.append(i)
        i += 1
    return err_list

def packet_diff(packet1, packet2):
    '''(list --> num)
	Returns the number of bit errors between packet 1 and 2
    '''
    err_list = error_indices(packet1, packet2)
    return len(err_list)

if __name__ == "__main__":
    # test your bit error rate detector here

    print(packet_size([0,1,0,1]))
    print(error_indices([0,1,1,1], [1,1,0,1]))
    print(error_indices([1,1,0,1], [1,1,0,1]))
    print(packet_diff([0,1,0,1], [1,1,0,1]))
    print(packet_diff([0,1,1,0], [0,1,1,0]))

    #packet_sent = [0, 1, 1, 1]
    #packet_received = [1, 1, 1, 1]
