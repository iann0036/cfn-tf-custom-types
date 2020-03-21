# Terraform::OCI::StreamingStreamArchiver

CloudFormation equivalent of oci_streaming_stream_archiver

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::StreamingStreamArchiver",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#batchrolloversizeinmbs" title="BatchRolloverSizeInMbs">BatchRolloverSizeInMbs</a>" : <i>Double</i>,
        "<a href="#batchrollovertimeinseconds" title="BatchRolloverTimeInSeconds">BatchRolloverTimeInSeconds</a>" : <i>Double</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#error" title="Error">Error</a>" : <i>[ &lt;a href=&#34;error.md&#34;&gt;Error&lt;/a&gt;, ... ]</i>,
        "<a href="#startposition" title="StartPosition">StartPosition</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#streamid" title="StreamId">StreamId</a>" : <i>String</i>,
        "<a href="#timecreated" title="TimeCreated">TimeCreated</a>" : <i>String</i>,
        "<a href="#useexistingbucket" title="UseExistingBucket">UseExistingBucket</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::StreamingStreamArchiver
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#batchrolloversizeinmbs" title="BatchRolloverSizeInMbs">BatchRolloverSizeInMbs</a>: <i>Double</i>
    <a href="#batchrollovertimeinseconds" title="BatchRolloverTimeInSeconds">BatchRolloverTimeInSeconds</a>: <i>Double</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#error" title="Error">Error</a>: <i>
      - &lt;a href=&#34;error.md&#34;&gt;Error&lt;/a&gt;</i>
    <a href="#startposition" title="StartPosition">StartPosition</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#streamid" title="StreamId">StreamId</a>: <i>String</i>
    <a href="#timecreated" title="TimeCreated">TimeCreated</a>: <i>String</i>
    <a href="#useexistingbucket" title="UseExistingBucket">UseExistingBucket</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchRolloverSizeInMbs

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchRolloverTimeInSeconds

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Error

_Required_: No

_Type_: List of &lt;a href=&#34;error.md&#34;&gt;Error&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartPosition

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeCreated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseExistingBucket

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Error

Returns the &lt;code&gt;Error&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

