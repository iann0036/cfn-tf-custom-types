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
    CloudAccountName: Optional[str]
    Description: Optional[str]
    Dome9CloudAccountId: Optional[str]
    Dome9SecurityGroupName: Optional[str]
    ExternalSecurityGroupId: Optional[str]
    Id: Optional[str]
    IsTamperProtected: Optional[bool]
    LastUpdatedByDome9: Optional[str]
    Region: Optional[str]
    ResourceGroup: Optional[str]
    Inbound: Optional[Sequence["_InboundDefinition"]]
    Outbound: Optional[Sequence["_OutboundDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]

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
            CloudAccountName=json_data.get("CloudAccountName"),
            Description=json_data.get("Description"),
            Dome9CloudAccountId=json_data.get("Dome9CloudAccountId"),
            Dome9SecurityGroupName=json_data.get("Dome9SecurityGroupName"),
            ExternalSecurityGroupId=json_data.get("ExternalSecurityGroupId"),
            Id=json_data.get("Id"),
            IsTamperProtected=json_data.get("IsTamperProtected"),
            LastUpdatedByDome9=json_data.get("LastUpdatedByDome9"),
            Region=json_data.get("Region"),
            ResourceGroup=json_data.get("ResourceGroup"),
            Inbound=deserialize_list(json_data.get("Inbound"), InboundDefinition),
            Outbound=deserialize_list(json_data.get("Outbound"), OutboundDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InboundDefinition(BaseModel):
    Access: Optional[str]
    Description: Optional[str]
    DestinationPortRanges: Optional[Sequence[str]]
    IsDefault: Optional[bool]
    Name: Optional[str]
    Priority: Optional[float]
    Protocol: Optional[str]
    SourcePortRanges: Optional[Sequence[str]]
    DestinationScopes: Optional[Sequence["_DestinationScopesDefinition"]]
    SourceScopes: Optional[Sequence["_SourceScopesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InboundDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Description=json_data.get("Description"),
            DestinationPortRanges=json_data.get("DestinationPortRanges"),
            IsDefault=json_data.get("IsDefault"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Protocol=json_data.get("Protocol"),
            SourcePortRanges=json_data.get("SourcePortRanges"),
            DestinationScopes=deserialize_list(json_data.get("DestinationScopes"), DestinationScopesDefinition),
            SourceScopes=deserialize_list(json_data.get("SourceScopes"), SourceScopesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundDefinition = InboundDefinition


@dataclass
class DestinationScopesDefinition(BaseModel):
    Data: Optional[Sequence["_DataDefinition"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationScopesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationScopesDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=deserialize_list(json_data.get("Data"), DataDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationScopesDefinition = DestinationScopesDefinition


@dataclass
class DataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDefinition = DataDefinition


@dataclass
class SourceScopesDefinition(BaseModel):
    Data: Optional[Sequence["_DataDefinition2"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceScopesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceScopesDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=deserialize_list(json_data.get("Data"), DataDefinition2),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceScopesDefinition = SourceScopesDefinition


@dataclass
class DataDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDefinition2 = DataDefinition2


@dataclass
class OutboundDefinition(BaseModel):
    Access: Optional[str]
    Description: Optional[str]
    DestinationPortRanges: Optional[Sequence[str]]
    IsDefault: Optional[bool]
    Name: Optional[str]
    Priority: Optional[float]
    Protocol: Optional[str]
    SourcePortRanges: Optional[Sequence[str]]
    DestinationScopes: Optional[Sequence["_DestinationScopesDefinition"]]
    SourceScopes: Optional[Sequence["_SourceScopesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutboundDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutboundDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Description=json_data.get("Description"),
            DestinationPortRanges=json_data.get("DestinationPortRanges"),
            IsDefault=json_data.get("IsDefault"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Protocol=json_data.get("Protocol"),
            SourcePortRanges=json_data.get("SourcePortRanges"),
            DestinationScopes=deserialize_list(json_data.get("DestinationScopes"), DestinationScopesDefinition),
            SourceScopes=deserialize_list(json_data.get("SourceScopes"), SourceScopesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutboundDefinition = OutboundDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


