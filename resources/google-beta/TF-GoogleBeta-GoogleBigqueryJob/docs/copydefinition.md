# TF::GoogleBeta::GoogleBigqueryJob CopyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#createdisposition" title="CreateDisposition">CreateDisposition</a>" : <i>String</i>,
    "<a href="#writedisposition" title="WriteDisposition">WriteDisposition</a>" : <i>String</i>,
    "<a href="#destinationencryptionconfiguration" title="DestinationEncryptionConfiguration">DestinationEncryptionConfiguration</a>" : <i>[ <a href="destinationencryptionconfigurationdefinition.md">DestinationEncryptionConfigurationDefinition</a>, ... ]</i>,
    "<a href="#destinationtable" title="DestinationTable">DestinationTable</a>" : <i>[ <a href="destinationtabledefinition.md">DestinationTableDefinition</a>, ... ]</i>,
    "<a href="#sourcetables" title="SourceTables">SourceTables</a>" : <i>[ <a href="sourcetablesdefinition.md">SourceTablesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#createdisposition" title="CreateDisposition">CreateDisposition</a>: <i>String</i>
<a href="#writedisposition" title="WriteDisposition">WriteDisposition</a>: <i>String</i>
<a href="#destinationencryptionconfiguration" title="DestinationEncryptionConfiguration">DestinationEncryptionConfiguration</a>: <i>
      - <a href="destinationencryptionconfigurationdefinition.md">DestinationEncryptionConfigurationDefinition</a></i>
<a href="#destinationtable" title="DestinationTable">DestinationTable</a>: <i>
      - <a href="destinationtabledefinition.md">DestinationTableDefinition</a></i>
<a href="#sourcetables" title="SourceTables">SourceTables</a>: <i>
      - <a href="sourcetablesdefinition.md">SourceTablesDefinition</a></i>
</pre>

## Properties

#### CreateDisposition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteDisposition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationEncryptionConfiguration

_Required_: No

_Type_: List of <a href="destinationencryptionconfigurationdefinition.md">DestinationEncryptionConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationTable

_Required_: No

_Type_: List of <a href="destinationtabledefinition.md">DestinationTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceTables

_Required_: No

_Type_: List of <a href="sourcetablesdefinition.md">SourceTablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

