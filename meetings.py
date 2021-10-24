class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __repr__(self):
      return f"Meeting({self.start}, {self.end})"


def merge_meetings(meetings):
    ordered = sorted(meetings, key=lambda x: x.start)
    tmp = ordered[0]
    condensed_meetings = [tmp]
    for i in ordered[1:]:
        #(1) If it overlaps a condensed element, replace with latest end
        if i.start < tmp.end:
          condensed_meetings[-1].end = i.end
          tmp = Meeting(tmp.start, i.end)
        #If it doesn't, append to output array and then (1) check overlaps for it.
        else:
          condensed_meetings.append(i)
          tmp = Meeting(tmp.start, i.end)
    print(f"Condensed Meetings: {condensed_meetings}")
if __name__ == '__main__':
    meetings = [Meeting(13, 18), Meeting(0, 1), Meeting(2, 5), Meeting(3, 5), Meeting(8, 10), Meeting(9, 14)]
    print(meetings)
    merge_meetings(meetings)