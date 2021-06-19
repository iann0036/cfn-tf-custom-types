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
    CanSwitchRole: Optional[bool]
    Create: Optional[Sequence[str]]
    CrossAccountAccess: Optional[Sequence[str]]
    Email: Optional[str]
    FirstName: Optional[str]
    HasApiKey: Optional[bool]
    HasApiKeyV1: Optional[bool]
    HasApiKeyV2: Optional[bool]
    IamSafe: Optional[Sequence["_IamSafeDefinition3"]]
    Id: Optional[str]
    IsAuditor: Optional[bool]
    IsLocked: Optional[bool]
    IsMfaEnabled: Optional[bool]
    IsMobileDevicePaired: Optional[bool]
    IsOwner: Optional[bool]
    IsSsoEnabled: Optional[bool]
    IsSuperUser: Optional[bool]
    IsSuspended: Optional[bool]
    LastLogin: Optional[str]
    LastName: Optional[str]
    PermitAlertActions: Optional[bool]
    PermitNotifications: Optional[bool]
    PermitOnBoarding: Optional[bool]
    PermitPolicies: Optional[bool]
    PermitRulesets: Optional[bool]
    RoleIds: Optional[Sequence[float]]
    Access: Optional[Sequence["_AccessDefinition"]]
    Manage: Optional[Sequence["_ManageDefinition"]]
    View: Optional[Sequence["_ViewDefinition"]]

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
            CanSwitchRole=json_data.get("CanSwitchRole"),
            Create=json_data.get("Create"),
            CrossAccountAccess=json_data.get("CrossAccountAccess"),
            Email=json_data.get("Email"),
            FirstName=json_data.get("FirstName"),
            HasApiKey=json_data.get("HasApiKey"),
            HasApiKeyV1=json_data.get("HasApiKeyV1"),
            HasApiKeyV2=json_data.get("HasApiKeyV2"),
            IamSafe=deserialize_list(json_data.get("IamSafe"), IamSafeDefinition3),
            Id=json_data.get("Id"),
            IsAuditor=json_data.get("IsAuditor"),
            IsLocked=json_data.get("IsLocked"),
            IsMfaEnabled=json_data.get("IsMfaEnabled"),
            IsMobileDevicePaired=json_data.get("IsMobileDevicePaired"),
            IsOwner=json_data.get("IsOwner"),
            IsSsoEnabled=json_data.get("IsSsoEnabled"),
            IsSuperUser=json_data.get("IsSuperUser"),
            IsSuspended=json_data.get("IsSuspended"),
            LastLogin=json_data.get("LastLogin"),
            LastName=json_data.get("LastName"),
            PermitAlertActions=json_data.get("PermitAlertActions"),
            PermitNotifications=json_data.get("PermitNotifications"),
            PermitOnBoarding=json_data.get("PermitOnBoarding"),
            PermitPolicies=json_data.get("PermitPolicies"),
            PermitRulesets=json_data.get("PermitRulesets"),
            RoleIds=json_data.get("RoleIds"),
            Access=deserialize_list(json_data.get("Access"), AccessDefinition),
            Manage=deserialize_list(json_data.get("Manage"), ManageDefinition),
            View=deserialize_list(json_data.get("View"), ViewDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IamSafeDefinition3(BaseModel):
    CloudAccounts: Optional[Sequence["_IamSafeDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_IamSafeDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamSafeDefinition3"]:
        if not json_data:
            return None
        return cls(
            CloudAccounts=deserialize_list(json_data.get("CloudAccounts"), IamSafeDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamSafeDefinition3 = IamSafeDefinition3


@dataclass
class IamSafeDefinition2(BaseModel):
    CloudAccountId: Optional[str]
    CloudAccountState: Optional[str]
    ExternalAccountNumber: Optional[str]
    IamEntities: Optional[Sequence[str]]
    IamEntitiesLastLeaseTime: Optional[Sequence["_IamSafeDefinition"]]
    IamEntity: Optional[str]
    LastLeaseTime: Optional[str]
    Name: Optional[str]
    State: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IamSafeDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamSafeDefinition2"]:
        if not json_data:
            return None
        return cls(
            CloudAccountId=json_data.get("CloudAccountId"),
            CloudAccountState=json_data.get("CloudAccountState"),
            ExternalAccountNumber=json_data.get("ExternalAccountNumber"),
            IamEntities=json_data.get("IamEntities"),
            IamEntitiesLastLeaseTime=deserialize_list(json_data.get("IamEntitiesLastLeaseTime"), IamSafeDefinition),
            IamEntity=json_data.get("IamEntity"),
            LastLeaseTime=json_data.get("LastLeaseTime"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamSafeDefinition2 = IamSafeDefinition2


@dataclass
class IamSafeDefinition(BaseModel):
    IamEntity: Optional[str]
    LastLeaseTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IamSafeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamSafeDefinition"]:
        if not json_data:
            return None
        return cls(
            IamEntity=json_data.get("IamEntity"),
            LastLeaseTime=json_data.get("LastLeaseTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamSafeDefinition = IamSafeDefinition


@dataclass
class AccessDefinition(BaseModel):
    MainId: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    Traffic: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessDefinition"]:
        if not json_data:
            return None
        return cls(
            MainId=json_data.get("MainId"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Traffic=json_data.get("Traffic"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessDefinition = AccessDefinition


@dataclass
class ManageDefinition(BaseModel):
    MainId: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    Traffic: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManageDefinition"]:
        if not json_data:
            return None
        return cls(
            MainId=json_data.get("MainId"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Traffic=json_data.get("Traffic"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManageDefinition = ManageDefinition


@dataclass
class ViewDefinition(BaseModel):
    MainId: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    Traffic: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ViewDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewDefinition"]:
        if not json_data:
            return None
        return cls(
            MainId=json_data.get("MainId"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Traffic=json_data.get("Traffic"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ViewDefinition = ViewDefinition


