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
    Description: Optional[str]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    State: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    ConnectionOption: Optional[Sequence["_ConnectionOptionDefinition"]]
    Credentials: Optional[Sequence["_CredentialsDefinition"]]
    DatabaseDetails: Optional[Sequence["_DatabaseDetailsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    TlsConfig: Optional[Sequence["_TlsConfigDefinition"]]

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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            State=json_data.get("State"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            ConnectionOption=deserialize_list(json_data.get("ConnectionOption"), ConnectionOptionDefinition),
            Credentials=deserialize_list(json_data.get("Credentials"), CredentialsDefinition),
            DatabaseDetails=deserialize_list(json_data.get("DatabaseDetails"), DatabaseDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TlsConfig=deserialize_list(json_data.get("TlsConfig"), TlsConfigDefinition),
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
class SystemTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTagsDefinition = SystemTagsDefinition


@dataclass
class ConnectionOptionDefinition(BaseModel):
    ConnectionType: Optional[str]
    DatasafePrivateEndpointId: Optional[str]
    OnPremConnectorId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionType=json_data.get("ConnectionType"),
            DatasafePrivateEndpointId=json_data.get("DatasafePrivateEndpointId"),
            OnPremConnectorId=json_data.get("OnPremConnectorId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionOptionDefinition = ConnectionOptionDefinition


@dataclass
class CredentialsDefinition(BaseModel):
    Password: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialsDefinition = CredentialsDefinition


@dataclass
class DatabaseDetailsDefinition(BaseModel):
    AutonomousDatabaseId: Optional[str]
    DatabaseType: Optional[str]
    DbSystemId: Optional[str]
    InfrastructureType: Optional[str]
    InstanceId: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    ListenerPort: Optional[float]
    ServiceName: Optional[str]
    VmClusterId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AutonomousDatabaseId=json_data.get("AutonomousDatabaseId"),
            DatabaseType=json_data.get("DatabaseType"),
            DbSystemId=json_data.get("DbSystemId"),
            InfrastructureType=json_data.get("InfrastructureType"),
            InstanceId=json_data.get("InstanceId"),
            IpAddresses=json_data.get("IpAddresses"),
            ListenerPort=json_data.get("ListenerPort"),
            ServiceName=json_data.get("ServiceName"),
            VmClusterId=json_data.get("VmClusterId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDetailsDefinition = DatabaseDetailsDefinition


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
class TlsConfigDefinition(BaseModel):
    CertificateStoreType: Optional[str]
    KeyStoreContent: Optional[str]
    Status: Optional[str]
    StorePassword: Optional[str]
    TrustStoreContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateStoreType=json_data.get("CertificateStoreType"),
            KeyStoreContent=json_data.get("KeyStoreContent"),
            Status=json_data.get("Status"),
            StorePassword=json_data.get("StorePassword"),
            TrustStoreContent=json_data.get("TrustStoreContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsConfigDefinition = TlsConfigDefinition


