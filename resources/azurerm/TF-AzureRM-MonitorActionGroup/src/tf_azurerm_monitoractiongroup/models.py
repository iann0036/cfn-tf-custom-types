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
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ShortName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ArmRoleReceiver: Optional[Sequence["_ArmRoleReceiverDefinition"]]
    AutomationRunbookReceiver: Optional[Sequence["_AutomationRunbookReceiverDefinition"]]
    AzureAppPushReceiver: Optional[Sequence["_AzureAppPushReceiverDefinition"]]
    AzureFunctionReceiver: Optional[Sequence["_AzureFunctionReceiverDefinition"]]
    EmailReceiver: Optional[Sequence["_EmailReceiverDefinition"]]
    ItsmReceiver: Optional[Sequence["_ItsmReceiverDefinition"]]
    LogicAppReceiver: Optional[Sequence["_LogicAppReceiverDefinition"]]
    SmsReceiver: Optional[Sequence["_SmsReceiverDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VoiceReceiver: Optional[Sequence["_VoiceReceiverDefinition"]]
    WebhookReceiver: Optional[Sequence["_WebhookReceiverDefinition"]]

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
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ShortName=json_data.get("ShortName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ArmRoleReceiver=deserialize_list(json_data.get("ArmRoleReceiver"), ArmRoleReceiverDefinition),
            AutomationRunbookReceiver=deserialize_list(json_data.get("AutomationRunbookReceiver"), AutomationRunbookReceiverDefinition),
            AzureAppPushReceiver=deserialize_list(json_data.get("AzureAppPushReceiver"), AzureAppPushReceiverDefinition),
            AzureFunctionReceiver=deserialize_list(json_data.get("AzureFunctionReceiver"), AzureFunctionReceiverDefinition),
            EmailReceiver=deserialize_list(json_data.get("EmailReceiver"), EmailReceiverDefinition),
            ItsmReceiver=deserialize_list(json_data.get("ItsmReceiver"), ItsmReceiverDefinition),
            LogicAppReceiver=deserialize_list(json_data.get("LogicAppReceiver"), LogicAppReceiverDefinition),
            SmsReceiver=deserialize_list(json_data.get("SmsReceiver"), SmsReceiverDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VoiceReceiver=deserialize_list(json_data.get("VoiceReceiver"), VoiceReceiverDefinition),
            WebhookReceiver=deserialize_list(json_data.get("WebhookReceiver"), WebhookReceiverDefinition),
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
class ArmRoleReceiverDefinition(BaseModel):
    Name: Optional[str]
    RoleId: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ArmRoleReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArmRoleReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RoleId=json_data.get("RoleId"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArmRoleReceiverDefinition = ArmRoleReceiverDefinition


@dataclass
class AutomationRunbookReceiverDefinition(BaseModel):
    AutomationAccountId: Optional[str]
    IsGlobalRunbook: Optional[bool]
    Name: Optional[str]
    RunbookName: Optional[str]
    ServiceUri: Optional[str]
    UseCommonAlertSchema: Optional[bool]
    WebhookResourceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutomationRunbookReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomationRunbookReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            AutomationAccountId=json_data.get("AutomationAccountId"),
            IsGlobalRunbook=json_data.get("IsGlobalRunbook"),
            Name=json_data.get("Name"),
            RunbookName=json_data.get("RunbookName"),
            ServiceUri=json_data.get("ServiceUri"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
            WebhookResourceId=json_data.get("WebhookResourceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomationRunbookReceiverDefinition = AutomationRunbookReceiverDefinition


@dataclass
class AzureAppPushReceiverDefinition(BaseModel):
    EmailAddress: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureAppPushReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureAppPushReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            EmailAddress=json_data.get("EmailAddress"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureAppPushReceiverDefinition = AzureAppPushReceiverDefinition


@dataclass
class AzureFunctionReceiverDefinition(BaseModel):
    FunctionAppResourceId: Optional[str]
    FunctionName: Optional[str]
    HttpTriggerUrl: Optional[str]
    Name: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFunctionReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFunctionReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            FunctionAppResourceId=json_data.get("FunctionAppResourceId"),
            FunctionName=json_data.get("FunctionName"),
            HttpTriggerUrl=json_data.get("HttpTriggerUrl"),
            Name=json_data.get("Name"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFunctionReceiverDefinition = AzureFunctionReceiverDefinition


@dataclass
class EmailReceiverDefinition(BaseModel):
    EmailAddress: Optional[str]
    Name: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EmailReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            EmailAddress=json_data.get("EmailAddress"),
            Name=json_data.get("Name"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailReceiverDefinition = EmailReceiverDefinition


@dataclass
class ItsmReceiverDefinition(BaseModel):
    ConnectionId: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    TicketConfiguration: Optional[str]
    WorkspaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ItsmReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItsmReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionId=json_data.get("ConnectionId"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            TicketConfiguration=json_data.get("TicketConfiguration"),
            WorkspaceId=json_data.get("WorkspaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItsmReceiverDefinition = ItsmReceiverDefinition


@dataclass
class LogicAppReceiverDefinition(BaseModel):
    CallbackUrl: Optional[str]
    Name: Optional[str]
    ResourceId: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LogicAppReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogicAppReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            CallbackUrl=json_data.get("CallbackUrl"),
            Name=json_data.get("Name"),
            ResourceId=json_data.get("ResourceId"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogicAppReceiverDefinition = LogicAppReceiverDefinition


@dataclass
class SmsReceiverDefinition(BaseModel):
    CountryCode: Optional[str]
    Name: Optional[str]
    PhoneNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmsReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmsReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            CountryCode=json_data.get("CountryCode"),
            Name=json_data.get("Name"),
            PhoneNumber=json_data.get("PhoneNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmsReceiverDefinition = SmsReceiverDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VoiceReceiverDefinition(BaseModel):
    CountryCode: Optional[str]
    Name: Optional[str]
    PhoneNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VoiceReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VoiceReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            CountryCode=json_data.get("CountryCode"),
            Name=json_data.get("Name"),
            PhoneNumber=json_data.get("PhoneNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VoiceReceiverDefinition = VoiceReceiverDefinition


@dataclass
class WebhookReceiverDefinition(BaseModel):
    Name: Optional[str]
    ServiceUri: Optional[str]
    UseCommonAlertSchema: Optional[bool]
    AadAuth: Optional[Sequence["_AadAuthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ServiceUri=json_data.get("ServiceUri"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
            AadAuth=deserialize_list(json_data.get("AadAuth"), AadAuthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookReceiverDefinition = WebhookReceiverDefinition


@dataclass
class AadAuthDefinition(BaseModel):
    IdentifierUri: Optional[str]
    ObjectId: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AadAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AadAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentifierUri=json_data.get("IdentifierUri"),
            ObjectId=json_data.get("ObjectId"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AadAuthDefinition = AadAuthDefinition


