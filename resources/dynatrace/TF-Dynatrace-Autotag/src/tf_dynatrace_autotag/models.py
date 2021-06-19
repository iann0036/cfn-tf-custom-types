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
    Id: Optional[str]
    Name: Optional[str]
    Unknowns: Optional[str]
    EntitySelectorBasedRule: Optional[Sequence["_EntitySelectorBasedRuleDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
            EntitySelectorBasedRule=deserialize_list(json_data.get("EntitySelectorBasedRule"), EntitySelectorBasedRuleDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EntitySelectorBasedRuleDefinition(BaseModel):
    Enabled: Optional[bool]
    Selector: Optional[str]
    Unknowns: Optional[str]
    ValueFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntitySelectorBasedRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntitySelectorBasedRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Selector=json_data.get("Selector"),
            Unknowns=json_data.get("Unknowns"),
            ValueFormat=json_data.get("ValueFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntitySelectorBasedRuleDefinition = EntitySelectorBasedRuleDefinition


@dataclass
class MetadataDefinition(BaseModel):
    ClusterVersion: Optional[str]
    ConfigurationVersions: Optional[Sequence[float]]
    CurrentConfigurationVersions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterVersion=json_data.get("ClusterVersion"),
            ConfigurationVersions=json_data.get("ConfigurationVersions"),
            CurrentConfigurationVersions=json_data.get("CurrentConfigurationVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class RulesDefinition(BaseModel):
    Enabled: Optional[bool]
    PropagationTypes: Optional[Sequence[str]]
    Type: Optional[str]
    Unknowns: Optional[str]
    ValueFormat: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            PropagationTypes=json_data.get("PropagationTypes"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            ValueFormat=json_data.get("ValueFormat"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    Unknowns: Optional[str]
    ApplicationType: Optional[Sequence["_ApplicationTypeDefinition"]]
    ApplicationTypeComparison: Optional[Sequence["_ApplicationTypeComparisonDefinition"]]
    AzureComputeMode: Optional[Sequence["_AzureComputeModeDefinition"]]
    AzureComputeModeComparison: Optional[Sequence["_AzureComputeModeComparisonDefinition"]]
    AzureSku: Optional[Sequence["_AzureSkuDefinition"]]
    AzureSkuComparision: Optional[Sequence["_AzureSkuComparisionDefinition"]]
    BaseComparisonBasic: Optional[Sequence["_BaseComparisonBasicDefinition"]]
    BaseConditionKey: Optional[Sequence["_BaseConditionKeyDefinition"]]
    Bitness: Optional[Sequence["_BitnessDefinition"]]
    BitnessComparision: Optional[Sequence["_BitnessComparisionDefinition"]]
    CloudType: Optional[Sequence["_CloudTypeDefinition"]]
    CloudTypeComparison: Optional[Sequence["_CloudTypeComparisonDefinition"]]
    Comparison: Optional[Sequence["_ComparisonDefinition"]]
    CustomApplicationType: Optional[Sequence["_CustomApplicationTypeDefinition"]]
    CustomApplicationTypeComparison: Optional[Sequence["_CustomApplicationTypeComparisonDefinition"]]
    CustomHostMetadata: Optional[Sequence["_CustomHostMetadataDefinition"]]
    CustomHostMetadataConditionKey: Optional[Sequence["_CustomHostMetadataConditionKeyDefinition"]]
    CustomProcessMetadata: Optional[Sequence["_CustomProcessMetadataDefinition"]]
    CustomProcessMetadataConditionKey: Optional[Sequence["_CustomProcessMetadataConditionKeyDefinition"]]
    DatabaseTopology: Optional[Sequence["_DatabaseTopologyDefinition"]]
    DatabaseTopologyComparison: Optional[Sequence["_DatabaseTopologyComparisonDefinition"]]
    DcrumDecoder: Optional[Sequence["_DcrumDecoderDefinition"]]
    DcrumDecoderComparison: Optional[Sequence["_DcrumDecoderComparisonDefinition"]]
    Entity: Optional[Sequence["_EntityDefinition"]]
    EntityIdComparison: Optional[Sequence["_EntityIdComparisonDefinition"]]
    HostTech: Optional[Sequence["_HostTechDefinition"]]
    Hypervisor: Optional[Sequence["_HypervisorDefinition"]]
    HypervisorTypeComparision: Optional[Sequence["_HypervisorTypeComparisionDefinition"]]
    IndexedName: Optional[Sequence["_IndexedNameDefinition"]]
    IndexedNameComparison: Optional[Sequence["_IndexedNameComparisonDefinition"]]
    IndexedString: Optional[Sequence["_IndexedStringDefinition"]]
    IndexedStringComparison: Optional[Sequence["_IndexedStringComparisonDefinition"]]
    IndexedTag: Optional[Sequence["_IndexedTagDefinition"]]
    IndexedTagComparison: Optional[Sequence["_IndexedTagComparisonDefinition"]]
    Integer: Optional[Sequence["_IntegerDefinition"]]
    IntegerComparison: Optional[Sequence["_IntegerComparisonDefinition"]]
    Ipaddress: Optional[Sequence["_IpaddressDefinition"]]
    IpaddressComparison: Optional[Sequence["_IpaddressComparisonDefinition"]]
    Key: Optional[Sequence["_KeyDefinition"]]
    MobilePlatform: Optional[Sequence["_MobilePlatformDefinition"]]
    MobilePlatformComparison: Optional[Sequence["_MobilePlatformComparisonDefinition"]]
    OsArch: Optional[Sequence["_OsArchDefinition"]]
    OsType: Optional[Sequence["_OsTypeDefinition"]]
    OsarchitectureComparison: Optional[Sequence["_OsarchitectureComparisonDefinition"]]
    OstypeComparison: Optional[Sequence["_OstypeComparisonDefinition"]]
    PaasType: Optional[Sequence["_PaasTypeDefinition"]]
    PaasTypeComparison: Optional[Sequence["_PaasTypeComparisonDefinition"]]
    ProcessMetadata: Optional[Sequence["_ProcessMetadataDefinition"]]
    ProcessMetadataConditionKey: Optional[Sequence["_ProcessMetadataConditionKeyDefinition"]]
    ServiceTopology: Optional[Sequence["_ServiceTopologyDefinition"]]
    ServiceTopologyComparison: Optional[Sequence["_ServiceTopologyComparisonDefinition"]]
    ServiceType: Optional[Sequence["_ServiceTypeDefinition"]]
    ServiceTypeComparison: Optional[Sequence["_ServiceTypeComparisonDefinition"]]
    SimpleHostTechComparison: Optional[Sequence["_SimpleHostTechComparisonDefinition"]]
    SimpleTechComparison: Optional[Sequence["_SimpleTechComparisonDefinition"]]
    String: Optional[Sequence["_StringDefinition"]]
    StringComparison: Optional[Sequence["_StringComparisonDefinition"]]
    StringConditionKey: Optional[Sequence["_StringConditionKeyDefinition"]]
    StringKey: Optional[Sequence["_StringKeyDefinition"]]
    SyntheticEngine: Optional[Sequence["_SyntheticEngineDefinition"]]
    SyntheticEngineTypeComparison: Optional[Sequence["_SyntheticEngineTypeComparisonDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    TagComparison: Optional[Sequence["_TagComparisonDefinition"]]
    Tech: Optional[Sequence["_TechDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            ApplicationType=deserialize_list(json_data.get("ApplicationType"), ApplicationTypeDefinition),
            ApplicationTypeComparison=deserialize_list(json_data.get("ApplicationTypeComparison"), ApplicationTypeComparisonDefinition),
            AzureComputeMode=deserialize_list(json_data.get("AzureComputeMode"), AzureComputeModeDefinition),
            AzureComputeModeComparison=deserialize_list(json_data.get("AzureComputeModeComparison"), AzureComputeModeComparisonDefinition),
            AzureSku=deserialize_list(json_data.get("AzureSku"), AzureSkuDefinition),
            AzureSkuComparision=deserialize_list(json_data.get("AzureSkuComparision"), AzureSkuComparisionDefinition),
            BaseComparisonBasic=deserialize_list(json_data.get("BaseComparisonBasic"), BaseComparisonBasicDefinition),
            BaseConditionKey=deserialize_list(json_data.get("BaseConditionKey"), BaseConditionKeyDefinition),
            Bitness=deserialize_list(json_data.get("Bitness"), BitnessDefinition),
            BitnessComparision=deserialize_list(json_data.get("BitnessComparision"), BitnessComparisionDefinition),
            CloudType=deserialize_list(json_data.get("CloudType"), CloudTypeDefinition),
            CloudTypeComparison=deserialize_list(json_data.get("CloudTypeComparison"), CloudTypeComparisonDefinition),
            Comparison=deserialize_list(json_data.get("Comparison"), ComparisonDefinition),
            CustomApplicationType=deserialize_list(json_data.get("CustomApplicationType"), CustomApplicationTypeDefinition),
            CustomApplicationTypeComparison=deserialize_list(json_data.get("CustomApplicationTypeComparison"), CustomApplicationTypeComparisonDefinition),
            CustomHostMetadata=deserialize_list(json_data.get("CustomHostMetadata"), CustomHostMetadataDefinition),
            CustomHostMetadataConditionKey=deserialize_list(json_data.get("CustomHostMetadataConditionKey"), CustomHostMetadataConditionKeyDefinition),
            CustomProcessMetadata=deserialize_list(json_data.get("CustomProcessMetadata"), CustomProcessMetadataDefinition),
            CustomProcessMetadataConditionKey=deserialize_list(json_data.get("CustomProcessMetadataConditionKey"), CustomProcessMetadataConditionKeyDefinition),
            DatabaseTopology=deserialize_list(json_data.get("DatabaseTopology"), DatabaseTopologyDefinition),
            DatabaseTopologyComparison=deserialize_list(json_data.get("DatabaseTopologyComparison"), DatabaseTopologyComparisonDefinition),
            DcrumDecoder=deserialize_list(json_data.get("DcrumDecoder"), DcrumDecoderDefinition),
            DcrumDecoderComparison=deserialize_list(json_data.get("DcrumDecoderComparison"), DcrumDecoderComparisonDefinition),
            Entity=deserialize_list(json_data.get("Entity"), EntityDefinition),
            EntityIdComparison=deserialize_list(json_data.get("EntityIdComparison"), EntityIdComparisonDefinition),
            HostTech=deserialize_list(json_data.get("HostTech"), HostTechDefinition),
            Hypervisor=deserialize_list(json_data.get("Hypervisor"), HypervisorDefinition),
            HypervisorTypeComparision=deserialize_list(json_data.get("HypervisorTypeComparision"), HypervisorTypeComparisionDefinition),
            IndexedName=deserialize_list(json_data.get("IndexedName"), IndexedNameDefinition),
            IndexedNameComparison=deserialize_list(json_data.get("IndexedNameComparison"), IndexedNameComparisonDefinition),
            IndexedString=deserialize_list(json_data.get("IndexedString"), IndexedStringDefinition),
            IndexedStringComparison=deserialize_list(json_data.get("IndexedStringComparison"), IndexedStringComparisonDefinition),
            IndexedTag=deserialize_list(json_data.get("IndexedTag"), IndexedTagDefinition),
            IndexedTagComparison=deserialize_list(json_data.get("IndexedTagComparison"), IndexedTagComparisonDefinition),
            Integer=deserialize_list(json_data.get("Integer"), IntegerDefinition),
            IntegerComparison=deserialize_list(json_data.get("IntegerComparison"), IntegerComparisonDefinition),
            Ipaddress=deserialize_list(json_data.get("Ipaddress"), IpaddressDefinition),
            IpaddressComparison=deserialize_list(json_data.get("IpaddressComparison"), IpaddressComparisonDefinition),
            Key=deserialize_list(json_data.get("Key"), KeyDefinition),
            MobilePlatform=deserialize_list(json_data.get("MobilePlatform"), MobilePlatformDefinition),
            MobilePlatformComparison=deserialize_list(json_data.get("MobilePlatformComparison"), MobilePlatformComparisonDefinition),
            OsArch=deserialize_list(json_data.get("OsArch"), OsArchDefinition),
            OsType=deserialize_list(json_data.get("OsType"), OsTypeDefinition),
            OsarchitectureComparison=deserialize_list(json_data.get("OsarchitectureComparison"), OsarchitectureComparisonDefinition),
            OstypeComparison=deserialize_list(json_data.get("OstypeComparison"), OstypeComparisonDefinition),
            PaasType=deserialize_list(json_data.get("PaasType"), PaasTypeDefinition),
            PaasTypeComparison=deserialize_list(json_data.get("PaasTypeComparison"), PaasTypeComparisonDefinition),
            ProcessMetadata=deserialize_list(json_data.get("ProcessMetadata"), ProcessMetadataDefinition),
            ProcessMetadataConditionKey=deserialize_list(json_data.get("ProcessMetadataConditionKey"), ProcessMetadataConditionKeyDefinition),
            ServiceTopology=deserialize_list(json_data.get("ServiceTopology"), ServiceTopologyDefinition),
            ServiceTopologyComparison=deserialize_list(json_data.get("ServiceTopologyComparison"), ServiceTopologyComparisonDefinition),
            ServiceType=deserialize_list(json_data.get("ServiceType"), ServiceTypeDefinition),
            ServiceTypeComparison=deserialize_list(json_data.get("ServiceTypeComparison"), ServiceTypeComparisonDefinition),
            SimpleHostTechComparison=deserialize_list(json_data.get("SimpleHostTechComparison"), SimpleHostTechComparisonDefinition),
            SimpleTechComparison=deserialize_list(json_data.get("SimpleTechComparison"), SimpleTechComparisonDefinition),
            String=deserialize_list(json_data.get("String"), StringDefinition),
            StringComparison=deserialize_list(json_data.get("StringComparison"), StringComparisonDefinition),
            StringConditionKey=deserialize_list(json_data.get("StringConditionKey"), StringConditionKeyDefinition),
            StringKey=deserialize_list(json_data.get("StringKey"), StringKeyDefinition),
            SyntheticEngine=deserialize_list(json_data.get("SyntheticEngine"), SyntheticEngineDefinition),
            SyntheticEngineTypeComparison=deserialize_list(json_data.get("SyntheticEngineTypeComparison"), SyntheticEngineTypeComparisonDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            TagComparison=deserialize_list(json_data.get("TagComparison"), TagComparisonDefinition),
            Tech=deserialize_list(json_data.get("Tech"), TechDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class ApplicationTypeDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationTypeDefinition = ApplicationTypeDefinition


@dataclass
class ApplicationTypeComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationTypeComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationTypeComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationTypeComparisonDefinition = ApplicationTypeComparisonDefinition


@dataclass
class AzureComputeModeDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureComputeModeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureComputeModeDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureComputeModeDefinition = AzureComputeModeDefinition


@dataclass
class AzureComputeModeComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureComputeModeComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureComputeModeComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureComputeModeComparisonDefinition = AzureComputeModeComparisonDefinition


@dataclass
class AzureSkuDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureSkuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureSkuDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureSkuDefinition = AzureSkuDefinition


@dataclass
class AzureSkuComparisionDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureSkuComparisionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureSkuComparisionDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureSkuComparisionDefinition = AzureSkuComparisionDefinition


@dataclass
class BaseComparisonBasicDefinition(BaseModel):
    Negate: Optional[bool]
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BaseComparisonBasicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaseComparisonBasicDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaseComparisonBasicDefinition = BaseComparisonBasicDefinition


@dataclass
class BaseConditionKeyDefinition(BaseModel):
    Attribute: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BaseConditionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaseConditionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaseConditionKeyDefinition = BaseConditionKeyDefinition


@dataclass
class BitnessDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BitnessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BitnessDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BitnessDefinition = BitnessDefinition


@dataclass
class BitnessComparisionDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BitnessComparisionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BitnessComparisionDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BitnessComparisionDefinition = BitnessComparisionDefinition


@dataclass
class CloudTypeDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudTypeDefinition = CloudTypeDefinition


@dataclass
class CloudTypeComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudTypeComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudTypeComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudTypeComparisonDefinition = CloudTypeComparisonDefinition


@dataclass
class ComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComparisonDefinition = ComparisonDefinition


@dataclass
class CustomApplicationTypeDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomApplicationTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomApplicationTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomApplicationTypeDefinition = CustomApplicationTypeDefinition


@dataclass
class CustomApplicationTypeComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomApplicationTypeComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomApplicationTypeComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomApplicationTypeComparisonDefinition = CustomApplicationTypeComparisonDefinition


@dataclass
class CustomHostMetadataDefinition(BaseModel):
    Attribute: Optional[str]
    Unknowns: Optional[str]
    DynamicKey: Optional[Sequence["_DynamicKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHostMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHostMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Unknowns=json_data.get("Unknowns"),
            DynamicKey=deserialize_list(json_data.get("DynamicKey"), DynamicKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHostMetadataDefinition = CustomHostMetadataDefinition


@dataclass
class DynamicKeyDefinition(BaseModel):
    Key: Optional[str]
    Source: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Source=json_data.get("Source"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicKeyDefinition = DynamicKeyDefinition


@dataclass
class CustomHostMetadataConditionKeyDefinition(BaseModel):
    Attribute: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    DynamicKey: Optional[Sequence["_DynamicKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHostMetadataConditionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHostMetadataConditionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            DynamicKey=deserialize_list(json_data.get("DynamicKey"), DynamicKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHostMetadataConditionKeyDefinition = CustomHostMetadataConditionKeyDefinition


@dataclass
class CustomProcessMetadataDefinition(BaseModel):
    Attribute: Optional[str]
    Unknowns: Optional[str]
    DynamicKey: Optional[Sequence["_DynamicKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomProcessMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomProcessMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Unknowns=json_data.get("Unknowns"),
            DynamicKey=deserialize_list(json_data.get("DynamicKey"), DynamicKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomProcessMetadataDefinition = CustomProcessMetadataDefinition


@dataclass
class CustomProcessMetadataConditionKeyDefinition(BaseModel):
    Attribute: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    DynamicKey: Optional[Sequence["_DynamicKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomProcessMetadataConditionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomProcessMetadataConditionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            DynamicKey=deserialize_list(json_data.get("DynamicKey"), DynamicKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomProcessMetadataConditionKeyDefinition = CustomProcessMetadataConditionKeyDefinition


@dataclass
class DatabaseTopologyDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseTopologyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseTopologyDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseTopologyDefinition = DatabaseTopologyDefinition


@dataclass
class DatabaseTopologyComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseTopologyComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseTopologyComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseTopologyComparisonDefinition = DatabaseTopologyComparisonDefinition


@dataclass
class DcrumDecoderDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DcrumDecoderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DcrumDecoderDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DcrumDecoderDefinition = DcrumDecoderDefinition


@dataclass
class DcrumDecoderComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DcrumDecoderComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DcrumDecoderComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DcrumDecoderComparisonDefinition = DcrumDecoderComparisonDefinition


@dataclass
class EntityDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityDefinition = EntityDefinition


@dataclass
class EntityIdComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntityIdComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityIdComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityIdComparisonDefinition = EntityIdComparisonDefinition


@dataclass
class HostTechDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostTechDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostTechDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostTechDefinition = HostTechDefinition


@dataclass
class ValueDefinition(BaseModel):
    Type: Optional[str]
    Unknowns: Optional[str]
    VerbatimType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            VerbatimType=json_data.get("VerbatimType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueDefinition = ValueDefinition


@dataclass
class HypervisorDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HypervisorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HypervisorDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HypervisorDefinition = HypervisorDefinition


@dataclass
class HypervisorTypeComparisionDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HypervisorTypeComparisionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HypervisorTypeComparisionDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HypervisorTypeComparisionDefinition = HypervisorTypeComparisionDefinition


@dataclass
class IndexedNameDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndexedNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexedNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexedNameDefinition = IndexedNameDefinition


@dataclass
class IndexedNameComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndexedNameComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexedNameComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexedNameComparisonDefinition = IndexedNameComparisonDefinition


@dataclass
class IndexedStringDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndexedStringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexedStringDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexedStringDefinition = IndexedStringDefinition


@dataclass
class IndexedStringComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndexedStringComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexedStringComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexedStringComparisonDefinition = IndexedStringComparisonDefinition


@dataclass
class IndexedTagDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IndexedTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexedTagDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexedTagDefinition = IndexedTagDefinition


@dataclass
class IndexedTagComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IndexedTagComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexedTagComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexedTagComparisonDefinition = IndexedTagComparisonDefinition


@dataclass
class IntegerDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IntegerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegerDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegerDefinition = IntegerDefinition


@dataclass
class IntegerComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IntegerComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegerComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegerComparisonDefinition = IntegerComparisonDefinition


@dataclass
class IpaddressDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpaddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpaddressDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpaddressDefinition = IpaddressDefinition


@dataclass
class IpaddressComparisonDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpaddressComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpaddressComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpaddressComparisonDefinition = IpaddressComparisonDefinition


@dataclass
class KeyDefinition(BaseModel):
    Attribute: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyDefinition = KeyDefinition


@dataclass
class MobilePlatformDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MobilePlatformDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MobilePlatformDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MobilePlatformDefinition = MobilePlatformDefinition


@dataclass
class MobilePlatformComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MobilePlatformComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MobilePlatformComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MobilePlatformComparisonDefinition = MobilePlatformComparisonDefinition


@dataclass
class OsArchDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsArchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsArchDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsArchDefinition = OsArchDefinition


@dataclass
class OsTypeDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsTypeDefinition = OsTypeDefinition


@dataclass
class OsarchitectureComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsarchitectureComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsarchitectureComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsarchitectureComparisonDefinition = OsarchitectureComparisonDefinition


@dataclass
class OstypeComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OstypeComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OstypeComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OstypeComparisonDefinition = OstypeComparisonDefinition


@dataclass
class PaasTypeDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PaasTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PaasTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PaasTypeDefinition = PaasTypeDefinition


@dataclass
class PaasTypeComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PaasTypeComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PaasTypeComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PaasTypeComparisonDefinition = PaasTypeComparisonDefinition


@dataclass
class ProcessMetadataDefinition(BaseModel):
    Attribute: Optional[str]
    DynamicKey: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            DynamicKey=json_data.get("DynamicKey"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessMetadataDefinition = ProcessMetadataDefinition


@dataclass
class ProcessMetadataConditionKeyDefinition(BaseModel):
    Attribute: Optional[str]
    DynamicKey: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessMetadataConditionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessMetadataConditionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            DynamicKey=json_data.get("DynamicKey"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessMetadataConditionKeyDefinition = ProcessMetadataConditionKeyDefinition


@dataclass
class ServiceTopologyDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceTopologyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceTopologyDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceTopologyDefinition = ServiceTopologyDefinition


@dataclass
class ServiceTopologyComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceTopologyComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceTopologyComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceTopologyComparisonDefinition = ServiceTopologyComparisonDefinition


@dataclass
class ServiceTypeDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceTypeDefinition = ServiceTypeDefinition


@dataclass
class ServiceTypeComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceTypeComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceTypeComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceTypeComparisonDefinition = ServiceTypeComparisonDefinition


@dataclass
class SimpleHostTechComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleHostTechComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleHostTechComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleHostTechComparisonDefinition = SimpleHostTechComparisonDefinition


@dataclass
class SimpleTechComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleTechComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleTechComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleTechComparisonDefinition = SimpleTechComparisonDefinition


@dataclass
class StringDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringDefinition = StringDefinition


@dataclass
class StringComparisonDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringComparisonDefinition = StringComparisonDefinition


@dataclass
class StringConditionKeyDefinition(BaseModel):
    Attribute: Optional[str]
    DynamicKey: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringConditionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringConditionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            DynamicKey=json_data.get("DynamicKey"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringConditionKeyDefinition = StringConditionKeyDefinition


@dataclass
class StringKeyDefinition(BaseModel):
    Attribute: Optional[str]
    DynamicKey: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            DynamicKey=json_data.get("DynamicKey"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringKeyDefinition = StringKeyDefinition


@dataclass
class SyntheticEngineDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SyntheticEngineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyntheticEngineDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyntheticEngineDefinition = SyntheticEngineDefinition


@dataclass
class SyntheticEngineTypeComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SyntheticEngineTypeComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyntheticEngineTypeComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyntheticEngineTypeComparisonDefinition = SyntheticEngineTypeComparisonDefinition


@dataclass
class TagDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class TagComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagComparisonDefinition = TagComparisonDefinition


@dataclass
class TechDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TechDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TechDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TechDefinition = TechDefinition


