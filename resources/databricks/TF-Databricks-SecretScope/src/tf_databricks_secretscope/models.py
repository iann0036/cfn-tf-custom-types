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
    BackendType: Optional[str]
    Id: Optional[str]
    InitialManagePrincipal: Optional[str]
    Name: Optional[str]
    KeyvaultMetadata: Optional[Sequence["_KeyvaultMetadataDefinition"]]

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
            BackendType=json_data.get("BackendType"),
            Id=json_data.get("Id"),
            InitialManagePrincipal=json_data.get("InitialManagePrincipal"),
            Name=json_data.get("Name"),
            KeyvaultMetadata=deserialize_list(json_data.get("KeyvaultMetadata"), KeyvaultMetadataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KeyvaultMetadataDefinition(BaseModel):
    DnsName: Optional[str]
    ResourceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyvaultMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyvaultMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsName=json_data.get("DnsName"),
            ResourceId=json_data.get("ResourceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyvaultMetadataDefinition = KeyvaultMetadataDefinition


