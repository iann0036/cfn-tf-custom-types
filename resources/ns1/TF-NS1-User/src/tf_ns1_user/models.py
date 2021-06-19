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
    AccountManageAccountSettings: Optional[bool]
    AccountManageApikeys: Optional[bool]
    AccountManageIpWhitelist: Optional[bool]
    AccountManagePaymentMethods: Optional[bool]
    AccountManagePlan: Optional[bool]
    AccountManageTeams: Optional[bool]
    AccountManageUsers: Optional[bool]
    AccountViewActivityLog: Optional[bool]
    AccountViewInvoices: Optional[bool]
    DataManageDatafeeds: Optional[bool]
    DataManageDatasources: Optional[bool]
    DataPushToDatafeeds: Optional[bool]
    DhcpManageDhcp: Optional[bool]
    DhcpViewDhcp: Optional[bool]
    DnsManageZones: Optional[bool]
    DnsViewZones: Optional[bool]
    DnsZonesAllow: Optional[Sequence[str]]
    DnsZonesAllowByDefault: Optional[bool]
    DnsZonesDeny: Optional[Sequence[str]]
    Email: Optional[str]
    Id: Optional[str]
    IpWhitelist: Optional[Sequence[str]]
    IpWhitelistStrict: Optional[bool]
    IpamManageIpam: Optional[bool]
    IpamViewIpam: Optional[bool]
    MonitoringManageJobs: Optional[bool]
    MonitoringManageLists: Optional[bool]
    MonitoringViewJobs: Optional[bool]
    Name: Optional[str]
    Notify: Optional[Sequence["_NotifyDefinition"]]
    SecurityManageActiveDirectory: Optional[bool]
    SecurityManageGlobal2fa: Optional[bool]
    Teams: Optional[Sequence[str]]
    Username: Optional[str]

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
            AccountManageAccountSettings=json_data.get("AccountManageAccountSettings"),
            AccountManageApikeys=json_data.get("AccountManageApikeys"),
            AccountManageIpWhitelist=json_data.get("AccountManageIpWhitelist"),
            AccountManagePaymentMethods=json_data.get("AccountManagePaymentMethods"),
            AccountManagePlan=json_data.get("AccountManagePlan"),
            AccountManageTeams=json_data.get("AccountManageTeams"),
            AccountManageUsers=json_data.get("AccountManageUsers"),
            AccountViewActivityLog=json_data.get("AccountViewActivityLog"),
            AccountViewInvoices=json_data.get("AccountViewInvoices"),
            DataManageDatafeeds=json_data.get("DataManageDatafeeds"),
            DataManageDatasources=json_data.get("DataManageDatasources"),
            DataPushToDatafeeds=json_data.get("DataPushToDatafeeds"),
            DhcpManageDhcp=json_data.get("DhcpManageDhcp"),
            DhcpViewDhcp=json_data.get("DhcpViewDhcp"),
            DnsManageZones=json_data.get("DnsManageZones"),
            DnsViewZones=json_data.get("DnsViewZones"),
            DnsZonesAllow=json_data.get("DnsZonesAllow"),
            DnsZonesAllowByDefault=json_data.get("DnsZonesAllowByDefault"),
            DnsZonesDeny=json_data.get("DnsZonesDeny"),
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            IpWhitelist=json_data.get("IpWhitelist"),
            IpWhitelistStrict=json_data.get("IpWhitelistStrict"),
            IpamManageIpam=json_data.get("IpamManageIpam"),
            IpamViewIpam=json_data.get("IpamViewIpam"),
            MonitoringManageJobs=json_data.get("MonitoringManageJobs"),
            MonitoringManageLists=json_data.get("MonitoringManageLists"),
            MonitoringViewJobs=json_data.get("MonitoringViewJobs"),
            Name=json_data.get("Name"),
            Notify=deserialize_list(json_data.get("Notify"), NotifyDefinition),
            SecurityManageActiveDirectory=json_data.get("SecurityManageActiveDirectory"),
            SecurityManageGlobal2fa=json_data.get("SecurityManageGlobal2fa"),
            Teams=json_data.get("Teams"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NotifyDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NotifyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotifyDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotifyDefinition = NotifyDefinition


