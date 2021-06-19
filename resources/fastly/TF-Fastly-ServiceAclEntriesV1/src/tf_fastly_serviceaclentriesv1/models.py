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
    AclId: Optional[str]
    Id: Optional[str]
    ServiceId: Optional[str]
    Entry: Optional[Sequence["_EntryDefinition"]]

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
            AclId=json_data.get("AclId"),
            Id=json_data.get("Id"),
            ServiceId=json_data.get("ServiceId"),
            Entry=deserialize_list(json_data.get("Entry"), EntryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EntryDefinition(BaseModel):
    Comment: Optional[str]
    Ip: Optional[str]
    Negated: Optional[bool]
    Subnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Ip=json_data.get("Ip"),
            Negated=json_data.get("Negated"),
            Subnet=json_data.get("Subnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntryDefinition = EntryDefinition


