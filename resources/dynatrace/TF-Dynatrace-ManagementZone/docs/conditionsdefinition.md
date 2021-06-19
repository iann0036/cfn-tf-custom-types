# TF::Dynatrace::ManagementZone ConditionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#applicationtype" title="ApplicationType">ApplicationType</a>" : <i>[ <a href="applicationtypedefinition.md">ApplicationTypeDefinition</a>, ... ]</i>,
    "<a href="#applicationtypecomparison" title="ApplicationTypeComparison">ApplicationTypeComparison</a>" : <i>[ <a href="applicationtypecomparisondefinition.md">ApplicationTypeComparisonDefinition</a>, ... ]</i>,
    "<a href="#azurecomputemode" title="AzureComputeMode">AzureComputeMode</a>" : <i>[ <a href="azurecomputemodedefinition.md">AzureComputeModeDefinition</a>, ... ]</i>,
    "<a href="#azurecomputemodecomparison" title="AzureComputeModeComparison">AzureComputeModeComparison</a>" : <i>[ <a href="azurecomputemodecomparisondefinition.md">AzureComputeModeComparisonDefinition</a>, ... ]</i>,
    "<a href="#azuresku" title="AzureSku">AzureSku</a>" : <i>[ <a href="azureskudefinition.md">AzureSkuDefinition</a>, ... ]</i>,
    "<a href="#azureskucomparision" title="AzureSkuComparision">AzureSkuComparision</a>" : <i>[ <a href="azureskucomparisiondefinition.md">AzureSkuComparisionDefinition</a>, ... ]</i>,
    "<a href="#basecomparisonbasic" title="BaseComparisonBasic">BaseComparisonBasic</a>" : <i>[ <a href="basecomparisonbasicdefinition.md">BaseComparisonBasicDefinition</a>, ... ]</i>,
    "<a href="#baseconditionkey" title="BaseConditionKey">BaseConditionKey</a>" : <i>[ <a href="baseconditionkeydefinition.md">BaseConditionKeyDefinition</a>, ... ]</i>,
    "<a href="#bitness" title="Bitness">Bitness</a>" : <i>[ <a href="bitnessdefinition.md">BitnessDefinition</a>, ... ]</i>,
    "<a href="#bitnesscomparision" title="BitnessComparision">BitnessComparision</a>" : <i>[ <a href="bitnesscomparisiondefinition.md">BitnessComparisionDefinition</a>, ... ]</i>,
    "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>[ <a href="cloudtypedefinition.md">CloudTypeDefinition</a>, ... ]</i>,
    "<a href="#cloudtypecomparison" title="CloudTypeComparison">CloudTypeComparison</a>" : <i>[ <a href="cloudtypecomparisondefinition.md">CloudTypeComparisonDefinition</a>, ... ]</i>,
    "<a href="#comparison" title="Comparison">Comparison</a>" : <i>[ <a href="comparisondefinition.md">ComparisonDefinition</a>, ... ]</i>,
    "<a href="#customapplicationtype" title="CustomApplicationType">CustomApplicationType</a>" : <i>[ <a href="customapplicationtypedefinition.md">CustomApplicationTypeDefinition</a>, ... ]</i>,
    "<a href="#customapplicationtypecomparison" title="CustomApplicationTypeComparison">CustomApplicationTypeComparison</a>" : <i>[ <a href="customapplicationtypecomparisondefinition.md">CustomApplicationTypeComparisonDefinition</a>, ... ]</i>,
    "<a href="#customhostmetadata" title="CustomHostMetadata">CustomHostMetadata</a>" : <i>[ <a href="customhostmetadatadefinition.md">CustomHostMetadataDefinition</a>, ... ]</i>,
    "<a href="#customhostmetadataconditionkey" title="CustomHostMetadataConditionKey">CustomHostMetadataConditionKey</a>" : <i>[ <a href="customhostmetadataconditionkeydefinition.md">CustomHostMetadataConditionKeyDefinition</a>, ... ]</i>,
    "<a href="#customprocessmetadata" title="CustomProcessMetadata">CustomProcessMetadata</a>" : <i>[ <a href="customprocessmetadatadefinition.md">CustomProcessMetadataDefinition</a>, ... ]</i>,
    "<a href="#customprocessmetadataconditionkey" title="CustomProcessMetadataConditionKey">CustomProcessMetadataConditionKey</a>" : <i>[ <a href="customprocessmetadataconditionkeydefinition.md">CustomProcessMetadataConditionKeyDefinition</a>, ... ]</i>,
    "<a href="#databasetopology" title="DatabaseTopology">DatabaseTopology</a>" : <i>[ <a href="databasetopologydefinition.md">DatabaseTopologyDefinition</a>, ... ]</i>,
    "<a href="#databasetopologycomparison" title="DatabaseTopologyComparison">DatabaseTopologyComparison</a>" : <i>[ <a href="databasetopologycomparisondefinition.md">DatabaseTopologyComparisonDefinition</a>, ... ]</i>,
    "<a href="#dcrumdecoder" title="DcrumDecoder">DcrumDecoder</a>" : <i>[ <a href="dcrumdecoderdefinition.md">DcrumDecoderDefinition</a>, ... ]</i>,
    "<a href="#dcrumdecodercomparison" title="DcrumDecoderComparison">DcrumDecoderComparison</a>" : <i>[ <a href="dcrumdecodercomparisondefinition.md">DcrumDecoderComparisonDefinition</a>, ... ]</i>,
    "<a href="#entity" title="Entity">Entity</a>" : <i>[ <a href="entitydefinition.md">EntityDefinition</a>, ... ]</i>,
    "<a href="#entityidcomparison" title="EntityIdComparison">EntityIdComparison</a>" : <i>[ <a href="entityidcomparisondefinition.md">EntityIdComparisonDefinition</a>, ... ]</i>,
    "<a href="#hosttech" title="HostTech">HostTech</a>" : <i>[ <a href="hosttechdefinition.md">HostTechDefinition</a>, ... ]</i>,
    "<a href="#hypervisor" title="Hypervisor">Hypervisor</a>" : <i>[ <a href="hypervisordefinition.md">HypervisorDefinition</a>, ... ]</i>,
    "<a href="#hypervisortypecomparision" title="HypervisorTypeComparision">HypervisorTypeComparision</a>" : <i>[ <a href="hypervisortypecomparisiondefinition.md">HypervisorTypeComparisionDefinition</a>, ... ]</i>,
    "<a href="#indexedname" title="IndexedName">IndexedName</a>" : <i>[ <a href="indexednamedefinition.md">IndexedNameDefinition</a>, ... ]</i>,
    "<a href="#indexednamecomparison" title="IndexedNameComparison">IndexedNameComparison</a>" : <i>[ <a href="indexednamecomparisondefinition.md">IndexedNameComparisonDefinition</a>, ... ]</i>,
    "<a href="#indexedstring" title="IndexedString">IndexedString</a>" : <i>[ <a href="indexedstringdefinition.md">IndexedStringDefinition</a>, ... ]</i>,
    "<a href="#indexedstringcomparison" title="IndexedStringComparison">IndexedStringComparison</a>" : <i>[ <a href="indexedstringcomparisondefinition.md">IndexedStringComparisonDefinition</a>, ... ]</i>,
    "<a href="#indexedtag" title="IndexedTag">IndexedTag</a>" : <i>[ <a href="indexedtagdefinition.md">IndexedTagDefinition</a>, ... ]</i>,
    "<a href="#indexedtagcomparison" title="IndexedTagComparison">IndexedTagComparison</a>" : <i>[ <a href="indexedtagcomparisondefinition.md">IndexedTagComparisonDefinition</a>, ... ]</i>,
    "<a href="#integer" title="Integer">Integer</a>" : <i>[ <a href="integerdefinition.md">IntegerDefinition</a>, ... ]</i>,
    "<a href="#integercomparison" title="IntegerComparison">IntegerComparison</a>" : <i>[ <a href="integercomparisondefinition.md">IntegerComparisonDefinition</a>, ... ]</i>,
    "<a href="#ipaddress" title="Ipaddress">Ipaddress</a>" : <i>[ <a href="ipaddressdefinition.md">IpaddressDefinition</a>, ... ]</i>,
    "<a href="#ipaddresscomparison" title="IpaddressComparison">IpaddressComparison</a>" : <i>[ <a href="ipaddresscomparisondefinition.md">IpaddressComparisonDefinition</a>, ... ]</i>,
    "<a href="#key" title="Key">Key</a>" : <i>[ <a href="keydefinition.md">KeyDefinition</a>, ... ]</i>,
    "<a href="#mobileplatform" title="MobilePlatform">MobilePlatform</a>" : <i>[ <a href="mobileplatformdefinition.md">MobilePlatformDefinition</a>, ... ]</i>,
    "<a href="#mobileplatformcomparison" title="MobilePlatformComparison">MobilePlatformComparison</a>" : <i>[ <a href="mobileplatformcomparisondefinition.md">MobilePlatformComparisonDefinition</a>, ... ]</i>,
    "<a href="#osarch" title="OsArch">OsArch</a>" : <i>[ <a href="osarchdefinition.md">OsArchDefinition</a>, ... ]</i>,
    "<a href="#ostype" title="OsType">OsType</a>" : <i>[ <a href="ostypedefinition.md">OsTypeDefinition</a>, ... ]</i>,
    "<a href="#osarchitecturecomparison" title="OsarchitectureComparison">OsarchitectureComparison</a>" : <i>[ <a href="osarchitecturecomparisondefinition.md">OsarchitectureComparisonDefinition</a>, ... ]</i>,
    "<a href="#ostypecomparison" title="OstypeComparison">OstypeComparison</a>" : <i>[ <a href="ostypecomparisondefinition.md">OstypeComparisonDefinition</a>, ... ]</i>,
    "<a href="#paastype" title="PaasType">PaasType</a>" : <i>[ <a href="paastypedefinition.md">PaasTypeDefinition</a>, ... ]</i>,
    "<a href="#paastypecomparison" title="PaasTypeComparison">PaasTypeComparison</a>" : <i>[ <a href="paastypecomparisondefinition.md">PaasTypeComparisonDefinition</a>, ... ]</i>,
    "<a href="#processmetadata" title="ProcessMetadata">ProcessMetadata</a>" : <i>[ <a href="processmetadatadefinition.md">ProcessMetadataDefinition</a>, ... ]</i>,
    "<a href="#processmetadataconditionkey" title="ProcessMetadataConditionKey">ProcessMetadataConditionKey</a>" : <i>[ <a href="processmetadataconditionkeydefinition.md">ProcessMetadataConditionKeyDefinition</a>, ... ]</i>,
    "<a href="#servicetopology" title="ServiceTopology">ServiceTopology</a>" : <i>[ <a href="servicetopologydefinition.md">ServiceTopologyDefinition</a>, ... ]</i>,
    "<a href="#servicetopologycomparison" title="ServiceTopologyComparison">ServiceTopologyComparison</a>" : <i>[ <a href="servicetopologycomparisondefinition.md">ServiceTopologyComparisonDefinition</a>, ... ]</i>,
    "<a href="#servicetype" title="ServiceType">ServiceType</a>" : <i>[ <a href="servicetypedefinition.md">ServiceTypeDefinition</a>, ... ]</i>,
    "<a href="#servicetypecomparison" title="ServiceTypeComparison">ServiceTypeComparison</a>" : <i>[ <a href="servicetypecomparisondefinition.md">ServiceTypeComparisonDefinition</a>, ... ]</i>,
    "<a href="#simplehosttechcomparison" title="SimpleHostTechComparison">SimpleHostTechComparison</a>" : <i>[ <a href="simplehosttechcomparisondefinition.md">SimpleHostTechComparisonDefinition</a>, ... ]</i>,
    "<a href="#simpletechcomparison" title="SimpleTechComparison">SimpleTechComparison</a>" : <i>[ <a href="simpletechcomparisondefinition.md">SimpleTechComparisonDefinition</a>, ... ]</i>,
    "<a href="#string" title="String">String</a>" : <i>[ <a href="stringdefinition.md">StringDefinition</a>, ... ]</i>,
    "<a href="#stringcomparison" title="StringComparison">StringComparison</a>" : <i>[ <a href="stringcomparisondefinition.md">StringComparisonDefinition</a>, ... ]</i>,
    "<a href="#stringconditionkey" title="StringConditionKey">StringConditionKey</a>" : <i>[ <a href="stringconditionkeydefinition.md">StringConditionKeyDefinition</a>, ... ]</i>,
    "<a href="#stringkey" title="StringKey">StringKey</a>" : <i>[ <a href="stringkeydefinition.md">StringKeyDefinition</a>, ... ]</i>,
    "<a href="#syntheticengine" title="SyntheticEngine">SyntheticEngine</a>" : <i>[ <a href="syntheticenginedefinition.md">SyntheticEngineDefinition</a>, ... ]</i>,
    "<a href="#syntheticenginetypecomparison" title="SyntheticEngineTypeComparison">SyntheticEngineTypeComparison</a>" : <i>[ <a href="syntheticenginetypecomparisondefinition.md">SyntheticEngineTypeComparisonDefinition</a>, ... ]</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>,
    "<a href="#tagcomparison" title="TagComparison">TagComparison</a>" : <i>[ <a href="tagcomparisondefinition.md">TagComparisonDefinition</a>, ... ]</i>,
    "<a href="#tech" title="Tech">Tech</a>" : <i>[ <a href="techdefinition.md">TechDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#applicationtype" title="ApplicationType">ApplicationType</a>: <i>
      - <a href="applicationtypedefinition.md">ApplicationTypeDefinition</a></i>
<a href="#applicationtypecomparison" title="ApplicationTypeComparison">ApplicationTypeComparison</a>: <i>
      - <a href="applicationtypecomparisondefinition.md">ApplicationTypeComparisonDefinition</a></i>
<a href="#azurecomputemode" title="AzureComputeMode">AzureComputeMode</a>: <i>
      - <a href="azurecomputemodedefinition.md">AzureComputeModeDefinition</a></i>
<a href="#azurecomputemodecomparison" title="AzureComputeModeComparison">AzureComputeModeComparison</a>: <i>
      - <a href="azurecomputemodecomparisondefinition.md">AzureComputeModeComparisonDefinition</a></i>
<a href="#azuresku" title="AzureSku">AzureSku</a>: <i>
      - <a href="azureskudefinition.md">AzureSkuDefinition</a></i>
<a href="#azureskucomparision" title="AzureSkuComparision">AzureSkuComparision</a>: <i>
      - <a href="azureskucomparisiondefinition.md">AzureSkuComparisionDefinition</a></i>
<a href="#basecomparisonbasic" title="BaseComparisonBasic">BaseComparisonBasic</a>: <i>
      - <a href="basecomparisonbasicdefinition.md">BaseComparisonBasicDefinition</a></i>
<a href="#baseconditionkey" title="BaseConditionKey">BaseConditionKey</a>: <i>
      - <a href="baseconditionkeydefinition.md">BaseConditionKeyDefinition</a></i>
<a href="#bitness" title="Bitness">Bitness</a>: <i>
      - <a href="bitnessdefinition.md">BitnessDefinition</a></i>
<a href="#bitnesscomparision" title="BitnessComparision">BitnessComparision</a>: <i>
      - <a href="bitnesscomparisiondefinition.md">BitnessComparisionDefinition</a></i>
<a href="#cloudtype" title="CloudType">CloudType</a>: <i>
      - <a href="cloudtypedefinition.md">CloudTypeDefinition</a></i>
<a href="#cloudtypecomparison" title="CloudTypeComparison">CloudTypeComparison</a>: <i>
      - <a href="cloudtypecomparisondefinition.md">CloudTypeComparisonDefinition</a></i>
<a href="#comparison" title="Comparison">Comparison</a>: <i>
      - <a href="comparisondefinition.md">ComparisonDefinition</a></i>
<a href="#customapplicationtype" title="CustomApplicationType">CustomApplicationType</a>: <i>
      - <a href="customapplicationtypedefinition.md">CustomApplicationTypeDefinition</a></i>
<a href="#customapplicationtypecomparison" title="CustomApplicationTypeComparison">CustomApplicationTypeComparison</a>: <i>
      - <a href="customapplicationtypecomparisondefinition.md">CustomApplicationTypeComparisonDefinition</a></i>
<a href="#customhostmetadata" title="CustomHostMetadata">CustomHostMetadata</a>: <i>
      - <a href="customhostmetadatadefinition.md">CustomHostMetadataDefinition</a></i>
<a href="#customhostmetadataconditionkey" title="CustomHostMetadataConditionKey">CustomHostMetadataConditionKey</a>: <i>
      - <a href="customhostmetadataconditionkeydefinition.md">CustomHostMetadataConditionKeyDefinition</a></i>
<a href="#customprocessmetadata" title="CustomProcessMetadata">CustomProcessMetadata</a>: <i>
      - <a href="customprocessmetadatadefinition.md">CustomProcessMetadataDefinition</a></i>
<a href="#customprocessmetadataconditionkey" title="CustomProcessMetadataConditionKey">CustomProcessMetadataConditionKey</a>: <i>
      - <a href="customprocessmetadataconditionkeydefinition.md">CustomProcessMetadataConditionKeyDefinition</a></i>
<a href="#databasetopology" title="DatabaseTopology">DatabaseTopology</a>: <i>
      - <a href="databasetopologydefinition.md">DatabaseTopologyDefinition</a></i>
<a href="#databasetopologycomparison" title="DatabaseTopologyComparison">DatabaseTopologyComparison</a>: <i>
      - <a href="databasetopologycomparisondefinition.md">DatabaseTopologyComparisonDefinition</a></i>
<a href="#dcrumdecoder" title="DcrumDecoder">DcrumDecoder</a>: <i>
      - <a href="dcrumdecoderdefinition.md">DcrumDecoderDefinition</a></i>
<a href="#dcrumdecodercomparison" title="DcrumDecoderComparison">DcrumDecoderComparison</a>: <i>
      - <a href="dcrumdecodercomparisondefinition.md">DcrumDecoderComparisonDefinition</a></i>
<a href="#entity" title="Entity">Entity</a>: <i>
      - <a href="entitydefinition.md">EntityDefinition</a></i>
<a href="#entityidcomparison" title="EntityIdComparison">EntityIdComparison</a>: <i>
      - <a href="entityidcomparisondefinition.md">EntityIdComparisonDefinition</a></i>
<a href="#hosttech" title="HostTech">HostTech</a>: <i>
      - <a href="hosttechdefinition.md">HostTechDefinition</a></i>
<a href="#hypervisor" title="Hypervisor">Hypervisor</a>: <i>
      - <a href="hypervisordefinition.md">HypervisorDefinition</a></i>
<a href="#hypervisortypecomparision" title="HypervisorTypeComparision">HypervisorTypeComparision</a>: <i>
      - <a href="hypervisortypecomparisiondefinition.md">HypervisorTypeComparisionDefinition</a></i>
<a href="#indexedname" title="IndexedName">IndexedName</a>: <i>
      - <a href="indexednamedefinition.md">IndexedNameDefinition</a></i>
<a href="#indexednamecomparison" title="IndexedNameComparison">IndexedNameComparison</a>: <i>
      - <a href="indexednamecomparisondefinition.md">IndexedNameComparisonDefinition</a></i>
<a href="#indexedstring" title="IndexedString">IndexedString</a>: <i>
      - <a href="indexedstringdefinition.md">IndexedStringDefinition</a></i>
<a href="#indexedstringcomparison" title="IndexedStringComparison">IndexedStringComparison</a>: <i>
      - <a href="indexedstringcomparisondefinition.md">IndexedStringComparisonDefinition</a></i>
<a href="#indexedtag" title="IndexedTag">IndexedTag</a>: <i>
      - <a href="indexedtagdefinition.md">IndexedTagDefinition</a></i>
<a href="#indexedtagcomparison" title="IndexedTagComparison">IndexedTagComparison</a>: <i>
      - <a href="indexedtagcomparisondefinition.md">IndexedTagComparisonDefinition</a></i>
<a href="#integer" title="Integer">Integer</a>: <i>
      - <a href="integerdefinition.md">IntegerDefinition</a></i>
<a href="#integercomparison" title="IntegerComparison">IntegerComparison</a>: <i>
      - <a href="integercomparisondefinition.md">IntegerComparisonDefinition</a></i>
<a href="#ipaddress" title="Ipaddress">Ipaddress</a>: <i>
      - <a href="ipaddressdefinition.md">IpaddressDefinition</a></i>
<a href="#ipaddresscomparison" title="IpaddressComparison">IpaddressComparison</a>: <i>
      - <a href="ipaddresscomparisondefinition.md">IpaddressComparisonDefinition</a></i>
<a href="#key" title="Key">Key</a>: <i>
      - <a href="keydefinition.md">KeyDefinition</a></i>
<a href="#mobileplatform" title="MobilePlatform">MobilePlatform</a>: <i>
      - <a href="mobileplatformdefinition.md">MobilePlatformDefinition</a></i>
<a href="#mobileplatformcomparison" title="MobilePlatformComparison">MobilePlatformComparison</a>: <i>
      - <a href="mobileplatformcomparisondefinition.md">MobilePlatformComparisonDefinition</a></i>
<a href="#osarch" title="OsArch">OsArch</a>: <i>
      - <a href="osarchdefinition.md">OsArchDefinition</a></i>
<a href="#ostype" title="OsType">OsType</a>: <i>
      - <a href="ostypedefinition.md">OsTypeDefinition</a></i>
<a href="#osarchitecturecomparison" title="OsarchitectureComparison">OsarchitectureComparison</a>: <i>
      - <a href="osarchitecturecomparisondefinition.md">OsarchitectureComparisonDefinition</a></i>
<a href="#ostypecomparison" title="OstypeComparison">OstypeComparison</a>: <i>
      - <a href="ostypecomparisondefinition.md">OstypeComparisonDefinition</a></i>
<a href="#paastype" title="PaasType">PaasType</a>: <i>
      - <a href="paastypedefinition.md">PaasTypeDefinition</a></i>
<a href="#paastypecomparison" title="PaasTypeComparison">PaasTypeComparison</a>: <i>
      - <a href="paastypecomparisondefinition.md">PaasTypeComparisonDefinition</a></i>
<a href="#processmetadata" title="ProcessMetadata">ProcessMetadata</a>: <i>
      - <a href="processmetadatadefinition.md">ProcessMetadataDefinition</a></i>
<a href="#processmetadataconditionkey" title="ProcessMetadataConditionKey">ProcessMetadataConditionKey</a>: <i>
      - <a href="processmetadataconditionkeydefinition.md">ProcessMetadataConditionKeyDefinition</a></i>
<a href="#servicetopology" title="ServiceTopology">ServiceTopology</a>: <i>
      - <a href="servicetopologydefinition.md">ServiceTopologyDefinition</a></i>
<a href="#servicetopologycomparison" title="ServiceTopologyComparison">ServiceTopologyComparison</a>: <i>
      - <a href="servicetopologycomparisondefinition.md">ServiceTopologyComparisonDefinition</a></i>
<a href="#servicetype" title="ServiceType">ServiceType</a>: <i>
      - <a href="servicetypedefinition.md">ServiceTypeDefinition</a></i>
<a href="#servicetypecomparison" title="ServiceTypeComparison">ServiceTypeComparison</a>: <i>
      - <a href="servicetypecomparisondefinition.md">ServiceTypeComparisonDefinition</a></i>
<a href="#simplehosttechcomparison" title="SimpleHostTechComparison">SimpleHostTechComparison</a>: <i>
      - <a href="simplehosttechcomparisondefinition.md">SimpleHostTechComparisonDefinition</a></i>
<a href="#simpletechcomparison" title="SimpleTechComparison">SimpleTechComparison</a>: <i>
      - <a href="simpletechcomparisondefinition.md">SimpleTechComparisonDefinition</a></i>
<a href="#string" title="String">String</a>: <i>
      - <a href="stringdefinition.md">StringDefinition</a></i>
<a href="#stringcomparison" title="StringComparison">StringComparison</a>: <i>
      - <a href="stringcomparisondefinition.md">StringComparisonDefinition</a></i>
<a href="#stringconditionkey" title="StringConditionKey">StringConditionKey</a>: <i>
      - <a href="stringconditionkeydefinition.md">StringConditionKeyDefinition</a></i>
<a href="#stringkey" title="StringKey">StringKey</a>: <i>
      - <a href="stringkeydefinition.md">StringKeyDefinition</a></i>
<a href="#syntheticengine" title="SyntheticEngine">SyntheticEngine</a>: <i>
      - <a href="syntheticenginedefinition.md">SyntheticEngineDefinition</a></i>
<a href="#syntheticenginetypecomparison" title="SyntheticEngineTypeComparison">SyntheticEngineTypeComparison</a>: <i>
      - <a href="syntheticenginetypecomparisondefinition.md">SyntheticEngineTypeComparisonDefinition</a></i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
<a href="#tagcomparison" title="TagComparison">TagComparison</a>: <i>
      - <a href="tagcomparisondefinition.md">TagComparisonDefinition</a></i>
<a href="#tech" title="Tech">Tech</a>: <i>
      - <a href="techdefinition.md">TechDefinition</a></i>
</pre>

## Properties

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationType

_Required_: No

_Type_: List of <a href="applicationtypedefinition.md">ApplicationTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationTypeComparison

_Required_: No

_Type_: List of <a href="applicationtypecomparisondefinition.md">ApplicationTypeComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureComputeMode

_Required_: No

_Type_: List of <a href="azurecomputemodedefinition.md">AzureComputeModeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureComputeModeComparison

_Required_: No

_Type_: List of <a href="azurecomputemodecomparisondefinition.md">AzureComputeModeComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureSku

_Required_: No

_Type_: List of <a href="azureskudefinition.md">AzureSkuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureSkuComparision

_Required_: No

_Type_: List of <a href="azureskucomparisiondefinition.md">AzureSkuComparisionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseComparisonBasic

_Required_: No

_Type_: List of <a href="basecomparisonbasicdefinition.md">BaseComparisonBasicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseConditionKey

_Required_: No

_Type_: List of <a href="baseconditionkeydefinition.md">BaseConditionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bitness

_Required_: No

_Type_: List of <a href="bitnessdefinition.md">BitnessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BitnessComparision

_Required_: No

_Type_: List of <a href="bitnesscomparisiondefinition.md">BitnessComparisionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

_Required_: No

_Type_: List of <a href="cloudtypedefinition.md">CloudTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudTypeComparison

_Required_: No

_Type_: List of <a href="cloudtypecomparisondefinition.md">CloudTypeComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comparison

_Required_: No

_Type_: List of <a href="comparisondefinition.md">ComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomApplicationType

_Required_: No

_Type_: List of <a href="customapplicationtypedefinition.md">CustomApplicationTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomApplicationTypeComparison

_Required_: No

_Type_: List of <a href="customapplicationtypecomparisondefinition.md">CustomApplicationTypeComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHostMetadata

_Required_: No

_Type_: List of <a href="customhostmetadatadefinition.md">CustomHostMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHostMetadataConditionKey

_Required_: No

_Type_: List of <a href="customhostmetadataconditionkeydefinition.md">CustomHostMetadataConditionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProcessMetadata

_Required_: No

_Type_: List of <a href="customprocessmetadatadefinition.md">CustomProcessMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProcessMetadataConditionKey

_Required_: No

_Type_: List of <a href="customprocessmetadataconditionkeydefinition.md">CustomProcessMetadataConditionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseTopology

_Required_: No

_Type_: List of <a href="databasetopologydefinition.md">DatabaseTopologyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseTopologyComparison

_Required_: No

_Type_: List of <a href="databasetopologycomparisondefinition.md">DatabaseTopologyComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DcrumDecoder

_Required_: No

_Type_: List of <a href="dcrumdecoderdefinition.md">DcrumDecoderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DcrumDecoderComparison

_Required_: No

_Type_: List of <a href="dcrumdecodercomparisondefinition.md">DcrumDecoderComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

_Required_: No

_Type_: List of <a href="entitydefinition.md">EntityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityIdComparison

_Required_: No

_Type_: List of <a href="entityidcomparisondefinition.md">EntityIdComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostTech

_Required_: No

_Type_: List of <a href="hosttechdefinition.md">HostTechDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hypervisor

_Required_: No

_Type_: List of <a href="hypervisordefinition.md">HypervisorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HypervisorTypeComparision

_Required_: No

_Type_: List of <a href="hypervisortypecomparisiondefinition.md">HypervisorTypeComparisionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexedName

_Required_: No

_Type_: List of <a href="indexednamedefinition.md">IndexedNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexedNameComparison

_Required_: No

_Type_: List of <a href="indexednamecomparisondefinition.md">IndexedNameComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexedString

_Required_: No

_Type_: List of <a href="indexedstringdefinition.md">IndexedStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexedStringComparison

_Required_: No

_Type_: List of <a href="indexedstringcomparisondefinition.md">IndexedStringComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexedTag

_Required_: No

_Type_: List of <a href="indexedtagdefinition.md">IndexedTagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexedTagComparison

_Required_: No

_Type_: List of <a href="indexedtagcomparisondefinition.md">IndexedTagComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Integer

_Required_: No

_Type_: List of <a href="integerdefinition.md">IntegerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegerComparison

_Required_: No

_Type_: List of <a href="integercomparisondefinition.md">IntegerComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipaddress

_Required_: No

_Type_: List of <a href="ipaddressdefinition.md">IpaddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpaddressComparison

_Required_: No

_Type_: List of <a href="ipaddresscomparisondefinition.md">IpaddressComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: List of <a href="keydefinition.md">KeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobilePlatform

_Required_: No

_Type_: List of <a href="mobileplatformdefinition.md">MobilePlatformDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobilePlatformComparison

_Required_: No

_Type_: List of <a href="mobileplatformcomparisondefinition.md">MobilePlatformComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsArch

_Required_: No

_Type_: List of <a href="osarchdefinition.md">OsArchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

_Required_: No

_Type_: List of <a href="ostypedefinition.md">OsTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsarchitectureComparison

_Required_: No

_Type_: List of <a href="osarchitecturecomparisondefinition.md">OsarchitectureComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OstypeComparison

_Required_: No

_Type_: List of <a href="ostypecomparisondefinition.md">OstypeComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaasType

_Required_: No

_Type_: List of <a href="paastypedefinition.md">PaasTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaasTypeComparison

_Required_: No

_Type_: List of <a href="paastypecomparisondefinition.md">PaasTypeComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessMetadata

_Required_: No

_Type_: List of <a href="processmetadatadefinition.md">ProcessMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessMetadataConditionKey

_Required_: No

_Type_: List of <a href="processmetadataconditionkeydefinition.md">ProcessMetadataConditionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceTopology

_Required_: No

_Type_: List of <a href="servicetopologydefinition.md">ServiceTopologyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceTopologyComparison

_Required_: No

_Type_: List of <a href="servicetopologycomparisondefinition.md">ServiceTopologyComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceType

_Required_: No

_Type_: List of <a href="servicetypedefinition.md">ServiceTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceTypeComparison

_Required_: No

_Type_: List of <a href="servicetypecomparisondefinition.md">ServiceTypeComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SimpleHostTechComparison

_Required_: No

_Type_: List of <a href="simplehosttechcomparisondefinition.md">SimpleHostTechComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SimpleTechComparison

_Required_: No

_Type_: List of <a href="simpletechcomparisondefinition.md">SimpleTechComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### String

_Required_: No

_Type_: List of <a href="stringdefinition.md">StringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringComparison

_Required_: No

_Type_: List of <a href="stringcomparisondefinition.md">StringComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringConditionKey

_Required_: No

_Type_: List of <a href="stringconditionkeydefinition.md">StringConditionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringKey

_Required_: No

_Type_: List of <a href="stringkeydefinition.md">StringKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyntheticEngine

_Required_: No

_Type_: List of <a href="syntheticenginedefinition.md">SyntheticEngineDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyntheticEngineTypeComparison

_Required_: No

_Type_: List of <a href="syntheticenginetypecomparisondefinition.md">SyntheticEngineTypeComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagComparison

_Required_: No

_Type_: List of <a href="tagcomparisondefinition.md">TagComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tech

_Required_: No

_Type_: List of <a href="techdefinition.md">TechDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

