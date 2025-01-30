from dataclasses import dataclass, asdict


@dataclass
class PayloadDTO:
    sub: str
    role: str

    def to_dict(self):
        return asdict(self)
