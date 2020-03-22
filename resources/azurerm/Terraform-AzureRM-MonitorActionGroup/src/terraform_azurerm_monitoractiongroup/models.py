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
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ShortName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ArmRoleReceiver: Optional[Sequence["_ArmRoleReceiver"]]
    AutomationRunbookReceiver: Optional[Sequence["_AutomationRunbookReceiver"]]
    AzureAppPushReceiver: Optional[Sequence["_AzureAppPushReceiver"]]
    AzureFunctionReceiver: Optional[Sequence["_AzureFunctionReceiver"]]
    EmailReceiver: Optional[Sequence["_EmailReceiver"]]
    ItsmReceiver: Optional[Sequence["_ItsmReceiver"]]
    LogicAppReceiver: Optional[Sequence["_LogicAppReceiver"]]
    SmsReceiver: Optional[Sequence["_SmsReceiver"]]
    Timeouts: Optional["_Timeouts"]
    VoiceReceiver: Optional[Sequence["_VoiceReceiver"]]
    WebhookReceiver: Optional[Sequence["_WebhookReceiver"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ShortName=json_data.get("ShortName"),
            Tags=json_data.get("Tags"),
            ArmRoleReceiver=json_data.get("ArmRoleReceiver"),
            AutomationRunbookReceiver=json_data.get("AutomationRunbookReceiver"),
            AzureAppPushReceiver=json_data.get("AzureAppPushReceiver"),
            AzureFunctionReceiver=json_data.get("AzureFunctionReceiver"),
            EmailReceiver=json_data.get("EmailReceiver"),
            ItsmReceiver=json_data.get("ItsmReceiver"),
            LogicAppReceiver=json_data.get("LogicAppReceiver"),
            SmsReceiver=json_data.get("SmsReceiver"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VoiceReceiver=json_data.get("VoiceReceiver"),
            WebhookReceiver=json_data.get("WebhookReceiver"),
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
class ArmRoleReceiver:
    Name: Optional[str]
    RoleId: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ArmRoleReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArmRoleReceiver"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RoleId=json_data.get("RoleId"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArmRoleReceiver = ArmRoleReceiver


@dataclass
class AutomationRunbookReceiver:
    AutomationAccountId: Optional[str]
    IsGlobalRunbook: Optional[bool]
    Name: Optional[str]
    RunbookName: Optional[str]
    ServiceUri: Optional[str]
    UseCommonAlertSchema: Optional[bool]
    WebhookResourceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutomationRunbookReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomationRunbookReceiver"]:
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
_AutomationRunbookReceiver = AutomationRunbookReceiver


@dataclass
class AzureAppPushReceiver:
    EmailAddress: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureAppPushReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureAppPushReceiver"]:
        if not json_data:
            return None
        return cls(
            EmailAddress=json_data.get("EmailAddress"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureAppPushReceiver = AzureAppPushReceiver


@dataclass
class AzureFunctionReceiver:
    FunctionAppResourceId: Optional[str]
    FunctionName: Optional[str]
    HttpTriggerUrl: Optional[str]
    Name: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFunctionReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFunctionReceiver"]:
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
_AzureFunctionReceiver = AzureFunctionReceiver


@dataclass
class EmailReceiver:
    EmailAddress: Optional[str]
    Name: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EmailReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailReceiver"]:
        if not json_data:
            return None
        return cls(
            EmailAddress=json_data.get("EmailAddress"),
            Name=json_data.get("Name"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailReceiver = EmailReceiver


@dataclass
class ItsmReceiver:
    ConnectionId: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    TicketConfiguration: Optional[str]
    WorkspaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ItsmReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItsmReceiver"]:
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
_ItsmReceiver = ItsmReceiver


@dataclass
class LogicAppReceiver:
    CallbackUrl: Optional[str]
    Name: Optional[str]
    ResourceId: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LogicAppReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogicAppReceiver"]:
        if not json_data:
            return None
        return cls(
            CallbackUrl=json_data.get("CallbackUrl"),
            Name=json_data.get("Name"),
            ResourceId=json_data.get("ResourceId"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogicAppReceiver = LogicAppReceiver


@dataclass
class SmsReceiver:
    CountryCode: Optional[str]
    Name: Optional[str]
    PhoneNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmsReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmsReceiver"]:
        if not json_data:
            return None
        return cls(
            CountryCode=json_data.get("CountryCode"),
            Name=json_data.get("Name"),
            PhoneNumber=json_data.get("PhoneNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmsReceiver = SmsReceiver


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class VoiceReceiver:
    CountryCode: Optional[str]
    Name: Optional[str]
    PhoneNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VoiceReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VoiceReceiver"]:
        if not json_data:
            return None
        return cls(
            CountryCode=json_data.get("CountryCode"),
            Name=json_data.get("Name"),
            PhoneNumber=json_data.get("PhoneNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VoiceReceiver = VoiceReceiver


@dataclass
class WebhookReceiver:
    Name: Optional[str]
    ServiceUri: Optional[str]
    UseCommonAlertSchema: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookReceiver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookReceiver"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ServiceUri=json_data.get("ServiceUri"),
            UseCommonAlertSchema=json_data.get("UseCommonAlertSchema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookReceiver = WebhookReceiver


