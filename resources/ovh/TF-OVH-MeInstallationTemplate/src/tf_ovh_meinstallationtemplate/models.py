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
    AvailableLanguages: Optional[Sequence[str]]
    BaseTemplateName: Optional[str]
    Beta: Optional[bool]
    BitFormat: Optional[float]
    Category: Optional[str]
    DefaultLanguage: Optional[str]
    Deprecated: Optional[bool]
    Description: Optional[str]
    Distribution: Optional[str]
    Family: Optional[str]
    Filesystems: Optional[Sequence[str]]
    HardRaidConfiguration: Optional[bool]
    Id: Optional[str]
    LastModification: Optional[str]
    LvmReady: Optional[bool]
    RemoveDefaultPartitionSchemes: Optional[bool]
    SupportsDistributionKernel: Optional[bool]
    SupportsGptLabel: Optional[bool]
    SupportsRtm: Optional[bool]
    SupportsSqlServer: Optional[bool]
    SupportsUefi: Optional[str]
    TemplateName: Optional[str]
    Customization: Optional[Sequence["_CustomizationDefinition"]]

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
            AvailableLanguages=json_data.get("AvailableLanguages"),
            BaseTemplateName=json_data.get("BaseTemplateName"),
            Beta=json_data.get("Beta"),
            BitFormat=json_data.get("BitFormat"),
            Category=json_data.get("Category"),
            DefaultLanguage=json_data.get("DefaultLanguage"),
            Deprecated=json_data.get("Deprecated"),
            Description=json_data.get("Description"),
            Distribution=json_data.get("Distribution"),
            Family=json_data.get("Family"),
            Filesystems=json_data.get("Filesystems"),
            HardRaidConfiguration=json_data.get("HardRaidConfiguration"),
            Id=json_data.get("Id"),
            LastModification=json_data.get("LastModification"),
            LvmReady=json_data.get("LvmReady"),
            RemoveDefaultPartitionSchemes=json_data.get("RemoveDefaultPartitionSchemes"),
            SupportsDistributionKernel=json_data.get("SupportsDistributionKernel"),
            SupportsGptLabel=json_data.get("SupportsGptLabel"),
            SupportsRtm=json_data.get("SupportsRtm"),
            SupportsSqlServer=json_data.get("SupportsSqlServer"),
            SupportsUefi=json_data.get("SupportsUefi"),
            TemplateName=json_data.get("TemplateName"),
            Customization=deserialize_list(json_data.get("Customization"), CustomizationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomizationDefinition(BaseModel):
    ChangeLog: Optional[str]
    CustomHostname: Optional[str]
    PostInstallationScriptLink: Optional[str]
    PostInstallationScriptReturn: Optional[str]
    Rating: Optional[float]
    SshKeyName: Optional[str]
    UseDistributionKernel: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizationDefinition"]:
        if not json_data:
            return None
        return cls(
            ChangeLog=json_data.get("ChangeLog"),
            CustomHostname=json_data.get("CustomHostname"),
            PostInstallationScriptLink=json_data.get("PostInstallationScriptLink"),
            PostInstallationScriptReturn=json_data.get("PostInstallationScriptReturn"),
            Rating=json_data.get("Rating"),
            SshKeyName=json_data.get("SshKeyName"),
            UseDistributionKernel=json_data.get("UseDistributionKernel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizationDefinition = CustomizationDefinition


