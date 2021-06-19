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
    Date: Optional[float]
    DynamicSortSubtable: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Log: Optional[str]
    LogPacket: Optional[str]
    Name: Optional[str]
    Os: Optional[str]
    Rev: Optional[float]
    RuleId: Optional[float]
    Service: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]

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
            Date=json_data.get("Date"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Log=json_data.get("Log"),
            LogPacket=json_data.get("LogPacket"),
            Name=json_data.get("Name"),
            Os=json_data.get("Os"),
            Rev=json_data.get("Rev"),
            RuleId=json_data.get("RuleId"),
            Service=json_data.get("Service"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    Id: Optional[float]
    Metaid: Optional[float]
    Valueid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Metaid=json_data.get("Metaid"),
            Valueid=json_data.get("Valueid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


