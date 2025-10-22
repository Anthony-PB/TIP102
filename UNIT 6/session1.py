# # """
# # class SongNode:
# #     def __init__(self, song, artist, next=None):
# #         self.song = song
# #         self.artist = artist
# #         self.next = next
    
# # def print_linked_list(node):
# #     current = node
# #     while current:
# #         print((current.song, current.artist), end=" -> " if current.next else "")
# #         current = current.next
# #     print()

# # # For testing
# # # def print_linked_list(node):
# # #     current = node
# # #     while current:
# # #         print(current.song, end=" -> " if current.next else "")
# # #         current = current.next
# # #     print()
        

    
# # # top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# # # node1 = SongNode("Bad Romance")
# # # node2 = SongNode("Party Rock Anthem", node1)
# # # node3 = SongNode("Uptown Funk", node2)


# # # print_linked_list(top_hits_2010s)
# # # print_linked_list(node3)

# # # U: Make a frequency map of each artist in the given playlist
# # # P: Make a dictionary
# # # For every new entry, make a new key and add 1 to its frequency
# # # Otherwise, add 1 to the artist's frequency
# # # return the dictionary


# # # Time: O(n), Space: O(n)
# # # def get_artist_frequency(playlist):
# # #     frequency = {}

# # #     curr = playlist
# # #     while curr:
# # #         frequency[curr.artist] = frequency.get(curr.artist, 0) + 1
# # #         curr = curr.next

# # #     return frequency


# # # playlist = SongNode("Saturn", "SZA", 
# # #                 SongNode("Who", "Jimin", 
# # #                         SongNode("Espresso", "Sabrina Carpenter", 
# # #                                 SongNode("Snooze", "SZA"))))

# # # print(get_artist_frequency(playlist))

# # # Function with a bug!
# # def remove_song(playlist_head, song):
# #     # if empty
# #     if not playlist_head:
# #         return None
# #     # remove head if head has the song
# #     if playlist_head.song == song:
# #         return playlist_head.next

# #     current = playlist_head
# #     while current.next:
# #         if current.next.song == song:
# #             current.next = current.next.next  
# #             return playlist_head 
# #         current = current.next

# #     return playlist_head

# # playlist = SongNode("SOS", "ABBA", 
# #                 SongNode("Simple Twist of Fate", "Bob Dylan",
# #                     SongNode("Dreams", "Fleetwood Mac",
# #                         SongNode("Lovely Day", "Bill Withers"))))

# # print_linked_list(remove_song(playlist, "Dreams"))
# # """
# # """""
# # class SongNode:
# #     def __init__(self, song, artist, next=None):
# #         self.song = song
# #         self.artist = artist
# #         self.next = next
# #     def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.value, end=" -> " if current.next else "\n")
# #         current = current.next
# # """
# # # # Time: O(n), Space: O(1)
# # # def on_repeat(playlist_head):
# # #     slow = playlist_head
# # #     fast = playlist_head
# # #     while fast and fast.next:
# # #         slow = slow.next
# # #         fast = fast.next.next
# # #         if fast == slow:
# # #             return True
# # #     return False

# # # song1 = SongNode("GO!", "Common")
# # # song2 = SongNode("N95", "Kendrick Lamar")
# # # song3 = SongNode("WIN", "Jay Rock")
# # # song4 = SongNode("ATM", "J. Cole")
# # # song1.next = song2
# # # song2.next = song3
# # # song3.next = song4
# # # song4.next = song2

# # # def loop_length(playlist_head):
# # #     slow = playlist_head
# # #     fast = playlist_head
# # #     count = 1
# # #     while fast and fast.next:
# # #         slow = slow.next
# # #         fast = fast.next.next
# # #         if fast == slow:
# # #             break
    
# # #     if fast != slow:
# # #         return 0
# # #     else:
# # #         fast = fast.next
# # #         while fast != slow:
# # #             fast = fast.next
# # #             count += 1
# # #     return count

# # # print(loop_length(song1))

# # # class Node:
# # #     def __init__(self, value, next=None):
# # #         self.value = value
# # #         self.next = next

# # # # For testing
# # # def print_linked_list(head):
# # #     current = head
# # #     while current:
# # #         print(current.value, end=" -> " if current.next else "\n")
# # #         current = current.next


# # # def count_critical_points(song_audio):
# # #     prev = song_audio
# # #     curr = song_audio.next
# # #     npoint = song_audio.next.next
# # #     if not curr or not npoint:
# # #         return 0
# # #     critical_points = 0
# # #     while(npoint):
# # #         if((prev.value < curr.value and curr.value > npoint.value) or (prev.value > curr.value and curr.value < npoint.value)):
# # #             critical_points += 1
# # #         prev = prev.next
# # #         curr = curr.next
# # #         npoint = npoint.next
# # #     return critical_points

# # # song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))
# # # print(count_critical_points(song_audio))

# # class Node:
# #     def __init__(self, potion, next=None):
# #         # self.house = house
# #         # self.value = score
# #         self.potion = potion
# #         self.next = next

# # # # For testing
# # # def print_linked_list(head):
# # #     current = head
# # #     while current:
# # #         print((current.house, current.value), end=" -> " if current.next else "\n")
# # #         current = current.next

# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.potion, end=" -> " if current.next else "\n")
# #         current = current.next


# # # def count_element(house_points, score):
# # #     curr = house_points
# # #     freq = 0
# # #     while(curr):
# # #         if curr.value == score:
# # #             freq += 1
# # #         curr = curr.next
# #     # return freq

# # # house_points = Node("Gryffindor", 600, 
# # #                 Node("Ravenclaw", 300,
# # #                     Node("Slytherin", 500,
# # #                         Node("Hufflepuff", 600))))                  

# # # print(count_element(house_points, 600))



# # def find_middle_potion(potions):
# #     slow, fast = potions, potions

# #     while(fast and fast.next):
# #         slow = slow.next
# #         fast = fast.next.next
    
# #     return slow.potion
    

# # potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
# # potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))

# # print(find_middle_potion(potions1))
# # print(find_middle_potion(potions2))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def reverse(events):
#     prev, curr = None, events

#     while(curr):
#         dummy = curr.next
#         curr.next = prev
#         prev = curr
#         curr = dummy
#     return prev


# events = Node("Potion Brewing", 
#             Node("Spell Casting", 
#                 Node("Wand Making", 
#                     Node("Dragon Taming", 
#                         Node("Broomstick Flying")))))

# print_linked_list(reverse(events))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def is_mirrored(head):
    pass


list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))

print(is_mirrored(list1))
print(is_mirrored(list2))