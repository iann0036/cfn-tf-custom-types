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
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    PlatformDisplayName: Optional[str]
    PlatformId: Optional[str]
    RevocationRecord: Optional[Sequence["_RevocationRecordDefinition"]]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Version: Optional[str]
    VersionArn: Optional[str]
    SignatureValidityPeriod: Optional[Sequence["_SignatureValidityPeriodDefinition"]]

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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            PlatformDisplayName=json_data.get("PlatformDisplayName"),
            PlatformId=json_data.get("PlatformId"),
            RevocationRecord=deserialize_list(json_data.get("RevocationRecord"), RevocationRecordDefinition),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Version=json_data.get("Version"),
            VersionArn=json_data.get("VersionArn"),
            SignatureValidityPeriod=deserialize_list(json_data.get("SignatureValidityPeriod"), SignatureValidityPeriodDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RevocationRecordDefinition(BaseModel):
    RevocationEffectiveFrom: Optional[str]
    RevokedAt: Optional[str]
    RevokedBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RevocationRecordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevocationRecordDefinition"]:
        if not json_data:
            return None
        return cls(
            RevocationEffectiveFrom=json_data.get("RevocationEffectiveFrom"),
            RevokedAt=json_data.get("RevokedAt"),
            RevokedBy=json_data.get("RevokedBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevocationRecordDefinition = RevocationRecordDefinition


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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class SignatureValidityPeriodDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SignatureValidityPeriodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignatureValidityPeriodDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignatureValidityPeriodDefinition = SignatureValidityPeriodDefinition


