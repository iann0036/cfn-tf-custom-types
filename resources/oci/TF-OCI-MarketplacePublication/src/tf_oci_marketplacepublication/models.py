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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Icon: Optional[Sequence["_IconDefinition"]]
    Id: Optional[str]
    IsAgreementAcknowledged: Optional[bool]
    ListingType: Optional[str]
    LongDescription: Optional[str]
    Name: Optional[str]
    PackageType: Optional[str]
    ShortDescription: Optional[str]
    State: Optional[str]
    SupportedOperatingSystems: Optional[Sequence["_SupportedOperatingSystemsDefinition"]]
    TimeCreated: Optional[str]
    PackageDetails: Optional[Sequence["_PackageDetailsDefinition"]]
    SupportContacts: Optional[Sequence["_SupportContactsDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Icon=deserialize_list(json_data.get("Icon"), IconDefinition),
            Id=json_data.get("Id"),
            IsAgreementAcknowledged=json_data.get("IsAgreementAcknowledged"),
            ListingType=json_data.get("ListingType"),
            LongDescription=json_data.get("LongDescription"),
            Name=json_data.get("Name"),
            PackageType=json_data.get("PackageType"),
            ShortDescription=json_data.get("ShortDescription"),
            State=json_data.get("State"),
            SupportedOperatingSystems=deserialize_list(json_data.get("SupportedOperatingSystems"), SupportedOperatingSystemsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            PackageDetails=deserialize_list(json_data.get("PackageDetails"), PackageDetailsDefinition),
            SupportContacts=deserialize_list(json_data.get("SupportContacts"), SupportContactsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class IconDefinition(BaseModel):
    ContentUrl: Optional[str]
    FileExtension: Optional[str]
    MimeType: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IconDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IconDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentUrl=json_data.get("ContentUrl"),
            FileExtension=json_data.get("FileExtension"),
            MimeType=json_data.get("MimeType"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IconDefinition = IconDefinition


@dataclass
class SupportedOperatingSystemsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SupportedOperatingSystemsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportedOperatingSystemsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportedOperatingSystemsDefinition = SupportedOperatingSystemsDefinition


@dataclass
class PackageDetailsDefinition(BaseModel):
    ImageId: Optional[str]
    PackageType: Optional[str]
    PackageVersion: Optional[str]
    Eula: Optional[Sequence["_EulaDefinition"]]
    OperatingSystem: Optional[Sequence["_OperatingSystemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PackageDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PackageDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageId=json_data.get("ImageId"),
            PackageType=json_data.get("PackageType"),
            PackageVersion=json_data.get("PackageVersion"),
            Eula=deserialize_list(json_data.get("Eula"), EulaDefinition),
            OperatingSystem=deserialize_list(json_data.get("OperatingSystem"), OperatingSystemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PackageDetailsDefinition = PackageDetailsDefinition


@dataclass
class EulaDefinition(BaseModel):
    EulaType: Optional[str]
    LicenseText: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EulaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EulaDefinition"]:
        if not json_data:
            return None
        return cls(
            EulaType=json_data.get("EulaType"),
            LicenseText=json_data.get("LicenseText"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EulaDefinition = EulaDefinition


@dataclass
class OperatingSystemDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OperatingSystemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OperatingSystemDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OperatingSystemDefinition = OperatingSystemDefinition


@dataclass
class SupportContactsDefinition(BaseModel):
    Email: Optional[str]
    Name: Optional[str]
    Phone: Optional[str]
    Subject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SupportContactsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportContactsDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Name=json_data.get("Name"),
            Phone=json_data.get("Phone"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportContactsDefinition = SupportContactsDefinition


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


