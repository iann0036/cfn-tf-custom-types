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
    DisksList: Optional[Sequence["_DisksListDefinition"]]
    ExternalId: Optional[str]
    ExternalRegionId: Optional[str]
    ExternalZoneId: Optional[str]
    Flavor: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    ImageRef: Optional[str]
    Links: Optional[Sequence["_LinksDefinition"]]
    Name: Optional[str]
    OrganizationId: Optional[str]
    Owner: Optional[str]
    PowerState: Optional[str]
    ProjectId: Optional[str]
    UpdatedAt: Optional[str]
    BootConfig: Optional[Sequence["_BootConfigDefinition"]]
    Constraints: Optional[Sequence["_ConstraintsDefinition"]]
    Disks: Optional[Sequence["_DisksDefinition"]]
    ImageDiskConstraints: Optional[Sequence["_ImageDiskConstraintsDefinition"]]
    Nics: Optional[Sequence["_NicsDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            DisksList=deserialize_list(json_data.get("DisksList"), DisksListDefinition),
            ExternalId=json_data.get("ExternalId"),
            ExternalRegionId=json_data.get("ExternalRegionId"),
            ExternalZoneId=json_data.get("ExternalZoneId"),
            Flavor=json_data.get("Flavor"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            ImageRef=json_data.get("ImageRef"),
            Links=deserialize_list(json_data.get("Links"), LinksDefinition),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            Owner=json_data.get("Owner"),
            PowerState=json_data.get("PowerState"),
            ProjectId=json_data.get("ProjectId"),
            UpdatedAt=json_data.get("UpdatedAt"),
            BootConfig=deserialize_list(json_data.get("BootConfig"), BootConfigDefinition),
            Constraints=deserialize_list(json_data.get("Constraints"), ConstraintsDefinition),
            Disks=deserialize_list(json_data.get("Disks"), DisksDefinition),
            ImageDiskConstraints=deserialize_list(json_data.get("ImageDiskConstraints"), ImageDiskConstraintsDefinition),
            Nics=deserialize_list(json_data.get("Nics"), NicsDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class DisksListDefinition(BaseModel):
    BlockDeviceId: Optional[str]
    Description: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DisksListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisksListDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockDeviceId=json_data.get("BlockDeviceId"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisksListDefinition = DisksListDefinition


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
class BootConfigDefinition(BaseModel):
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootConfigDefinition = BootConfigDefinition


@dataclass
class ConstraintsDefinition(BaseModel):
    Expression: Optional[str]
    Mandatory: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Mandatory=json_data.get("Mandatory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintsDefinition = ConstraintsDefinition


@dataclass
class DisksDefinition(BaseModel):
    BlockDeviceId: Optional[str]
    Description: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DisksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisksDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockDeviceId=json_data.get("BlockDeviceId"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisksDefinition = DisksDefinition


@dataclass
class ImageDiskConstraintsDefinition(BaseModel):
    Expression: Optional[str]
    Mandatory: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ImageDiskConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageDiskConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Mandatory=json_data.get("Mandatory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageDiskConstraintsDefinition = ImageDiskConstraintsDefinition


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
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


