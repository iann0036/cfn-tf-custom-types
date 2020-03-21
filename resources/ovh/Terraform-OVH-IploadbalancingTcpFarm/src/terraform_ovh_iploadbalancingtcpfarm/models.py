# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Balance: Optional[str]
    DisplayName: Optional[str]
    Port: Optional[float]
    ServiceName: Optional[str]
    Stickiness: Optional[str]
    VrackNetworkId: Optional[float]
    Zone: Optional[str]
    Probe: Optional[Sequence["_Probe"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Balance=json_data.get("Balance"),
            DisplayName=json_data.get("DisplayName"),
            Port=json_data.get("Port"),
            ServiceName=json_data.get("ServiceName"),
            Stickiness=json_data.get("Stickiness"),
            VrackNetworkId=json_data.get("VrackNetworkId"),
            Zone=json_data.get("Zone"),
            Probe=json_data.get("Probe"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Probe:
    ForceSsl: Optional[bool]
    Interval: Optional[float]
    Match: Optional[str]
    Method: Optional[str]
    Negate: Optional[bool]
    Pattern: Optional[str]
    Port: Optional[float]
    Type: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Probe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Probe"]:
        if not json_data:
            return None
        return cls(
            ForceSsl=json_data.get("ForceSsl"),
            Interval=json_data.get("Interval"),
            Match=json_data.get("Match"),
            Method=json_data.get("Method"),
            Negate=json_data.get("Negate"),
            Pattern=json_data.get("Pattern"),
            Port=json_data.get("Port"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Probe = Probe


