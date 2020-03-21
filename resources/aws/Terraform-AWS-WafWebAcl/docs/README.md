# Terraform::AWS::WafWebAcl

CloudFormation equivalent of aws_waf_web_acl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::WafWebAcl",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>[ &lt;a href=&#34;defaultaction.md&#34;&gt;DefaultAction&lt;/a&gt;, ... ]</i>,
        "<a href="#loggingconfiguration" title="LoggingConfiguration">LoggingConfiguration</a>" : <i>[ &lt;a href=&#34;loggingconfiguration.md&#34;&gt;LoggingConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ &lt;a href=&#34;rules.md&#34;&gt;Rules&lt;/a&gt;, ... ]</i>,
        "<a href="#redactedfields" title="RedactedFields">RedactedFields</a>" : <i>[ &lt;a href=&#34;redactedfields.md&#34;&gt;RedactedFields&lt;/a&gt;, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
        "<a href="#overrideaction" title="OverrideAction">OverrideAction</a>" : <i>[ &lt;a href=&#34;overrideaction.md&#34;&gt;OverrideAction&lt;/a&gt;, ... ]</i>,
        "<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>" : <i>[ &lt;a href=&#34;fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::WafWebAcl
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>
      - &lt;a href=&#34;defaultaction.md&#34;&gt;DefaultAction&lt;/a&gt;</i>
    <a href="#loggingconfiguration" title="LoggingConfiguration">LoggingConfiguration</a>: <i>
      - &lt;a href=&#34;loggingconfiguration.md&#34;&gt;LoggingConfiguration&lt;/a&gt;</i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - &lt;a href=&#34;rules.md&#34;&gt;Rules&lt;/a&gt;</i>
    <a href="#redactedfields" title="RedactedFields">RedactedFields</a>: <i>
      - &lt;a href=&#34;redactedfields.md&#34;&gt;RedactedFields&lt;/a&gt;</i>
    <a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;</i>
    <a href="#overrideaction" title="OverrideAction">OverrideAction</a>: <i>
      - &lt;a href=&#34;overrideaction.md&#34;&gt;OverrideAction&lt;/a&gt;</i>
    <a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>: <i>
      - &lt;a href=&#34;fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAction

_Required_: No

_Type_: List of &lt;a href=&#34;defaultaction.md&#34;&gt;DefaultAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;loggingconfiguration.md&#34;&gt;LoggingConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of &lt;a href=&#34;rules.md&#34;&gt;Rules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedactedFields

_Required_: No

_Type_: List of &lt;a href=&#34;redactedfields.md&#34;&gt;RedactedFields&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideAction

_Required_: No

_Type_: List of &lt;a href=&#34;overrideaction.md&#34;&gt;OverrideAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldToMatch

_Required_: No

_Type_: List of &lt;a href=&#34;fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

