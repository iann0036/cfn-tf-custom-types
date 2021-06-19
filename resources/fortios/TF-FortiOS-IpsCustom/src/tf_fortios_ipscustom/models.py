# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Action: Optional[str]
    Application: Optional[str]
    Comment: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Log: Optional[str]
    LogPacket: Optional[str]
    Os: Optional[str]
    Protocol: Optional[str]
    RuleId: Optional[float]
    Severity: Optional[str]
    SigName: Optional[str]
    Signature: Optional[str]
    Status: Optional[str]
    Tag: Optional[str]
    Vdomparam: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Action=json_data.get("Action"),
            Application=json_data.get("Application"),
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Log=json_data.get("Log"),
            LogPacket=json_data.get("LogPacket"),
            Os=json_data.get("Os"),
            Protocol=json_data.get("Protocol"),
            RuleId=json_data.get("RuleId"),
            Severity=json_data.get("Severity"),
            SigName=json_data.get("SigName"),
            Signature=json_data.get("Signature"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


