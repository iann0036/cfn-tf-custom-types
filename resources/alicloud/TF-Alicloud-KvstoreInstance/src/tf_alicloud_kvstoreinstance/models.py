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
    AutoRenew: Optional[bool]
    AutoRenewPeriod: Optional[float]
    AutoUseCoupon: Optional[bool]
    AvailabilityZone: Optional[str]
    BackupId: Optional[str]
    BackupPeriod: Optional[Sequence[str]]
    BackupTime: Optional[str]
    Bandwidth: Optional[float]
    BusinessInfo: Optional[str]
    Capacity: Optional[float]
    Config: Optional[Sequence["_ConfigDefinition"]]
    ConnectionDomain: Optional[str]
    ConnectionString: Optional[str]
    ConnectionStringPrefix: Optional[str]
    CouponNo: Optional[str]
    DbInstanceName: Optional[str]
    DedicatedHostGroupId: Optional[str]
    EnableBackupLog: Optional[float]
    EnablePublic: Optional[bool]
    EndTime: Optional[str]
    EngineVersion: Optional[str]
    ForceUpgrade: Optional[bool]
    GlobalInstance: Optional[bool]
    GlobalInstanceId: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    InstanceClass: Optional[str]
    InstanceName: Optional[str]
    InstanceReleaseProtection: Optional[bool]
    InstanceType: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContextDefinition"]]
    MaintainEndTime: Optional[str]
    MaintainStartTime: Optional[str]
    ModifyMode: Optional[float]
    NodeType: Optional[str]
    OrderType: Optional[str]
    Password: Optional[str]
    PaymentType: Optional[str]
    Period: Optional[str]
    Port: Optional[float]
    PrivateConnectionPort: Optional[str]
    PrivateConnectionPrefix: Optional[str]
    PrivateIp: Optional[str]
    Qps: Optional[float]
    ResourceGroupId: Optional[str]
    RestoreTime: Optional[str]
    SecurityGroupId: Optional[str]
    SecurityIpGroupAttribute: Optional[str]
    SecurityIpGroupName: Optional[str]
    SecurityIps: Optional[Sequence[str]]
    SrcdbInstanceId: Optional[str]
    SslEnable: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VpcAuthMode: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
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
            AutoRenew=json_data.get("AutoRenew"),
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            AutoUseCoupon=json_data.get("AutoUseCoupon"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BackupId=json_data.get("BackupId"),
            BackupPeriod=json_data.get("BackupPeriod"),
            BackupTime=json_data.get("BackupTime"),
            Bandwidth=json_data.get("Bandwidth"),
            BusinessInfo=json_data.get("BusinessInfo"),
            Capacity=json_data.get("Capacity"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            ConnectionDomain=json_data.get("ConnectionDomain"),
            ConnectionString=json_data.get("ConnectionString"),
            ConnectionStringPrefix=json_data.get("ConnectionStringPrefix"),
            CouponNo=json_data.get("CouponNo"),
            DbInstanceName=json_data.get("DbInstanceName"),
            DedicatedHostGroupId=json_data.get("DedicatedHostGroupId"),
            EnableBackupLog=json_data.get("EnableBackupLog"),
            EnablePublic=json_data.get("EnablePublic"),
            EndTime=json_data.get("EndTime"),
            EngineVersion=json_data.get("EngineVersion"),
            ForceUpgrade=json_data.get("ForceUpgrade"),
            GlobalInstance=json_data.get("GlobalInstance"),
            GlobalInstanceId=json_data.get("GlobalInstanceId"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceClass=json_data.get("InstanceClass"),
            InstanceName=json_data.get("InstanceName"),
            InstanceReleaseProtection=json_data.get("InstanceReleaseProtection"),
            InstanceType=json_data.get("InstanceType"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=deserialize_list(json_data.get("KmsEncryptionContext"), KmsEncryptionContextDefinition),
            MaintainEndTime=json_data.get("MaintainEndTime"),
            MaintainStartTime=json_data.get("MaintainStartTime"),
            ModifyMode=json_data.get("ModifyMode"),
            NodeType=json_data.get("NodeType"),
            OrderType=json_data.get("OrderType"),
            Password=json_data.get("Password"),
            PaymentType=json_data.get("PaymentType"),
            Period=json_data.get("Period"),
            Port=json_data.get("Port"),
            PrivateConnectionPort=json_data.get("PrivateConnectionPort"),
            PrivateConnectionPrefix=json_data.get("PrivateConnectionPrefix"),
            PrivateIp=json_data.get("PrivateIp"),
            Qps=json_data.get("Qps"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            RestoreTime=json_data.get("RestoreTime"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityIpGroupAttribute=json_data.get("SecurityIpGroupAttribute"),
            SecurityIpGroupName=json_data.get("SecurityIpGroupName"),
            SecurityIps=json_data.get("SecurityIps"),
            SrcdbInstanceId=json_data.get("SrcdbInstanceId"),
            SslEnable=json_data.get("SslEnable"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VpcAuthMode=json_data.get("VpcAuthMode"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class KmsEncryptionContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionContextDefinition = KmsEncryptionContextDefinition


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


