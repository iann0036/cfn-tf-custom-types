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
    AvailabilityDomain: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    Domain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Hostname: Optional[str]
    Id: Optional[str]
    LastMaintenanceRunId: Optional[str]
    LicenseModel: Optional[str]
    LifecycleDetails: Optional[str]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindow"]]
    NextMaintenanceRunId: Optional[str]
    NsgIds: Optional[Sequence[str]]
    Shape: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]
    MaintenanceWindowDetails: Optional[Sequence["_MaintenanceWindowDetails"]]
    Timeouts: Optional["_Timeouts"]
    DaysOfWeek: Optional[Sequence["_DaysOfWeek2"]]
    Months: Optional[Sequence["_Months2"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            Domain=json_data.get("Domain"),
            FreeformTags=json_data.get("FreeformTags"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            LastMaintenanceRunId=json_data.get("LastMaintenanceRunId"),
            LicenseModel=json_data.get("LicenseModel"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
            NextMaintenanceRunId=json_data.get("NextMaintenanceRunId"),
            NsgIds=json_data.get("NsgIds"),
            Shape=json_data.get("Shape"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
            MaintenanceWindowDetails=json_data.get("MaintenanceWindowDetails"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            DaysOfWeek=json_data.get("DaysOfWeek"),
            Months=json_data.get("Months"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class MaintenanceWindow:
    DaysOfWeek: Optional[Sequence["_DaysOfWeek"]]
    HoursOfDay: Optional[Sequence[float]]
    Months: Optional[Sequence["_Months"]]
    Preference: Optional[str]
    WeeksOfMonth: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindow"]:
        if not json_data:
            return None
        return cls(
            DaysOfWeek=json_data.get("DaysOfWeek"),
            HoursOfDay=json_data.get("HoursOfDay"),
            Months=json_data.get("Months"),
            Preference=json_data.get("Preference"),
            WeeksOfMonth=json_data.get("WeeksOfMonth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindow = MaintenanceWindow


@dataclass
class DaysOfWeek:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DaysOfWeek"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DaysOfWeek"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DaysOfWeek = DaysOfWeek


@dataclass
class Months:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Months"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Months"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Months = Months


@dataclass
class MaintenanceWindowDetails:
    HoursOfDay: Optional[Sequence[float]]
    Preference: Optional[str]
    WeeksOfMonth: Optional[Sequence[float]]
    DaysOfWeek: Optional[Sequence["_DaysOfWeek2"]]
    Months: Optional[Sequence["_Months2"]]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDetails"]:
        if not json_data:
            return None
        return cls(
            HoursOfDay=json_data.get("HoursOfDay"),
            Preference=json_data.get("Preference"),
            WeeksOfMonth=json_data.get("WeeksOfMonth"),
            DaysOfWeek=json_data.get("DaysOfWeek"),
            Months=json_data.get("Months"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDetails = MaintenanceWindowDetails


@dataclass
class DaysOfWeek2:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DaysOfWeek2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DaysOfWeek2"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DaysOfWeek2 = DaysOfWeek2


@dataclass
class Months2:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Months2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Months2"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Months2 = Months2


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


