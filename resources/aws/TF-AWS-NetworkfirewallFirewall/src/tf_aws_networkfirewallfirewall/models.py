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
    Arn: Optional[str]
    DeleteProtection: Optional[bool]
    Description: Optional[str]
    FirewallPolicyArn: Optional[str]
    FirewallPolicyChangeProtection: Optional[bool]
    FirewallStatus: Optional[Sequence["_FirewallStatusDefinition3"]]
    Id: Optional[str]
    Name: Optional[str]
    SubnetChangeProtection: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UpdateToken: Optional[str]
    VpcId: Optional[str]
    SubnetMapping: Optional[Sequence["_SubnetMappingDefinition"]]

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
            Arn=json_data.get("Arn"),
            DeleteProtection=json_data.get("DeleteProtection"),
            Description=json_data.get("Description"),
            FirewallPolicyArn=json_data.get("FirewallPolicyArn"),
            FirewallPolicyChangeProtection=json_data.get("FirewallPolicyChangeProtection"),
            FirewallStatus=deserialize_list(json_data.get("FirewallStatus"), FirewallStatusDefinition3),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SubnetChangeProtection=json_data.get("SubnetChangeProtection"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UpdateToken=json_data.get("UpdateToken"),
            VpcId=json_data.get("VpcId"),
            SubnetMapping=deserialize_list(json_data.get("SubnetMapping"), SubnetMappingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FirewallStatusDefinition3(BaseModel):
    SyncStates: Optional[Sequence["_FirewallStatusDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallStatusDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallStatusDefinition3"]:
        if not json_data:
            return None
        return cls(
            SyncStates=deserialize_list(json_data.get("SyncStates"), FirewallStatusDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallStatusDefinition3 = FirewallStatusDefinition3


@dataclass
class FirewallStatusDefinition2(BaseModel):
    Attachment: Optional[Sequence["_FirewallStatusDefinition"]]
    AvailabilityZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallStatusDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallStatusDefinition2"]:
        if not json_data:
            return None
        return cls(
            Attachment=deserialize_list(json_data.get("Attachment"), FirewallStatusDefinition),
            AvailabilityZone=json_data.get("AvailabilityZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallStatusDefinition2 = FirewallStatusDefinition2


@dataclass
class FirewallStatusDefinition(BaseModel):
    EndpointId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointId=json_data.get("EndpointId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallStatusDefinition = FirewallStatusDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class SubnetMappingDefinition(BaseModel):
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetMappingDefinition = SubnetMappingDefinition


