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
    CreateTime: Optional[str]
    Etag: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    ServiceAccount: Optional[str]
    UpdateTime: Optional[str]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    MatchingCriteria: Optional[Sequence["_MatchingCriteriaDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Transport: Optional[Sequence["_TransportDefinition"]]

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
            CreateTime=json_data.get("CreateTime"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            ServiceAccount=json_data.get("ServiceAccount"),
            UpdateTime=json_data.get("UpdateTime"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            MatchingCriteria=deserialize_list(json_data.get("MatchingCriteria"), MatchingCriteriaDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Transport=deserialize_list(json_data.get("Transport"), TransportDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class DestinationDefinition(BaseModel):
    CloudRunService: Optional[Sequence["_CloudRunServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudRunService=deserialize_list(json_data.get("CloudRunService"), CloudRunServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class CloudRunServiceDefinition(BaseModel):
    Path: Optional[str]
    Region: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudRunServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudRunServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Region=json_data.get("Region"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudRunServiceDefinition = CloudRunServiceDefinition


@dataclass
class MatchingCriteriaDefinition(BaseModel):
    Attribute: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchingCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchingCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchingCriteriaDefinition = MatchingCriteriaDefinition


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


@dataclass
class TransportDefinition(BaseModel):
    Pubsub: Optional[Sequence["_PubsubDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TransportDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransportDefinition"]:
        if not json_data:
            return None
        return cls(
            Pubsub=deserialize_list(json_data.get("Pubsub"), PubsubDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransportDefinition = TransportDefinition


@dataclass
class PubsubDefinition(BaseModel):
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PubsubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PubsubDefinition"]:
        if not json_data:
            return None
        return cls(
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PubsubDefinition = PubsubDefinition


