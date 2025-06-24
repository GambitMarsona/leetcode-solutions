class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_stack = [0]
        visited = set()
        while key_stack:
            room = key_stack.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    key_stack.append(key)
        return len(visited) == len(rooms)