"""
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. 
Write a program that reads this file as a stream and returns the top 3 candidates at any given time. If you find a voter voting more than once, report this as fraud.

"""

import sys
import heapq
from collections import defaultdict

class StreamTally:
    def __init__(self, k=3):
        self.k = k
        self.seen_voters = set()
        self.fraud_voters = set()
        self.counts = defaultdict(int)          # candidate_id -> count
        self.heap = []                           # lazy max-heap via (-count, candidate_id)

    def _push_candidate(self, candidate_id):
        # Push current snapshot into heap for lazy retrieval
        heapq.heappush(self.heap, (-self.counts[candidate_id], candidate_id))

    def _top_k(self):
        # Pop until we have k valid entries matching current counts
        result = []
        seen_candidates = set()
        while self.heap and len(result) < self.k:
            neg_cnt, cid = heapq.heappop(self.heap)
            cnt = -neg_cnt
            # Validate snapshot
            if self.counts.get(cid, 0) == cnt and cid not in seen_candidates:
                result.append((cid, cnt))
                seen_candidates.add(cid)
        # Reinsert what we used so future queries still work lazily
        for cid, cnt in result:
            heapq.heappush(self.heap, (-cnt, cid))
        return result

    def process_record(self, voter_id, candidate_id):
        """
        Process a single (voter_id, candidate_id).
        Returns:
          fraud_flag: bool
          topk: list[(candidate_id, count)] sorted by count desc, then candidate_id
        """
        fraud_flag = False
        if voter_id in self.seen_voters:
            # Fraud detected, do not count this vote
            fraud_flag = True
            self.fraud_voters.add(voter_id)
        else:
            self.seen_voters.add(voter_id)
            self.counts[candidate_id] += 1
            self._push_candidate(candidate_id)

        topk = self._top_k()
        return fraud_flag, topk

def parse_line(line):
    """
    Accepts lines like:
      (123, 7)
      123,7
      123 7
    Returns (voter_id, candidate_id) as ints, or None if malformed.
    """
    s = line.strip()
    if not s:
        return None
    # Remove optional parentheses
    if s[0] == '(' and s[-1] == ')':
        s = s[1:-1]
    # Split on comma or whitespace
    if ',' in s:
        parts = [p.strip() for p in s.split(',', 1)]
    else:
        parts = s.split()
    if len(parts) != 2:
        return None
    try:
        voter_id = int(parts[0])
        candidate_id = int(parts[1])
        return voter_id, candidate_id
    except ValueError:
        return None

def stream_from_file(fileobj=sys.stdin):
    """
    Reads from a text stream line by line and prints state after each record.
    """
    tally = StreamTally(k=3)
    for line_no, line in enumerate(fileobj, 1):
        rec = parse_line(line)
        if rec is None:
            # Skip malformed line
            continue
        voter_id, candidate_id = rec
        fraud, top3 = tally.process_record(voter_id, candidate_id)
        if fraud:
            print(f"[line {line_no}] FRAUD: voter {voter_id} attempted multiple votes")
        # Print current top-3
        pretty = ", ".join(f"{cid}:{cnt}" for cid, cnt in top3)
        print(f"[line {line_no}] top3 -> [{pretty}]")

if __name__ == "__main__":
    # Usage:
    #   python tally.py < votes.txt
    # Where votes.txt contains one record per line, e.g.:
    #   (101, 5)
    #   102, 7
    #   103 5
    #   101, 9   # duplicate voter_id -> fraud
    stream_from_file()
