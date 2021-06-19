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
    CloudName: Optional[str]
    Components: Optional[Sequence["_ComponentsDefinition"]]
    Id: Optional[str]
    MaintenanceWindowDow: Optional[str]
    MaintenanceWindowTime: Optional[str]
    Plan: Optional[str]
    Project: Optional[str]
    ProjectVpcId: Optional[str]
    ServiceHost: Optional[str]
    ServiceName: Optional[str]
    ServicePassword: Optional[str]
    ServicePort: Optional[float]
    ServiceType: Optional[str]
    ServiceUri: Optional[str]
    ServiceUsername: Optional[str]
    State: Optional[str]
    TerminationProtection: Optional[bool]
    Influxdb: Optional[Sequence["_InfluxdbDefinition"]]
    InfluxdbUserConfig: Optional[Sequence["_InfluxdbUserConfigDefinition"]]
    ServiceIntegrations: Optional[Sequence["_ServiceIntegrationsDefinition"]]
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
            CloudName=json_data.get("CloudName"),
            Components=deserialize_list(json_data.get("Components"), ComponentsDefinition),
            Id=json_data.get("Id"),
            MaintenanceWindowDow=json_data.get("MaintenanceWindowDow"),
            MaintenanceWindowTime=json_data.get("MaintenanceWindowTime"),
            Plan=json_data.get("Plan"),
            Project=json_data.get("Project"),
            ProjectVpcId=json_data.get("ProjectVpcId"),
            ServiceHost=json_data.get("ServiceHost"),
            ServiceName=json_data.get("ServiceName"),
            ServicePassword=json_data.get("ServicePassword"),
            ServicePort=json_data.get("ServicePort"),
            ServiceType=json_data.get("ServiceType"),
            ServiceUri=json_data.get("ServiceUri"),
            ServiceUsername=json_data.get("ServiceUsername"),
            State=json_data.get("State"),
            TerminationProtection=json_data.get("TerminationProtection"),
            Influxdb=deserialize_list(json_data.get("Influxdb"), InfluxdbDefinition),
            InfluxdbUserConfig=deserialize_list(json_data.get("InfluxdbUserConfig"), InfluxdbUserConfigDefinition),
            ServiceIntegrations=deserialize_list(json_data.get("ServiceIntegrations"), ServiceIntegrationsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ComponentsDefinition(BaseModel):
    Component: Optional[str]
    Host: Optional[str]
    KafkaAuthenticationMethod: Optional[str]
    Port: Optional[float]
    Route: Optional[str]
    Ssl: Optional[bool]
    Usage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentsDefinition"]:
        if not json_data:
            return None
        return cls(
            Component=json_data.get("Component"),
            Host=json_data.get("Host"),
            KafkaAuthenticationMethod=json_data.get("KafkaAuthenticationMethod"),
            Port=json_data.get("Port"),
            Route=json_data.get("Route"),
            Ssl=json_data.get("Ssl"),
            Usage=json_data.get("Usage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentsDefinition = ComponentsDefinition


@dataclass
class InfluxdbDefinition(BaseModel):
    LogQueriesAfter: Optional[str]
    MaxRowLimit: Optional[str]
    MaxSelectBuckets: Optional[str]
    MaxSelectPoint: Optional[str]
    QueryTimeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InfluxdbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfluxdbDefinition"]:
        if not json_data:
            return None
        return cls(
            LogQueriesAfter=json_data.get("LogQueriesAfter"),
            MaxRowLimit=json_data.get("MaxRowLimit"),
            MaxSelectBuckets=json_data.get("MaxSelectBuckets"),
            MaxSelectPoint=json_data.get("MaxSelectPoint"),
            QueryTimeout=json_data.get("QueryTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfluxdbDefinition = InfluxdbDefinition


@dataclass
class InfluxdbUserConfigDefinition(BaseModel):
    CustomDomain: Optional[str]
    IpFilter: Optional[Sequence[str]]
    ProjectToForkFrom: Optional[str]
    RecoveryBasebackupName: Optional[str]
    ServiceToForkFrom: Optional[str]
    Influxdb: Optional[Sequence["_InfluxdbDefinition"]]
    PrivateAccess: Optional[Sequence["_PrivateAccessDefinition"]]
    PrivatelinkAccess: Optional[Sequence["_PrivatelinkAccessDefinition"]]
    PublicAccess: Optional[Sequence["_PublicAccessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InfluxdbUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfluxdbUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomDomain=json_data.get("CustomDomain"),
            IpFilter=json_data.get("IpFilter"),
            ProjectToForkFrom=json_data.get("ProjectToForkFrom"),
            RecoveryBasebackupName=json_data.get("RecoveryBasebackupName"),
            ServiceToForkFrom=json_data.get("ServiceToForkFrom"),
            Influxdb=deserialize_list(json_data.get("Influxdb"), InfluxdbDefinition),
            PrivateAccess=deserialize_list(json_data.get("PrivateAccess"), PrivateAccessDefinition),
            PrivatelinkAccess=deserialize_list(json_data.get("PrivatelinkAccess"), PrivatelinkAccessDefinition),
            PublicAccess=deserialize_list(json_data.get("PublicAccess"), PublicAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfluxdbUserConfigDefinition = InfluxdbUserConfigDefinition


@dataclass
class PrivateAccessDefinition(BaseModel):
    Influxdb: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Influxdb=json_data.get("Influxdb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateAccessDefinition = PrivateAccessDefinition


@dataclass
class PrivatelinkAccessDefinition(BaseModel):
    Influxdb: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivatelinkAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivatelinkAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Influxdb=json_data.get("Influxdb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivatelinkAccessDefinition = PrivatelinkAccessDefinition


@dataclass
class PublicAccessDefinition(BaseModel):
    Influxdb: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Influxdb=json_data.get("Influxdb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccessDefinition = PublicAccessDefinition


@dataclass
class ServiceIntegrationsDefinition(BaseModel):
    IntegrationType: Optional[str]
    SourceServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIntegrationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIntegrationsDefinition"]:
        if not json_data:
            return None
        return cls(
            IntegrationType=json_data.get("IntegrationType"),
            SourceServiceName=json_data.get("SourceServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIntegrationsDefinition = ServiceIntegrationsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


