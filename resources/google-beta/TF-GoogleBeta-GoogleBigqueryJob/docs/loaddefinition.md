# TF::GoogleBeta::GoogleBigqueryJob LoadDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowjaggedrows" title="AllowJaggedRows">AllowJaggedRows</a>" : <i>Boolean</i>,
    "<a href="#allowquotednewlines" title="AllowQuotedNewlines">AllowQuotedNewlines</a>" : <i>Boolean</i>,
    "<a href="#autodetect" title="Autodetect">Autodetect</a>" : <i>Boolean</i>,
    "<a href="#createdisposition" title="CreateDisposition">CreateDisposition</a>" : <i>String</i>,
    "<a href="#encoding" title="Encoding">Encoding</a>" : <i>String</i>,
    "<a href="#fielddelimiter" title="FieldDelimiter">FieldDelimiter</a>" : <i>String</i>,
    "<a href="#ignoreunknownvalues" title="IgnoreUnknownValues">IgnoreUnknownValues</a>" : <i>Boolean</i>,
    "<a href="#maxbadrecords" title="MaxBadRecords">MaxBadRecords</a>" : <i>Double</i>,
    "<a href="#nullmarker" title="NullMarker">NullMarker</a>" : <i>String</i>,
    "<a href="#projectionfields" title="ProjectionFields">ProjectionFields</a>" : <i>[ String, ... ]</i>,
    "<a href="#quote" title="Quote">Quote</a>" : <i>String</i>,
    "<a href="#schemaupdateoptions" title="SchemaUpdateOptions">SchemaUpdateOptions</a>" : <i>[ String, ... ]</i>,
    "<a href="#skipleadingrows" title="SkipLeadingRows">SkipLeadingRows</a>" : <i>Double</i>,
    "<a href="#sourceformat" title="SourceFormat">SourceFormat</a>" : <i>String</i>,
    "<a href="#sourceuris" title="SourceUris">SourceUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#writedisposition" title="WriteDisposition">WriteDisposition</a>" : <i>String</i>,
    "<a href="#destinationencryptionconfiguration" title="DestinationEncryptionConfiguration">DestinationEncryptionConfiguration</a>" : <i>[ <a href="destinationencryptionconfigurationdefinition.md">DestinationEncryptionConfigurationDefinition</a>, ... ]</i>,
    "<a href="#destinationtable" title="DestinationTable">DestinationTable</a>" : <i>[ <a href="destinationtabledefinition.md">DestinationTableDefinition</a>, ... ]</i>,
    "<a href="#timepartitioning" title="TimePartitioning">TimePartitioning</a>" : <i>[ <a href="timepartitioningdefinition.md">TimePartitioningDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowjaggedrows" title="AllowJaggedRows">AllowJaggedRows</a>: <i>Boolean</i>
<a href="#allowquotednewlines" title="AllowQuotedNewlines">AllowQuotedNewlines</a>: <i>Boolean</i>
<a href="#autodetect" title="Autodetect">Autodetect</a>: <i>Boolean</i>
<a href="#createdisposition" title="CreateDisposition">CreateDisposition</a>: <i>String</i>
<a href="#encoding" title="Encoding">Encoding</a>: <i>String</i>
<a href="#fielddelimiter" title="FieldDelimiter">FieldDelimiter</a>: <i>String</i>
<a href="#ignoreunknownvalues" title="IgnoreUnknownValues">IgnoreUnknownValues</a>: <i>Boolean</i>
<a href="#maxbadrecords" title="MaxBadRecords">MaxBadRecords</a>: <i>Double</i>
<a href="#nullmarker" title="NullMarker">NullMarker</a>: <i>String</i>
<a href="#projectionfields" title="ProjectionFields">ProjectionFields</a>: <i>
      - String</i>
<a href="#quote" title="Quote">Quote</a>: <i>String</i>
<a href="#schemaupdateoptions" title="SchemaUpdateOptions">SchemaUpdateOptions</a>: <i>
      - String</i>
<a href="#skipleadingrows" title="SkipLeadingRows">SkipLeadingRows</a>: <i>Double</i>
<a href="#sourceformat" title="SourceFormat">SourceFormat</a>: <i>String</i>
<a href="#sourceuris" title="SourceUris">SourceUris</a>: <i>
      - String</i>
<a href="#writedisposition" title="WriteDisposition">WriteDisposition</a>: <i>String</i>
<a href="#destinationencryptionconfiguration" title="DestinationEncryptionConfiguration">DestinationEncryptionConfiguration</a>: <i>
      - <a href="destinationencryptionconfigurationdefinition.md">DestinationEncryptionConfigurationDefinition</a></i>
<a href="#destinationtable" title="DestinationTable">DestinationTable</a>: <i>
      - <a href="destinationtabledefinition.md">DestinationTableDefinition</a></i>
<a href="#timepartitioning" title="TimePartitioning">TimePartitioning</a>: <i>
      - <a href="timepartitioningdefinition.md">TimePartitioningDefinition</a></i>
</pre>

## Properties

#### AllowJaggedRows

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowQuotedNewlines

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autodetect

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDisposition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encoding

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldDelimiter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreUnknownValues

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBadRecords

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NullMarker

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectionFields

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quote

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaUpdateOptions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipLeadingRows

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUris

_Required_: Yes

_Type_: List of String

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

#### TimePartitioning

_Required_: No

_Type_: List of <a href="timepartitioningdefinition.md">TimePartitioningDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

