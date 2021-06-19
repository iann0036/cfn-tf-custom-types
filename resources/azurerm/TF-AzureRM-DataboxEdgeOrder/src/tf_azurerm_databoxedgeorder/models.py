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
    DeviceName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ReturnTracking: Optional[Sequence["_ReturnTrackingDefinition"]]
    SerialNumber: Optional[str]
    ShipmentHistory: Optional[Sequence["_ShipmentHistoryDefinition2"]]
    ShipmentTracking: Optional[Sequence["_ShipmentTrackingDefinition"]]
    Status: Optional[Sequence["_StatusDefinition2"]]
    Contact: Optional[Sequence["_ContactDefinition"]]
    ShipmentAddress: Optional[Sequence["_ShipmentAddressDefinition"]]
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
            DeviceName=json_data.get("DeviceName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ReturnTracking=deserialize_list(json_data.get("ReturnTracking"), ReturnTrackingDefinition),
            SerialNumber=json_data.get("SerialNumber"),
            ShipmentHistory=deserialize_list(json_data.get("ShipmentHistory"), ShipmentHistoryDefinition2),
            ShipmentTracking=deserialize_list(json_data.get("ShipmentTracking"), ShipmentTrackingDefinition),
            Status=deserialize_list(json_data.get("Status"), StatusDefinition2),
            Contact=deserialize_list(json_data.get("Contact"), ContactDefinition),
            ShipmentAddress=deserialize_list(json_data.get("ShipmentAddress"), ShipmentAddressDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ReturnTrackingDefinition(BaseModel):
    CarrierName: Optional[str]
    SerialNumber: Optional[str]
    TrackingId: Optional[str]
    TrackingUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReturnTrackingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReturnTrackingDefinition"]:
        if not json_data:
            return None
        return cls(
            CarrierName=json_data.get("CarrierName"),
            SerialNumber=json_data.get("SerialNumber"),
            TrackingId=json_data.get("TrackingId"),
            TrackingUrl=json_data.get("TrackingUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReturnTrackingDefinition = ReturnTrackingDefinition


@dataclass
class ShipmentHistoryDefinition2(BaseModel):
    AdditionalDetails: Optional[Sequence["_ShipmentHistoryDefinition"]]
    Comments: Optional[str]
    LastUpdate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ShipmentHistoryDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShipmentHistoryDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalDetails=deserialize_list(json_data.get("AdditionalDetails"), ShipmentHistoryDefinition),
            Comments=json_data.get("Comments"),
            LastUpdate=json_data.get("LastUpdate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShipmentHistoryDefinition2 = ShipmentHistoryDefinition2


@dataclass
class ShipmentHistoryDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ShipmentHistoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShipmentHistoryDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShipmentHistoryDefinition = ShipmentHistoryDefinition


@dataclass
class ShipmentTrackingDefinition(BaseModel):
    CarrierName: Optional[str]
    SerialNumber: Optional[str]
    TrackingId: Optional[str]
    TrackingUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ShipmentTrackingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShipmentTrackingDefinition"]:
        if not json_data:
            return None
        return cls(
            CarrierName=json_data.get("CarrierName"),
            SerialNumber=json_data.get("SerialNumber"),
            TrackingId=json_data.get("TrackingId"),
            TrackingUrl=json_data.get("TrackingUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShipmentTrackingDefinition = ShipmentTrackingDefinition


@dataclass
class StatusDefinition2(BaseModel):
    AdditionalDetails: Optional[Sequence["_StatusDefinition"]]
    Comments: Optional[str]
    Info: Optional[str]
    LastUpdate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalDetails=deserialize_list(json_data.get("AdditionalDetails"), StatusDefinition),
            Comments=json_data.get("Comments"),
            Info=json_data.get("Info"),
            LastUpdate=json_data.get("LastUpdate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition2 = StatusDefinition2


@dataclass
class StatusDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition = StatusDefinition


@dataclass
class ContactDefinition(BaseModel):
    CompanyName: Optional[str]
    Emails: Optional[Sequence[str]]
    Name: Optional[str]
    PhoneNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContactDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContactDefinition"]:
        if not json_data:
            return None
        return cls(
            CompanyName=json_data.get("CompanyName"),
            Emails=json_data.get("Emails"),
            Name=json_data.get("Name"),
            PhoneNumber=json_data.get("PhoneNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContactDefinition = ContactDefinition


@dataclass
class ShipmentAddressDefinition(BaseModel):
    Address: Optional[Sequence[str]]
    City: Optional[str]
    Country: Optional[str]
    PostalCode: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ShipmentAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShipmentAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            City=json_data.get("City"),
            Country=json_data.get("Country"),
            PostalCode=json_data.get("PostalCode"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShipmentAddressDefinition = ShipmentAddressDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


