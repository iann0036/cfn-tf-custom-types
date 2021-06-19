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
    Mysql: Optional[Sequence["_MysqlDefinition"]]
    MysqlUserConfig: Optional[Sequence["_MysqlUserConfigDefinition"]]
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
            Mysql=deserialize_list(json_data.get("Mysql"), MysqlDefinition),
            MysqlUserConfig=deserialize_list(json_data.get("MysqlUserConfig"), MysqlUserConfigDefinition),
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
class MysqlDefinition(BaseModel):
    ConnectTimeout: Optional[str]
    DefaultTimeZone: Optional[str]
    GroupConcatMaxLen: Optional[str]
    InformationSchemaStatsExpiry: Optional[str]
    InnodbFtMinTokenSize: Optional[str]
    InnodbFtServerStopwordTable: Optional[str]
    InnodbLockWaitTimeout: Optional[str]
    InnodbLogBufferSize: Optional[str]
    InnodbOnlineAlterLogMaxSize: Optional[str]
    InnodbPrintAllDeadlocks: Optional[str]
    InnodbRollbackOnTimeout: Optional[str]
    InteractiveTimeout: Optional[str]
    LongQueryTime: Optional[str]
    MaxAllowedPacket: Optional[str]
    MaxHeapTableSize: Optional[str]
    NetReadTimeout: Optional[str]
    NetWriteTimeout: Optional[str]
    SlowQueryLog: Optional[str]
    SortBufferSize: Optional[str]
    SqlMode: Optional[str]
    SqlRequirePrimaryKey: Optional[str]
    TmpTableSize: Optional[str]
    WaitTimeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectTimeout=json_data.get("ConnectTimeout"),
            DefaultTimeZone=json_data.get("DefaultTimeZone"),
            GroupConcatMaxLen=json_data.get("GroupConcatMaxLen"),
            InformationSchemaStatsExpiry=json_data.get("InformationSchemaStatsExpiry"),
            InnodbFtMinTokenSize=json_data.get("InnodbFtMinTokenSize"),
            InnodbFtServerStopwordTable=json_data.get("InnodbFtServerStopwordTable"),
            InnodbLockWaitTimeout=json_data.get("InnodbLockWaitTimeout"),
            InnodbLogBufferSize=json_data.get("InnodbLogBufferSize"),
            InnodbOnlineAlterLogMaxSize=json_data.get("InnodbOnlineAlterLogMaxSize"),
            InnodbPrintAllDeadlocks=json_data.get("InnodbPrintAllDeadlocks"),
            InnodbRollbackOnTimeout=json_data.get("InnodbRollbackOnTimeout"),
            InteractiveTimeout=json_data.get("InteractiveTimeout"),
            LongQueryTime=json_data.get("LongQueryTime"),
            MaxAllowedPacket=json_data.get("MaxAllowedPacket"),
            MaxHeapTableSize=json_data.get("MaxHeapTableSize"),
            NetReadTimeout=json_data.get("NetReadTimeout"),
            NetWriteTimeout=json_data.get("NetWriteTimeout"),
            SlowQueryLog=json_data.get("SlowQueryLog"),
            SortBufferSize=json_data.get("SortBufferSize"),
            SqlMode=json_data.get("SqlMode"),
            SqlRequirePrimaryKey=json_data.get("SqlRequirePrimaryKey"),
            TmpTableSize=json_data.get("TmpTableSize"),
            WaitTimeout=json_data.get("WaitTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlDefinition = MysqlDefinition


@dataclass
class MysqlUserConfigDefinition(BaseModel):
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    BackupHour: Optional[str]
    BackupMinute: Optional[str]
    BinlogRetentionPeriod: Optional[str]
    IpFilter: Optional[Sequence[str]]
    MysqlVersion: Optional[str]
    ProjectToForkFrom: Optional[str]
    RecoveryTargetTime: Optional[str]
    ServiceToForkFrom: Optional[str]
    Migration: Optional[Sequence["_MigrationDefinition"]]
    Mysql: Optional[Sequence["_MysqlDefinition"]]
    PrivateAccess: Optional[Sequence["_PrivateAccessDefinition"]]
    PrivatelinkAccess: Optional[Sequence["_PrivatelinkAccessDefinition"]]
    PublicAccess: Optional[Sequence["_PublicAccessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            BackupHour=json_data.get("BackupHour"),
            BackupMinute=json_data.get("BackupMinute"),
            BinlogRetentionPeriod=json_data.get("BinlogRetentionPeriod"),
            IpFilter=json_data.get("IpFilter"),
            MysqlVersion=json_data.get("MysqlVersion"),
            ProjectToForkFrom=json_data.get("ProjectToForkFrom"),
            RecoveryTargetTime=json_data.get("RecoveryTargetTime"),
            ServiceToForkFrom=json_data.get("ServiceToForkFrom"),
            Migration=deserialize_list(json_data.get("Migration"), MigrationDefinition),
            Mysql=deserialize_list(json_data.get("Mysql"), MysqlDefinition),
            PrivateAccess=deserialize_list(json_data.get("PrivateAccess"), PrivateAccessDefinition),
            PrivatelinkAccess=deserialize_list(json_data.get("PrivatelinkAccess"), PrivatelinkAccessDefinition),
            PublicAccess=deserialize_list(json_data.get("PublicAccess"), PublicAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlUserConfigDefinition = MysqlUserConfigDefinition


@dataclass
class MigrationDefinition(BaseModel):
    Dbname: Optional[str]
    Host: Optional[str]
    IgnoreDbs: Optional[str]
    Password: Optional[str]
    Port: Optional[str]
    Ssl: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MigrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MigrationDefinition"]:
        if not json_data:
            return None
        return cls(
            Dbname=json_data.get("Dbname"),
            Host=json_data.get("Host"),
            IgnoreDbs=json_data.get("IgnoreDbs"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Ssl=json_data.get("Ssl"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MigrationDefinition = MigrationDefinition


@dataclass
class PrivateAccessDefinition(BaseModel):
    Mysql: Optional[str]
    Mysqlx: Optional[str]
    Prometheus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Mysql=json_data.get("Mysql"),
            Mysqlx=json_data.get("Mysqlx"),
            Prometheus=json_data.get("Prometheus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateAccessDefinition = PrivateAccessDefinition


@dataclass
class PrivatelinkAccessDefinition(BaseModel):
    Mysql: Optional[str]
    Mysqlx: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivatelinkAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivatelinkAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Mysql=json_data.get("Mysql"),
            Mysqlx=json_data.get("Mysqlx"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivatelinkAccessDefinition = PrivatelinkAccessDefinition


@dataclass
class PublicAccessDefinition(BaseModel):
    Mysql: Optional[str]
    Mysqlx: Optional[str]
    Prometheus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Mysql=json_data.get("Mysql"),
            Mysqlx=json_data.get("Mysqlx"),
            Prometheus=json_data.get("Prometheus"),
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


