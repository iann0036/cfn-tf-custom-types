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
    After: Optional[str]
    Arn: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Recipients: Optional[Sequence[str]]
    RuleSetName: Optional[str]
    ScanEnabled: Optional[bool]
    TlsPolicy: Optional[str]
    AddHeaderAction: Optional[Sequence["_AddHeaderActionDefinition"]]
    BounceAction: Optional[Sequence["_BounceActionDefinition"]]
    LambdaAction: Optional[Sequence["_LambdaActionDefinition"]]
    S3Action: Optional[Sequence["_S3ActionDefinition"]]
    SnsAction: Optional[Sequence["_SnsActionDefinition"]]
    StopAction: Optional[Sequence["_StopActionDefinition"]]
    WorkmailAction: Optional[Sequence["_WorkmailActionDefinition"]]

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
            After=json_data.get("After"),
            Arn=json_data.get("Arn"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Recipients=json_data.get("Recipients"),
            RuleSetName=json_data.get("RuleSetName"),
            ScanEnabled=json_data.get("ScanEnabled"),
            TlsPolicy=json_data.get("TlsPolicy"),
            AddHeaderAction=deserialize_list(json_data.get("AddHeaderAction"), AddHeaderActionDefinition),
            BounceAction=deserialize_list(json_data.get("BounceAction"), BounceActionDefinition),
            LambdaAction=deserialize_list(json_data.get("LambdaAction"), LambdaActionDefinition),
            S3Action=deserialize_list(json_data.get("S3Action"), S3ActionDefinition),
            SnsAction=deserialize_list(json_data.get("SnsAction"), SnsActionDefinition),
            StopAction=deserialize_list(json_data.get("StopAction"), StopActionDefinition),
            WorkmailAction=deserialize_list(json_data.get("WorkmailAction"), WorkmailActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddHeaderActionDefinition(BaseModel):
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    Position: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AddHeaderActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddHeaderActionDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            Position=json_data.get("Position"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddHeaderActionDefinition = AddHeaderActionDefinition


@dataclass
class BounceActionDefinition(BaseModel):
    Message: Optional[str]
    Position: Optional[float]
    Sender: Optional[str]
    SmtpReplyCode: Optional[str]
    StatusCode: Optional[str]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BounceActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BounceActionDefinition"]:
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
_BounceActionDefinition = BounceActionDefinition


@dataclass
class LambdaActionDefinition(BaseModel):
    FunctionArn: Optional[str]
    InvocationType: Optional[str]
    Position: Optional[float]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaActionDefinition"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
            InvocationType=json_data.get("InvocationType"),
            Position=json_data.get("Position"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaActionDefinition = LambdaActionDefinition


@dataclass
class S3ActionDefinition(BaseModel):
    BucketName: Optional[str]
    KmsKeyArn: Optional[str]
    ObjectKeyPrefix: Optional[str]
    Position: Optional[float]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ActionDefinition"]:
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
_S3ActionDefinition = S3ActionDefinition


@dataclass
class SnsActionDefinition(BaseModel):
    Encoding: Optional[str]
    Position: Optional[float]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Encoding=json_data.get("Encoding"),
            Position=json_data.get("Position"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsActionDefinition = SnsActionDefinition


@dataclass
class StopActionDefinition(BaseModel):
    Position: Optional[float]
    Scope: Optional[str]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StopActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StopActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Position=json_data.get("Position"),
            Scope=json_data.get("Scope"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StopActionDefinition = StopActionDefinition


@dataclass
class WorkmailActionDefinition(BaseModel):
    OrganizationArn: Optional[str]
    Position: Optional[float]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkmailActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkmailActionDefinition"]:
        if not json_data:
            return None
        return cls(
            OrganizationArn=json_data.get("OrganizationArn"),
            Position=json_data.get("Position"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkmailActionDefinition = WorkmailActionDefinition


