# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AdminPassword: Optional[str]
    CompartmentId: Optional[str]
    ConnectionStrings: Optional[Sequence["_ConnectionStrings"]]
    CpuCoreCount: Optional[float]
    DataStorageSizeInTbs: Optional[float]
    DbName: Optional[str]
    DbVersion: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    LicenseModel: Optional[str]
    LifecycleDetails: Optional[str]
    ServiceConsoleUrl: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminPassword=json_data.get("AdminPassword"),
            CompartmentId=json_data.get("CompartmentId"),
            ConnectionStrings=json_data.get("ConnectionStrings"),
            CpuCoreCount=json_data.get("CpuCoreCount"),
            DataStorageSizeInTbs=json_data.get("DataStorageSizeInTbs"),
            DbName=json_data.get("DbName"),
            DbVersion=json_data.get("DbVersion"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            LicenseModel=json_data.get("LicenseModel"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            ServiceConsoleUrl=json_data.get("ServiceConsoleUrl"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionStrings:
    AllConnectionStrings: Optional[Sequence["_AllConnectionStrings"]]
    High: Optional[str]
    Low: Optional[str]
    Medium: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStrings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStrings"]:
        if not json_data:
            return None
        return cls(
            AllConnectionStrings=json_data.get("AllConnectionStrings"),
            High=json_data.get("High"),
            Low=json_data.get("Low"),
            Medium=json_data.get("Medium"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStrings = ConnectionStrings


@dataclass
class AllConnectionStrings:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllConnectionStrings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllConnectionStrings"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllConnectionStrings = AllConnectionStrings


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


