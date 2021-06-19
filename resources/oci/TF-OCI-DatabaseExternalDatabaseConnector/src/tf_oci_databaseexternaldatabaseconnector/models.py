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
    ConnectionStatus: Optional[str]
    ConnectorAgentId: Optional[str]
    ConnectorType: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    ExternalDatabaseId: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    State: Optional[str]
    TimeConnectionStatusLastUpdated: Optional[str]
    TimeCreated: Optional[str]
    ConnectionCredentials: Optional[Sequence["_ConnectionCredentialsDefinition"]]
    ConnectionString: Optional[Sequence["_ConnectionStringDefinition"]]
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
            ConnectionStatus=json_data.get("ConnectionStatus"),
            ConnectorAgentId=json_data.get("ConnectorAgentId"),
            ConnectorType=json_data.get("ConnectorType"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            ExternalDatabaseId=json_data.get("ExternalDatabaseId"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            State=json_data.get("State"),
            TimeConnectionStatusLastUpdated=json_data.get("TimeConnectionStatusLastUpdated"),
            TimeCreated=json_data.get("TimeCreated"),
            ConnectionCredentials=deserialize_list(json_data.get("ConnectionCredentials"), ConnectionCredentialsDefinition),
            ConnectionString=deserialize_list(json_data.get("ConnectionString"), ConnectionStringDefinition),
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
class ConnectionCredentialsDefinition(BaseModel):
    CredentialName: Optional[str]
    CredentialType: Optional[str]
    Password: Optional[str]
    Role: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            CredentialName=json_data.get("CredentialName"),
            CredentialType=json_data.get("CredentialType"),
            Password=json_data.get("Password"),
            Role=json_data.get("Role"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionCredentialsDefinition = ConnectionCredentialsDefinition


@dataclass
class ConnectionStringDefinition(BaseModel):
    Hostname: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringDefinition = ConnectionStringDefinition


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


