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
    AttachedVcnId: Optional[str]
    CompartmentId: Optional[str]
    DefaultViewId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    Endpoints: Optional[Sequence["_EndpointsDefinition"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsProtected: Optional[bool]
    ResolverId: Optional[str]
    Scope: Optional[str]
    Self: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    AttachedViews: Optional[Sequence["_AttachedViewsDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]
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
            AttachedVcnId=json_data.get("AttachedVcnId"),
            CompartmentId=json_data.get("CompartmentId"),
            DefaultViewId=json_data.get("DefaultViewId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            Endpoints=deserialize_list(json_data.get("Endpoints"), EndpointsDefinition),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsProtected=json_data.get("IsProtected"),
            ResolverId=json_data.get("ResolverId"),
            Scope=json_data.get("Scope"),
            Self=json_data.get("Self"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            AttachedViews=deserialize_list(json_data.get("AttachedViews"), AttachedViewsDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
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
class EndpointsDefinition(BaseModel):
    CompartmentId: Optional[str]
    EndpointType: Optional[str]
    ForwardingAddress: Optional[str]
    IsForwarding: Optional[bool]
    IsListening: Optional[bool]
    ListeningAddress: Optional[str]
    Name: Optional[str]
    Self: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            CompartmentId=json_data.get("CompartmentId"),
            EndpointType=json_data.get("EndpointType"),
            ForwardingAddress=json_data.get("ForwardingAddress"),
            IsForwarding=json_data.get("IsForwarding"),
            IsListening=json_data.get("IsListening"),
            ListeningAddress=json_data.get("ListeningAddress"),
            Name=json_data.get("Name"),
            Self=json_data.get("Self"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointsDefinition = EndpointsDefinition


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
class AttachedViewsDefinition(BaseModel):
    ViewId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttachedViewsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachedViewsDefinition"]:
        if not json_data:
            return None
        return cls(
            ViewId=json_data.get("ViewId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachedViewsDefinition = AttachedViewsDefinition


@dataclass
class RulesDefinition(BaseModel):
    Action: Optional[str]
    ClientAddressConditions: Optional[Sequence[str]]
    DestinationAddresses: Optional[Sequence[str]]
    QnameCoverConditions: Optional[Sequence[str]]
    SourceEndpointName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ClientAddressConditions=json_data.get("ClientAddressConditions"),
            DestinationAddresses=json_data.get("DestinationAddresses"),
            QnameCoverConditions=json_data.get("QnameCoverConditions"),
            SourceEndpointName=json_data.get("SourceEndpointName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


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


