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
    GpoContainer: Optional[str]
    Id: Optional[str]
    AccountLockout: Optional[Sequence["_AccountLockoutDefinition"]]
    ApplicationLog: Optional[Sequence["_ApplicationLogDefinition"]]
    AuditLog: Optional[Sequence["_AuditLogDefinition"]]
    EventAudit: Optional[Sequence["_EventAuditDefinition"]]
    Filesystem: Optional[Sequence["_FilesystemDefinition"]]
    KerberosPolicy: Optional[Sequence["_KerberosPolicyDefinition"]]
    PasswordPolicies: Optional[Sequence["_PasswordPoliciesDefinition"]]
    RegistryKeys: Optional[Sequence["_RegistryKeysDefinition"]]
    RegistryValues: Optional[Sequence["_RegistryValuesDefinition"]]
    RestrictedGroups: Optional[Sequence["_RestrictedGroupsDefinition"]]
    SystemLog: Optional[Sequence["_SystemLogDefinition"]]
    SystemServices: Optional[Sequence["_SystemServicesDefinition"]]

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
            GpoContainer=json_data.get("GpoContainer"),
            Id=json_data.get("Id"),
            AccountLockout=deserialize_list(json_data.get("AccountLockout"), AccountLockoutDefinition),
            ApplicationLog=deserialize_list(json_data.get("ApplicationLog"), ApplicationLogDefinition),
            AuditLog=deserialize_list(json_data.get("AuditLog"), AuditLogDefinition),
            EventAudit=deserialize_list(json_data.get("EventAudit"), EventAuditDefinition),
            Filesystem=deserialize_list(json_data.get("Filesystem"), FilesystemDefinition),
            KerberosPolicy=deserialize_list(json_data.get("KerberosPolicy"), KerberosPolicyDefinition),
            PasswordPolicies=deserialize_list(json_data.get("PasswordPolicies"), PasswordPoliciesDefinition),
            RegistryKeys=deserialize_list(json_data.get("RegistryKeys"), RegistryKeysDefinition),
            RegistryValues=deserialize_list(json_data.get("RegistryValues"), RegistryValuesDefinition),
            RestrictedGroups=deserialize_list(json_data.get("RestrictedGroups"), RestrictedGroupsDefinition),
            SystemLog=deserialize_list(json_data.get("SystemLog"), SystemLogDefinition),
            SystemServices=deserialize_list(json_data.get("SystemServices"), SystemServicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountLockoutDefinition(BaseModel):
    ForceLogoffWhenHourExpire: Optional[str]
    LockoutBadCount: Optional[str]
    LockoutDuration: Optional[str]
    ResetLockoutCount: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccountLockoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountLockoutDefinition"]:
        if not json_data:
            return None
        return cls(
            ForceLogoffWhenHourExpire=json_data.get("ForceLogoffWhenHourExpire"),
            LockoutBadCount=json_data.get("LockoutBadCount"),
            LockoutDuration=json_data.get("LockoutDuration"),
            ResetLockoutCount=json_data.get("ResetLockoutCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountLockoutDefinition = AccountLockoutDefinition


@dataclass
class ApplicationLogDefinition(BaseModel):
    AuditLogRetentionPeriod: Optional[str]
    MaximumLogSize: Optional[str]
    RestrictGuestAccess: Optional[str]
    RetentionDays: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationLogDefinition"]:
        if not json_data:
            return None
        return cls(
            AuditLogRetentionPeriod=json_data.get("AuditLogRetentionPeriod"),
            MaximumLogSize=json_data.get("MaximumLogSize"),
            RestrictGuestAccess=json_data.get("RestrictGuestAccess"),
            RetentionDays=json_data.get("RetentionDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationLogDefinition = ApplicationLogDefinition


@dataclass
class AuditLogDefinition(BaseModel):
    AuditLogRetentionPeriod: Optional[str]
    MaximumLogSize: Optional[str]
    RestrictGuestAccess: Optional[str]
    RetentionDays: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuditLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditLogDefinition"]:
        if not json_data:
            return None
        return cls(
            AuditLogRetentionPeriod=json_data.get("AuditLogRetentionPeriod"),
            MaximumLogSize=json_data.get("MaximumLogSize"),
            RestrictGuestAccess=json_data.get("RestrictGuestAccess"),
            RetentionDays=json_data.get("RetentionDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditLogDefinition = AuditLogDefinition


@dataclass
class EventAuditDefinition(BaseModel):
    AuditAccountLogon: Optional[str]
    AuditAccountManage: Optional[str]
    AuditDsAccess: Optional[str]
    AuditLogonEvents: Optional[str]
    AuditObjectAccess: Optional[str]
    AuditPolicyChange: Optional[str]
    AuditPrivilegeUse: Optional[str]
    AuditProcessTracking: Optional[str]
    AuditSystemEvents: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventAuditDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventAuditDefinition"]:
        if not json_data:
            return None
        return cls(
            AuditAccountLogon=json_data.get("AuditAccountLogon"),
            AuditAccountManage=json_data.get("AuditAccountManage"),
            AuditDsAccess=json_data.get("AuditDsAccess"),
            AuditLogonEvents=json_data.get("AuditLogonEvents"),
            AuditObjectAccess=json_data.get("AuditObjectAccess"),
            AuditPolicyChange=json_data.get("AuditPolicyChange"),
            AuditPrivilegeUse=json_data.get("AuditPrivilegeUse"),
            AuditProcessTracking=json_data.get("AuditProcessTracking"),
            AuditSystemEvents=json_data.get("AuditSystemEvents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventAuditDefinition = EventAuditDefinition


@dataclass
class FilesystemDefinition(BaseModel):
    Acl: Optional[str]
    Path: Optional[str]
    PropagationMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilesystemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilesystemDefinition"]:
        if not json_data:
            return None
        return cls(
            Acl=json_data.get("Acl"),
            Path=json_data.get("Path"),
            PropagationMode=json_data.get("PropagationMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilesystemDefinition = FilesystemDefinition


@dataclass
class KerberosPolicyDefinition(BaseModel):
    MaxClockSkew: Optional[str]
    MaxRenewAge: Optional[str]
    MaxServiceAge: Optional[str]
    MaxTicketAge: Optional[str]
    TicketValidateClient: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KerberosPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KerberosPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxClockSkew=json_data.get("MaxClockSkew"),
            MaxRenewAge=json_data.get("MaxRenewAge"),
            MaxServiceAge=json_data.get("MaxServiceAge"),
            MaxTicketAge=json_data.get("MaxTicketAge"),
            TicketValidateClient=json_data.get("TicketValidateClient"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KerberosPolicyDefinition = KerberosPolicyDefinition


@dataclass
class PasswordPoliciesDefinition(BaseModel):
    ClearTextPassword: Optional[str]
    MaximumPasswordAge: Optional[str]
    MinimumPasswordAge: Optional[str]
    MinimumPasswordLength: Optional[str]
    PasswordComplexity: Optional[str]
    PasswordHistorySize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            ClearTextPassword=json_data.get("ClearTextPassword"),
            MaximumPasswordAge=json_data.get("MaximumPasswordAge"),
            MinimumPasswordAge=json_data.get("MinimumPasswordAge"),
            MinimumPasswordLength=json_data.get("MinimumPasswordLength"),
            PasswordComplexity=json_data.get("PasswordComplexity"),
            PasswordHistorySize=json_data.get("PasswordHistorySize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordPoliciesDefinition = PasswordPoliciesDefinition


@dataclass
class RegistryKeysDefinition(BaseModel):
    Acl: Optional[str]
    KeyName: Optional[str]
    PropagationMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegistryKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegistryKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            Acl=json_data.get("Acl"),
            KeyName=json_data.get("KeyName"),
            PropagationMode=json_data.get("PropagationMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegistryKeysDefinition = RegistryKeysDefinition


@dataclass
class RegistryValuesDefinition(BaseModel):
    KeyName: Optional[str]
    Value: Optional[str]
    ValueType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegistryValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegistryValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyName=json_data.get("KeyName"),
            Value=json_data.get("Value"),
            ValueType=json_data.get("ValueType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegistryValuesDefinition = RegistryValuesDefinition


@dataclass
class RestrictedGroupsDefinition(BaseModel):
    GroupMemberof: Optional[str]
    GroupMembers: Optional[str]
    GroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictedGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictedGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupMemberof=json_data.get("GroupMemberof"),
            GroupMembers=json_data.get("GroupMembers"),
            GroupName=json_data.get("GroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestrictedGroupsDefinition = RestrictedGroupsDefinition


@dataclass
class SystemLogDefinition(BaseModel):
    AuditLogRetentionPeriod: Optional[str]
    MaximumLogSize: Optional[str]
    RestrictGuestAccess: Optional[str]
    RetentionDays: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemLogDefinition"]:
        if not json_data:
            return None
        return cls(
            AuditLogRetentionPeriod=json_data.get("AuditLogRetentionPeriod"),
            MaximumLogSize=json_data.get("MaximumLogSize"),
            RestrictGuestAccess=json_data.get("RestrictGuestAccess"),
            RetentionDays=json_data.get("RetentionDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemLogDefinition = SystemLogDefinition


@dataclass
class SystemServicesDefinition(BaseModel):
    Acl: Optional[str]
    ServiceName: Optional[str]
    StartupMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Acl=json_data.get("Acl"),
            ServiceName=json_data.get("ServiceName"),
            StartupMode=json_data.get("StartupMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemServicesDefinition = SystemServicesDefinition


