# Terraform::Kubernetes::StatefulSet

CloudFormation equivalent of kubernetes_stateful_set

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::StatefulSet",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;, ... ]</i>,
        "<a href="#selector" title="Selector">Selector</a>" : <i>[ &lt;a href=&#34;selector.md&#34;&gt;Selector&lt;/a&gt;, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;, ... ]</i>,
        "<a href="#updatestrategy" title="UpdateStrategy">UpdateStrategy</a>" : <i>[ &lt;a href=&#34;updatestrategy.md&#34;&gt;UpdateStrategy&lt;/a&gt;, ... ]</i>,
        "<a href="#volumeclaimtemplate" title="VolumeClaimTemplate">VolumeClaimTemplate</a>" : <i>[ &lt;a href=&#34;volumeclaimtemplate.md&#34;&gt;VolumeClaimTemplate&lt;/a&gt;, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;, ... ]</i>,
        "<a href="#rollingupdate" title="RollingUpdate">RollingUpdate</a>" : <i>[ &lt;a href=&#34;rollingupdate.md&#34;&gt;RollingUpdate&lt;/a&gt;, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::StatefulSet
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;</i>
    <a href="#selector" title="Selector">Selector</a>: <i>
      - &lt;a href=&#34;selector.md&#34;&gt;Selector&lt;/a&gt;</i>
    <a href="#template" title="Template">Template</a>: <i>
      - &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;</i>
    <a href="#updatestrategy" title="UpdateStrategy">UpdateStrategy</a>: <i>
      - &lt;a href=&#34;updatestrategy.md&#34;&gt;UpdateStrategy&lt;/a&gt;</i>
    <a href="#volumeclaimtemplate" title="VolumeClaimTemplate">VolumeClaimTemplate</a>: <i>
      - &lt;a href=&#34;volumeclaimtemplate.md&#34;&gt;VolumeClaimTemplate&lt;/a&gt;</i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;</i>
    <a href="#rollingupdate" title="RollingUpdate">RollingUpdate</a>: <i>
      - &lt;a href=&#34;rollingupdate.md&#34;&gt;RollingUpdate&lt;/a&gt;</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No

_Type_: List of &lt;a href=&#34;selector.md&#34;&gt;Selector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateStrategy

_Required_: No

_Type_: List of &lt;a href=&#34;updatestrategy.md&#34;&gt;UpdateStrategy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeClaimTemplate

_Required_: No

_Type_: List of &lt;a href=&#34;volumeclaimtemplate.md&#34;&gt;VolumeClaimTemplate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollingUpdate

_Required_: No

_Type_: List of &lt;a href=&#34;rollingupdate.md&#34;&gt;RollingUpdate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

