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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    ClusterId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    SendResolved: Optional[bool]
    DingtalkConfig: Optional[Sequence["_DingtalkConfigDefinition"]]
    MsteamsConfig: Optional[Sequence["_MsteamsConfigDefinition"]]
    PagerdutyConfig: Optional[Sequence["_PagerdutyConfigDefinition"]]
    SlackConfig: Optional[Sequence["_SlackConfigDefinition"]]
    SmtpConfig: Optional[Sequence["_SmtpConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WebhookConfig: Optional[Sequence["_WebhookConfigDefinition"]]
    WechatConfig: Optional[Sequence["_WechatConfigDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            ClusterId=json_data.get("ClusterId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            SendResolved=json_data.get("SendResolved"),
            DingtalkConfig=deserialize_list(json_data.get("DingtalkConfig"), DingtalkConfigDefinition),
            MsteamsConfig=deserialize_list(json_data.get("MsteamsConfig"), MsteamsConfigDefinition),
            PagerdutyConfig=deserialize_list(json_data.get("PagerdutyConfig"), PagerdutyConfigDefinition),
            SlackConfig=deserialize_list(json_data.get("SlackConfig"), SlackConfigDefinition),
            SmtpConfig=deserialize_list(json_data.get("SmtpConfig"), SmtpConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WebhookConfig=deserialize_list(json_data.get("WebhookConfig"), WebhookConfigDefinition),
            WechatConfig=deserialize_list(json_data.get("WechatConfig"), WechatConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class DingtalkConfigDefinition(BaseModel):
    ProxyUrl: Optional[str]
    Secret: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DingtalkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DingtalkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ProxyUrl=json_data.get("ProxyUrl"),
            Secret=json_data.get("Secret"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DingtalkConfigDefinition = DingtalkConfigDefinition


@dataclass
class MsteamsConfigDefinition(BaseModel):
    ProxyUrl: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MsteamsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MsteamsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ProxyUrl=json_data.get("ProxyUrl"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MsteamsConfigDefinition = MsteamsConfigDefinition


@dataclass
class PagerdutyConfigDefinition(BaseModel):
    ProxyUrl: Optional[str]
    ServiceKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PagerdutyConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PagerdutyConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ProxyUrl=json_data.get("ProxyUrl"),
            ServiceKey=json_data.get("ServiceKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PagerdutyConfigDefinition = PagerdutyConfigDefinition


@dataclass
class SlackConfigDefinition(BaseModel):
    DefaultRecipient: Optional[str]
    ProxyUrl: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultRecipient=json_data.get("DefaultRecipient"),
            ProxyUrl=json_data.get("ProxyUrl"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackConfigDefinition = SlackConfigDefinition


@dataclass
class SmtpConfigDefinition(BaseModel):
    DefaultRecipient: Optional[str]
    Host: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    Sender: Optional[str]
    Tls: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmtpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmtpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultRecipient=json_data.get("DefaultRecipient"),
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Sender=json_data.get("Sender"),
            Tls=json_data.get("Tls"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmtpConfigDefinition = SmtpConfigDefinition


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


@dataclass
class WebhookConfigDefinition(BaseModel):
    ProxyUrl: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ProxyUrl=json_data.get("ProxyUrl"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookConfigDefinition = WebhookConfigDefinition


@dataclass
class WechatConfigDefinition(BaseModel):
    Agent: Optional[str]
    Corp: Optional[str]
    DefaultRecipient: Optional[str]
    ProxyUrl: Optional[str]
    RecipientType: Optional[str]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WechatConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WechatConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Agent=json_data.get("Agent"),
            Corp=json_data.get("Corp"),
            DefaultRecipient=json_data.get("DefaultRecipient"),
            ProxyUrl=json_data.get("ProxyUrl"),
            RecipientType=json_data.get("RecipientType"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WechatConfigDefinition = WechatConfigDefinition


