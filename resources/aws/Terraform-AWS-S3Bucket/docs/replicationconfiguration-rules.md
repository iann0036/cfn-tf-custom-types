# Terraform::AWS::S3Bucket ReplicationConfiguration Rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ &lt;a href=&#34;replicationconfiguration-rules-destination.md&#34;&gt;Destination&lt;/a&gt;, ... ]</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ &lt;a href=&#34;replicationconfiguration-rules-filter.md&#34;&gt;Filter&lt;/a&gt;, ... ]</i>,
    "<a href="#sourceselectioncriteria" title="SourceSelectionCriteria">SourceSelectionCriteria</a>" : <i>[ &lt;a href=&#34;replicationconfiguration-rules-sourceselectioncriteria.md&#34;&gt;SourceSelectionCriteria&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - &lt;a href=&#34;replicationconfiguration-rules-destination.md&#34;&gt;Destination&lt;/a&gt;</i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - &lt;a href=&#34;replicationconfiguration-rules-filter.md&#34;&gt;Filter&lt;/a&gt;</i>
<a href="#sourceselectioncriteria" title="SourceSelectionCriteria">SourceSelectionCriteria</a>: <i>
      - &lt;a href=&#34;replicationconfiguration-rules-sourceselectioncriteria.md&#34;&gt;SourceSelectionCriteria&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No
_Type_: List of &lt;a href=&#34;replicationconfiguration-rules-destination.md&#34;&gt;Destination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No
_Type_: List of &lt;a href=&#34;replicationconfiguration-rules-filter.md&#34;&gt;Filter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSelectionCriteria

_Required_: No
_Type_: List of &lt;a href=&#34;replicationconfiguration-rules-sourceselectioncriteria.md&#34;&gt;SourceSelectionCriteria&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

