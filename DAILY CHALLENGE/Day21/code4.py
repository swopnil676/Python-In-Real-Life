class TicketNumbers:

    def __iter__(self):
        self.number = 10
        return self

    def __next__(self):
        current = self.number
        self.number += 1
        return current


tickets = TicketNumbers()
ticket_iterator = iter(tickets)

print(next(ticket_iterator))
print(next(ticket_iterator))
print(next(ticket_iterator))