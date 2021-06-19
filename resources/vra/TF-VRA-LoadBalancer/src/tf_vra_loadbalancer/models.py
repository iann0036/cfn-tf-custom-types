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
    Address: Optional[str]
    CreatedAt: Optional[str]
    CustomProperties: Optional[Sequence["_CustomPropertiesDefinition"]]
    DeploymentId: Optional[str]
    Description: Optional[str]
    ExternalId: Optional[str]
    ExternalRegionId: Optional[str]
    ExternalZoneId: Optional[str]
    Id: Optional[str]
    InternetFacing: Optional[bool]
    Links: Optional[Sequence["_LinksDefinition"]]
    Name: Optional[str]
    OrganizationId: Optional[str]
    Owner: Optional[str]
    ProjectId: Optional[str]
    UpdatedAt: Optional[str]
    Nics: Optional[Sequence["_NicsDefinition"]]
    Routes: Optional[Sequence["_RoutesDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Targets: Optional[Sequence["_TargetsDefinition"]]

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
            Address=json_data.get("Address"),
            CreatedAt=json_data.get("CreatedAt"),
            CustomProperties=deserialize_list(json_data.get("CustomProperties"), CustomPropertiesDefinition),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            ExternalId=json_data.get("ExternalId"),
            ExternalRegionId=json_data.get("ExternalRegionId"),
            ExternalZoneId=json_data.get("ExternalZoneId"),
            Id=json_data.get("Id"),
            InternetFacing=json_data.get("InternetFacing"),
            Links=deserialize_list(json_data.get("Links"), LinksDefinition),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            Owner=json_data.get("Owner"),
            ProjectId=json_data.get("ProjectId"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Nics=deserialize_list(json_data.get("Nics"), NicsDefinition),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Targets=deserialize_list(json_data.get("Targets"), TargetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPropertiesDefinition = CustomPropertiesDefinition


@dataclass
class LinksDefinition(BaseModel):
    Href: Optional[str]
    Hrefs: Optional[Sequence[str]]
    Rel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinksDefinition"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
            Hrefs=json_data.get("Hrefs"),
            Rel=json_data.get("Rel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinksDefinition = LinksDefinition


@dataclass
class NicsDefinition(BaseModel):
    Addresses: Optional[Sequence[str]]
    CustomProperties: Optional[Sequence["_CustomPropertiesDefinition2"]]
    Description: Optional[str]
    DeviceIndex: Optional[float]
    Name: Optional[str]
    NetworkId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NicsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            CustomProperties=deserialize_list(json_data.get("CustomProperties"), CustomPropertiesDefinition2),
            Description=json_data.get("Description"),
            DeviceIndex=json_data.get("DeviceIndex"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicsDefinition = NicsDefinition


@dataclass
class CustomPropertiesDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPropertiesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPropertiesDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPropertiesDefinition2 = CustomPropertiesDefinition2


@dataclass
class RoutesDefinition(BaseModel):
    HealthCheckConfiguration: Optional[Sequence["_HealthCheckConfigurationDefinition"]]
    MemberPort: Optional[str]
    MemberProtocol: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthCheckConfiguration=deserialize_list(json_data.get("HealthCheckConfiguration"), HealthCheckConfigurationDefinition),
            MemberPort=json_data.get("MemberPort"),
            MemberProtocol=json_data.get("MemberProtocol"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class HealthCheckConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfigurationDefinition = HealthCheckConfigurationDefinition


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


@dataclass
class TargetsDefinition(BaseModel):
    MachineId: Optional[str]
    NetworkInterfaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            MachineId=json_data.get("MachineId"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetsDefinition = TargetsDefinition


