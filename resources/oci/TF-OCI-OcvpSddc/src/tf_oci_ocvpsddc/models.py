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
    ActualEsxiHostsCount: Optional[float]
    CompartmentId: Optional[str]
    ComputeAvailabilityDomain: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    EsxiHostsCount: Optional[float]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    HcxAction: Optional[str]
    HcxFqdn: Optional[str]
    HcxInitialPassword: Optional[str]
    HcxOnPremKey: Optional[str]
    HcxOnPremLicenses: Optional[Sequence["_HcxOnPremLicensesDefinition"]]
    HcxPrivateIpId: Optional[str]
    HcxVlanId: Optional[str]
    Id: Optional[str]
    InitialSku: Optional[str]
    InstanceDisplayNamePrefix: Optional[str]
    IsHcxEnabled: Optional[bool]
    IsHcxEnterpriseEnabled: Optional[bool]
    IsHcxPendingDowngrade: Optional[bool]
    NsxEdgeUplink1vlanId: Optional[str]
    NsxEdgeUplink2vlanId: Optional[str]
    NsxEdgeUplinkIpId: Optional[str]
    NsxEdgeVtepVlanId: Optional[str]
    NsxManagerFqdn: Optional[str]
    NsxManagerInitialPassword: Optional[str]
    NsxManagerPrivateIpId: Optional[str]
    NsxManagerUsername: Optional[str]
    NsxOverlaySegmentName: Optional[str]
    NsxVtepVlanId: Optional[str]
    ProvisioningSubnetId: Optional[str]
    ProvisioningVlanId: Optional[str]
    RefreshHcxLicenseStatus: Optional[bool]
    ReplicationVlanId: Optional[str]
    ReservingHcxOnPremiseLicenseKeys: Optional[Sequence[str]]
    SshAuthorizedKeys: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeHcxBillingCycleEnd: Optional[str]
    TimeHcxLicenseStatusUpdated: Optional[str]
    TimeUpdated: Optional[str]
    VcenterFqdn: Optional[str]
    VcenterInitialPassword: Optional[str]
    VcenterPrivateIpId: Optional[str]
    VcenterUsername: Optional[str]
    VmotionVlanId: Optional[str]
    VmwareSoftwareVersion: Optional[str]
    VsanVlanId: Optional[str]
    VsphereVlanId: Optional[str]
    WorkloadNetworkCidr: Optional[str]
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
            ActualEsxiHostsCount=json_data.get("ActualEsxiHostsCount"),
            CompartmentId=json_data.get("CompartmentId"),
            ComputeAvailabilityDomain=json_data.get("ComputeAvailabilityDomain"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            EsxiHostsCount=json_data.get("EsxiHostsCount"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            HcxAction=json_data.get("HcxAction"),
            HcxFqdn=json_data.get("HcxFqdn"),
            HcxInitialPassword=json_data.get("HcxInitialPassword"),
            HcxOnPremKey=json_data.get("HcxOnPremKey"),
            HcxOnPremLicenses=deserialize_list(json_data.get("HcxOnPremLicenses"), HcxOnPremLicensesDefinition),
            HcxPrivateIpId=json_data.get("HcxPrivateIpId"),
            HcxVlanId=json_data.get("HcxVlanId"),
            Id=json_data.get("Id"),
            InitialSku=json_data.get("InitialSku"),
            InstanceDisplayNamePrefix=json_data.get("InstanceDisplayNamePrefix"),
            IsHcxEnabled=json_data.get("IsHcxEnabled"),
            IsHcxEnterpriseEnabled=json_data.get("IsHcxEnterpriseEnabled"),
            IsHcxPendingDowngrade=json_data.get("IsHcxPendingDowngrade"),
            NsxEdgeUplink1vlanId=json_data.get("NsxEdgeUplink1vlanId"),
            NsxEdgeUplink2vlanId=json_data.get("NsxEdgeUplink2vlanId"),
            NsxEdgeUplinkIpId=json_data.get("NsxEdgeUplinkIpId"),
            NsxEdgeVtepVlanId=json_data.get("NsxEdgeVtepVlanId"),
            NsxManagerFqdn=json_data.get("NsxManagerFqdn"),
            NsxManagerInitialPassword=json_data.get("NsxManagerInitialPassword"),
            NsxManagerPrivateIpId=json_data.get("NsxManagerPrivateIpId"),
            NsxManagerUsername=json_data.get("NsxManagerUsername"),
            NsxOverlaySegmentName=json_data.get("NsxOverlaySegmentName"),
            NsxVtepVlanId=json_data.get("NsxVtepVlanId"),
            ProvisioningSubnetId=json_data.get("ProvisioningSubnetId"),
            ProvisioningVlanId=json_data.get("ProvisioningVlanId"),
            RefreshHcxLicenseStatus=json_data.get("RefreshHcxLicenseStatus"),
            ReplicationVlanId=json_data.get("ReplicationVlanId"),
            ReservingHcxOnPremiseLicenseKeys=json_data.get("ReservingHcxOnPremiseLicenseKeys"),
            SshAuthorizedKeys=json_data.get("SshAuthorizedKeys"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeHcxBillingCycleEnd=json_data.get("TimeHcxBillingCycleEnd"),
            TimeHcxLicenseStatusUpdated=json_data.get("TimeHcxLicenseStatusUpdated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            VcenterFqdn=json_data.get("VcenterFqdn"),
            VcenterInitialPassword=json_data.get("VcenterInitialPassword"),
            VcenterPrivateIpId=json_data.get("VcenterPrivateIpId"),
            VcenterUsername=json_data.get("VcenterUsername"),
            VmotionVlanId=json_data.get("VmotionVlanId"),
            VmwareSoftwareVersion=json_data.get("VmwareSoftwareVersion"),
            VsanVlanId=json_data.get("VsanVlanId"),
            VsphereVlanId=json_data.get("VsphereVlanId"),
            WorkloadNetworkCidr=json_data.get("WorkloadNetworkCidr"),
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
class HcxOnPremLicensesDefinition(BaseModel):
    ActivationKey: Optional[str]
    Status: Optional[str]
    SystemName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HcxOnPremLicensesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HcxOnPremLicensesDefinition"]:
        if not json_data:
            return None
        return cls(
            ActivationKey=json_data.get("ActivationKey"),
            Status=json_data.get("Status"),
            SystemName=json_data.get("SystemName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HcxOnPremLicensesDefinition = HcxOnPremLicensesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


