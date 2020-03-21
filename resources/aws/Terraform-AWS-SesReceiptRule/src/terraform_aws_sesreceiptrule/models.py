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
    After: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Recipients: Optional[Sequence[str]]
    RuleSetName: Optional[str]
    ScanEnabled: Optional[bool]
    TlsPolicy: Optional[str]
    AddHeaderAction: Optional[Sequence["_AddHeaderAction"]]
    BounceAction: Optional[Sequence["_BounceAction"]]
    LambdaAction: Optional[Sequence["_LambdaAction"]]
    S3Action: Optional[Sequence["_S3Action"]]
    SnsAction: Optional[Sequence["_SnsAction"]]
    StopAction: Optional[Sequence["_StopAction"]]
    WorkmailAction: Optional[Sequence["_WorkmailAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            After=json_data.get("After"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Recipients=json_data.get("Recipients"),
            RuleSetName=json_data.get("RuleSetName"),
            ScanEnabled=json_data.get("ScanEnabled"),
            TlsPolicy=json_data.get("TlsPolicy"),
            AddHeaderAction=json_data.get("AddHeaderAction"),
            BounceAction=json_data.get("BounceAction"),
            LambdaAction=json_data.get("LambdaAction"),
            S3Action=json_data.get("S3Action"),
            SnsAction=json_data.get("SnsAction"),
            StopAction=json_data.get("StopAction"),
            WorkmailAction=json_data.get("WorkmailAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddHeaderAction:
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    Position: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AddHeaderAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddHeaderAction"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            Position=json_data.get("Position"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddHeaderAction = AddHeaderAction


@dataclass
class BounceAction:
    Message: Optional[str]
    Position: Optional[float]
    Sender: Optional[str]
    SmtpReplyCode: Optional[str]
    StatusCode: Optional[str]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BounceAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BounceAction"]:
        if not json_data:
            return None
        return cls(
            Message=json_data.get("Message"),
            Position=json_data.get("Position"),
            Sender=json_data.get("Sender"),
            SmtpReplyCode=json_data.get("SmtpReplyCode"),
            StatusCode=json_data.get("StatusCode"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BounceAction = BounceAction


@dataclass
class LambdaAction:
    FunctionArn: Optional[str]
    InvocationType: Optional[str]
    Position: Optional[float]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaAction"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
            InvocationType=json_data.get("InvocationType"),
            Position=json_data.get("Position"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaAction = LambdaAction


@dataclass
class S3Action:
    BucketName: Optional[str]
    KmsKeyArn: Optional[str]
    ObjectKeyPrefix: Optional[str]
    Position: Optional[float]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Action"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            ObjectKeyPrefix=json_data.get("ObjectKeyPrefix"),
            Position=json_data.get("Position"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Action = S3Action


@dataclass
class SnsAction:
    Position: Optional[float]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsAction"]:
        if not json_data:
            return None
        return cls(
            Position=json_data.get("Position"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsAction = SnsAction


@dataclass
class StopAction:
    Position: Optional[float]
    Scope: Optional[str]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StopAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StopAction"]:
        if not json_data:
            return None
        return cls(
            Position=json_data.get("Position"),
            Scope=json_data.get("Scope"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StopAction = StopAction


@dataclass
class WorkmailAction:
    OrganizationArn: Optional[str]
    Position: Optional[float]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkmailAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkmailAction"]:
        if not json_data:
            return None
        return cls(
            OrganizationArn=json_data.get("OrganizationArn"),
            Position=json_data.get("Position"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkmailAction = WorkmailAction


