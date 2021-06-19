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
    ClientConnThrottle: Optional[float]
    Created: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Ipv4: Optional[str]
    Ipv6: Optional[str]
    Label: Optional[str]
    Region: Optional[str]
    Tags: Optional[Sequence[str]]
    Transfer: Optional[Sequence["_TransferDefinition"]]
    Updated: Optional[str]

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
            ClientConnThrottle=json_data.get("ClientConnThrottle"),
            Created=json_data.get("Created"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Label=json_data.get("Label"),
            Region=json_data.get("Region"),
            Tags=json_data.get("Tags"),
            Transfer=deserialize_list(json_data.get("Transfer"), TransferDefinition),
            Updated=json_data.get("Updated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TransferDefinition(BaseModel):
    In: Optional[float]
    Out: Optional[float]
    Total: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TransferDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransferDefinition"]:
        if not json_data:
            return None
        return cls(
            In=json_data.get("In"),
            Out=json_data.get("Out"),
            Total=json_data.get("Total"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransferDefinition = TransferDefinition


