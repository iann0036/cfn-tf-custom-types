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
    CidrIp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpProtocol: Optional[str]
    Policy: Optional[str]
    PortRange: Optional[str]
    SecurityGroupId: Optional[str]
    SourceSgid: Optional[str]
    Type: Optional[str]
    AddressTemplate: Optional[Sequence["_AddressTemplateDefinition"]]
    ProtocolTemplate: Optional[Sequence["_ProtocolTemplateDefinition"]]

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
            CidrIp=json_data.get("CidrIp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpProtocol=json_data.get("IpProtocol"),
            Policy=json_data.get("Policy"),
            PortRange=json_data.get("PortRange"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SourceSgid=json_data.get("SourceSgid"),
            Type=json_data.get("Type"),
            AddressTemplate=deserialize_list(json_data.get("AddressTemplate"), AddressTemplateDefinition),
            ProtocolTemplate=deserialize_list(json_data.get("ProtocolTemplate"), ProtocolTemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddressTemplateDefinition(BaseModel):
    GroupId: Optional[str]
    TemplateId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddressTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            TemplateId=json_data.get("TemplateId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressTemplateDefinition = AddressTemplateDefinition


@dataclass
class ProtocolTemplateDefinition(BaseModel):
    GroupId: Optional[str]
    TemplateId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            TemplateId=json_data.get("TemplateId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolTemplateDefinition = ProtocolTemplateDefinition


