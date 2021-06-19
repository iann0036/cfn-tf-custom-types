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
    AvailabilityZones: Optional[Sequence[str]]
    CloudPassword: Optional[str]
    CloudUsername: Optional[str]
    ClusterId: Optional[str]
    ClusterInfo: Optional[Sequence["_ClusterInfoDefinition"]]
    DelayAccountLink: Optional[bool]
    DeploymentType: Optional[str]
    EdrsPolicyType: Optional[str]
    EnableEdrs: Optional[bool]
    HostInstanceType: Optional[str]
    Id: Optional[str]
    IntranetMtuUplink: Optional[float]
    MaxHosts: Optional[float]
    MinHosts: Optional[float]
    NsxtReverseProxyUrl: Optional[str]
    NumHost: Optional[float]
    ProviderType: Optional[str]
    Region: Optional[str]
    SddcName: Optional[str]
    SddcSize: Optional[Sequence["_SddcSizeDefinition"]]
    SddcState: Optional[str]
    SddcTemplateId: Optional[str]
    SddcType: Optional[str]
    Size: Optional[str]
    SkipCreatingVxlan: Optional[bool]
    SsoDomain: Optional[str]
    StorageCapacity: Optional[str]
    VcUrl: Optional[str]
    VpcCidr: Optional[str]
    VxlanSubnet: Optional[str]
    AccountLinkSddcConfig: Optional[Sequence["_AccountLinkSddcConfigDefinition"]]
    MicrosoftLicensingConfig: Optional[Sequence["_MicrosoftLicensingConfigDefinition"]]
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
            AvailabilityZones=json_data.get("AvailabilityZones"),
            CloudPassword=json_data.get("CloudPassword"),
            CloudUsername=json_data.get("CloudUsername"),
            ClusterId=json_data.get("ClusterId"),
            ClusterInfo=deserialize_list(json_data.get("ClusterInfo"), ClusterInfoDefinition),
            DelayAccountLink=json_data.get("DelayAccountLink"),
            DeploymentType=json_data.get("DeploymentType"),
            EdrsPolicyType=json_data.get("EdrsPolicyType"),
            EnableEdrs=json_data.get("EnableEdrs"),
            HostInstanceType=json_data.get("HostInstanceType"),
            Id=json_data.get("Id"),
            IntranetMtuUplink=json_data.get("IntranetMtuUplink"),
            MaxHosts=json_data.get("MaxHosts"),
            MinHosts=json_data.get("MinHosts"),
            NsxtReverseProxyUrl=json_data.get("NsxtReverseProxyUrl"),
            NumHost=json_data.get("NumHost"),
            ProviderType=json_data.get("ProviderType"),
            Region=json_data.get("Region"),
            SddcName=json_data.get("SddcName"),
            SddcSize=deserialize_list(json_data.get("SddcSize"), SddcSizeDefinition),
            SddcState=json_data.get("SddcState"),
            SddcTemplateId=json_data.get("SddcTemplateId"),
            SddcType=json_data.get("SddcType"),
            Size=json_data.get("Size"),
            SkipCreatingVxlan=json_data.get("SkipCreatingVxlan"),
            SsoDomain=json_data.get("SsoDomain"),
            StorageCapacity=json_data.get("StorageCapacity"),
            VcUrl=json_data.get("VcUrl"),
            VpcCidr=json_data.get("VpcCidr"),
            VxlanSubnet=json_data.get("VxlanSubnet"),
            AccountLinkSddcConfig=deserialize_list(json_data.get("AccountLinkSddcConfig"), AccountLinkSddcConfigDefinition),
            MicrosoftLicensingConfig=deserialize_list(json_data.get("MicrosoftLicensingConfig"), MicrosoftLicensingConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClusterInfoDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterInfoDefinition = ClusterInfoDefinition


@dataclass
class SddcSizeDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SddcSizeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SddcSizeDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SddcSizeDefinition = SddcSizeDefinition


@dataclass
class AccountLinkSddcConfigDefinition(BaseModel):
    ConnectedAccountId: Optional[str]
    CustomerSubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccountLinkSddcConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountLinkSddcConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectedAccountId=json_data.get("ConnectedAccountId"),
            CustomerSubnetIds=json_data.get("CustomerSubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountLinkSddcConfigDefinition = AccountLinkSddcConfigDefinition


@dataclass
class MicrosoftLicensingConfigDefinition(BaseModel):
    MssqlLicensing: Optional[str]
    WindowsLicensing: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftLicensingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftLicensingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MssqlLicensing=json_data.get("MssqlLicensing"),
            WindowsLicensing=json_data.get("WindowsLicensing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftLicensingConfigDefinition = MicrosoftLicensingConfigDefinition


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


