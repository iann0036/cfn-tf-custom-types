# Terraform::AWS::S3BucketAnalyticsConfiguration DataExport

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#outputschemaversion" title="OutputSchemaVersion">OutputSchemaVersion</a>" : <i>String</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ &lt;a href=&#34;dataexport-destination.md&#34;&gt;Destination&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#outputschemaversion" title="OutputSchemaVersion">OutputSchemaVersion</a>: <i>String</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - &lt;a href=&#34;dataexport-destination.md&#34;&gt;Destination&lt;/a&gt;</i>
</pre>

## Properties

#### OutputSchemaVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No
_Type_: List of &lt;a href=&#34;dataexport-destination.md&#34;&gt;Destination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

