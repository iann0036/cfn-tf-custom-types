# TF::Google::BigqueryJob QueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowlargeresults" title="AllowLargeResults">AllowLargeResults</a>" : <i>Boolean</i>,
    "<a href="#createdisposition" title="CreateDisposition">CreateDisposition</a>" : <i>String</i>,
    "<a href="#flattenresults" title="FlattenResults">FlattenResults</a>" : <i>Boolean</i>,
    "<a href="#maximumbillingtier" title="MaximumBillingTier">MaximumBillingTier</a>" : <i>Double</i>,
    "<a href="#maximumbytesbilled" title="MaximumBytesBilled">MaximumBytesBilled</a>" : <i>String</i>,
    "<a href="#parametermode" title="ParameterMode">ParameterMode</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="querydefinition.md">QueryDefinition</a>, ... ]</i>,
    "<a href="#schemaupdateoptions" title="SchemaUpdateOptions">SchemaUpdateOptions</a>" : <i>[ String, ... ]</i>,
    "<a href="#uselegacysql" title="UseLegacySql">UseLegacySql</a>" : <i>Boolean</i>,
    "<a href="#usequerycache" title="UseQueryCache">UseQueryCache</a>" : <i>Boolean</i>,
    "<a href="#writedisposition" title="WriteDisposition">WriteDisposition</a>" : <i>String</i>,
    "<a href="#defaultdataset" title="DefaultDataset">DefaultDataset</a>" : <i>[ <a href="defaultdatasetdefinition.md">DefaultDatasetDefinition</a>, ... ]</i>,
    "<a href="#destinationencryptionconfiguration" title="DestinationEncryptionConfiguration">DestinationEncryptionConfiguration</a>" : <i>[ <a href="destinationencryptionconfigurationdefinition.md">DestinationEncryptionConfigurationDefinition</a>, ... ]</i>,
    "<a href="#destinationtable" title="DestinationTable">DestinationTable</a>" : <i>[ <a href="destinationtabledefinition.md">DestinationTableDefinition</a>, ... ]</i>,
    "<a href="#scriptoptions" title="ScriptOptions">ScriptOptions</a>" : <i>[ <a href="scriptoptionsdefinition.md">ScriptOptionsDefinition</a>, ... ]</i>,
    "<a href="#userdefinedfunctionresources" title="UserDefinedFunctionResources">UserDefinedFunctionResources</a>" : <i>[ <a href="userdefinedfunctionresourcesdefinition.md">UserDefinedFunctionResourcesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowlargeresults" title="AllowLargeResults">AllowLargeResults</a>: <i>Boolean</i>
<a href="#createdisposition" title="CreateDisposition">CreateDisposition</a>: <i>String</i>
<a href="#flattenresults" title="FlattenResults">FlattenResults</a>: <i>Boolean</i>
<a href="#maximumbillingtier" title="MaximumBillingTier">MaximumBillingTier</a>: <i>Double</i>
<a href="#maximumbytesbilled" title="MaximumBytesBilled">MaximumBytesBilled</a>: <i>String</i>
<a href="#parametermode" title="ParameterMode">ParameterMode</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="querydefinition.md">QueryDefinition</a></i>
<a href="#schemaupdateoptions" title="SchemaUpdateOptions">SchemaUpdateOptions</a>: <i>
      - String</i>
<a href="#uselegacysql" title="UseLegacySql">UseLegacySql</a>: <i>Boolean</i>
<a href="#usequerycache" title="UseQueryCache">UseQueryCache</a>: <i>Boolean</i>
<a href="#writedisposition" title="WriteDisposition">WriteDisposition</a>: <i>String</i>
<a href="#defaultdataset" title="DefaultDataset">DefaultDataset</a>: <i>
      - <a href="defaultdatasetdefinition.md">DefaultDatasetDefinition</a></i>
<a href="#destinationencryptionconfiguration" title="DestinationEncryptionConfiguration">DestinationEncryptionConfiguration</a>: <i>
      - <a href="destinationencryptionconfigurationdefinition.md">DestinationEncryptionConfigurationDefinition</a></i>
<a href="#destinationtable" title="DestinationTable">DestinationTable</a>: <i>
      - <a href="destinationtabledefinition.md">DestinationTableDefinition</a></i>
<a href="#scriptoptions" title="ScriptOptions">ScriptOptions</a>: <i>
      - <a href="scriptoptionsdefinition.md">ScriptOptionsDefinition</a></i>
<a href="#userdefinedfunctionresources" title="UserDefinedFunctionResources">UserDefinedFunctionResources</a>: <i>
      - <a href="userdefinedfunctionresourcesdefinition.md">UserDefinedFunctionResourcesDefinition</a></i>
</pre>

## Properties

#### AllowLargeResults

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDisposition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlattenResults

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBillingTier

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBytesBilled

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: List of <a href="querydefinition.md">QueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaUpdateOptions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseLegacySql

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseQueryCache

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteDisposition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultDataset

_Required_: No

_Type_: List of <a href="defaultdatasetdefinition.md">DefaultDatasetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationEncryptionConfiguration

_Required_: No

_Type_: List of <a href="destinationencryptionconfigurationdefinition.md">DestinationEncryptionConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationTable

_Required_: No

_Type_: List of <a href="destinationtabledefinition.md">DestinationTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptOptions

_Required_: No

_Type_: List of <a href="scriptoptionsdefinition.md">ScriptOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDefinedFunctionResources

_Required_: No

_Type_: List of <a href="userdefinedfunctionresourcesdefinition.md">UserDefinedFunctionResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

