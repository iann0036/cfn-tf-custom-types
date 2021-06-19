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
    ArtifactGcsUri: Optional[str]
    EndpointUri: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Location: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    Port: Optional[float]
    Project: Optional[str]
    ServiceId: Optional[str]
    State: Optional[str]
    StateMessage: Optional[str]
    Tier: Optional[str]
    HiveMetastoreConfig: Optional[Sequence["_HiveMetastoreConfigDefinition"]]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition"]]
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
            ArtifactGcsUri=json_data.get("ArtifactGcsUri"),
            EndpointUri=json_data.get("EndpointUri"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            Port=json_data.get("Port"),
            Project=json_data.get("Project"),
            ServiceId=json_data.get("ServiceId"),
            State=json_data.get("State"),
            StateMessage=json_data.get("StateMessage"),
            Tier=json_data.get("Tier"),
            HiveMetastoreConfig=deserialize_list(json_data.get("HiveMetastoreConfig"), HiveMetastoreConfigDefinition),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class HiveMetastoreConfigDefinition(BaseModel):
    ConfigOverrides: Optional[Sequence["_ConfigOverridesDefinition"]]
    Version: Optional[str]
    KerberosConfig: Optional[Sequence["_KerberosConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HiveMetastoreConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HiveMetastoreConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigOverrides=deserialize_list(json_data.get("ConfigOverrides"), ConfigOverridesDefinition),
            Version=json_data.get("Version"),
            KerberosConfig=deserialize_list(json_data.get("KerberosConfig"), KerberosConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HiveMetastoreConfigDefinition = HiveMetastoreConfigDefinition


@dataclass
class ConfigOverridesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigOverridesDefinition = ConfigOverridesDefinition


@dataclass
class KerberosConfigDefinition(BaseModel):
    Krb5ConfigGcsUri: Optional[str]
    Principal: Optional[str]
    Keytab: Optional[Sequence["_KeytabDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KerberosConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KerberosConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Krb5ConfigGcsUri=json_data.get("Krb5ConfigGcsUri"),
            Principal=json_data.get("Principal"),
            Keytab=deserialize_list(json_data.get("Keytab"), KeytabDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_KerberosConfigDefinition = KerberosConfigDefinition


@dataclass
class KeytabDefinition(BaseModel):
    CloudSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeytabDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeytabDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudSecret=json_data.get("CloudSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeytabDefinition = KeytabDefinition


@dataclass
class MaintenanceWindowDefinition(BaseModel):
    DayOfWeek: Optional[str]
    HourOfDay: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            HourOfDay=json_data.get("HourOfDay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition = MaintenanceWindowDefinition


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


