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
    Acl: Optional[str]
    AutoRenew: Optional[bool]
    AutoRenewPeriod: Optional[float]
    AutoUpgradeMinorVersion: Optional[str]
    CaType: Optional[str]
    ClientCaCert: Optional[str]
    ClientCaEnabled: Optional[float]
    ClientCertRevocationList: Optional[str]
    ClientCrlEnabled: Optional[float]
    ConnectionString: Optional[str]
    DbInstanceStorageType: Optional[str]
    EncryptionKey: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    ForceRestart: Optional[bool]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    InstanceName: Optional[str]
    InstanceStorage: Optional[float]
    InstanceType: Optional[str]
    MaintainTime: Optional[str]
    MonitoringPeriod: Optional[float]
    Period: Optional[float]
    Port: Optional[str]
    ReplicationAcl: Optional[str]
    ResourceGroupId: Optional[str]
    SecurityGroupId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SecurityIpMode: Optional[str]
    SecurityIps: Optional[Sequence[str]]
    ServerCert: Optional[str]
    ServerKey: Optional[str]
    SqlCollectorConfigValue: Optional[float]
    SqlCollectorStatus: Optional[str]
    SslAction: Optional[str]
    SslStatus: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TdeStatus: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    ZoneIdSlaveA: Optional[str]
    ZoneIdSlaveB: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
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
            Acl=json_data.get("Acl"),
            AutoRenew=json_data.get("AutoRenew"),
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            AutoUpgradeMinorVersion=json_data.get("AutoUpgradeMinorVersion"),
            CaType=json_data.get("CaType"),
            ClientCaCert=json_data.get("ClientCaCert"),
            ClientCaEnabled=json_data.get("ClientCaEnabled"),
            ClientCertRevocationList=json_data.get("ClientCertRevocationList"),
            ClientCrlEnabled=json_data.get("ClientCrlEnabled"),
            ConnectionString=json_data.get("ConnectionString"),
            DbInstanceStorageType=json_data.get("DbInstanceStorageType"),
            EncryptionKey=json_data.get("EncryptionKey"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            ForceRestart=json_data.get("ForceRestart"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceName=json_data.get("InstanceName"),
            InstanceStorage=json_data.get("InstanceStorage"),
            InstanceType=json_data.get("InstanceType"),
            MaintainTime=json_data.get("MaintainTime"),
            MonitoringPeriod=json_data.get("MonitoringPeriod"),
            Period=json_data.get("Period"),
            Port=json_data.get("Port"),
            ReplicationAcl=json_data.get("ReplicationAcl"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SecurityIpMode=json_data.get("SecurityIpMode"),
            SecurityIps=json_data.get("SecurityIps"),
            ServerCert=json_data.get("ServerCert"),
            ServerKey=json_data.get("ServerKey"),
            SqlCollectorConfigValue=json_data.get("SqlCollectorConfigValue"),
            SqlCollectorStatus=json_data.get("SqlCollectorStatus"),
            SslAction=json_data.get("SslAction"),
            SslStatus=json_data.get("SslStatus"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TdeStatus=json_data.get("TdeStatus"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            ZoneIdSlaveA=json_data.get("ZoneIdSlaveA"),
            ZoneIdSlaveB=json_data.get("ZoneIdSlaveB"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


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


