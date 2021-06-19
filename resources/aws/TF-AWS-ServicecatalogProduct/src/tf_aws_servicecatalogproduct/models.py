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
    AcceptLanguage: Optional[str]
    Arn: Optional[str]
    CreatedTime: Optional[str]
    Description: Optional[str]
    Distributor: Optional[str]
    HasDefaultPath: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    Status: Optional[str]
    SupportDescription: Optional[str]
    SupportEmail: Optional[str]
    SupportUrl: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]
    ProvisioningArtifactParameters: Optional[Sequence["_ProvisioningArtifactParametersDefinition"]]

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
            AcceptLanguage=json_data.get("AcceptLanguage"),
            Arn=json_data.get("Arn"),
            CreatedTime=json_data.get("CreatedTime"),
            Description=json_data.get("Description"),
            Distributor=json_data.get("Distributor"),
            HasDefaultPath=json_data.get("HasDefaultPath"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Status=json_data.get("Status"),
            SupportDescription=json_data.get("SupportDescription"),
            SupportEmail=json_data.get("SupportEmail"),
            SupportUrl=json_data.get("SupportUrl"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
            ProvisioningArtifactParameters=deserialize_list(json_data.get("ProvisioningArtifactParameters"), ProvisioningArtifactParametersDefinition),
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
class ProvisioningArtifactParametersDefinition(BaseModel):
    Description: Optional[str]
    DisableTemplateValidation: Optional[bool]
    Name: Optional[str]
    TemplatePhysicalId: Optional[str]
    TemplateUrl: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisioningArtifactParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisioningArtifactParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DisableTemplateValidation=json_data.get("DisableTemplateValidation"),
            Name=json_data.get("Name"),
            TemplatePhysicalId=json_data.get("TemplatePhysicalId"),
            TemplateUrl=json_data.get("TemplateUrl"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisioningArtifactParametersDefinition = ProvisioningArtifactParametersDefinition


