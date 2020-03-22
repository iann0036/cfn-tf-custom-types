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
    AutoRenew: Optional[bool]
    AutoRenewPeriod: Optional[float]
    AutoUpgradeMinorVersion: Optional[str]
    ConnectionString: Optional[str]
    DbInstanceStorageType: Optional[str]
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
    SecurityGroupId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SecurityIpMode: Optional[str]
    SecurityIps: Optional[Sequence[str]]
    SqlCollectorConfigValue: Optional[float]
    SqlCollectorStatus: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    Parameters: Optional[Sequence["_Parameters"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoRenew=json_data.get("AutoRenew"),
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            AutoUpgradeMinorVersion=json_data.get("AutoUpgradeMinorVersion"),
            ConnectionString=json_data.get("ConnectionString"),
            DbInstanceStorageType=json_data.get("DbInstanceStorageType"),
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
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SecurityIpMode=json_data.get("SecurityIpMode"),
            SecurityIps=json_data.get("SecurityIps"),
            SqlCollectorConfigValue=json_data.get("SqlCollectorConfigValue"),
            SqlCollectorStatus=json_data.get("SqlCollectorStatus"),
            Tags=json_data.get("Tags"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Parameters=json_data.get("Parameters"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Parameters:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


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


